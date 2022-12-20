import re
phoneNumberFile = open('PhoneNumbers.Txt','r')
phoneNumberData = phoneNumberFile.read()
phoneNumberList = phoneNumberData.split("\n")
print(phoneNumberList)
for index,x in list(enumerate(phoneNumberList)):
    x = re.sub('[^0-9]','', x)
    x = "(" + x[:3] + ")" + x[3:] #adds brackets
    x = x[:5] + " " + x[5:]       #adds space
    x = x[:-4] + "-" + x[-4:]     #adds hyphen
    phoneNumberList[index] = x

#formatted_numbers = ["(" + number[:3] + ")" + number[3:] for number in phoneNumberList]

#spaced_numbers = [number[:5] + " " + number[5:] for number in formatted_numbers]

#hyphen_numbers = [number[:-4] + "-" + number[-4:] for number in spaced_numbers]

print(phoneNumberList)





