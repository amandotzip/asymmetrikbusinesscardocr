#ContactInfo class that for storing and representing
#parsed data
class ContactInfo:
    
    #default constructor
    def __init__(self):
        self.name = "N/A"
        self.phoneNumber = "N/A"
        self.emailAddress = "N/A"
    #Constructor with fields
    def __init__(self, name, phoneNumber, emailAddress):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress

    #getters for contact fields
    def getName(self) -> str:
        return self.name

    def getPhoneNumber(self) -> str:
        return self.phoneNumber

    def getEmailAddress(self) -> str:
        return self.emailAddress
    
    #If after parsing data must be updated, use these methods
    def updateName(self, name: str):
        self.name = name

    def updatePhoneNumber(self, phoneNumber: str):
        self.phoneNumber = phoneNumber
    
    def updateEmailAdress(self, emailAddress: str):
        self.emailAddress = emailAddress

    # string func
    def __str__(self):
        return "Name: " + str(self.name) + "\nPhone: " + str(self.phoneNumber) +"\nEmail: " + str(self.emailAddress)
