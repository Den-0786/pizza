print("Welcome to the leap year checker site\n")

year = int(input("Kindly enter the year you want to check\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The {year} is a leap year")
        else:
            print(f"The {year} is not a leap year")
    else:
        print(f"The {year} is  a leap year")
else:
    print(f"{year} is not a leap year")
    
    

        
        
def is_a_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
            