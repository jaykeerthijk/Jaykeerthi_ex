from time import sleep
from frame_work.Library.selenium_wrapper import SeleniumWrapper
from pytest import mark
from frame_work.POM import loginpage
from frame_work.POM import homepage


header = ["email", "password"]
data = [("steve.jobs@gmail.com", "Password123")]

@mark.parametrize(header, data)
def test_login(setup, email, password):
    h1 = homepage.HomePage(setup)
    s = SeleniumWrapper(setup)        # passing the driver instance that is created in 15th line
    s1 = loginpage.LoginPage(setup)
    h1.home_click_login()
    sleep(2)
    s1.login_enter_email(email)
    sleep(2)
    s1.login_enter_password(password)
    sleep(2)
    s1.login_click_login()
    sleep(2)

