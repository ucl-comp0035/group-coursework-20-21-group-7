import abc
import unittest

'''
Name: Xuantong Lu
Purpose: (User class) hello
Instance variables: (visitDate: visit Date,  ipAddress: ip address)
Methods: (viewPage: view page
           __repr__: display user's info )
'''

class User(metaclass=abc.ABCMeta):
    def __init__(self, visitDate: int, ipAddress: int):
        self.__visitDate = visitDate
        self.__ipAddress = ipAddress
    @abc.abstractmethod
    def viewPage(self):
        pass
    def __repr__(self):
        return 'User(visitDate={},ipAddress={})'.format(self.__visitDate, self.__ipAddress)

'''
Name: Xuantong Lu 
Purpose: (RegisteredUser class inherit from the User class and extend it by override) 
Instance variables: (visitDate: visit Date,  ipAddress: ip address, userID: user ID, password: password, registerDate: 
register Date) 
Methods: (viewPage: view page __repr__: display RegisteredUser's info ,verifyLogin: verify Login user is in user list)
'''       
class RegisteredUser(User):
    def __init__(self, visitDate, ipAddress, userID: int, password: str, registerDate: int):
        super().__init__(visitDate, ipAddress)
        self.__userID = userID
        self.__password = password
        self.__registerDate = registerDate

    def verifyLogin(self):
        user_dicts = {1: "root", 2: "admin", 3: "password"}
        if self.__userID in user_dicts.keys():
            if user_dicts[self.__userID] == self.__password:
                return True
        return False

    def viewPage(self):
        print('RegisteredUser-viewPage')

    def __repr__(self):
        return '{}RegisteredUser(userID={},password={},registerDate={})'.format(super().__repr__(), self.__userID,
                                                                                self.__password,
                                                                                self.__registerDate)
       
class MyTestCase(unittest.TestCase):
       def testInitRegisteredUser(self):
               registeredUser = RegisteredUser(1, 16801, 1, '123455', 12312)
               self.assertEqual(registeredUser.__repr__(),
                                'User(visitDate=1,ipAddress=16801)RegisteredUser(userID=1,password=123455,registerDate=12312)')
       def test_registeredUser_verify_login(self):
               registeredUser = RegisteredUser(1, 16801, 1, '123455', 12312)
               self.assertEqual(registeredUser.verifyLogin(), False)
               registeredUser = RegisteredUser(1, 16801, 1, 'root', 12312)
               self.assertEqual(registeredUser.verifyLogin(), True)
               registeredUser = RegisteredUser(100, 16801, 100, 'root', 12312)
               self.assertEqual(registeredUser.verifyLogin(), False)

if __name__ == '__main__':
    unittest.main()
