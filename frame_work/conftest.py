from selenium import webdriver
from time import sleep
from pytest import fixture
from frame_work.Library.config import Config

@fixture
def setup():
    driver = webdriver.Chrome(r"C:\Users\Jagadeesh\PycharmProjects\ Selenium_Training1\frame_work\Driver\chromedriver.exe")
    driver.maximize_window()
    driver.get(Config.URL)
    sleep(3)
    yield driver
    driver.close()
