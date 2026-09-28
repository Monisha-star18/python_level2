
# ============================================================
# Method Overriding / Polymorphism with Inheritance
# ============================================================

'''
Method overriding happens when a child class
provides its own implementation of a parent method.
'''


class Notification:

    def send(self, message):

        print(f"Sending notification: {message}")


class EmailNotification(Notification):

    def send(self, message):

        print(f"Sending EMAIL: {message}")


class SMSNotification(Notification):

    def send(self, message):

        print(f"Sending SMS: {message}")


notifications = [
    EmailNotification(),
    SMSNotification()
]

for notification in notifications:

    notification.send("Your order is shipped")


'''
Output:

Sending EMAIL: Your order is shipped
Sending SMS: Your order is shipped


Same method:

    send()

Different implementations.

This is polymorphism through method overriding.
'''
