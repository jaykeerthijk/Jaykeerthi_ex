from time import sleep
from pytest import mark
from frame_work.POM.homepage import HomePage
from frame_work.POM.registration import RegistrationPage


header = ["gender", "fname", "lname", "email", "password", "password1"]
data = [('male', 'steve', 'jobs', 'steve.jobs@company.com', 'Password123', "Password123"),
        ]


@mark.parametrize(header, data)
def test_Register(setup, gender, fname, lname, email, password, password1):
    hp = HomePage(setup)
    hp.home_click_register()
    reg = RegistrationPage(setup)
    if gender == 'male':
        reg.register_select_male()
        sleep(2)
    else:
        reg.register_select_female()
        sleep(2)
    reg.register_enter_fname(fname)
    sleep(2)
    reg.register_enter_lname(lname)
    sleep(2)
    reg.register_enter_email(email)
    sleep(2)
    reg.register_enter_password(password)
    sleep(2)
    reg.register_enter_confirm_password(password1)
    sleep(2)
    reg.register_click_btn()
    sleep(2)
