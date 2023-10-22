from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv("USER_REMOTE_PROXY")
PASS = os.getenv("PASS_REMOTE_PROXY")
AUTH = f'{USER}:{PASS}'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

class scraper():
    def __init__(self):
        # make a connection
        pass

    def scrape_url():
        pass
    
def main():
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')

    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get('https://example.com')

        # print('Taking page screenshot to file page.png')
        # driver.get_screenshot_as_file('./page.png')

        print('Navigated! Scraping page content...')
        html = driver.page_source

        print(html)

# if __name__ == '__main__':
main()