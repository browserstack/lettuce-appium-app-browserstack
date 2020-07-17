import time
from lettuce import *
from nose.tools import assert_equals
from lettuce_webdriver.util import AssertContextManager
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step(u'I open app and click on button')
def click_on_button(step):
    with AssertContextManager(step):
        element = WebDriverWait(world.browser, 30).until(
            EC.presence_of_element_located((MobileBy.ID, "com.example.android.basicnetworking:id/test_action"))
        )
        element.click()
        WebDriverWait(world.browser, 30).until(
            EC.presence_of_element_located((MobileBy.CLASS_NAME, "android.widget.TextView"))
        )
        
@step(u'Then page contains "([^"]*)"')
def then_page_contains(step, regex):
    test_element = None
    search_results = world.browser.find_elements_by_class_name("android.widget.TextView")
    for result in search_results:
        if result.text.__contains__("The active connection is"):
            test_element = result

    if test_element is None:
        raise Exception("Cannot find the needed TextView element from app")

    matched_string = test_element.text
    print matched_string
    assert matched_string.__contains__("The active connection is wifi"), "Incorrect Text"
    assert matched_string.__contains__("Up and running"), "Incorrect Text"
