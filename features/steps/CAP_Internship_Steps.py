from behave import given, when, then
from time import sleep


@given('Open the main home page')
def open_home_page(context):
    context.app.login_page.open_main_page()


@when('Login to page')
def login(context):
    context.app.login_page.login_to_page()


@when('Click continue button')
def click_continue_btn(context):
    context.app.login_page.click_continue_btn()


@when('Click on "Connect The Company"')
def click_connect_the_company_button(context):
    context.app.home_page.click_connect_the_company_button()
    sleep(4)


@when('Switch to a new window')
def switch_to_new_window(context):
    context.app.home_page.switch_to_new_window()
    print('new window', context.driver.window_handles)


@then('Enter test form information')
def enter_test_form_information(context):
    context.app.connect_the_company_page.test_information()


@then('Verify information is present')
def verify_test_information_present(context):
    context.app.connect_the_company_page.verify_test_information()


@then('Verify "Send Request" button')
def verify_send_request(context):
    context.app.connect_the_company_page.verify_send_request_btn()


@then('Verify "Buy a Subscription" button')
def verify_buy_a_subscription(context):
    context.app.connect_the_company_page.verify_subscription_btn()
