from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
driver = webdriver.Chrome





class BasePage:
    
    def __init__(self, driver):
        self.driver: WebDriver = driver    
        self.Base_url = 'https://www.saucedemo.com/'

    def visit(self):
        return self.driver.get(self.Base_url)
    
    def find_element(self, locator):
       return self.driver.find_element(By.CSS_SELECTOR, locator)
        

    def find_username_field(self,locator):
        return self.driver.find_element(By.XPATH, locator)
        
    def find_password_field(self,locator):
        return self.driver.find_element(By.XPATH, locator)
        

    
        