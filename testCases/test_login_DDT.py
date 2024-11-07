import pytest
from utilities.customLogger import LogGen
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from pageObjects.LoginPage import LoginPage 
from selenium.webdriver.support import expected_conditions as EC 
from utilities.readProperties import ReadConfig
from utilities import ExcelUtils

class Test_001_DDT_Login:
    logger = LogGen.loggen()
    base_URL = ReadConfig.getApplicationURL()
    path = 'TestData/LoginData.xlsx'

    @pytest.mark.regression   
    def test_login_DDT(self, setup):
        self.logger.info("*************** Test_002_DDT_Login ***************")
        self.logger.info("*************** Verifying Login DDT testCase ***************")
        self.driver, self.wait = setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button-1 login-button")]')))
        self.lp = LoginPage(self.driver)
        
        self.row = ExcelUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []
        for r in range(2, self.row+1):
            self.username = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            actual_title = self.driver.title 
            if actual_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("*************** Passed ***************")
                    self.lp.clickLogout() 
                    lst_status.append("Pass")
                    ExcelUtils.writeData(self.path, 'Sheet1', r, 4, "Pass")

                else:
                    self.logger.info("*************** Failed ***************")
                    self.driver.save_screenshot(".\\Screenshots\\"+"test_loginDDT.png")
                    self.lp.clickLogout() 
                    lst_status.append("Fail")

            else:
                if self.exp == "Pass":
                    self.logger.info("*************** Failed ***************")
                    self.driver.save_screenshot(".\\Screenshots\\"+"test_loginDDT.png")
                    lst_status.append("Fail")                
                else:
                    self.logger.error("*************** Passed ***************")
                    lst_status.append("Pass")
                    ExcelUtils.writeData(self.path, 'Sheet1', r, 4, "Pass")
        if "Fail" not in lst_status:
            self.logger.info('*************** Login DDT test Passed ***************')
            self.driver.quit()
        else:
            self.logger.info("*************** Login DDT test Failed ***************")
            self.driver.quit()
