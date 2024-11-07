import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class AddCustomers:
    button_customerMenu_xpath = "//ul[contains(@class, 'nav nav-pills nav-sidebar flex-column nav-legacy')]/li"
    button_customerMenuitem_xpath = "//a[@href='/Admin/Customer/List']"

    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_firstname_id = "FirstName"
    textbox_lastname_id = "LastName"
    input_gender_male_id = "Gender_Male"
    input_gender_female_id = "Gender_Female"
    textbox_dob_id = "DateOfBirth"
    textbox_companyname_id = "Company"
    input_is_tax_exempt_id = "IsTaxExempt"
    textbox_newsletter_xpath = '//input[contains(@class, "select2-search__field")]'
    lstitem_test_store_xpath = '//*[@id="select2-SelectedNewsletterSubscriptionStoreIds-result-nbx5-2"]'
    lstitem_your_store_xpath = '//*[@id="select2-SelectedNewsletterSubscriptionStoreIds-result-tv7r-1"]'

    textbox_customer_roles_xpath = '//ul[contains(@class, "select2-selection__rendered")]'
    dropdown_vendor_id = "VendorId"
    tick_active_status_id = "Active"
    textbox_admin_comment_id = "AdminComment"

    btn_addnew_xpath = '//i[contains(@class, "fas fa-plus-square")]'
    btn_save_xpath = '//button[@name="save"]'
    
    def __init__(self, driver, wait):
        self.driver = driver 
        self.wait = wait 

    def clickOnCustomersMenu(self):
        try:
            customer_menu = self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH, self.button_customerMenu_xpath))
            )[3]
            ActionChains(self.driver).move_to_element(customer_menu).click(customer_menu).perform()
        except ElementNotInteractableException:
            self.driver.execute_script("arguments[0].click();", customer_menu)

    def clickOnCustomerMenuItem(self):
        try:
            customer_menu_item = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.button_customerMenuitem_xpath))
            )
            customer_menu_item.click()
        except ElementNotInteractableException:
            self.driver.execute_script("arguments[0].click();", customer_menu_item)

    def clickOnAddNewCustomer(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)
    
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
    
    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)
        
    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.input_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.input_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.input_gender_male_id).click()

    def setDateOfBirth(self, dob):
        self.driver.find_element(By.ID, self.textbox_dob_id).send_keys(dob)

    def setCompanyName(self, company):
        self.driver.find_element(By.ID, self.textbox_companyname_id).send_keys(company)
    
    def setIsTaxExempt(self, is_tax_exempt):
        if is_tax_exempt == "Yes":
            self.driver.find_element(By.ID, self.input_is_tax_exempt_id).click()
        else:
            pass 

    def setNewsletter(self, newsletter):

        self.driver.find_element(By.XPATH, self.textbox_newsletter_xpath).click()
        self.all_options = self.driver.find_elements(By.XPATH, '//ul[contains(@class, "select2-results__options")]//li')
        time.sleep(3)
        if newsletter == "Test store 2":
            self.listitem = self.all_options[1]
        else:
            self.listitem = self.all_options[0]
        self.listitem.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.textbox_newsletter_xpath).click()
    
    def setCustomerRoles(self, customer_roles):
        self.driver.find_elements(By.XPATH, self.textbox_customer_roles_xpath)[1].click()
        self.all_options = self.driver.find_elements(By.XPATH, '//ul[contains(@class, "select2-results__options")]//li')
        time.sleep(3)
        if customer_roles == "Administrator":
            self.listitem = self.all_options[0]
        elif customer_roles == "Moderator":
            self.listitem = self.all_options[1]
        elif customer_roles == "Registered":
            self.listitem = self.all_options[2]
        elif customer_roles == "Guest":
            self.all_options[2].click()
            self.listitem = self.all_options[3]
        elif customer_roles == "Vendor":
            self.listitem = self.all_options[4]
        else:
            self.listitem = self.all_options[3]
        time.sleep(3)
        self.listitem.click()
        self.driver.find_elements(By.XPATH, self.textbox_customer_roles_xpath)[1].click()

    def setVendorId(self, vendor_id):
        self.driver.find_element(By.ID, self.dropdown_vendor_id).send_keys(vendor_id)

    def setActiveStatus(self, active_status):
        if active_status == "Active":
            pass
        else:
            self.driver.find_element(By.ID, self.tick_active_status_id).click()


    def setAdminComment(self, admin_comment):
        self.driver.find_element(By.ID, self.textbox_admin_comment_id).send_keys(admin_comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
