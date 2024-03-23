from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import Page


class LoginPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='email-2']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='Password']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[class*='login-button']")

    def open_main_page(self):
        self.open("https://soft.reelly.io/sign-in")

    def login_to_page(self):
        self.input_text('elizabethtenpow@gmail.com', *self.EMAIL_FIELD)
        self.input_text('Beth10Careerist', *self.PASSWORD_FIELD)

    def click_continue_btn(self):
        self.click(*self.CONTINUE_BTN)

