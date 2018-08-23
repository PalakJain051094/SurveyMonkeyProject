import pytest
from utilities.sendkeysconfig import *
from pages.login_page import LoginPage


@pytest.mark.run(order=1)
def test_invalidLogin(get_driver):
    print("test_invalidLogin started")
    lp = LoginPage(get_driver)
    lp.login(username, invalid_password)
    result = lp.verify_login_failed()
    assert result == True

@pytest.mark.run(order=2)
def test_validLogin(get_driver):
    print("test_validLogin started")
    lp = LoginPage(get_driver)
    lp.login(username, pass_word)
    result = lp.verify_login_successful()
    assert result == True
