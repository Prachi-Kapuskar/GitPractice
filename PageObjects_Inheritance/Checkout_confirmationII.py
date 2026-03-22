from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.PageObj_InheritanceConcept import PageObj_InheritanceConcept


class checkout_confirmationII(PageObj_InheritanceConcept):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.XPATH, "//td/button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.consent_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.XPATH, "//input[@type='submit']")
        self.success_msg = (By.CLASS_NAME, "alert-success")


    def checkout(self):

        # Click on 'Checkout' button on cart page
        self.driver.find_element(*self.checkout_button).click()


    def enter_delivery_address(self, country_name):

        # Enter the country name in auto-suggest dropdown
        self.driver.find_element(*self.country_input).send_keys(country_name)

        # Wait until the dropdown options are visible - EXPLICIT WAIT
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))   #no * needed because, expected_condition() accepts tuple only
        self.driver.find_element(*self.country_option).click()

        # Click on Checkbox
        self.driver.find_element(*self.consent_checkbox).click()

        # Click on Submit/Purchase
        self.driver.find_element(*self.submit_button).click()


    def validate_order(self):

        # fetch the text from the success message
        SuccessMsg = self.driver.find_element(*self.success_msg).text
        assert "Success! Thank you!" in SuccessMsg