from lettuce import before, after, world
from browserstack.local import Local
from appium import webdriver
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), '..', "config.json")
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

# Take user credentials from environment variables if they are defined
if 'BROWSERSTACK_USERNAME' in os.environ: CONFIG['capabilities']['browserstack.user'] = os.environ['BROWSERSTACK_USERNAME'] 
if 'BROWSERSTACK_ACCESS_KEY' in os.environ: CONFIG['capabilities']['browserstack.key'] = os.environ['BROWSERSTACK_ACCESS_KEY']

@before.each_feature
def setup_browser(feature):
    desired_capabilities = CONFIG['capabilities']
    world.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://hub-cloud.browserstack.com/wd/hub"
    )

@after.each_feature
def cleanup_browser(feature):
    # Invoke world.browser.quit() to indicate that the test is completed. 
    # Otherwise, it will appear as timed out on BrowserStack.
    world.browser.quit()
