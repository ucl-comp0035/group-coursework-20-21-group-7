import abc
import unittest
import tkinter as Tk
from tkinter import *

'''
Name: Xuantong Lu
Purpose: (User class)
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
As Enquiry is at the behind of User from UML class diagram, I attached class of User which was done by Xuantong as former.
'''

'''
Name: Zihao Du  18016926
Purpose: (Enquiry class inherit from the User class and extend it by getting users' preference ) 
Instance variables: (visitDate: visit Date,  ipAddress: ip address, userID: user ID, enquiryTime: float) 
Methods: (enquiryByOccupation: enable user to select interested occupation
          enquiryByEducation: enable user to select interested education/qualification
          enquiryByIndustry: enable user to select interested industry
)
'''


class Enquiry(User):
    def __init__(self, visitDate, ipAddress, enquiryTime: float):
        super().__init__(visitDate, ipAddress)
        self.__enquiryTime = enquiryTime
        self.user_click = []

    def viewPage(self):
        pass

    def enquiryByOccupation(self):
        window = Tk()
        window.title("Enquiry Occupation")
        r_value = IntVar()

        def r_print():
            self.user_click.append(r_value.get())
            print(self.user_click)

        rb_oc1 = Radiobutton(window, text='Administrative And Secretarial Occupations', variable=r_value, value=1,
                             command=r_print).pack()
        rb_oc2 = Radiobutton(window, text='Associate Professional And Technical Occupations', variable=r_value, value=2,
                             command=r_print).pack()
        rb_oc3 = Radiobutton(window,
                             text='Caring, Leisure And Other Service Occupations; and Sales And Customer Service Occupations',
                             variable=r_value, value=3, command=r_print).pack()
        rb_oc4 = Radiobutton(window, text="Managers, Directors And Senior Officials", variable=r_value, value=4,
                             command=r_print).pack()
        rb_oc5 = Radiobutton(window, text="Process, Plant And Machine Operatives; and Elementary Occupations",
                             variable=r_value, value=5, command=r_print).pack()
        rb_oc6 = Radiobutton(window, text="Professional Occupations", variable=r_value, value=6, command=r_print).pack()
        rb_oc7 = Radiobutton(window, text="Skilled Trades Occupations", variable=r_value, value=7,
                             command=r_print).pack()
        rb_oc8 = Radiobutton(window, text="Total in all occupations", variable=r_value, value=8, command=r_print).pack()
        window.mainloop()

    def enquiryByEducation(self):
        window = Tk()
        window.title("Enquiry Occupation")
        r_value = IntVar()

        def r_print():
            self.user_click.append(r_value.get())
            print(self.user_click)

        rb_edu1 = Radiobutton(window, text='GCE, A-level or equivalent', variable=r_value, value=1,
                              command=r_print).pack()
        rb_edu2 = Radiobutton(window, text='GCSE grades A*-C or equivalent', variable=r_value, value=2,
                              command=r_print).pack()
        rb_edu3 = Radiobutton(window, text='Higher degree', variable=r_value, value=3, command=r_print).pack()
        rb_edu4 = Radiobutton(window, text="Higher education", variable=r_value, value=4, command=r_print).pack()
        rb_edu5 = Radiobutton(window, text="No qualification", variable=r_value, value=5, command=r_print).pack()
        rb_edu6 = Radiobutton(window, text="Ordinary degree or equivalent", variable=r_value, value=6,
                              command=r_print).pack()
        rb_edu7 = Radiobutton(window, text="Other qualifications", variable=r_value, value=7, command=r_print).pack()
        window.mainloop()

    def enquiryByIndustry(self):
        window = Tk()
        window.title("Enquiry Occupation")
        r_value = IntVar()

        def r_print():
            self.user_click.append(r_value.get())
            print(self.user_click)

        rb_ind1 = Radiobutton(window, text='Accommodation and food service activities', variable=r_value, value=1,
                              command=r_print).pack()
        rb_ind2 = Radiobutton(window, text='Administrative and support service activities', variable=r_value, value=2,
                              command=r_print).pack()
        rb_ind3 = Radiobutton(window, text='Arts, entertainment and recreation', variable=r_value, value=3,
                              command=r_print).pack()
        rb_ind4 = Radiobutton(window, text="Construction", variable=r_value, value=4, command=r_print).pack()
        rb_ind5 = Radiobutton(window, text="Education", variable=r_value, value=5, command=r_print).pack()
        rb_ind6 = Radiobutton(window, text="Financial and insurance activities", variable=r_value, value=6,
                              command=r_print).pack()
        rb_ind7 = Radiobutton(window, text="Human health and social work activities", variable=r_value, value=7,
                              command=r_print).pack()
        rb_ind8 = Radiobutton(window, text="Information and communication", variable=r_value, value=8,
                              command=r_print).pack()
        rb_ind9 = Radiobutton(window, text="Manufacturing", variable=r_value, value=9, command=r_print).pack()
        rb_ind10 = Radiobutton(window, text="Other service activities", variable=r_value, value=10,
                               command=r_print).pack()
        rb_ind11 = Radiobutton(window, text="Primary and utilities", variable=r_value, value=11, command=r_print).pack()
        rb_ind12 = Radiobutton(window, text="Professional, scientific and technical", variable=r_value, value=12,
                               command=r_print).pack()
        rb_ind13 = Radiobutton(window, text="Public administration and defence; compulsory social security",
                               variable=r_value, value=13, command=r_print).pack()
        rb_ind14 = Radiobutton(window, text="Real estate", variable=r_value, value=14, command=r_print).pack()
        rb_ind15 = Radiobutton(window, text="Real estate; Professional, scientific and technical", variable=r_value,
                               value=15, command=r_print).pack()
        rb_ind16 = Radiobutton(window, text="Retail", variable=r_value, value=16, command=r_print).pack()
        rb_ind17 = Radiobutton(window, text="Transportation and storage", variable=r_value, value=17,
                               command=r_print).pack()
        rb_ind18 = Radiobutton(window, text="Wholesale and motor trades", variable=r_value, value=18,
                               command=r_print).pack()
        rb_ind19 = Radiobutton(window, text="Total in all industries", variable=r_value, value=19,
                               command=r_print).pack()

        window.mainloop()


class Myunittest(unittest.TestCase, Enquiry):
    def test_enquiryByOccupation(self):
        clicks = [4, 3, 6, 7, 5, 1, 2, 8]
        print("Please click the button in the following order, and then exit")
        print(clicks)
        enquiry = Enquiry(1, 2, 0.1)
        enquiry.enquiryByOccupation()
        self.assertEqual(clicks, enquiry.user_click)

    def test_enquiryByEducation(self):
        clicks = [4, 3, 6, 7, 5, 1, 2]
        print("Please click the button in the following order, and then exit")
        print(clicks)
        enquiry = Enquiry(1, 2, 0.1)
        enquiry.enquiryByEducation()
        self.assertEqual(clicks, enquiry.user_click)

    def test_enquiryByIndustry(self):
        clicks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        print("Please click the button in the following order, and then exit")
        print(clicks)
        enquiry = Enquiry(1, 2, 0.1)
        enquiry.enquiryByIndustry()
        self.assertEqual(clicks, enquiry.user_click)


if __name__ == '__main__':
    unittest.main()
