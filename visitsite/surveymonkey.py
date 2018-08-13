from utilites.chromebrowser import DriverSet
from pages.login import Login
from pages.createsurvey import CreateSurvey


class SurveyMonkeyWebsite():

    def __init__(self):
        self.driver = DriverSet.setDriver(self)
        self.driver.get("https://www.surveymonkey.com")
        Login.get_loginpage(self,self.driver)
        CreateSurvey.create_new_survey(self,self.driver)
        self.driver.close()


survey_monkey=SurveyMonkeyWebsite()
