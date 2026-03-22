#NOTE: In this file, we'll fetch the test data from .json file
import json

import pytest

from PageObjects_Inheritance.LoginII import LoginPageII

json_file_path = '../Data/test_POMSampleProjecte2e.json'   #path of the file that contains test data
with open(json_file_path) as f:    #opening the file (f= object)
    test_data = json.load( f )       #json.load() method converts the .json file data into python data
    test_list = test_data["data"]  # "data" --> dictionary's key in .json file
                                   # here, dictionary values from .json file is extracted and stored it in the list type variable 'test_list'



#use parameterized fixture to send the list data that is extracted from dictionary in .json
#this parameterized fixture will run separate iterations with different indices of the list in .json
#("test_list_item") is a list-variable into which the elements of dictionary-List 'test_list' are stored one by one for each iteration

@pytest.mark.smoketesting    #Resolving the registration warning (check file = .ini)
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):     # fixture's param whose values are going to be used inside this method should be passed as an argument to the same method
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise")

    #Login flow
    loginPage = LoginPageII(driver)    #Activating the driver for Child class (LoginPageII)
                                       #Activation of driver for parent class is also needed
                                       #Parent class driver activated in file (LoginII) with below syntax:
                                       #line-29:  (super().__init__(driver))

    print(loginPage.getTitle())      #fetching getTitle() from parent class (PageObj_InheritanceConcept)

    shoppingPage = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])


    shoppingPage.add_to_cart(test_list_item["productName"])   # Add item to cart

    print(shoppingPage.getTitle())

    cartPage = shoppingPage.go_to_cart()     # Navigate to checkout (i.e cart) page
    cartPage.checkout()                      # Click on 'Checkout' button on cart page
    cartPage.enter_delivery_address("ind")   # Enter country name in auto-suggest dropdown
    cartPage.validate_order()                # fetch the text from the success message

    #Comment added in the cloned folder
    #Comment added in GitPractice User B folder -- while Pull command
    #Comment added after creating Sub branch 'development' Architect A