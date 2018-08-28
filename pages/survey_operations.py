from base.base_page import BasePage
import time


class EditElements(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _survey_title = "//span[@class='title-text']"
    _survey_title_box = "surveyTitle"
    _save_new_survey_title = "//form[@id='surveyTitleForm']//a[text()='SAVE']"
    _pagetitle_edit = "//span[text()='PAGE TITLE']"
    _page_title = "pageTitle"
    _save_pagetitle = " //form[@id='pageTitleForm']//a[text()='SAVE'] "
    _survey_body = "create"
    _design_survey = "//a[text()='DESIGN SURVEY']"

    # method to click on survey_title_link
    def survey_title_link(self):
        self.wait_for_element(locator=self._survey_title, locator_type="xpath", pollFrequency=1)
        self.element_click(self._survey_title, locator_type="xpath")

    # method to send title
    def send_survey_title(self,new_survey_title):
        self.wait_for_element(locator=self._survey_title_box, locator_type="xpath", pollFrequency=1)
        self.clear_field(locator=self._survey_title_box)
        self.send_keys(new_survey_title, self._survey_title_box)

    #method to save survey
    def save_survey(self):
        self.wait_for_element(locator=self._save_new_survey_title, locator_type="xpath", pollFrequency=1)
        self.element_click(self._save_new_survey_title, locator_type="xpath")

    #method to edit survey title
    def edit_survey_title(self,new_survey_title):
        EditElements.survey_title_link(self)
        EditElements.send_survey_title(self,new_survey_title)
        EditElements.save_survey(self)

    # method to click on page_title_link
    def page_title_link(self):
        time.sleep(5)
        self.element_click(self._pagetitle_edit, locator_type="xpath")

    # method to send page_title
    def send_page_title(self, new_page_title):
        self.send_keys(new_page_title, self._page_title)

    # method to save page_title
    def save_page_title(self):
        self.element_click(self._save_pagetitle, locator_type="xpath")

    # method to edit PAGE title
    def edit_page_title(self,new_page_title):
        EditElements.page_title_link(self)
        EditElements.send_page_title(self, new_page_title)
        EditElements.save_page_title(self)

    # call edit page and edit survey methods
    def survey_operations(self,new_survey_title="",new_page_title=""):
        EditElements.edit_survey_title(self,new_survey_title)
        EditElements.edit_page_title(self,new_page_title)

    def verify_surveyoperation_successful(self):
        self.wait_for_element(locator=self._design_survey, locator_type="xpath")
        result = self.is_element_present(locator=self._design_survey, locator_type="xpath")
        return result