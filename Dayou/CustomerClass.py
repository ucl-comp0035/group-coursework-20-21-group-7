import RegisteredUserClass

'''
Purpose: Inherit from the RegisteredUser Class, contains Customer information
Instance variables: (userID: user ID, password: password, registerDate: 
registered date, firstName: first name, lastName: last name, email: email, age: age)
Methods: __init__: Create an customer object(account); updateProfile: Change the
email or/and the age of the customer; __repr__: display customer info
'''


class Customer(RegisteredUserClass.RegisteredUser):
    """
    Inherit from parent RegisterUser Class，
    follows the Liskov substitution principle
    """

    def __init__(self, userID: int, password: str, registerDate: str,
                 firstName: str, lastName: str, email: str, age: int):
        super().__init__(userID, password, registerDate)
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__age = age

    def updateProfile(self, email: str, age: int):
        self.__email = email
        self.__age = age

    def __repr__(self):
        return 'Customer(firstName={},lastName={},email={},age={})' \
            .format(self.__firstName, self.__lastName, self.__email, self.__age)
