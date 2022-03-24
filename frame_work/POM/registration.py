from frame_work.Library.selenium_wrapper import SeleniumWrapper


class RegistrationPage(SeleniumWrapper):
    _rdo_male = ("id", "gender-male")
    _rdo_female = ("id", "gender-female")
    _txt_fname = ("name", "FirstName")
    _txt_lname = ("name", "LastName")
    _txt_email = ("id", "Email")
    _txt_password = ("id", "Password")
    _txt_confirmpassword = ("id", "ConfirmPassword")
    _btn_register = ("id", "Register")

    def __init__(self, driver):
        super().__init__(driver)

    def register_select_male(self):
        self.click_element(RegistrationPage._rdo_male)
    def register_select_female(self):
        self.click_element(RegistrationPage._rdo_female)
    def register_enter_namef(self):
        self.enter_text(RegistrationPage._txt_fname, value="hello")
    def register_enter_lname(self):
        self.enter_text(RegistrationPage._txt_lname, value="world")
    def register_enter_email(self):
        self.enter_text(RegistrationPage._txt_email, value="helloworld@gmail.com")
    def register_enter_password(self):
        self.enter_text(RegistrationPage._txt_password, value=2234567)
    def register_enter_confirm_password(self):
        self.click_element(RegistrationPage._txt_confirmpassword, value=2234567)
    def register_click_btn(self):
        self.click_element(RegistrationPage._btn_register)
