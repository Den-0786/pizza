# Tip calculator
print("Welcome to tip calculator\n")

bill = float(input("What is the total bill? $\n"))
tip = int(input("What is the percentage of tip you would like to give? 10, 12, 15?\n"))
people = int(input("How many people to split the bill?\n"))

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

final_amount = "{:.2f}" .format(bill_per_person)

print(f"Each person should pays: ${final_amount}\n")
