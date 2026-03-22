#Page Object Model:
#Associated test file = test_POMSampleProjecte2e.py

# A directory is created named as 'PageObjects' --> it is like a folder
# This current file 'LoginII.py' is created under this 'PageObjects' folder/directory

#Concept:
# A separate CLASS is created for every WEBPAGE
# All locators, actions etc associated with a webpage will go into its respective class
# This class and its objects can be easily called in the main test script

from selenium.webdriver.common.by import By

from PageObjects.ShopPage import ShopPage
from PageObjects_Inheritance.ShopPageII import ShopPageII
from utils.PageObj_InheritanceConcept import PageObj_InheritanceConcept


class LoginPageII(PageObj_InheritanceConcept):     #'LoginPage' class inherited the parent (PageObj_InheritanceConcept)

                                   #defining a constructor, self is by default present for all class methods & constructors
    def __init__(self, driver):    #self: instance/object of class. It is 1st argument/parameter of constructor/method
                                   #driver: passing driver as an argument, this means whoever calling this (LoginPage) class, they are forced to call with (driver) variable
                                   #How to forcefully call the class with driver variable in the main test script file?
                                   # ANS:--> loginPage_obj = LoginPage(driver)
                                   # 'driver' is originally present in main test file
                                   # 'driver' is sent to this Page Object file from the test file

        super().__init__(driver)   #super()= refer to parent class (PageObj_InheritanceConcept.py) by creating parent constructor -- activation of parent's driver
        self.driver = driver  # Making 'driver' globally available outside this constructor


        #Creating Tuple variables below inside the constructor:
        #Below variables are only limited to constructor unless (self.variableName) is used
        #(self.variableName) --> 'self' makes it globally available in the entire class
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signin_btn = (By.ID, "signInBtn")


    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signin_btn).click()

        shoppingPage = ShopPageII(self.driver)    #after login, default navigation is to shopping page
        return shoppingPage       #this means: login() returns the obj 'shoppingPage'
                                  #therefore, the value of login() = shoppingPage


        # NOTE-1: (*) symbol used as a prefix of tuple variables:
        # (*) splits the tuple into 2 arguments -> (By.ID) and ("username")
        # Why the splitting required? --> ANS: find_element() method only accepts 2 arguments NOT tuple


        #NOTE-2: Whenever any action on one page takes the flow to another page, then:
        # --> create the object for that destination page on the source page's method only -- line-42 & 43 in file (LoginII.py)
        # --> And then, while calling this source method in the main test file, assign this destination page's object to the source method (check below)
        # --> line-19 in file (test_POMSampleProjecte2e.py)



