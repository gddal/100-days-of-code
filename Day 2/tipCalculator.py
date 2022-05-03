bill = float(input("What was the total bill?\n"))
percentage = float(
    "1."+(input("What percentage tip would you like to give? ex:10\n")))
number_of_people = int(input("How many people to split the bill?\n"))
total = round(bill*percentage)
per_person = "{:.2f}".format(round(total/number_of_people, 2))
print(f"Each person should pay: {per_person} euros")
