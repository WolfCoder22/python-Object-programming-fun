import string
import random

"""
These functions are used to generate a text document with random phone numbers and userIDs
-Make sure not to have the amount of numbers exceed 10^10; should use much
  smaller since numbers randomly and recuresivley computer
-import make and call makeTextDoc(outFilName, numUser/phonenumbers) to generate the document
"""

#make the whole text doc
def makeTextDoc(outFile, numPhones) :

    # make sure don't do more than every possible phone number
    if numPhones > 10 ** 10:
        print("Number of phones exceeded possible amount. Use 10^10 or less"+'\n'+"Advice using much smaller since number recursivley computer"+'\n')
        return

    idSet= set()
    phoneSet= set()
    out= open(outFile, 'w')
    for i in range(numPhones):

        id= makeUserId()
        phone= makePhoneNum()
        id= checkUniqueId(idSet, id)
        phone= checkUniqueNum(phoneSet, phone)

        line= id+', '+phone
        if i!= numPhones-1:
            line= line+'\n' #don't add new line on last
        out.write(line)
    out.close()

# recursively check if an ID already made
def checkUniqueId(idSet, id):
    if id in idSet:
        newId = makeUserId()
        return checkUniqueId(idSet, newId)

    else:  # wasn't in set return
        idSet.add(id)
        return id

# recursively check if an phoneNumber already made
def checkUniqueNum(phoneSet, phone):
    checkphone= phone
    l=0
    if phone in phoneSet:
        newPhone = makePhoneNum()
        return checkUniqueNum(phoneSet, newPhone)
    else:
        # add dashes half the time and () around area code
        if random.uniform(0,1) > .5:
            first = phone[0:3]
            if random.uniform(0,1) > .5:
                first= '('+first+')'
            second = phone[3:6]
            third = phone[6:10]
            phone = first + '-' + second + '-' + third

        phoneSet.add(phone)
        return phone

# make a random userID
def makeUserId():
    return''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

# make a random phone number
def makePhoneNum():
    phone=''.join(random.choices(string.digits, k=10))
    return phone


#driver for function
# makeTextDoc("testFile1", 10)
# makeTextDoc("testFile2", 100)
# makeTextDoc("testFile3", 10000)
# makeTextDoc("testFile4", 9999999999)


