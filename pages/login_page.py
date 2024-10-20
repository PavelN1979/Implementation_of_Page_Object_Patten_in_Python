from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url , "Substring 'login' is not present in current browser url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "There is no login form on the page"

    def should_be_register_form(self):
         assert self.browser.find_element(*LoginPageLocators.LOGIN_REGISTER), "There is no login form on the page"

    def register_new_user(self):
        self.email = str(time.time()) + "@fakemail.org"
        self.browser.find_element(*BasePageLocators.USER_EMAIL).send_keys(str(self.email))
        self.browser.find_element(*BasePageLocators.USER_PASSWORD).send_keys("1234HELLO")
        self.browser.find_element(*BasePageLocators.USER_REPEAT_PASSWORD).send_keys("1234HELLO")
        self.browser.find_element(*BasePageLocators.USER_BUTTON).click()
