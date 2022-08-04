FROM python:3.7-slim-stretch

WORKDIR /code
COPY requirements.txt requirements.txt
RUN apt-get update && \
    python -m pip install -r requirements.txt
EXPOSE 9000
COPY . .
CMD gunicorn --timeout 1800 --bind 0.0.0.0:9000 --workers=2 --threads=4 --worker-class=gthread app:app
