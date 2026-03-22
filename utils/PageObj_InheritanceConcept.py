#Associated file = test_InheritanceDataDrivenPOMSampleProjectse2e.py
#Associated Directory = PageObjects_Inheritance

#This file/class is created under the directory named as -'utils'
#In this file, we are creating a class 'PageObj_InheritanceConcept' --> PARENT CLASS
#This class contains common code of fetching page titles of all pages in above associated file
#Hence, 'PageObjects_Inheritance' directory is the duplicated version of 'PageObjects' to show this Inheritance concept
#In 'PageObjects_Inheritance' is

class PageObj_InheritanceConcept:

    def __init__(self, driver):
        self.driver = driver


    def getTitle(self):
        return self.driver.title