# life in week
age = input("What is your current year?")
years = 90 - int(age)
months = round(years * 12)
weeks = years * 52
days = years * 365
print(f"You have {years} years, {months} months, {weeks} weeks and  {days} days remaining")