from pages.base_page import BasePage
from selenium import webdriver
driver = webdriver.Chrome
from selenium.common.exceptions import NoSuchElementException

class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator= 'div.login_logo')
        except NoSuchElementException:
            return False
        return True
    def username_field(self):
        self.find_username_field(locator= '//input[@id="user-name"]')
       
    
    def password_field(self):
        self.find_password_field(locator= '//input[@id="password"]')