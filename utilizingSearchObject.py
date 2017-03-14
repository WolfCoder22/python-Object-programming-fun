from phonesearch import phonesearch
import time
from createTxtFile import makeTextDoc

#make the phone list
#makeTextDoc("phoneDirectory.txt", 100000)

searcher= phonesearch("phoneDirectory.txt")

#search for phone numbers with userID

phone1= searcher.searchPhone("TQU28QFAU9S37LCR")
phone2= searcher.searchPhone("29NSHGWPL3MNSP32")
phone3= searcher.searchPhone("ARK1N2TK56UGHMYO")
phone4= searcher.searchPhone("TQU28QFAU9S37LCR")
phone5= searcher.searchPhone("NP9XTO2NPVM56C4Q")
phone6= searcher.searchPhone("2PET2SQ3RVWSIVP7")
phone7= searcher.searchPhone("CNSJ72NS0KI23NB4")

#print phone when searchPhone() does not return false
if phone1:
    print("found number-"+phone1)
if phone2:
    print("found number-"+phone2)
if phone3:
    print("found number-"+phone3)
if phone4:
    print("found number-"+phone4)
if phone5:
    print("found number-"+phone5)
if phone6:
    print("found number-"+phone6)
if phone7:
    print("found number-"+phone7)

#Search for user ID's given phone number
userId1= searcher.searchID("3663526885")
print(userId1+"\n")
userId2= searcher.searchID("366-352-6885")
print(userId2+"\n")
userId3= searcher.searchID("(353)-632-7790")
print(userId3+"\n")
userId4= searcher.searchID("353-632-7790")
print(userId4+"\n")
userId5= searcher.searchID("3801707239")
userId6= searcher.searchID("120-283-2930")
userId7= searcher.searchID("(827)-239-1108")

#print Id when searchID() does not return false
if userId1:
    print ("found UserId-"+userId1)
if userId2:
    print ("found UserId-"+userId2)
if userId3:
    print ("found UserId-"+userId3)
if userId4:
    print ("found UserId-"+userId4)
if userId5:
    print ("found UserId-"+userId5)
if userId6:
    print ("found UserId-"+userId6)
if userId7:
    print ("found UserId-"+userId7)

time.sleep(10) #pause to see good results from above
allData= searcher.getAll()






