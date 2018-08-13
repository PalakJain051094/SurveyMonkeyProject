from utilites.elementsxpath import*
from utilites.testdata import*
from selenium.webdriver.common.by import By
import time


class CreateSurvey():

    def create_new_survey(self,driver):
        create_survey=self.driver.find_element(By.XPATH,create_survey_link)
        create_survey.click()
        survey_name_box=self.driver.find_element(By.XPATH,survey_name_textbox)
        survey_name_box.send_keys(survey_name)
        surey_category=self.driver.find_element(By.XPATH,survey_options)
        surey_category.click()
        option_selected=self.driver.find_element(By.XPATH,select_political)
        option_selected.click()
        survey_button=self.driver.find_element(By.XPATH,create_survey_button)
        survey_button.click()








