from selenium import webdriver
from pageObjects.AddCustomers import AddCustomers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomers import AddCustomers
import pytest 

class Test_003_AddCustomer:
    logger = LogGen.loggen()
    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("***************** Test_003__AddCustomer *******************")
        self.driver, self.wait = setup 
        self.driver.get(self.base_URL)
        self.driver.maximize_window() 
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button-1 login-button")]')))

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***************** Login Successful *******************")
        self.logger.info("***************** Start Adding Customer *******************")
        time.sleep(3)
        self.addcust = AddCustomers(self.driver, self.wait)
        self.addcust.clickOnCustomersMenu()
        opened = self.driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']").is_displayed()

        while not opened:
            self.addcust.clickOnCustomersMenu()
            opened = self.driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']").is_displayed()
            time.sleep(2)
        self.addcust.clickOnCustomerMenuItem()
        time.sleep(3)
        self.addcust.clickOnAddNewCustomer()
        time.sleep(4)
        actual_title = self.driver.title
        if actual_title == "Add a new customer / nopCommerce administration":
            self.logger.info("***************** Providing Info about Customer *******************")
            self.email = ReadConfig.random_mail_generator()
            self.addcust.setEmail(self.email)
            self.addcust.setPassword("123456789")
            self.addcust.setFirstName("Aniket")
            self.addcust.setLastName("Kumar")
            self.addcust.setGender("Male")
            self.addcust.setDateOfBirth("20-03-2002")
            self.addcust.setCompanyName("BusyQA")
            self.addcust.setIsTaxExempt("Yes")
            time.sleep(2)
            self.addcust.setNewsletter("Test store 2")
            time.sleep(1)
            self.addcust.setCustomerRoles("Guest")
            time.sleep(1)
            self.addcust.setVendorId("Vendor 2")
            time.sleep(1)
            self.addcust.setActiveStatus("Active")
            time.sleep(1)
            self.addcust.setAdminComment("Going Great!!")
            self.logger.info("***************** Saving Customer Info *******************")
            time.sleep(2)
            self.addcust.clickOnSave()
            cur_title = self.driver.title
            print(cur_title)
            if cur_title == "Customers / nopCommerce administration":
                self.logger.info("***************** Customer Added Successfully *******************")   
                self.driver.quit()
                assert True

            else:
                self.logger.info("***************** Customer Not Added Successfully *******************")
                self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer.png")
                self.driver.quit()
                assert False
        else:
            assert False
