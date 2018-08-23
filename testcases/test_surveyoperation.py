import pytest
import unittest
from pages.survey_operations import EditElements
from utilities.sendkeysconfig import *
from utilities.custom_logger import *
import logging


@pytest.mark.usefixtures("get_survey")
class TestSurveyOperation(unittest.TestCase):
    log = customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_level_setup(self,get_survey):
        self.operation_survey=EditElements(get_survey)

    @pytest.mark.run(order=1)
    def test_survey_operation(self):
        self.log.info("test_survey_operation started")
        self.operation_survey.survey_operations(new_survey_title, new_page_title)
        result = self.operation_survey.verify_surveyoperation_successful()
        self.log.info("Result: " + str(result))
        assert result == True
