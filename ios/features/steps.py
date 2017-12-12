import time
from lettuce import *
from nose.tools import assert_equals
from lettuce_webdriver.util import AssertContextManager
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


@step('I open the app and click on login')
def click_on_login(step):
    with AssertContextManager(step):
        element = WebDriverWait(world.browser, 30).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Log In"))
        )
        element.click()


@step(u'Enter email "(.*?)" and click on next')
def enter_email_and_click_next(step, email):
    email_input = WebDriverWait(world.browser, 30).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Email address"))
    )
    email_input.send_keys(email)
    world.browser.find_element_by_accessibility_id("Next").click()
    time.sleep(5)
    

@step(u'Verify login error')
def verfiy_login_error(step):
    text_elements = world.browser.find_elements_by_xpath("//XCUIElementTypeStaticText")
    assert(len(text_elements) > 0)
    elements = filter(
        lambda x: x and x.__contains__("not registered on WordPress.com"),
        [x.text for x in text_elements]
    )
    assert(len(elements) > 0)
    

# Local Steps
@step(u'I open app and click on button')
def click_on_button(step):
    with AssertContextManager(step):
        test_button = WebDriverWait(world.browser, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "TestBrowserStackLocal"))
        )
        test_button.click()


@step(u'Then page contains "([^"]*)"')
def then_page_contains(step, regex):
    WebDriverWait(world.browser, 30).until(existence_lambda)
    result_element = world.browser.find_element_by_accessibility_id("ResultBrowserStackLocal")
    result_string = result_element.text.lower()

    if result_string.__contains__("not working"):
        screenshot_file = "%s/screenshot.png" % os.getcwd()
        driver.save_screenshot(screenshot_file)
        print "Screenshot stored at %s" % screenshot_file
        raise Exception("Unexpected BrowserStackLocal test result")
    else:
        assert(result_string.__contains__(regex.lower()))

def existence_lambda(s):
    result = s.find_element_by_accessibility_id("ResultBrowserStackLocal").get_attribute("value")
    return result and len(result) > 0
