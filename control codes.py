marks=int(input("weka alama yako"))
#if elif else statement
if  marks > 80 and marks <= 100:
    print("You scored an A")
elif marks > 60 and marks <= 80:
    print("you scored a B")
elif marks > 40 and marks <= 60:
    print("You have a C")
elif marks > 30 and marks <= 40:
    print("you have a D")
elif marks >=0 and marks <= 30:
    print("You have an E")
else:
    print("wrong input!")

price=int(input("enter you price range"))
#if elif else statement
if price>5000000 and price<10000000:
    print("you can purchase a Tesla")
elif price>3000000 and price<5000000:
    print("you can buy a BMW and a mercedes benz and V8")
elif price>1000000 and price<3000000:
    print("you can purchase a harrier")
elif price>500000 and price<1000000:
    print("you can purchase a vitz or probox")
else:
    print("WRONG INPUT!!!")


color = input("enter color")
#if elif else statement
if color == "red":
    print("wear red on monday")
elif color== "Blue":
    print("i wear Blue on tuesday")
elif color == "Yellow":
    print("i wear Yellow on wednesday")
elif color == "white":
    print("i wear white on thursday")
elif color == "black":
    print("i wear black on friday")
else:
    print("I do not have those clothes")
