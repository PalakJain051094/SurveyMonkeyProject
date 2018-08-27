from pages.login_page import  LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
from utilities.sendkeysconfig import *
import logging
from ddt import ddt,data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("get_driver")
@ddt
class TestLogin(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, get_driver):
        self.lp = LoginPage(get_driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("D:/Python_workspace/AutomationAss/logindata.csv"))
    @unpack
    def test_validLogin(self,username, pass_word):
        print("test_validLogin started")
        self.lp.logout()
        self.lp.login(username, pass_word)
        result = self.lp.verify_login_successful()
        assert result == True
