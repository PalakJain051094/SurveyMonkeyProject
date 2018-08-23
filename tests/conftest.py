import pytest
from base.browsersetup import DriverSet
from pages.login_page import LoginPage
from utilities.sendkeysconfig import*


@pytest.fixture(scope="module")
def oneTimeSetUp():
    print("Running one time setUp")
    web_driver = DriverSet()
    driver = web_driver.get_web_driver_instance()
    return driver

