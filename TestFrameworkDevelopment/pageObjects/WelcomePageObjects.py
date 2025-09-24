from selenium.webdriver.common.by import By


class WelcomePage:

    txt_welcomeTxt_xpath="//span[@class='greetUser']"

    def __init__(self,driver):
        self.driver=driver

    def getWelcomeText(self):
        return self.driver.find_element(By.XPATH,self.txt_welcomeTxt_xpath).text