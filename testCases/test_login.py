import pytest
from utilities.customLogger import LogGen
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from pageObjects.LoginPage import LoginPage 
from selenium.webdriver.support import expected_conditions as EC 
from utilities.readProperties import ReadConfig
import time

class Test_001_Login:
    logger = LogGen.loggen()
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login ***************")
        self.logger.info("*************** Verifying Home Page Title ***************")
        self.driver, self.wait = setup
        self.driver.get(self.base_URL)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button-1 login-button")]')))
        actual_title = self.driver.title
        if actual_title=="Your store. Login":
            assert True, "PageTitle Matched!"
            self.logger.info("*************** Home Page Title Test is Passed ***************")
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error("*************** Home page title test is failed ***************")
            self.driver.quit()
            assert False, "PageTitle Didn't Matched!"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver, self.wait = setup
        self.logger.info("*************** Test_001_Login ***************")
        self.driver.get(self.base_URL)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button-1 login-button")]')))
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title 
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("*************** Login test is Passed ***************")
            self.driver.quit()
            assert True 
            
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.logger.error("*************** Login test is failed ***************")
            self.driver.quit()
            assert False
