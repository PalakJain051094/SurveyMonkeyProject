from base.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = "//a[text()='LOG IN']"
    _email_field = "username"
    _password_field = "password"
    _login_button = "//button[@type='submit']"
    _login_success="userAcctTab_MainMenu"
    _login_fail="//div[@id='sign-in']//li[contains(text(),'The username or password you entered is incorrect')]"
    _logout="//ul[@class='nav-submenu']//a[text()='Sign Out']"

    def click_login_link(self):
        self.element_click(self._login_link, locator_type="xpath")

    def enter_email(self, email):
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="xpath")

    def login(self, email="", password=""):
        LoginPage.click_login_link(self)
        self.clear_field(locator=self._email_field)
        LoginPage.enter_email(self,email)
        self.clear_field(locator=self._password_field)
        LoginPage.enter_password(self,password)
        LoginPage.click_login_button(self)

    def verify_login_successful(self):
        self.wait_for_element(locator=self._login_success, timeout=5,pollFrequency=1)
        result = self.is_element_present(locator=self._login_success)
        return result

    def verify_login_failed(self):
        result = self.is_element_present(locator=self._login_fail,locator_type="xpath")
        return result

