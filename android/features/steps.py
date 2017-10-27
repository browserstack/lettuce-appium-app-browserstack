import time
from lettuce import *
from nose.tools import assert_equals
from lettuce_webdriver.util import AssertContextManager
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step('I open the app and search for keyword "(.*?)"')
def search_with_keyword(step, keyword):
    with AssertContextManager(step):
        search_element = WebDriverWait(world.browser, 10).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        )
        search_element.click()

        search_input = WebDriverWait(world.browser, 30).until(
            EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        )
        search_input.send_keys(keyword)
        time.sleep(5)


@step(u'Search results should appear')
def verfiy_result_should_present(step):
    elems = world.browser.find_elements_by_class_name("android.widget.TextView")
    assert len(elems) > 0, "results not populated"


# Local Steps
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
