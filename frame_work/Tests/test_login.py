from time import sleep
from frame_work.Library.selenium_wrapper import SeleniumWrapper
from pytest import mark
from frame_work.test_data.input import values
# header = ["email", "password"]
# data = [("steve.jobs@gmail.com", "Password123"),
#         ("")]

@mark.parametrize(values)
def test_login(setup, values):
    s = SeleniumWrapper(setup)        # passing the driver instance that is created in 15th line
    s.click_element(("link text", "Log in"))
    sleep(2)
    s.enter_text(("id", "Email"), value=values)
    sleep(2)
    s.enter_text(("id", "Password"), value=values)
    sleep(2)
    s.click_element(("xpath", "//input[@value='Log in']"))
    sleep(2)
