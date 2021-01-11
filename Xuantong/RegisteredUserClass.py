'''
Name: Xuantong Lu Make A Change!!!
Purpose: (RegisteredUser class from UML Class)
Instance variables: (userID: user ID, password: password, registerDate:
register Date)
Methods: (viewPage: view page __repr__: display RegisteredUser's info ,verifyLogin: verify Login user is in user list)
'''


class RegisteredUser():
    def __init__(self, userID: int, password: str, registerDate: str):
        self.__userID = userID
        self.__password = password
        self.__registerDate = registerDate

    def verifyLogin(self, password: str):
        if self.__password == password:
            return True
        return False

    def viewPage(self):
        print('RegisteredUser-viewPage')

    def __repr__(self):
        return 'RegisteredUser(userID={},password={},registerDate={})' \
            .format(self.__userID, self.__password, self.__registerDate)