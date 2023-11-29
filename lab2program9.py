month= input("Enter the month: ").capitalize()
day= int(input("Enter the date: "))
if(month == "March" and day >= 20) or (month == "April" or month == "May")or (month=="June" and day<21):
    print("summer")
elif(month == "June" and day >= 21) or (month == "July" or month == "August")or(month=="September" and day<22):
    print("spring")
elif(month == "September" and day >= 22) or (month == "October" or month == "November")or (month=="December" and day<21):
    print("Fall")
else:
    print("Winter")

