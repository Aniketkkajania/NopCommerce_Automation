import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen 
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomer
from pageObjects.AddCustomers import AddCustomers
import pytest 

class Test_SearchCustomerByName__005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("********** SearchCustomerByName__005 *************")
        self.driver, self.wait = setup 
        self.driver.get(self.baseURL)
        self.driver.maximize_window() 
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button-1 login-button")]')))

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********** Login Successful ************")
        self.logger.info("********** Start Searching Customer By Name ************")
        self.addcust = AddCustomers(self.driver, self.wait)
        self.addcust.clickOnCustomersMenu()
        opened = self.driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']").is_displayed()

        while not opened:
            self.addcust.clickOnCustomersMenu()
            opened = self.driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']").is_displayed()

            time.sleep(3)
        self.addcust.clickOnCustomerMenuItem()
        self.logger.info("********** Searching Customer By Name ************")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("Victoria")
        self.searchcust.setLastName("Terces")
        self.searchcust.clickOnSearch()
        time.sleep(4)
        self.driver.execute_script("window.scrollBy(0, 500);")
        table_visibility_text = self.driver.find_element(By.XPATH, '//table[@id="customers-grid"]').text
        while "Registered" not in table_visibility_text:
            self.driver.refresh()
            time.sleep(4)
            self.searchcust.setFirstName("Victoria")
            self.searchcust.setLastName("Terces")
            self.searchcust.clickOnSearch()
            self.driver.execute_script("window.scrollBy(0, 500);")
            table_visibility_text = self.driver.find_element(By.XPATH, '//table[@id="customers-grid"]').text
            time.sleep(2)
        status = self.searchcust.searchCustomerByName("Victoria Terces")
        if status == True:
            self.logger.info("********** TC_SearchCustomerByName__005 Passed ************")
            self.driver.quit()
            assert True

        else:
            self.logger.info("********** TC_SearchCustomerByName__005 Failed ************")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_searchCustomerByName.png")
            self.driver.quit()
            assert False
        

