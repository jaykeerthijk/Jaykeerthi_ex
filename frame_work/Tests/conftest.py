from selenium import webdriver
from time import sleep
from pytest import fixture
from frame_work.Library.config import Config

@fixture
def setup():
    driver = webdriver.Chrome("C:/Users/User/PycharmProjects/Jaykeerthi_ex/frame_work/Driver/chromedriver.exe")
    driver.maximize_window()
    driver.get(Config.URL)
    sleep(3)
    yield driver
    driver.close()


@fixture
def setup1():
    driver = webdriver.Chrome("C:/Users/User/PycharmProjects/Jaykeerthi_ex/frame_work/Driver/chromedriver.exe")
    driver.maximize_window()
    driver.get(Config.URL)
    sleep(3)
    yield driver
    driver.close()
