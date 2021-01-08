from datetime import datetime
# mawenteng niubi
'''
Name: Xuantong Lu 
Purpose: (RegisteredUser class inherit from the User class and extend it by override) 
Instance variables: (visitDate: visit Date,  ipAddress: ip address, userID: user ID, password: password, registerDate: 
register Date) 
Methods: (viewPage: view page __repr__: display RegisteredUser's info ,verifyLogin: verify Login user is in user list)
'''       
class RegisteredUser():
    def __init__(self, userID: int, password: str, registerDate: str):
        self.__userID = userID
        self.__password = password
        self.__registerDate = registerDate

    def verifyLogin(self):
        if self.__userID == self.__password:
                return True
        return False

    def viewPage(self):
        print('RegisteredUser-viewPage')

    def __repr__(self):
        return 'RegisteredUser(userID={},password={},registerDate={})'\
            .format(self.__userID, self.__password, self.__registerDate)

'''
Student: Dayou
'''
class Customer(RegisteredUser):
    def __init__(self, userID: int, password: str, registerDate: str, \
                 FirstName: str, LastName: str, email: str, age: int):
        super().__init__(userID, password, registerDate)
        self.FirstName = FirstName
        self.LastName = LastName
        self.email = email
        self.age = age

    def updateProfile(self, email: str, age: int):
        self.email = email
        self.age = age

    def __repr__(self):
        return 'Customer(FirstName={},LastName={},email={},age={})'\
            .format(self.FirstName, self.LastName, self.email, self.age)


class StudentDetail():
    def __init__(self, StudentID: int, status: str,dateCreated: str = \
            datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), ):
        self.StudentID = StudentID
        self.status = status

    def __repr__(self):
        return 'StudentDetail(StudentID={},status={})'\
            .format(self.StudentID, self.status)


if __name__ == '__main__':
    '''
    a = RegisteredUser(1000,'abc', datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
    '''
    a = Customer(1000, 'abc', datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), 'Dayou', 'Chen', 'nikobourne',21)
    print(a.__repr__())

    a.updateProfile('nikobourne','22')
    print('test to update the Profile')
    print(a.__repr__())

    s = StudentDetail(12354,'College')
    print(s.__repr__())