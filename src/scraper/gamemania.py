from scraper.common import ScrapeResult, Scraper, ScraperFactory


class GameManiaScrapeResult(ScrapeResult):
    def parse(self):
        alert_subject = 'In Stock'
        alert_content = ''

        # get name of product
        tag = self.soup.body.select_one('div.banner > div.headerWrap1 > h1 > span')
        if tag:
            alert_content += tag.text.strip() + '\n'
        else:
            self.logger.warning(f'missing title: {self.url}')

        # get listed price
        tag = self.soup.body.select_one('label.order--new').select_one('div.price')
        price_str = self.set_price(tag)
        if price_str:
            alert_subject = f'In Stock for {price_str}'

        tag = self.soup.body.select_one('div.message--delivery > p > span')
        if tag and 'levertermijn' in tag.text.lower():
            self.alert_subject = alert_subject
            self.alert_content = f'{alert_content.strip()}\n{self.url}'


@ScraperFactory.register
class GameManiaScraper(Scraper):
    @staticmethod
    def get_domain():
        return 'gamemania'

    @staticmethod
    def get_driver_type():
        return 'requests'

    @staticmethod
    def get_result_type():
        return GameManiaScrapeResult
