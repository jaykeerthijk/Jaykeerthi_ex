from _pytest.hookspec import pytest_assertion_pass

from frame_work.Library.selenium_wrapper import SeleniumWrapper


class RegistrationPage(SeleniumWrapper):
    _rdo_male = ("id", "gender-male")
    _rdo_female = ("id", "gender-female")
    _txt_fname = ("name", "FirstName")
    _txt_lname = ("name", "LastName")
    _txt_email = ("id", "Email")
    _txt_password = ("id", "Password")
    _txt_confirmpassword = ("id", "ConfirmPassword")
    _btn_register = ("id", "register-button")

    def __init__(self, driver):
        super().__init__(driver)

    def register_select_male(self):
        self.click_element(RegistrationPage._rdo_male)

    def register_select_female(self):
        self.click_element(RegistrationPage._rdo_female)

    def register_enter_fname(self, fname):
        self.enter_text(RegistrationPage._txt_fname, value=fname)

    def register_enter_lname(self, lname):
        self.enter_text(RegistrationPage._txt_lname, value=lname)

    def register_enter_email(self, email):
        self.enter_text(RegistrationPage._txt_email, value=email)

    def register_enter_password(self, password):
        self.enter_text(RegistrationPage._txt_password, value=password)

    def register_enter_confirm_password(self, password1):
        self.enter_text(RegistrationPage._txt_confirmpassword, value=password1)

    def register_click_btn(self):
        self.click_element(self._btn_register)
