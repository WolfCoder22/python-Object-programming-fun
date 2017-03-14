import re

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
        self.idHash= {} #stores ids with hash as key
        self.phoneHash = {} #stores hash with ids as key
        self.file= inFile

    def searchPhone(self, id):

        #get phone from ID
        toSearch= open(self.file, "r")
        toSearch= toSearch.read()
        regex= '(?<='+id+', )(.*)(?='+'\n'+')'
        phone= re.search(regex , toSearch, re.IGNORECASE)

        if type(phone.group(0))== string

        # remove dashes and parathesis in phone number
        phone = re.sub(r'[^\w]', "", phone)

        #add to hashtables
        self.idHash[phone]= id
        self.phoneHash[id] = phone

        return phone

    def searchID(self, phone):
        # get ID from phone
        toSearch = open(self.file, "r")
        toSearch = toSearch.read()
        regex = '(?<=' + '\n' + ', )(.*)(?=' +  + ')'
        phone = re.search(regex, toSearch, re.IGNORECASE).group(0)

        # remove dashes and parathesis in phone number
        phone = re.sub(r'[^\w]', "", phone)

        # add to hashtables
        self.idHash[phone] = id
        self.phoneHash[id] = phone

        return phone



search= phonesearch("searchTestFile.txt")
search.searchPhone('YGE2KCEPENADKDYYH4')










#makeTextDoc('searchTestFile', 25)