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
