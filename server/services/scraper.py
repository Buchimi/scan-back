from configs.setup import connect_web_proxy
from urllib.parse import quote
import selenium


class Scraper():
    def __init__(self):
        self.driver = connect_web_proxy()

    def test_scraper(self):
        self.driver.get('https://example.com')

        print('Taking page screenshot to file page.png')
        self.driver.get_screenshot_as_file('./page.png')

        print('Navigated! Scraping page content...')
        html = self.driver.page_source

        print(html)

    def scrape_item_price(self, name, price):
        """
        given the name of an item and its recipt
        price scrape the price of it from walmart.com
        and return the difference
        """

        # get the url of searching the item
        search_url = 'https://www.walmart.com/search?q=' + quote(f'{name}')
        # print(f'This is the serach url {search_url}')

        self.driver.get(search_url)

        source = self.driver.page_source
        print(source)

        # go to walmart.com
        # self.driver.get('https://www.walmart.com/')

        # enter the name of the item
        # input_form = self.driver.get(By.)
        # input_form.sendKeys()

        # press the search button

        # selct the first result (if it exists)

        # get the price from the item webpate

        # return the price
        price = {}
        return price