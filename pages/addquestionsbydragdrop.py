from base.base_page import BasePage
import time
from utilities.sendkeysconfig import*



# add question by drag and  drop
class SurveyQuestion(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _design = "//li[@title='Builder']"
    _question_title_box = "editTitle"
    _editquestion_div= "editQuestion"
    _question_type = "changeQType"
    _save_question = "//div[@id='editQuestion']//section[@class='t1']//a[text()='SAVE']"
    _new_question = "//div[@id='livePreview']//a[text()='NEW QUESTION']"
    _cancel = "//div[@id='editQuestion']//section[@class='t1']//a[text()='CANCEL']"
    _destination="//div[@class='add-question-btn zero-state-hide ui-droppable']"

    #question1
    _question_1_type = "//div[@id='builderQuestionContainer']//span[text()='Single Textbox']"

    # question 2
    _question_2_type="//div[@id='builderQuestionContainer']//span[text()='Multiple Choice']"
    _question_two_select_type = "//option[contains(text(),'Always - Never')]"
    _question_select_choice = "answerBankCategorySelect"

    #question 5th
    _question_five_type = "//div[@id='builderQuestionContainer']//span[text()='Dropdown']"

    # question 9th
    _question_nine_select_type = "//option[contains(text(),'Yes - No')]"

    # question 10th
    _question_ten_type = "//div[@id='builderQuestionContainer']//span[text()='Comment Box']"

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
    def add_question_1(self,question_no_1=""):
        self.element_click(self._design,locator_type="xpath")
        self.web_scroll(direction = "down")
        self.drag_drop(self._question_1_type,self._destination,locator_type="xpath")
        self.element_click(self._editquestion_div)
        self.send_keys(question_no_1, self._question_title_box)
        SurveyQuestion.save(self)

    def add_question_2(self, question_no_2=""):
        SurveyQuestion.next(self)
        self.element_click(self._design, locator_type="xpath")
        self.drag_drop(self._question_2_type, self._destination, locator_type="xpath")
        self.element_click(self._editquestion_div)
        self.send_keys(question_no_2, self._question_title_box)
        self.wait_for_element(self._question_select_choice, pollFrequency=1)
        self.element_click(self._question_select_choice)
        self.wait_for_element(self._question_two_select_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_two_select_type, locator_type="xpath")
        SurveyQuestion.save(self)

    def add_question_5(self, question_no_5=""):
        SurveyQuestion.next(self)
        self.element_click(self._design, locator_type="xpath")
        self.drag_drop(self._question_five_type, self._destination, locator_type="xpath")
        self.element_click(self._editquestion_div)
        self.send_keys(question_no_5, self._question_title_box)
        self.element_click(self._question_select_choice)
        self.wait_for_element(locator=self._question_nine_select_type, locator_type="xpath",pollFrequency=1)
        self.element_click(self._question_nine_select_type,locator_type="xpath")
        SurveyQuestion.save(self)


    def add_question_9(self, question_no_9=""):
        SurveyQuestion.next(self)
        self.element_click(self._design, locator_type="xpath")
        self.drag_drop(self._question_2_type, self._destination, locator_type="xpath")
        self.wait_for_element(self._question_title_box)
        self.element_click(self._editquestion_div)
        self.send_keys(question_no_9, self._question_title_box)
        self.wait_for_element(locator=self._question_select_choice, pollFrequency=1)
        self.element_click(self._question_select_choice)
        self.wait_for_element(locator=self._question_nine_select_type, locator_type="xpath", pollFrequency=1)
        self.element_click(self._question_nine_select_type, locator_type="xpath")
        SurveyQuestion.save(self)

    def add_question_10(self, question_no_10=""):
        SurveyQuestion.next(self)
        self.element_click(self._design, locator_type="xpath")
        self.drag_drop(self._question_ten_type, self._destination, locator_type="xpath")
        self.element_click(self._editquestion_div)
        self.send_keys(question_no_10, self._question_title_box)
        SurveyQuestion.save(self)