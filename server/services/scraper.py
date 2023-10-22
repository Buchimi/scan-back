from configs.setup import connect_web_proxy
from urllib.parse import quote
from selenium.webdriver.common.by import By

class Scraper():
    def __init__(self):
        self.driver = connect_web_proxy()

    def scrape_item_price(self, name):
        """
        given the name of an item and its recipt
        price scrape the price of it from walmart.com
        and return the difference
        """

        # get the url of searching the item
        search_url = 'https://www.walmart.com/search?q=' + quote(f'{name}')
        self.driver.get(search_url)

        # get the link of the first item
        link = self.driver.find_element(By.XPATH, '//*[@id="maincontent"]/main/div/div[2]/div/div/div[1]/div[2]/div/section/div/div[1]/div/div/a')
        link.click()

        # wait until the webpage is loaded after clicking
        self.driver.implicitly_wait(10)  # Wait up to 10 seconds

        # get the price from the item webpage
        price_element = self.driver.find_element(By.XPATH, '//*[@id="maincontent"]/section/main/div[2]/div[2]/div/div[2]/div/div[2]/div/div/span[1]/span[2]/span')
        price = price_element.text

        # remove the $
        price = price[1:]
        price = float(price)
        
        return price