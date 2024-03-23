from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage(Page):
    Connect_The_Company_button = (By.XPATH, '//div[text()="Connect the company"]')

    def click_connect_the_company_button(self):
        self.wait_element_clickable_click(*self.Connect_The_Company_button)

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])
