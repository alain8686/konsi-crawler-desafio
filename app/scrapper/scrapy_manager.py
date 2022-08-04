from app.scrapper.definition.Scrapy import ScrapyScraper

from scrapy import signals
from twisted.internet import reactor
from app import runner

def benefits_extractor(cpf, user, password):
    d = runner.crawl(ScrapyScraper, cpf=cpf, user=user, password=password)
    d.addBoth(lambda _: reactor.stop())

    items = []
    item_manager = lambda item, response, spider: items.append(item['item'])

    for crawler in runner.crawlers:
        crawler.signals.connect(item_manager, signal=signals.item_scraped)

    reactor.run()

    return items


