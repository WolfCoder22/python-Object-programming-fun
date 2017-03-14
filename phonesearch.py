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
        -phone number just needs the correct digits in order
        -stores both in hashtable
    -getAll
        -searchs whole text document and returns a 2d list of [UserID, Phone]
    -getAllIds
        -searchs whole text and searches returns list with all phones
"""

class phonesearch:
    def __init__(self, inFile):
        self.idHash= {} #stores ids with phones as key
        self.phoneHash = {} #stores phones with ids as key
        self.file= inFile

    def searchPhone(self, id):

        #check if already found and return
        phoneHashed= checkIfPhoneFound(self, id)
        if phoneHashed!= False:
            return phoneHashed

        #get phone from ID
        toSearch= open(self.file, "r")
        toSearch= toSearch.read()
        regex= '(?<='+id+', )(.*)(?='+'\n'+')'
        phone= re.search(regex , toSearch, re.IGNORECASE)

        if phone != None:
            # remove dashes and parathesis in phone number
            phone = re.sub(r'[^\w]', "", phone.group(0))

            #add to hashtables
            phone4Hash= re.sub(r'[^\w]', "", phone)
            self.phoneHash[id] = phone4Hash
            return phone
        else:
            print("Phone number not found with ID- "+id)


    def searchID(self, phoneOrg):
        toSearch = open(self.file, "r")
        toSearch = toSearch.read()

        #make phone input numbers only
        phone = re.sub(r'[^\w]', "", phoneOrg)

        # check if already found and return
        idHashed = checkIfIdFound(self, phone)
        if idHashed != False:
            return idHashed

        #make all possible phone types for search
        phones= []
        phones.append(phone)
        phones.append(phone[0:3]+'-'+phone[3:6]+'-'+phone[6:10])
        phones.append('\('+phones[1][0:3]+'\)'+ phones[1][3:12])

        for phone in phones:
                # try to get ID from phone
                regex = '(?<=\n)(.*?)(?=, '+phone+')'
                id = re.search(regex, toSearch)
                if id!= None:
                    # add to hashtables
                    self.idHash[phones[0]] = id.group(0)
                    return id.group(0)

        print("UserId not found with phone number- " + phoneOrg)

    def getAll(self):
        toRead = open(self.file, "r")
        lines= toRead.readlines()

        #remove end line char
        i=0
        for line in lines:
            line= line.strip()
            iDandPhone= line.split(', ')
            id= iDandPhone[0]
            phone= iDandPhone[1]

            print("Found id-"+id+"- with phone, "+phone+ "\n")

            #add to hashtables
            self.idHash[phone] = id
            self.phoneHash[id] = phone

            lines[0]= iDandPhone

        toRead.close()
        return lines


# return phone if already found
def checkIfPhoneFound(self, id):
    phone= self.phoneHash.get(id)
    if phone== None:
        return False
    else:
        print('phone was found in hashtable\n')
        return phone

#return id if already found
def checkIfIdFound(self, phone):
    id= self.idHash.get(phone)
    if id== None:
        return False
    else:
        print('id was found in hashtable\n')
        return id

# makeTextDoc('searchTestFile', 25)

# search= phonesearch("searchTestFile.txt")
# search.searchPhone('testing Bad Phone Search')
#
# #testing good id search
# id= 'R9BP7TU7UYXQRORG'
# phone=search.searchPhone(id)
# print("UserID-"+id+"- had phone number "+phone+"\n")
#
# id= 'JZDKHUDFKECR0549'
# phone=search.searchPhone(id)
# print("UserID-"+id+"- had phone number "+phone+"\n")
#
# #testing bad id search
# search.searchID('testing Bad ID Search')
#
# phone= '2192983771'
# idOther=search.searchID(phone)
# print("UserID-"+id+"- had phone number "+phone+"\n")
#
# id1= search.searchID('283-753-9648')
#
# #testing good id search with all types of phone numbers
# id1= search.searchID('(617)-300-2978')
# id2= search.searchID('617-300-2978')
# id3= search.searchID('6173002978')
#
# if id1 == id2 == id3:
#      print("User ID-"+id1+"- found with all type of phone number inputs\n")
#
# search.getAll()