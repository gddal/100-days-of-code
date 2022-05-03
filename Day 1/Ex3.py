firstVariable = input("Write a number: a=")
secondVariable = input("Write another number: b=")

temVariable = firstVariable
firstVariable = secondVariable
secondVariable = temVariable

print("They got switched!")
print(firstVariable)
print(secondVariable)
