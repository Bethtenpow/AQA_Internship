from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class ConnectTheCompanyPage(Page):
    YOUR_COUNTRY = (By.XPATH, "//*[@name='Your-country']")
    COMPANY_NAME = (By.XPATH, "//*[@data-name='Company Name 2']")
    POSITION = (By.XPATH, "//*[@data-name='Position.']")
    YOUR_NAME_TEST = (By.XPATH, "//*[@data-name='Director name']")
    YOUR_PHONE_TEST = (By.XPATH, "//*[@data-name='Director phone']")
    AMOUNT_AGENTS_COMPANY = (By.XPATH, "//*[@data-name='Amount of agents in company']")
    EMAIL_TEST = (By.XPATH, "//*[@data-name='Email 2']")
    SEND_REQUEST_BTN = (By.XPATH, "//*[@value='Send request']")
    BUY_SUBSCRIPTION_BTN = (By.CSS_SELECTOR, "[class*='step-button']")

    def verify_connect_company_page_opened(self):
        self.verify_url('https://soft.reely.io/book-presentation')

    def test_information(self):
        sleep(4)
        self.wait_for_element_visible(*self.YOUR_COUNTRY)
        self.find_element(*self.YOUR_COUNTRY)
        self.input_text('United States', *self.YOUR_COUNTRY)
        self.input_text('TEST', *self.COMPANY_NAME)
        self.input_text('President', *self.POSITION)
        self.input_text('TestElizabeth', *self.YOUR_NAME_TEST)
        self.input_text('4985557864', *self.YOUR_PHONE_TEST)
        self.input_text('5', *self.AMOUNT_AGENTS_COMPANY)
        self.input_text('123testing@example.com', *self.EMAIL_TEST)

    def verify_test_information(self):
        assert len(self.YOUR_COUNTRY) == len(self.YOUR_COUNTRY)
        assert len(self.COMPANY_NAME) == len(self.COMPANY_NAME)
        assert len(self.POSITION) == len(self.POSITION)
        assert len(self.YOUR_NAME_TEST) == len(self.YOUR_NAME_TEST)
        assert len(self.YOUR_PHONE_TEST) == len(self.YOUR_PHONE_TEST)
        assert len(self.AMOUNT_AGENTS_COMPANY) == len(self.AMOUNT_AGENTS_COMPANY)
        assert len(self.EMAIL_TEST) == len(self.EMAIL_TEST)

    def verify_send_request_btn(self):
        self.driver.find_element(*self.SEND_REQUEST_BTN)
        print('Send Request button is available')

    def verify_subscription_btn(self):
        self.driver.find_element(*self.BUY_SUBSCRIPTION_BTN)
        print('Buy Subscription button is available')
