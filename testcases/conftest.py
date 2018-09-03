import pytest
from base.browsersetup import DriverSet
from pages.login_page import LoginPage
from pages.createsurvey import CreateSurvey
from utilities.sendkeysconfig import*

@pytest.yield_fixture(scope="class")
def get_driver():
    print("in get_driver")
    web_driver = DriverSet()
    driver = web_driver.get_web_driver_instance()
    lp = LoginPage(driver)
    lp.login(username, pass_word)
    print("end of get_driver")
    yield driver
    driver.quit()

@pytest.yield_fixture(scope="class")
def get_survey():
    print("in get_survey")
    web_driver = DriverSet()
    driver = web_driver.get_web_driver_instance()
    lp = LoginPage(driver)
    lp.login(username, pass_word)
    cs=CreateSurvey(driver)
    cs.create_survey(first_survey_title)
    print("end of get_survey")
    yield driver
    driver.quit()




