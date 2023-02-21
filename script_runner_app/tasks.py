import time
from django.core.mail import send_mail, BadHeaderError

import os
from python_on_whales import docker

def run_script():
    output = docker.run(
        "iqvia:repoA" , ["/results/aaa.xlsx", "nvidia-smi"],
        volumes=[(os.path.abspath("./OUTPUTS"), "/results")] 
    )


def long_task(to, subject, message):
    print(f"from={...}, {to=}, {subject=}, {message=}")
    try:
        print("About to send_mail")
        print('starting task...')
        time.sleep(33)
        print('still running...')
        time.sleep(33)
        print('done!')
    except BadHeaderError:
        print("BadHeaderError")
    except Exception as e:
        print(e)
