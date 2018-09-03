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
    _new_question = "//div[@id='livePreview']//a[text()='NEW QUESTION']"
    _cancel="//div[@id='editQuestion']//section[@class='t1']//a[text()='CANCEL']"

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

    #verify questions
    _text_1 = "//span[text()='"+ question_no_1+"']"
    _text_1_type="//a[@id='changeQType']//span[text()='" + type_singletextbox + "']"
    _text_2 = "//span[text()='"+ question_no_2+"']"
    _text_2_type = "//a[@id='changeQType']//span[text()='" + type_multiplechoice + "']"
    _text_3 = "//span[text()='"+ question_no_3+"']"
    _text_3_type = "//a[@id='changeQType']//span[text()='" + type_datetime + "']"
    _text_4 = "//span[text()='"+ question_no_4+"']"
    _text_4_type = "//a[@id='changeQType']//span[text()='" + type_starrating + "']"
    _text_5 = "//span[text()='"+ question_no_5+"']"
    _text_5_type = "//a[@id='changeQType']//span[text()='" + type_dropdown + "']"
    _text_6 = "//span[text()='"+ question_no_6+"']"
    _text_6_type = "//a[@id='changeQType']//span[text()='" + type_checkboxes + "']"
    _text_7 = "//span[text()='"+ question_no_7+"']"
    _text_7_type = "//a[@id='changeQType']//span[text()='" + type_matrix + "']"
    _text_8 = "//span[text()='"+ question_no_8+"']"
    _text_8_type = "//a[@id='changeQType']//span[text()='" + type_multipletextbox + "']"
    _text_9 = "//span[text()='"+ question_no_9+"']"
    _text_9_type = "//a[@id='changeQType']//span[text()='" + type_multiplechoice + "']"
    _text_10 = "//span[text()='"+ question_no_10+"']"
    _text_10_type = "//a[@id='changeQType']//span[text()='" + type_commentbox + "']"

    # method to save and next question
    def save(self):
        self.wait_for_element(locator=self._save_question, locator_type="xpath", timeout=5,pollFrequency=1)
        time.sleep(5)
        self.element_click(self._save_question,locator_type="xpath")

    def next(self):
        self.wait_for_element(locator=self._new_question, locator_type="xpath", timeout=5, pollFrequency=1)
        time.sleep(5)
        self.element_click(self._new_question, locator_type="xpath")

    def cancel(self):
        self.element_click(self._cancel, locator_type="xpath")

    # method to get question type
    def get_question_type(self):
        self.wait_for_element(self._question_type)
        self.element_click(self._question_type)

    # method to add 1st question
    def add_question_one(self,question_no_1=""):
        self.send_keys(question_no_1, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.element_click(self._question_first_type, locator_type="xpath")
        SurveyQuestionPage.save(self)

    # method to add 2nd question
    def add_question_two(self, question_no_2=""):
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_2, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_two_and_nine_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_two_and_nine_type, locator_type="xpath")
        self.wait_for_element(self._question_select_choice, pollFrequency=1)
        self.element_click(self._question_select_choice)
        self.wait_for_element(self._question_two_select_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_two_select_type, locator_type="xpath")
        SurveyQuestionPage.save(self)

    # method to add 3rd question
    def add_question_three(self, question_no_3=""):
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_3, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.element_click(self._question_third_type, locator_type="xpath")
        self.element_click(self._time_info_box, locator_type="xpath")
        SurveyQuestionPage.save(self)

    # method to add 4th question
    def add_question_four(self, question_no_4=""):
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_4, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_four_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_four_type, locator_type="xpath")
        SurveyQuestionPage.save(self)

    # method to add 5th question
    def add_question_five(self, question_no_5=""):
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_5, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_five_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_five_type, locator_type="xpath")
        self.element_click(self._question_select_choice)
        self.wait_for_element(locator=self._question_nine_select_type, locator_type="xpath",pollFrequency=1)
        self.element_click(self._question_nine_select_type,locator_type="xpath")
        SurveyQuestionPage.save(self)

    # method to add 6th question
    def add_question_six(self, question_no_6=""):
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_6, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_six_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_six_type, locator_type="xpath")
        SurveyQuestionPage.set_checkboxes(self)
        SurveyQuestionPage.save(self)

    # set checkboxes
    def set_checkboxes(self):
        self.send_keys(checkbox_1_data, self._checkbox_1,locator_type="xpath")
        self.send_keys(checkbox_2_data, self._checkbox_2, locator_type="xpath")
        self.send_keys(checkbox_3_data, self._checkbox_3, locator_type="xpath")
        self.send_keys(checkbox_4_data, self._checkbox_4, locator_type="xpath")
        self.send_keys(checkbox_5_data, self._checkbox_5, locator_type="xpath")

    # method to add 7th question
    def add_question_seventh(self, question_no_7=""):
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_7, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_seven_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_seven_type, locator_type="xpath")
        SurveyQuestionPage.set_labels_matix(self)
        SurveyQuestionPage.save(self)

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
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_8, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_eight_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_eight_type, locator_type="xpath")
        SurveyQuestionPage.set_multipletextbox_label(self)
        SurveyQuestionPage.save(self)

    # method to set textboxes
    def set_multipletextbox_label(self):
        self.send_keys(multiple_textbox_label_1, self._multiple_textbox_level_1, locator_type="xpath")
        self.send_keys(multiple_textbox_label_2, self._multiple_textbox_level_2, locator_type="xpath")
        self.send_keys(multiple_textbox_label_3, self._multiple_textbox_level_3, locator_type="xpath")

    # method to add 9th question
    def add_question_nine(self, question_no_9=""):
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_9, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.wait_for_element(locator=self._question_two_and_nine_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_two_and_nine_type, locator_type="xpath")
        self.wait_for_element(locator=self._question_select_choice, pollFrequency=1)
        self.element_click(self._question_select_choice)
        self.wait_for_element(locator=self._question_nine_select_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_nine_select_type, locator_type="xpath")
        SurveyQuestionPage.save(self)

    # method to add 10th question
    def add_question_ten(self, question_no_10=""):
        SurveyQuestionPage.next(self)
        self.send_keys(question_no_10, self._question_title_box)
        SurveyQuestionPage.get_question_type(self)
        self.element_click(self._question_ten_type, locator_type="xpath")
        SurveyQuestionPage.save(self)

    # success of questions(verification) by question title/text
    def verify_question_one(self):
        self.wait_for_element(locator=self._text_1, locator_type="xpath", timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._text_1, locator_type="xpath")
        return result

    def verify_question_two(self):
        self.wait_for_element(locator=self._text_2, locator_type="xpath", timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._text_2, locator_type="xpath")
        return result

    def verify_question_three(self):
        self.wait_for_element(locator=self._text_3, locator_type="xpath", timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._text_3, locator_type="xpath")
        return result

    def verify_question_four(self):
        self.wait_for_element(locator=self._text_4, locator_type="xpath", timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._text_4, locator_type="xpath")
        return result

    def verify_question_five(self):
        self.wait_for_element(locator=self._text_5, locator_type="xpath", timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._text_5, locator_type="xpath")
        return result

    def verify_question_six(self):
        self.wait_for_element(locator=self._text_6, locator_type="xpath", timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._text_6, locator_type="xpath")
        return result

    def verify_question_seven(self):
        self.wait_for_element(locator=self._text_7, locator_type="xpath", timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._text_7, locator_type="xpath")
        return result

    def verify_question_eight(self):
        self.wait_for_element(locator=self._text_8, locator_type="xpath", timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._text_8, locator_type="xpath")
        return result

    def verify_question_nine(self):
        self.wait_for_element(locator=self._text_9, locator_type="xpath", timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._text_9, locator_type="xpath")
        return result

    def verify_question_ten(self):
        self.wait_for_element(locator=self._text_10, locator_type="xpath", timeout=5, pollFrequency=1)
        result = self.is_element_present(locator=self._text_10, locator_type="xpath")
        return result

    # verification of question by question type and text/title
    # def verify_question_one(self):
    #     self.wait_for_element(locator=self._text_1, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result1 = self.is_element_present(locator=self._text_1, locator_type="xpath")
    #     self.element_click(self._text_1, locator_type="xpath")
    #     self.wait_for_element(locator=self._text_1_type, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result2 = self.is_element_present(locator=self._text_1_type, locator_type="xpath")
    #     results = [result1, result2]
    #     self.log.info(results)
    #     SurveyQuestionPage.save(self)
    #     return results

    # def verify_question_two(self):
    #     self.wait_for_element(locator=self._text_2, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result1 = self.is_element_present(locator=self._text_2, locator_type="xpath")
    #     self.element_click(self._text_2, locator_type="xpath")
    #     self.wait_for_element(locator=self._text_2_type, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result2 = self.is_element_present(locator=self._text_2_type, locator_type="xpath")
    #     results = [result1, result2]
    #     if (result1 and result2):
    #         return results
    #
    # def verify_question_three(self):
    #     self.wait_for_element(locator=self._text_3, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result1 = self.is_element_present(locator=self._text_3, locator_type="xpath")
    #     self.element_click(self._text_3, locator_type="xpath")
    #     self.wait_for_element(locator=self._text_3_type, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result2 = self.is_element_present(locator=self._text_3_type, locator_type="xpath")
    #     results = [result1, result2]
    #     if (result1 and result2):
    #         return results
    #
    # def verify_question_four(self):
    #     self.wait_for_element(locator=self._text_4, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result1 = self.is_element_present(locator=self._text_4, locator_type="xpath")
    #     self.element_click(self._text_4, locator_type="xpath")
    #     self.wait_for_element(locator=self._text_4_type, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result2 = self.is_element_present(locator=self._text_4_type, locator_type="xpath")
    #     results = [result1, result2]
    #     if (result1 and result2):
    #         return results
    #
    #
    # def verify_question_five(self):
    #     self.wait_for_element(locator=self._text_5, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result1 = self.is_element_present(locator=self._text_5, locator_type="xpath")
    #     self.element_click(self._text_5, locator_type="xpath")
    #     self.wait_for_element(locator=self._text_5_type, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result2 = self.is_element_present(locator=self._text_5_type, locator_type="xpath")
    #     results = [result1, result2]
    #     if (result1 and result2):
    #         return results
    #
    # def verify_question_six(self):
    #     self.wait_for_element(locator=self._text_6, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result1 = self.is_element_present(locator=self._text_6, locator_type="xpath")
    #     self.element_click(self._text_6, locator_type="xpath")
    #     self.wait_for_element(locator=self._text_6_type, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result2 = self.is_element_present(locator=self._text_6_type, locator_type="xpath")
    #     results = [result1, result2]
    #     if (result1 and result2):
    #         return results
    #
    # def verify_question_seven(self):
    #     self.wait_for_element(locator=self._text_7, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result1 = self.is_element_present(locator=self._text_7, locator_type="xpath")
    #     self.element_click(self._text_7, locator_type="xpath")
    #     self.wait_for_element(locator=self._text_7_type, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result2 = self.is_element_present(locator=self._text_7_type, locator_type="xpath")
    #     results = [result1, result2]
    #     if (result1 and result2):
    #         return results
    #
    # def verify_question_eight(self):
    #     self.wait_for_element(locator=self._text_8, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result1 = self.is_element_present(locator=self._text_8, locator_type="xpath")
    #     self.element_click(self._text_2, locator_type="xpath")
    #     self.wait_for_element(locator=self._text_8_type, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result2 = self.is_element_present(locator=self._text_8_type, locator_type="xpath")
    #     results = [result1, result2]
    #     if (result1 and result2):
    #         return results
    #
    # def verify_question_nine(self):
    #     self.wait_for_element(locator=self._text_9, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result1 = self.is_element_present(locator=self._text_9, locator_type="xpath")
    #     self.element_click(self._text_9, locator_type="xpath")
    #     self.wait_for_element(locator=self._text_9_type, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result2 = self.is_element_present(locator=self._text_9_type, locator_type="xpath")
    #     results = [result1, result2]
    #     if (result1 and result2):
    #         return results
    #
    # def verify_question_ten(self):
    #     self.wait_for_element(locator=self._text_10, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result1 = self.is_element_present(locator=self._text_10, locator_type="xpath")
    #     self.element_click(self._text_10, locator_type="xpath")
    #     self.wait_for_element(locator=self._text_10_type, locator_type="xpath", timeout=5, pollFrequency=1)
    #     result2 = self.is_element_present(locator=self._text_10_type, locator_type="xpath")
    #     results = [result1, result2]
    #     if (result1 and result2):
    #         return results
