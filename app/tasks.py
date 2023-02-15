import time
from django.core.mail import send_mail, BadHeaderError


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
