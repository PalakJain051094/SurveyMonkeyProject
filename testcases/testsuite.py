import unittest
from testcases.test_login import TestLogin
from testcases.test_createsurvey import TestCreateSurvey
from testcases.test_surveyoperation import TestSurveyOperation
from testcases.test_question import TestQuestion

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCreateSurvey)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestSurveyOperation)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestQuestion)
# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner(verbosity=2).run(smokeTest)