from lettuce import *
from lettuce_webdriver.util import AssertContextManager


@step('I search using AI Agent for keyword "(.*?)"')
def search_with_ai_agent(step, keyword):
    with AssertContextManager(step):
        world.browser.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": ["Tap on Search Wikipedia"]}'
        )
        world.browser.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": ["Type %s in the search field"]}' % keyword
        )


@step(u'AI Agent verifies search results are displayed')
def verify_results_with_ai(step):
    world.browser.execute_script(
        'browserstack_executor: {"action": "ai", "arguments": ["Verify search results are displayed"]}'
    )
