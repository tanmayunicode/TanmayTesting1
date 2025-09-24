import time

from selenium.webdriver.chrome.options import Options

from TestFrameworkDevelopment.pageObjects.HomePageObjects import HomePage
from TestFrameworkDevelopment.pageObjects.LoginPageObjects import LoginPage
from selenium import webdriver
import pytest

from TestFrameworkDevelopment.pageObjects.WelcomePageObjects import WelcomePage

class TestValidateUser:

    def test_validateUser(self):

        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("http://localhost/uth/gadgetsgallery/catalog/index.php")

        self.hp = HomePage(self.driver)
        self.hp.clickLogyourselfIn()
        time.sleep(1)
        self.lp = LoginPage(self.driver)
        self.lp.setEmailAddress("demo2@unicodetechnologies.in")
        self.lp.setPassword("unicode")
        self.lp.clickSignIn()

        self.wp = WelcomePage(self.driver)
        self.welcomeText = self.wp.txt_welcomeTxt_xpath

        if self.welcomeText=="Nirmal!":
            print("User is logged in successfully")
        else:
            print("Invalid email address or password")

        time.sleep(10)
