#Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods,
#  and it is implemented by `GoogleAuth` and `FacebookAuth` classes.

from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print('Google logged in')
    def logout(self):
        print('Google logout')
class FacebookAuth(UserAuthentication):
    def login(self):
        print('Facebook logged in')
    def logout(self):
        print('BFacebook logout in')
google=GoogleAuth()
google.login()
google.logout()
fb=FacebookAuth()
fb.login()
fb.logout()