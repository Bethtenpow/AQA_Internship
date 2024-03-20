from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from CAP_pages_internship.cap_base_page import Page


class LoginPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name='email-2']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-name='password']")
    CONTINUE_BTN = (By.XPATH, "//a{contains(@class='login-button']")

    def open_main_page(self):
        self.open("https://soft.reelly.io/sign-in")

    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(self.EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(self.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)

    def click_continue_btn(self):
        self.click(self.CONTINUE_BTN)
