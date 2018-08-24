import pytest
from utilities.sendkeysconfig import *
from pages.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests():

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.driver=oneTimeSetUp()
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        print("test_invalidLogin started")
        self.lp.login(username, invalid_password)
        result = self.lp.verify_login_failed(self)
        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        print("test_validLogin started")
        self.lp.login(username, pass_word)
        result = self.lp.verify_login_successful(self)
        print("Result: " + str(result))
        assert result == True

