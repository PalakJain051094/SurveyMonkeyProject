from selenium import webdriver
import os
import time


class DriverSet():

    def setDriver(self):
        driverlocation = "D:\\Python_workspace\\seleniumlib\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver