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

def start_local():
    """Starts BrowserStack Local"""
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": CONFIG['capabilities']['browserstack.key'], "forcelocal": "true" }
    bs_local.start(**bs_local_args)

def stop_local():
    """Stops BrowserStack Local"""
    global bs_local
    if bs_local is not None:
        bs_local.stop()

@before.all
def before_all():
    # Start BrowserStack Local before start of the test suite
    start_local()

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
    stop_local()

@after.all
def after_all(totalResult):
    # Stop BrowserStack Local after end of the test suite
    stop_local()
