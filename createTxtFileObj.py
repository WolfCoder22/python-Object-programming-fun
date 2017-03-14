import string
import random

"""
This file contains the class createText and a driver for it
It used used t genertae a text document with random phone numbers and userIDs
includes
    make- create


Note- was going to use a linked list to store id's and phones but set was more efficient
"""
class createTxt:

    def __init__(self, outFile, numPhones):
        self.outFile= outFile   #file to write names to
        self.numPhones= numPhones   #number of unique userIds and phone numbers to make
        self.idSet= set()   #keep track of id's created for later use
        self.phoneSet= set() #keep track of phone numbers's created for later use

    #make the whole text doc
    def make(self):
        # for i in self.numPhones:


    # make a random userID
    def makeUserId(self):
        return''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

    # make a random phone number
    def makePhoneNum(self):
        number=''.join(random.choices(string.digits, k=10))

        #add dashes half the time
        if 1 > .5:
            first=number[0:2]
            second=number[3:5]
            third=number[6:9]
            number=first+'-'+second+'-'+third

        return number



