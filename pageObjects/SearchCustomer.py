from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SearchCustomer:

    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_ID = "//table[@role='grid']"
    table_id = "customers-grid"
    tableRows_xpath = '//table[@id="customers-grid"]//tbody//tr'
    tableColumns_xpath = '//table[@id="customers-grid"]//tbody//tr//td'


    def __init__(self, driver):
        self.driver = driver 
    
    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)
    
    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lastname)

    def clickOnSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))
    
    def searchCustomerByEmail(self, email):
        flag = False 
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.ID, self.table_id)
            cur_email = table.find_element(By.XPATH, f'//tbody/tr[{str(r)}]/td[2]').text 
            if cur_email == email:
                flag = True
                break
        return flag
    
    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            cur_name = self.driver.find_element(By.XPATH, f'//*[@id="customers-grid"]/tbody/tr[{str(r)}]/td[3]').text.strip()
            if cur_name == name:
                flag = True
                break
            else:
                pass
        return flag
    
