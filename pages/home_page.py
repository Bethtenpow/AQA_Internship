from CAP_pages_internship.base_page import Page
from selenium.webdriver.common.by import By


class HomePage(Page):
    Connect_The_Company_button = (By.XPATH, '//div[text()="Connect the company"]')

    def click_connect_the_company_button(self):
        self.wait_element_clickable_click(*self.Connect_The_Company_button)
