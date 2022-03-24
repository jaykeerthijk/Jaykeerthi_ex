from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com")
sleep(4)


class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False
# wait = WebDriverWait(driver,20)
# v = _visibility_of_element_located(locator)
# wait.until(v)


def wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locator = args[1]
        wait = WebDriverWait(instance.driver, 20)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper


class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    @wait
    def test_click_element(self, locator):
        self.driver.find_element(*locator).click()

    @wait
    def test_enter_text(self, locator, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def test_select_item(self, locator, *, item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise TypeError


s = SeleniumWrapper(driver)
s.test_click_element(("link text", "Register"))
sleep(2)
# driver.find_element_by_id("gender-male").click()
s.test_click_element(("id", "gender-male"))
sleep(2)
# driver.find_element_by_name("FirstName").send_keys("hi")
s.test_enter_text(("name", "FirstName"), value="hi")

sleep(2)
# driver.find_element_by_name("LastName").send_keys("hello")
s.test_enter_text(("name", "LastName"), value="hello")
sleep(2)
# driver.find_element_by_id("Email").send_keys("hellohi@gmail.com")
s.test_enter_text(("id", "Email"), value="hellohi@gmail.com")
sleep(2)
# driver.find_element_by_id("Password").send_keys("123456")
s.test_enter_text(("id","Password"), value="123456")
sleep(2)
# driver.find_element_by_id("ConfirmPassword").send_keys("123456")
s.test_enter_text(("id","ConfirmPassword"), value="123456")
sleep(2)
# driver.find_element_by_id("register-button").click()
s.test_click_element(("id", "register-button"))
sleep(2)

# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         else:
#             return False
# # wait = WebDriverWait(driver,20)
# # v = _visibility_of_element_located(locator)
# # wait.until(v)
# def wait(func):
#     def wrapper(*args, **kwargs):
#         locator = args[0]
#         wait = WebDriverWait(driver, 20)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args, **kwargs)
#     return wrapper
# @wait
# def click_element(locator):
#     driver.find_element(*locator).click()
#
# @wait
# def enter_text(locator, *, value):
#     driver.find_element(*locator).clear()
#     driver.find_element(*locator).send_keys(value)
#
# def select_item(locator, * item):
#     element = driver.find_element(*locator)
#     s = Select(element)
#     if isinstance(item, str):
#         s.select_by_visible_text(item)
#     elif isinstance(item, int):
#         s.select_by_index(item)
#     else:
#         raise TypeError
#
#
#
#
#
# #driver.find_element_by_link_text("Register").click()
# #driver.find_element("link text", "Register").click()
# s = Selenium_Wrapper()
# click_element(("link text", "Register"))
# # driver.find_element_by_id("gender-male").click()
# click_element(("id", "gender-male"))
# # driver.find_element_by_name("FirstName").send_keys("hi")
# enter_text(("name", "FirstName"), value="hi")
# # driver.find_element_by_name("LastName").send_keys("hello")
# enter_text(("name", "LastName"), value="hello")
# # driver.find_element_by_id("Email").send_keys("hellohi@gmail.com")
# enter_text(("id", "Email"), value="hellohi@gmail.com")
# # driver.find_element_by_id("Password").send_keys("123456")
# enter_text(("id","Password"), value="123456")
# # driver.find_element_by_id("ConfirmPassword").send_keys("123456")
# enter_text(("id","ConfirmPassword"), value="123456")
# # driver.find_element_by_id("register-button").click()
# click_element(("id", "register-button"))
#












# import re
# print(re.findall(r'[^\w\s]', 'word@##$  _ 78998'))

