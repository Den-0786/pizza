print("Welcome to my pizza delivery service!\n")

bill = 0
pepperoni_small = 2
pepperoni_large = 3

Size = input("What size of the pizza do you want? S, M, or L\n")

if Size == "S":
    print("You have ordered a small pizza\n")
    bill +=15
    print(f"The cost will be ${bill}")
    
elif Size == "M":
    print("You have ordered a medium pizza\n")
    bill +=20
    print(f"The cost will be ${bill}")
    
elif Size == "L":
    print("You have ordered a large pizza\n")
    bill +=25
    print(f"The cost will be ${bill}")
    
Add_pepperoni = input("Do you want pepperoni? Y or N\n")
if Add_pepperoni == "Y":
    size_of_pepperoni = input("What size of pepperoni do you want? S or M\n")
    print("You have ordered pepperoni\n")
    if Size == "S":
        bill += pepperoni_small
        print(f"The cost will be ${bill}")
    elif Size == "M":
        bill += pepperoni_large
        print(f"The cost will be ${bill}")
        
add_cheese = input("Do you want cheese? Y or N\n")
if add_cheese == "Y":
        print("You have ordered cheese\n")
        bill += 1
        print(f"The cost will be ${bill}")
print(f"Please your total bill is ${bill}. Thanks for ordering from us! Have a nice day!")