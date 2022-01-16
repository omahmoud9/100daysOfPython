print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = float(input("How many people to split the bill? "))

bill_plus_tip = bill * (1 + (tip / 100 ))
cost_per_person = round(bill_plus_tip / (number_of_people), 2)
cost_per_person = "{:.2f}".format(cost_per_person)
print(f"Each person should pay : ${cost_per_person}")
