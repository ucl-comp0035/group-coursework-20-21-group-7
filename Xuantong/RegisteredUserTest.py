import unittest
import RegisteredUserClass

class MyTestCase(unittest.TestCase):
    def testInitRegisteredUser(self):
        registeredUser = RegisteredUserClass.RegisteredUser(1, '123455', 12312)
        self.assertEqual(registeredUser.__repr__(),
                         'RegisteredUser(userID=1,password=123455,registerDate=12312)')

    def test_registeredUser_verify_login(self):
        registeredUser = RegisteredUserClass.RegisteredUser(1, '123455', 12312)
        self.assertEqual(registeredUser.verifyLogin('123455'), True)
        registeredUser = RegisteredUserClass.RegisteredUser(1, '123455', 12312)
        self.assertEqual(registeredUser.verifyLogin('123123'), False)
        registeredUser = RegisteredUserClass.RegisteredUser(100, 'root', 12312)
        self.assertEqual(registeredUser.verifyLogin('admin'), False)


if __name__ == '__main__':
    unittest.main()