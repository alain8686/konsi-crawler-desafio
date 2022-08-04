import json
from flask import Flask
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

app = Flask(__name__, instance_relative_config=False)
cors = CORS(app)

app.config.from_pyfile('config/__init__.py')

runner = CrawlerRunner(get_project_settings())


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


from app.controller.benefits_controller import benefits_blue_print
app.register_blueprint(benefits_blue_print)

