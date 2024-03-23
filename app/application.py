from pages.base_page import Page
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.connect_the_company_page import ConnectTheCompanyPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
        self.connect_the_company_page = ConnectTheCompanyPage(driver)