from selenium.webdriver.common.by import By


class HomePage:

    lnk_logyourselfin_linkText="log yourself in"
    lnk_createanaccount_linkText="create an account"

    def __init__(self,driver):
        self.driver=driver

    def clickLogyourselfIn(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_logyourselfin_linkText).click()