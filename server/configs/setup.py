from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from dotenv import load_dotenv
import os
from mongoengine import connect

def connect_db():
    """
    Makes connection to database and returns the client connection
    """
    load_dotenv()
    USER = os.getenv("USER_ROOT_MONGODB")
    PASS = os.getenv("PASS_ROOT_MONGODB")
    uri = f"mongodb+srv://{USER}:{PASS}@scan-back-cluster.eoldn4r.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    connect(host=uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client

def connect_web_proxy():
    """
    Make connection to the webproxy driver and return the driver
    """
    load_dotenv()
    USER = os.getenv("USER_REMOTE_PROXY")
    PASS = os.getenv("PASS_REMOTE_PROXY")
    SBR_WEBDRIVER = f'https://{USER}:{PASS}@brd.superproxy.io:9515'
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    print('Connecting scraper to proxy...')
    driver = Remote(sbr_connection, options=ChromeOptions())
    print('Connected!')

    # The program will hang if the driver does not make a connection (sad face)
    return driver

