import pytest
import unittest
from pages.surveyquestions import SurveyQuestionPage
from utilities.sendkeysconfig import *
from utilities.custom_logger import *
import logging


@pytest.mark.usefixtures("get_survey")
class TestQuestions(unittest.TestCase):
    log = customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_level_setup(self, get_survey):
        self.survey_questions = SurveyQuestionPage(get_survey)

    @pytest.mark.run(order=1)
    def test_question_1(self):
        self.log.info("test_question_1 started")
        self.survey_questions.add_question_one(question_no_1)
        result = self.survey_questions.verify_question_one()
        self.log.info("Result: " + result)
        results = list(result)
        self.log.info(results)
        result1 = bool(results[0])
        self.log.info(result1)
        result2 = bool(results[1])
        self.log.info(result2)
        if ((result1==True) and (result2==True)):
            assert True
        else:
            assert False

