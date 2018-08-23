import pytest
import unittest
from pages.createsurvey import CreateSurvey
from utilities.sendkeysconfig import*
from utilities.custom_logger import *
import logging


@pytest.mark.usefixtures("get_driver")
class TestCreateSurvey(unittest.TestCase):
    log = customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_level_setup(self,get_driver):
        self.create_survey=CreateSurvey(get_driver)

    @pytest.mark.run(order=1)
    def test_create_survey(self):
        self.log.info("test_create_survey started")
        self.create_survey.create_survey(first_survey_title)
        result = self.create_survey.verify_createsurvey_successful()
        self.log.info("Result: " + str(result))
        assert result == True