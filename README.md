# python-object-programming-fun
###Playing around with python, object oriented programming, and data structures

###Things that I used to note
1. Recurion used to check if randomly generted userId/phoneNumber already made
	- see creatTextFile.py line 35 and 45
2. Used Set to keep track of which UserId's or Phone numbers already created
	- see line 19+ 20 in creatTextFile.py
	- wanted to use linked list but using a Set made much more sense
3. Created a searcher class which searches the genereted text document
	- methods for searhing and returning by userID, phone, and all data
4. Found ids/phone numbers stored in hastable(dictionary) to make searching quicker
	- all hashed numbers stored without the () or - in phone numbers
5. Regexs used to search the textdocument and normalize phone numbers
	- See line 37, 72, and 41
6. Made commented out drivers on the bottom of each file for testing
7. A complete driver for the class showing its execution on a large document
	- File named utilizingSearchObject.py

