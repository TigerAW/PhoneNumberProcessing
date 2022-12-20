import re
phoneNumberFile = open('PhoneNumbers.Txt','r')
phoneNumberData = phoneNumberFile.read()
phoneNumberList = phoneNumberData.split("\n")
print(phoneNumberList)
for index,x in list(enumerate(phoneNumberList)):
    x = re.sub('[^0-9]','', x)
    phoneNumberList[index] = x

print(phoneNumberList)






