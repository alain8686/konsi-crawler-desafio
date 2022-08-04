import time
from rq import Queue, Connection
from rq.job import JobStatus
import redis
from app import app
from app.scrapper.scrapy_manager import benefits_extractor
from app.exception.InvalidCpf import InvalidCpfException


class UserOptionsManager:
    def __init__(self):
        pass

    def find_benefits_identificators(self, cpf, user, password):
        enqueue = self.async_find_benefits_identificators(cpf, user, password)
        task_id = enqueue['data']['task_id']

        response = self.find_benefits_identificators_status(task_id)
        while response['data']['task_status'] in [JobStatus.QUEUED, JobStatus.STARTED, JobStatus.SCHEDULED]:
            response = self.find_benefits_identificators_status(task_id)
            time.sleep(1)
        if response['data']['task_result'] is not None:
            return response['data']['task_result']
        else:
            raise InvalidCpfException('Cpf não valido')

    def async_find_benefits_identificators(self, cpf, user, password):
        with Connection(redis.from_url(app.config["REDIS_URL"])):
            q = Queue()
            task = q.enqueue(benefits_extractor, cpf, user, password)
            response_object = {
                "status": "success",
                "data": {
                    "task_id": task.get_id()
                }
            }
            return response_object

    def find_benefits_identificators_status(self, task_id):
        with Connection(redis.from_url(app.config["REDIS_URL"])):
            q = Queue()
            task = q.fetch_job(task_id)
        if task:
            response_object = {
                "status": "success",
                "data": {
                    "task_id": task.get_id(),
                    "task_status": task.get_status(),
                    "task_result": task.result,
                },
            }
        else:
            response_object = {"status": "error"}
        return response_object