
# ============================================================
# Duck Typing
# ============================================================

'''
Duck Typing is one of the most important forms
of polymorphism in Python.

Duck typing can be considered a form of runtime polymorphism in Python

Python focuses on:

    "What an object can do"

rather than:

    "What class the object belongs to"

Common idea:

    If it behaves like the required object,
    Python can use it.
'''

class EmailNotification:

    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification:
    pass
    #def send(self, message):
       # print(f"SMS sent: {message}")


def send_notification(notification, message):
    notification.send(message)


email = EmailNotification()
sms = SMSNotification()

send_notification(email, "Order confirmed")
send_notification(sms, "Order confirmed")

# Output:
# Email sent: Order confirmed
# SMS sent: Order confirmed


'''
Notice:

send_notification()

does not care whether the object is:

    EmailNotification
    SMSNotification

It only expects:

    notification.send()

This is Duck Typing.
'''