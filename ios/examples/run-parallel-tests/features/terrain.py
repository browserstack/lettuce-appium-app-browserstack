from lettuce import before, after, world
from browserstack.local import Local
from appium import webdriver
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), '..', "config.json")
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

# Take user credentials from environment variables if they are defined
if 'BROWSERSTACK_USERNAME' in os.environ: CONFIG['capabilities']['browserstack.user'] = os.environ['BROWSERSTACK_USERNAME'] 
if 'BROWSERSTACK_ACCESS_KEY' in os.environ: CONFIG['capabilities']['browserstack.key'] = os.environ['BROWSERSTACK_ACCESS_KEY']

@before.each_feature
def setup_browser(feature):
    desired_capabilities = CONFIG['capabilities']
    desired_capabilities['device'] = CONFIG['environments'][TASK_ID]['device']
    world.browser = webdriver.Remote(
        desired_capabilities=dict(desired_capabilities),
        command_executor="http://hub-cloud.browserstack.com/wd/hub"
    )

@after.each_feature
def cleanup_browser(feature):
    # Invoke world.browser.quit() to indicate that the test is completed. 
    # Otherwise, it will appear as timed out on BrowserStack.
    world.browser.quit()
