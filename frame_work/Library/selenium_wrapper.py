from selenium.webdriver.support.select import Select
from frame_work.Library.wait import wait


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @wait
    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def select_item(self, locator, *, item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise TypeError


