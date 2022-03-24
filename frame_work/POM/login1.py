from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from frame_work.selenium_wrapper import SeleniumWrapper
from frame_work.config import Config


def test_login():
    driver = webdriver.Chrome("./chromedriver")
    driver.maximize_window()
    driver.get(Config.URL)
    sleep(3)
    s = SeleniumWrapper(driver)        # passing the driver instance that is created in 15th line
    s.click_element((By.LINK_TEXT, "Log in"))
    sleep(2)
    s.enter_text((By.ID, "Email"), value="hello.world@company.com")
    sleep(2)
    s.enter_text((By.ID, "Password"), value="Password123")
    sleep(2)
    s.click_element((By.XPATH, "//input[@value='Log in']"))
    sleep(2)
