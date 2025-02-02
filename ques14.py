#Implement method overriding for a `Notification` class where 
# `send()` is overridden in `EmailNotification` and `SMSNotification`

class Notification:
    def send(self):
        print("Notification is a popup mssg")
class Email_notification(Notification):
    def send(self):
        print("There is an email notification")
class SMS_notification(Notification):
    def send(self):
        print("There is a SMS Notification")
s=SMS_notification()
s.send()
e=Email_notification()
e.send()