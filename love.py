print("Welcome to the love calculator!\n")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_names = name1.lower() + name2.lower()

t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')

first_digit = t + r + u + e

l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')

second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.\n")
elif (love_score >= 40 and love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.\n")
else:
    print(f"Your score is {love_score}.")