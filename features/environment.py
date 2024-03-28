from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from app.application import Application
from selenium.webdriver.chrome.options import Options


def browser_init(context):
    """
    :param context: Behave context
    """

#Chrome
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)


#Firefox
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

#Headless Chrome
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('--window-size=1920x1080')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # context.driver.maximize_window()

    # context.driver.implicitly_wait(4)
    # context.wait = WebDriverWait(context.driver, 15)
    # context.app = Application(context.driver)

    ##BROWSERSTACK##
    bs_user = 'elizabethtenpow_F7SmpD'
    bs_key = 'k7RLEpXzytZZCiPze3sV'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Firefox',
        'sessionName': 'User clicks on “Connect the company” button and can use the form to register a new agency'
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()

    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

    context.driver.get('https://soft.reelly.io/sign-in')
    context.driver.find_element(By.ID, 'email-2').send_keys("your_email")
    context.driver.find_element(By.ID, 'field').send_keys("your_password")
    context.driver.find_element(By.CSS_SELECTOR, ".login-button").click()


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
