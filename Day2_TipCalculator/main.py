total = 0.0
people = 0
tip = 0

print("Welcome to the tip calculator")
total = float(input("What was the total bill?\n>$"))
people = int(input("How many people split the bill?\n>"))

while tip != 10 and tip != 12 and tip != 15:
    tip = int(input("How much tip would you like to give? 10, 12 or 15?\n>"))

    if tip != 10 and tip != 12 and tip != 15:
        print("ERROR\nInvalid percentage!\n")

tip_per_person = (total * (tip / 100) + total) / people
print(f"Every person should pay: $" + "{:.2f}".format(tip_per_person))