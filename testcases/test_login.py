from pages.login_page import  LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
from utilities.sendkeysconfig import *
import logging

@pytest.mark.usefixtures("get_driver")
class TestLogin(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, get_driver):
        self.lp = LoginPage(get_driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        print("test_invalidLogin started")
        self.lp.logout()
        self.lp.login(username, invalid_password)
        result = self.lp.verify_login_failed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        print("test_validLogin started")
        self.lp.login(username, pass_word)
        result = self.lp.verify_login_successful()
        assert result == True