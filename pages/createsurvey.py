from base.base_page import BasePage

class CreateSurvey(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _create_survey_link = "//a[text()='CREATE SURVEY']"
    _survey_name_textbox = "surveyTitle"
    _survey_options = "//div[text()='Survey category']"
    _category_list=['react-select-2--option-']
    _select_community =_category_list[0]+str(0)
    _select_customer_feedback = _category_list[0]+str(1)
    _select_customer_satisfaction = _category_list[0]+str(2)
    _select_demographics = _category_list[0]+str(3)
    _select_education = _category_list[0]+str(4)
    _select_events = _category_list[0]+str(5)
    _select_healthcare = _category_list[0]+str(6)
    _select_human_resources = _category_list[0]+str(7)
    _select_industry_specific = _category_list[0]+str(8)
    _select_just_for_fun = _category_list[0]+str(9)
    _select_market_research = _category_list[0]+str(10)
    _select_non_profit = _category_list[0]+str(11)
    _select_political = _category_list[0]+str(12)
    _select_other = _category_list[0]+str(13)
    _create_survey_button = "//button[text()='CREATE SURVEY']"
    _popup_Remove = "//div[@class='dialog-btn-bar']//a[contains(text(),'REMOVE')]"
    _survey_body = "create"
    _from_scratch = "scratch"
    _design_survey="//a[text()='DESIGN SURVEY']"

    # method to click on survey link
    def click_survey_link(self):
        self.element_click(self._create_survey_link, locator_type="xpath")

    #method to click on from scratch
    def click_from_scratch_link(self):
        self.element_click(self._from_scratch)

    # method to send title
    def send_title(self,first_survey_title):
        self.send_keys(first_survey_title, self._survey_name_textbox)

    # method to set survey category
    def send_survey_category(self):
        self.element_click(self._survey_options, locator_type="xpath")

    # method to select option
    def select_option(self):
        self.element_click(self._select_political,locator_type="id")

    # method to save survey
    def save_survey(self):
        self.element_click(self._create_survey_button,locator_type="xpath")

    # method to handle popup
    def handle_remove_popuup(self):
        self.element_click(self._popup_Remove, locator_type="xpath")

    # method to create survey
    def create_survey(self,first_survey_title=""):
        CreateSurvey.click_survey_link(self)
        if(self.is_element_present(locator=self._from_scratch)):
            CreateSurvey.click_from_scratch_link(self)
        CreateSurvey.send_title(self, first_survey_title)
        CreateSurvey.send_survey_category(self)
        CreateSurvey.select_option(self)
        CreateSurvey.save_survey(self)
        if(self.is_element_present(locator=self._popup_Remove,locator_type="xpath")):
            CreateSurvey.handle_remove_popuup(self)

    def verify_createsurvey_successful(self):
        self.wait_for_element(locator=self._design_survey,locator_type="xpath")
        result = self.is_element_present(locator=self._design_survey,locator_type="xpath")
        return result