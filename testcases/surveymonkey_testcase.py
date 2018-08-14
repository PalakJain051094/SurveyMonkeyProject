import pytest
from utilities.sendkeysconfig import *
from base.browsersetup import DriverSet
from pages.login_page import LoginPage
from pages.createsurvey import CreateSurvey
from pages.survey_operations import EditElements
from pages.surveyquestions import SurveyQuestionPage

@pytest.fixture(scope='module')
def get_driver():
    web_driver = DriverSet()
    driver = web_driver.get_web_driver_instance()
    return driver

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
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=3)
def test_create_survey(get_driver):
    print("test_create_survey started")
    cs = CreateSurvey(get_driver)
    cs.create_survey(first_survey_title)
    result=cs.verify_createsurvey_successful()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=4)
def test_survey_operation(get_driver):
    print("test_survey_operation started")
    operation_survey=EditElements(get_driver)
    operation_survey.survey_operations(new_survey_title,new_page_title)
    result = operation_survey.verify_surveyoperation_successful()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=5)
def test_question_1(get_driver):
    print("test_question_1 started")
    survey_questions = SurveyQuestionPage(get_driver)
    survey_questions.add_question_one(question_no_1)
    result = survey_questions.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=6)
def test_question_2(get_driver):
    print("test_question_2 started")
    survey_questions = SurveyQuestionPage(get_driver)
    survey_questions.add_question_two(question_no_2)
    result = survey_questions.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=7)
def test_question_3(get_driver):
    print("test_question_3 started")
    survey_questions = SurveyQuestionPage(get_driver)
    survey_questions.add_question_three(question_no_3)
    result = survey_questions.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=8)
def test_question_4(get_driver):
    print("test_question_4 started")
    survey_questions = SurveyQuestionPage(get_driver)
    survey_questions.add_question_four(question_no_4)
    result = survey_questions.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=9)
def test_question_5(get_driver):
    print("test_question_5 started")
    survey_questions = SurveyQuestionPage(get_driver)
    survey_questions.add_question_five(question_no_5)
    result = survey_questions.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=10)
def test_question_6(get_driver):
    print("test_question_6 started")
    survey_questions = SurveyQuestionPage(get_driver)
    survey_questions.add_question_six(question_no_6)
    result = survey_questions.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=11)
def test_question_7(get_driver):
    print("test_question_7 started")
    survey_questions = SurveyQuestionPage(get_driver)
    survey_questions.add_question_seventh(question_no_7)
    result = survey_questions.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=12)
def test_question_8(get_driver):
    print("test_question_8 started")
    survey_questions = SurveyQuestionPage(get_driver)
    survey_questions.add_question_eight(question_no_8)
    result = survey_questions.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=13)
def test_question_9(get_driver):
    print("test_question_9 started")
    survey_questions = SurveyQuestionPage(get_driver)
    survey_questions.add_question_nine(question_no_9)
    result = survey_questions.verify_question()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=14)
def test_question_10(get_driver):
    print("test_question_10 started")
    survey_questions = SurveyQuestionPage(get_driver)
    survey_questions.add_question_ten(question_no_10)
    result = survey_questions.verify_question()
    print("Result: " + str(result))
    assert result == True
