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

def run_lettuce_test():
    sh('lettuce features/local_test.feature')

@task
@consume_nargs(1)
def run(args):
    if args[0] == 'local_test':
        run_lettuce_test()
    else:
        print("Wrong paver task given") 
