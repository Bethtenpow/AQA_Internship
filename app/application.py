from CAP_pages_internship.cap_base_page import Page
from CAP_pages_internship.cap_login_page import LoginPage
from CAP_pages_internship.cap_home_page import HomePage
from CAP_pages_internship.cap_connect_the_company_page import ConnectTheCompanyPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.cap_login_page = LoginPage(driver)
        self.cap_home_page = HomePage(driver)
        self.cap_connect_the_company_page = ConnectTheCompanyPage(driver)