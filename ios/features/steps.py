import time
from lettuce import *
from nose.tools import assert_equals
from lettuce_webdriver.util import AssertContextManager
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


@step('I open the app and click on Text Button')
def click_on_textbutton(step):
    with AssertContextManager(step):
        element = WebDriverWait(world.browser, 30).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Text Button"))
        )
        element.click()


@step(u'Type "(.*?)" and hit enter')
def enter_text(step, text):
    text_input = WebDriverWait(world.browser, 30).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Input"))
    )
    text_input.send_keys(text+"\n")
    time.sleep(5)
    

@step(u'Verify displayed text matches input text')
def verfiy_match(step):
    text_output = WebDriverWait(world.browser, 30).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Output"))
    )
    if text_output!=None and text_output.text=="hello@browserstack.com":
        assert True
    else:
        assert False
    

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
