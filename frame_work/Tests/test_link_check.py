from frame_work.POM.homepage import HomePage
from pytest import mark

home = "Demo Web Shop. Register"
login = "Demo Web Shop. Login"


def test_home_page_check(setup):
    hp = HomePage(setup)
    hp.home_click_register()
    title = setup.title
    if title == home:
        assert True
    else:
        assert False


def test_login_page_check(setup):
    hp = HomePage(setup)
    hp.home_click_login()
    title = setup.title
    if title == login:
        assert True
    else:
        assert False
