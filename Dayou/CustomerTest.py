import unittest
import CustomerClass

class MyTestCase(unittest.TestCase):
    def test_init_Customer(self):
        print('Test: init_Customer')
        customer = CustomerClass.Customer(1000, 'abc', '08012021', 'Dayou',
                                          'Chen', 'abc@ucl.ac.uk', 21)
        self.assertEqual(customer.__repr__(),
                         'Customer(firstName=Dayou,lastName=Chen,email=abc@ucl.ac.uk,age=21)')

    def test_updateProfile(self):
        customer = CustomerClass.Customer(1000, 'abc', '08012021', 'Dayou',
                                          'Chen', 'abc@ucl.ac.uk', 21)
        self.assertEqual(customer.__repr__(),
                         'Customer(firstName=Dayou,lastName=Chen,email=abc@ucl.ac.uk,age=21)')
        print('Test: update age to 21')
        customer.updateProfile('dayou@ucl.ac.uk',21)
        self.assertEqual(customer.__repr__(),
                         'Customer(firstName=Dayou,lastName=Chen,email=dayou@ucl.ac.uk,age=21)')
        customer.updateProfile('dayou@ucl.ac.uk',22)
        print('Test: update age to 22')
        self.assertEqual(customer.__repr__(),
                         'Customer(firstName=Dayou,lastName=Chen,email=dayou@ucl.ac.uk,age=22)')

if __name__ == '__main__':
    unittest.main()