from paver.easy import *
from paver.setuputils import setup
import threading, os, platform

setup(
    name = "lettuce-browserstack",
    version = "0.1.0",
    author = "BrowserStack",
    author_email = "support@browserstack.com",
    description = ("Lettuce Integration with BrowserStack"),
    license = "MIT",
    keywords = "example selenium browserstack",
    url = "https://github.com/browserstack/lettuce-appium-app-browserstack",
    packages=['packages']
)

def run_behave_test():
    sh('lettuce features/first_test.feature')

@task
@consume_nargs(1)
def run(args):
    if args[0] == 'first_test':
        run_behave_test()
    else:
        print("Wrong paver task given") 
