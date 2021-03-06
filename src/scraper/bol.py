from scraper.common import ScrapeResult, Scraper, ScraperFactory


class BolScrapeResult(ScrapeResult):
    def parse(self):
        alert_content = ''

        # get name of product
        tag = self.soup.body.select_one('h1.page-heading > span.h-boxedright--xs')
        if tag:
            alert_content += tag.text.strip() + '\n'
        else:
            self.logger.warning(f'missing title: {self.url}')

        # get listed price
        tag = self.soup.body.select_one('span.promo-price')
        price_str = self.set_price(tag)
        if price_str:
            alert_subject = f'In Stock for {price_str}'
            self.alert_subject = alert_subject
            self.alert_content = f'{alert_content.strip()}\n{self.url}'


@ScraperFactory.register
class BolScraper(Scraper):
    @staticmethod
    def get_domain():
        return 'bol'

    @staticmethod
    def get_driver_type():
        return 'requests'

    @staticmethod
    def get_result_type():
        return BolScrapeResult
