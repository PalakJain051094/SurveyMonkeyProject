from selenium import webdriver
import os
from base.browserconfig import *

class DriverSet():

    def __init__(self):
        browser_type = browser.upper()

    def get_web_driver_instance(self):
        browser_type = browser.upper()
        if (browser_type == "CHROME"):
            return DriverSet.set_chrome_driver(self)
        elif (browser_type == "IE"):
            return DriverSet.set_fire_fox_driver(self)
        elif (browser_type == "FIREFOX"):
            return DriverSet.set_internet_explorer(self)
        else:
            print("Not a Valid browser Please enter 'chrome','ie' or 'firefox' only ")

    #method to set chrome browser
    def set_chrome_driver(self):
        driverlocation = "D:\\Python_workspace\\seleniumlib\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        self.driver = webdriver.Chrome(driverlocation)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    #method to set fire fox driver
    def set_fire_fox_driver(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    # method to set internet explorer driver
    def set_internet_explorer(self):
        driverlocation="D:\\Python_workspace\\seleniumlib\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"]=driverlocation
        self.driver=webdriver.Ie(driverlocation)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver