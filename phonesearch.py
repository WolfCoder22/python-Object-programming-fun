from createTxtFile import makeTextDoc

"""
Class for searching a text document for phone nmber or ids
Initialize with - phoneSearch(fileToReadFrom)
methods
    - searchPhone(USERID)
        -searches for a phone number given userID
        -store in Hashtable
    -searchID(phoneNumber)
        -searches for a User iD given a phone number
        -stores both in hashtable
    -getFoundItems
        -2d array of all found items like: [[userId, key][userId, key]]
    -getAllPhones
        -searchs whole text and searches returns list with all phones
    -getAllIds
        -searchs whole text and searches returns list with all phones
"""

class phonesearch:
    def __init__(self, inFile):
        self.idHash= {}
        self.phoneHash = {}
        self.inFile= inFile

        def searchPhone(id):









#makeTextDoc('searchTestFile', 25)