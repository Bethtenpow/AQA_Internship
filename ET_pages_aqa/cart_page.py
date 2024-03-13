from ET_pages_aqa.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR,  "h1[class*='StyledHeading']")

    def verify_cart_empty_message(self):
        actual_text = self.find_element(*self.CART_HEADER).text
        assert 'Your cart is empty' == actual_text, f"Expected 'Your cart is empty' but got {actual_text}"
