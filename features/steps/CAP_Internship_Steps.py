from behave import given, when, then


@given('Open the main home page')
def open_home_page(context):
    context.CAP_pages_internship.cap_home_page.open_home()


@when('Login to page')
def login(context):
    context.CAP_pages_internship.cap_login_page.login()


@when('Click on "Connect The Company"')
def click_on_connect_company(context):
    context.CAP_pages_internship.cap_main_page.connect_company()


@when('Switch to a new tab')
def switch_to_new_tab(context):
    context.CAP_pages_internship.cap_main_page.switch_to_new_tab()


@then('Enter test form information')
def enter_test_form_information(context):
    context.CAP_pages_internship.cap_connect_the_company_page.test_info()


@then('Verify information is present')
def verify_test_information_present(context):
    context.CAP_pages_internship.cap_connect_the_company_page.verify_test_information()


@then('Verify "Send Request" button')
def verify_send_request(context):
    context.CAP_pages_internship.cap_connect_the_company_page.verify_request_btn()


@then('Verify "Buy a Subscription" button')
def verify_buy_a_subscription(context):
    context.cap_pages_internship.cap_connect_the_company_page.verify_buying_subscription()
