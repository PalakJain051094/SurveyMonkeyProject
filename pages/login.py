from utilites.elementsxpath import*
from utilites.testdata import*

class Login():


    def get_loginpage(self,driver):

        login = self.driver.find_element_by_xpath(login_link)
        login.click()
        user = self.driver.find_element_by_xpath(username_textbox)
        user.send_keys(username)
        password= self.driver.find_element_by_xpath(password_textbox)
        password.send_keys(pass_word)
        button = self.driver.find_element_by_xpath(login_sumit_button)
        button.click()












