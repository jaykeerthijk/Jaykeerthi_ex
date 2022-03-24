from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com")
sleep(2)