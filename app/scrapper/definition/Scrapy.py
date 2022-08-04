import json
import scrapy
from app.exception.InvalidCpf import InvalidCpfException
from app.config import login_url, headers, benefits_url, main_page


class ScrapyScraper(scrapy.Spider):
    name = 'scrapy_desafio'

    def __init__(self, cpf, user, password):
        self.cpf = cpf
        self.user = user
        self.password = password

    def start_requests(self):
        return [scrapy.Request(login_url, body=json.dumps({'login': self.user, 'senha': self.password}), method='POST',
                               callback=self.request_benefits)]

    def request_benefits(self, response):
        token = response.headers["Authorization"]

        headers_ = headers.copy()
        headers_["Authorization"] = token

        yield scrapy.Request(f'{benefits_url}/{self.cpf}', headers=headers_, method='GET', callback=self.process_benefits)

    def process_benefits(self, response):
        benefits_list = response.json()
        for benefit in benefits_list['beneficios']:
            if benefit['id'] != 0:
                yield {'item': benefit['nb']}



