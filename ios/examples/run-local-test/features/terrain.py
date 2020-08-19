from lettuce import before, after, world
from browserstack.local import Local
from appium import webdriver
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), '..', "config.json")
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['username']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['access_key']

def start_local():
    """Starts BrowserStack Local"""
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY, "forcelocal": "true" }
    bs_local.start(**bs_local_args)

def stop_local():
    """Stops BrowserStack Local"""
    global bs_local
    if bs_local is not None:
        bs_local.stop()


@before.each_feature
def setup_browser(feature):
    desired_capabilities = CONFIG['capabilities']
    # Start BrowserStack local before start of the test
    start_local()
    world.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://%s:%s@%s/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY, CONFIG['server'])
    )

@after.each_feature
def cleanup_browser(feature):
    # Invoke world.browser.quit() to indicate that the test is completed. 
    # Otherwise, it will appear as timed out on BrowserStack.
    world.browser.quit()
    stop_local()
