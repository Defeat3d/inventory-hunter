import scraper.adorama
import scraper.amazon
import scraper.bestbuy
import scraper.bhphotovideo
import scraper.canadacomputers
import scraper.costcoca
import scraper.ebgames
import scraper.bol
import scraper.coolblue
import scraper.gamemania
import scraper.intertoys
import scraper.mediamarkt
import scraper.microcenter
import scraper.nedgame
import scraper.newegg
import scraper.playstation
import scraper.samsclub
import scraper.toysrus
import scraper.walmart

from scraper.common import ScraperFactory


def init_scrapers(config, drivers):
    return [ScraperFactory.create(drivers, url) for url in config.urls]
