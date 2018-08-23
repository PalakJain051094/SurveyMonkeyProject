from base.base_page import BasePage
import time
from utilities.sendkeysconfig import*


class SurveyQuestionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Add questions in survey
    _question_title_box = "editTitle"
    _question_type = "changeQType"
    _save_question = "//div[@id='editQuestion']//section[@class='t1']//a[text()='SAVE']"
    _next_question = "//div[@class='add-question-btn zero-state-hide ui-droppable']//a[contains(text(),'NEW QUESTION')]"

    # question 1
    _question_first_type = "//ul[@class='add-q-menu-left']//a[text()='Single Textbox']"

    # question 2
    _question_two_and_nine_type = "//ul[@class='add-q-menu-left']//a[text()='Multiple Choice']"
    _question_two_select_type = "//option[contains(text(),'Always - Never')]"

    # question 3
    _question_third_type = "//ul[@class='add-q-menu-right']//a[text()='Date / Time']"
    _time_info_box = "//table[@id='rows']//label[text()='Time Info']"

    # question 4
    _question_four_type = "//ul[@class='add-q-menu-left']//a[text()='Star Rating']"

    # question 5
    _question_five_type = "//ul[@class='add-q-menu-right']//a[text()='Dropdown']"
    _question_select_choice = "answerBankCategorySelect"

    # question 6
    _question_six_type = "//ul[@class='add-q-menu-left']//a[text()='Checkboxes']"
    _checkbox_1 = "//section[2]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[2]/div[1]/div[1]"
    _checkbox_2 = "//section[2]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[5]/td[2]/div[1]/div[1]"
    _checkbox_3 = "//section[2]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[6]/td[2]/div[1]/div[1]"
    _checkbox_4 = "//section[2]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[7]/td[2]/div[1]/div[1]"
    _checkbox_5 = "//section[2]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[8]/td[2]/div[1]/div[1]"

    # question 7
    _question_seven_type = "//ul[@class='add-q-menu-right']//a[text()='Matrix / Rating Scale']"
    _row_label_1 = "//section[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]"
    _row_label_2 = "//section[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/div[1]"
    _row_label_3 = "//section[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[1]"
    _column_label_1 = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]"
    _column_label_2 = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]"
    _column_label_3 = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/div[1]"
    _column_label_4 = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[1]"
    _remove_label = "//tr[6]//a[@title='Delete this choice.']"

    # question 8
    _question_eight_type = "//ul[@class='add-q-menu-right']//a[text()='Multiple Textboxes']"
    _multiple_textbox_level_1 = "//section[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]"
    _multiple_textbox_level_2 = "//section[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/div[1]"
    _multiple_textbox_level_3 = "//section[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[1]"

    # question 9
    _question_nine_select_type = "//option[contains(text(),'Yes - No')]"

    # question 10
    _question_ten_type = "//ul[@class='add-q-menu-left']//a[text()='Comment Box']"

    _survey_body = "create"

    # method to save and next question
    def save_and_next(self):
        self.wait_for_element(locator=self._save_question, locator_type="xpath", timeout=5,pollFrequency=1)
        time.sleep(5)
        self.element_click(self._save_question,locator_type="xpath")
        self.wait_for_element(locator=self._next_question, locator_type="xpath", timeout=5, pollFrequency=1)
        time.sleep(5)
        self.element_click(self._next_question,locator_type="xpath")

    # method to get question type
    def get_question_type(self):
        self.element_click(self._question_type)

    # method to add 1st question
    def add_question_one(self,question_no_1=""):
        self.send_keys(question_no_1, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.element_click(self._question_first_type, locator_type="xpath")
        SurveyQuestionPage.save_and_next(self)


    # method to add 2nd question
    def add_question_two(self, question_no_2=""):
        self.send_keys(question_no_2, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.element_click(self._question_two_and_nine_type, locator_type="xpath")
        self.element_click(self._question_select_choice)
        self.element_click(self._question_two_select_type, locator_type="xpath")
        SurveyQuestionPage.save_and_next(self)


    # method to add 3rd question
    def add_question_three(self, question_no_3=""):
        self.send_keys(question_no_3, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.element_click(self._question_third_type, locator_type="xpath")
        self.element_click(self._time_info_box, locator_type="xpath")
        SurveyQuestionPage.save_and_next(self)

    # method to add 4th question
    def add_question_four(self, question_no_4=""):
        self.send_keys(question_no_4, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_four_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_four_type, locator_type="xpath")
        SurveyQuestionPage.save_and_next(self)

    # method to add 5th question
    def add_question_five(self, question_no_5=""):
        self.send_keys(question_no_5, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_five_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_five_type, locator_type="xpath")
        self.element_click(self._question_select_choice)
        self.wait_for_element(locator=self._question_nine_select_type, locator_type="xpath",pollFrequency=1)
        self.element_click(self._question_nine_select_type,locator_type="xpath")
        SurveyQuestionPage.save_and_next(self)

    # method to add 6th question
    def add_question_six(self, question_no_6=""):
        self.send_keys(question_no_6, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_six_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_six_type, locator_type="xpath")
        SurveyQuestionPage.set_checkboxes(self)
        SurveyQuestionPage.save_and_next(self)

    # set checkboxes
    def set_checkboxes(self):
        self.send_keys(checkbox_1_data, self._checkbox_1,locator_type="xpath")
        self.send_keys(checkbox_2_data, self._checkbox_2, locator_type="xpath")
        self.send_keys(checkbox_3_data, self._checkbox_3, locator_type="xpath")
        self.send_keys(checkbox_4_data, self._checkbox_4, locator_type="xpath")
        self.send_keys(checkbox_5_data, self._checkbox_5, locator_type="xpath")

    # method to add 7th question
    def add_question_seventh(self, question_no_7=""):
        self.send_keys(question_no_7, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_seven_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_seven_type, locator_type="xpath")
        SurveyQuestionPage.set_labels_matix(self)
        SurveyQuestionPage.save_and_next(self)

    # method to set rows
    def set_labels_matix(self):
        self.send_keys(scale_1, self._row_label_1, locator_type="xpath")
        self.send_keys(scale_2, self._row_label_2, locator_type="xpath")
        self.send_keys(scale_3, self._row_label_3, locator_type="xpath")
        self.send_keys(one, self._column_label_1, locator_type="xpath")
        self.send_keys(two, self._column_label_2, locator_type="xpath")
        self.send_keys(three, self._column_label_3, locator_type="xpath")
        self.send_keys(four, self._column_label_4, locator_type="xpath")
        self.element_click(self._remove_label, locator_type="xpath")

    # method to add 8th question
    def add_question_eight(self,question_no_8=""):
        self.send_keys(question_no_8, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_eight_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_eight_type, locator_type="xpath")
        SurveyQuestionPage.set_multipletextbox_label(self)
        SurveyQuestionPage.save_and_next(self)

    # method to set textboxes
    def set_multipletextbox_label(self):
        self.send_keys(multiple_textbox_label_1, self._multiple_textbox_level_1, locator_type="xpath")
        self.send_keys(multiple_textbox_label_2, self._multiple_textbox_level_2, locator_type="xpath")
        self.send_keys(multiple_textbox_label_3, self._multiple_textbox_level_3, locator_type="xpath")

    # method to add 9th question
    def add_question_nine(self, question_no_9=""):
        self.send_keys(question_no_9, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_two_and_nine_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_two_and_nine_type, locator_type="xpath")
        self.wait_for_element(locator=self._question_select_choice, pollFrequency=1)
        self.element_click(self._question_select_choice)
        self.wait_for_element(locator=self._question_nine_select_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_nine_select_type, locator_type="xpath")
        SurveyQuestionPage.save_and_next(self)

    # method to add 10th question
    def add_question_ten(self, question_no_10=""):
        self.send_keys(question_no_9, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.element_click(self._question_ten_type, locator_type="xpath")
        self.wait_for_element(locator=self._save_question, locator_type="xpath", timeout=5, pollFrequency=1)
        time.sleep(5)
        self.element_click(self._save_question, locator_type="xpath")

    def verify_question(self):
        self.wait_for_element(locator=self._survey_body, timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._survey_body)
        return result
