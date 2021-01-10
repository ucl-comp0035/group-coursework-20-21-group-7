'''
Name: Zhilong Song
Purpose: (Provide agency details, use superlink to switch pages , shown in UML Class)
Instance variables: (agencyName, contactNumber, superlink, address, imageLink)
Methods: ( __repr__: display Agency details,__image__:display image with superlink ,UpdateAd:Update details)
'''
class Advertisement():
    def __init__(self, agencyName: str, contactNumber: int, superlink: str, 
    address: str, imageLink: str):
        self.agencyname = agencyName
        self.contactnumber = contactNumber
        self.superlink = superlink
        self.address = address
        self.imagelink = imageLink

    def UpdateAd(self, agencyName: str, contactNumber: int, superlink: str,address: str, imageLink: str):
        self.agencyname = agencyName
        self.contactnumber = contactNumber
        self.superlink = superlink
        self.address = address
        self.imagelink = imageLink


    def __repr__(self):
        return 'Advertisement(Agency={},Tel={},Address={})' \
            .format(self.agencyname, self.contactnumber,  self.address)

    