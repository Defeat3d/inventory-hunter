from scraper.common import ScrapeResult, Scraper, ScraperFactory


class MediamarktScrapeResult(ScrapeResult):
    def parse(self):
        alert_subject = 'In Stock'
        alert_content = ''

        # get name of product
        tag = self.soup.find('meta', property='og:title')
        if tag:
            alert_content += tag['content'] + '\n'
        else:
            self.logger.warning(f'missing title: {self.url}')

        # get listed price
        tag = self.soup.find('meta', property='product:price:amount')
        price_str = self.set_price(tag['content'])
        if price_str:
            alert_subject = f'In Stock for {price_str}'

        # check for add to cart button
        tag = self.soup.find('meta', property='og:availability')
        if tag and 'uitverkocht' not in tag['content']:
            self.alert_subject = alert_subject
            self.alert_content = f'{alert_content.strip()}\n{self.url}'


@ScraperFactory.register
class MediamarktScraper(Scraper):
    @staticmethod
    def get_domain():
        return 'mediamarkt'

    @staticmethod
    def get_driver_type():
        return 'requests'

    @staticmethod
    def get_result_type():
        return MediamarktScrapeResult
