import re                                       #module to work in regular expression
phoneNumberFile = open('PhoneNumbers.Txt','r')  #opens txt file
phoneNumberData = phoneNumberFile.read()        #reads txt file
phoneNumberList = phoneNumberData.split("\n")   #makes a list of where each row is an item

for index,x in list(enumerate(phoneNumberList)):     #loop to go through all items in list
    x = re.sub('[^0-9]','', x)    #removes non-numeric values
    x = "(" + x[:3] + ")" + x[3:] #adds brackets
    x = x[:5] + " " + x[5:]       #adds space
    x = x[:-4] + "-" + x[-4:]     #adds hyphen
    phoneNumberList[index] = x    #rewrites list item

print(phoneNumberList)     #Writes list to new txt file
with open('FormattedPhoneNumbers.txt', 'w') as f:
    for item in phoneNumberList:
        f.write(item + '\n')






