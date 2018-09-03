from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities.custom_logger import*
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumDriver():

    log =customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
           return By.NAME
        elif locator_type == "xpath":
           return By.XPATH
        elif locator_type == "css":
           return By.CSS_SELECTOR
        elif locator_type == "class":
           return By.CLASS_NAME
        elif locator_type == "link":
           return By.LINK_TEXT
        else:
           print("Locator type " + locator_type + " not correct/supported")
           return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def send_keys(self, data, locator="", locator_type="id", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locator_type)
            print_stack()

    def clear_field(self, locator="", locator_type="id"):
        """
        Clear an element field
        """
        element = self.get_element(locator, locator_type)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
        " locatorType: " + locator_type)

    def wait_for_element(self, locator, locator_type="id",
                               timeout=60, pollFrequency=1):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def is_element_present(self, locator="", locator_type="id", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locator_type)
                return False
        except:
            self.log.info("Element not found")
            return False

    def web_scroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def drag_drop(self,source_locator,destination_locator,locator_type="id"):
        source_element = None
        destination_element = None
        action = None
        try:
            if source_locator:
                source_element = self.get_element(source_locator, locator_type)
                self.log.info("source_element is found "+source_locator+"with locator type"+ locator_type)
            if  destination_locator:
                destination_element = self.get_element(destination_locator, locator_type)
                self.log.info("destination element is found " + destination_locator + "with locator type" + locator_type)

            actionChains = ActionChains(self.driver)
            self.log.info(actionChains)
            action = actionChains.drag_and_drop(source_element, destination_element).perform()
            self.log.info(action)
            self.log.info("drag and drop done")

        except:
            self.log.info("Cannot perfrom drag nad drop " + source_locator +
                  " locatorType: " + locator_type)
            print_stack()
