phoneNumberFile = open('PhoneNumbers.Txt','r')
phoneNumberData = phoneNumberFile.read()
phoneNumberList = phoneNumberData.split("\n")
print(phoneNumberList)