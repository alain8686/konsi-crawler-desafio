from flask import Blueprint, request, jsonify
from app.service.benefits_service import UserOptionsManager


benefits_blue_print = Blueprint('user_options', __name__, url_prefix='/user_options')
user_options_manager = UserOptionsManager()


@benefits_blue_print.route('/benefits/<cpf>', methods=['POST'])
def user_benefits(cpf):
    post_data = request.get_json()
    try:
        response = user_options_manager.find_benefits_identificators(cpf, post_data['user'], post_data['password'])
    except:
        raise
    return jsonify(response)


@benefits_blue_print.route('/benefits/<cpf>/async', methods=['POST'])
def async_user_benefits(cpf):
    post_data = request.get_json()
    response = user_options_manager.async_find_benefits_identificators(cpf, post_data['user'], post_data['password'])
    return jsonify(response)


@benefits_blue_print.route("/benefits/<task_id>/async", methods=["GET"])
def response_request(task_id):
    response_object = user_options_manager.find_benefits_identificators_status(task_id)
    return jsonify(response_object)



