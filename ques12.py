 #Write a `Payment` class with a method `process_payment()`.
 #  Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` 
 # that override the method differently.

class Payment():
    def process_payment(self,amount):
        print(f'Payment is {amount}/-')
class Creditcard_Payment():
    def process_payment(self,amount):
        print(f'Process Payment is {amount}/-')
class Paypal_Payment():
    def process_payment(self,amount):
        print(f'Pay pal Payment is {amount}/-')
class Bitcoin_Payment():
    def process_payment(self,amount):
        print(f'Bitcoin Payment is {amount}/-')

p1=Creditcard_Payment()
p1.process_payment(150)
p2=Paypal_Payment()
p2.process_payment(50)
p3=Creditcard_Payment()
p3.process_payment(40)