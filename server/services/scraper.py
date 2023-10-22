from configs.setup import connect_web_proxy

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

    def scrape_item_price(self, name):
        """
        given the name of an item
        scrape the price of it from walmart.com
        """

        # go to walmart.com
        self.driver.get('https://www.walmart.com/')

        # enter the name of the item

        # press the search button

        # selct the first result (if it exists)

        # get the price from the item webpate

        # return the price 
        return price