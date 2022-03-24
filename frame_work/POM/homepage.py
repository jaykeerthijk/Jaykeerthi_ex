from frame_work.Library.selenium_wrapper import SeleniumWrapper

class HomePage(SeleniumWrapper):
    _lnk_register = ("link text", "Register")
    _lnk_login = ("link text", "Log in")

    def __init__(self, driver):
        super().__init__(driver)

    def home_click_register(self):
        self.click_element(HomePage._lnk_register)

    def home_click_login(self):
        self.click_element(HomePage._lnk_login)

#from selenium_wrapper import SeleniumWrapper

# class HomePage(Selenium_Wrapper):
#     _lnk_register = ("link text", "Register")
#     _lnk_login = ("link text", "Log in")
#
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     def home_click_register(self):
#         self.click_element(HomePage._lnk_register)
#
#     def home_click_login(self):
#         self.click_element(HomePage._lnk_login)