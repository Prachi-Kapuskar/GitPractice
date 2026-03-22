from selenium.webdriver.common.by import By

from PageObjects.Checkout_confirmation import checkout_confirmation
from utils.PageObj_InheritanceConcept import PageObj_InheritanceConcept


class ShopPageII(PageObj_InheritanceConcept):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, " a[href*='shop']")
        self.cards_list = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button =(By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_to_cart(self, item_name):
        self.driver.find_element(*self.shop_link).click()  # Regex= a[href*='Shop'] --instead of giving entire Href string, * can be used and partial string can be used

        # Find the desired product from the list of products
        products = self.driver.find_elements(*self.cards_list)

        for product in products:
            ProductName = product.find_element(By.XPATH, "div/h4/a").text    #sub xpath -- keep as is
            if ProductName == item_name:
                product.find_element(By.XPATH, "div/button").click()


    def go_to_cart(self):
        self.driver.find_element(*self.checkout_button).click()
        cartPage = checkout_confirmation(self.driver)
        return cartPage
