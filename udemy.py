
#Nested if statement
print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm?\n"))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster\n")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print(f"Please pay ${bill}\n")
    elif age <= 18:
        bill = 7
        print(f"Please pay ${bill}\n")
    elif age >= 45 & age <= 55:
        print("Everything is gonna be ok, enjoy a free ride with us!")
    else:
        bill = 12
        print(f"Please pay ${bill}\n")
        
    wants_photo = input("Do you want a photo taken? Y/N\n")
    if wants_photo == "Y":
     bill += 3
        
    print(f"Your final bill is ${bill}\n")   
else:
    print("Sorry you have to grow taller before you can ride.!\n")
