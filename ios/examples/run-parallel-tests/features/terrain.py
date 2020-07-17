from lettuce import before, after, world
from browserstack.local import Local
from appium import webdriver
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), '..', "config.json")

with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['username']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['access_key']

@before.each_feature
def setup_browser(feature):
    desired_capabilities = CONFIG['capabilities']
    desired_capabilities['device'] = CONFIG['environments'][TASK_ID]['device']
    world.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://%s:%s@hub-cloud.browserstack.com/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    )

@after.each_feature
def cleanup_browser(feature):
    world.browser.quit()
