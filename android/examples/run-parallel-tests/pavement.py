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
    packages=['features']
)

def run_lettuce_test(task_id=0):
    if platform.system() == 'Windows':
        sh('SET TASK_ID=%s & lettuce features/parallel_test.feature' % (task_id))
    else:
        sh('export TASK_ID=%s && lettuce features/parallel_test.feature' % (task_id))

@task
@consume_nargs(1)
def run(args):
    if args[0] == 'parallel_tests':
        jobs = []
        for index in range(2):
            thread = threading.Thread(target=run_lettuce_test,args=(index,))
            jobs.append(thread)
            thread.start()

        for thread in jobs:
            thread.join()
    else:
        print("Wrong paver task given") 
