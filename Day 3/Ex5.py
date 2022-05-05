print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1_lower = name1.lower()
name2_lower = name2.lower()
total_true = 0
total_love = 0
# first name
total_true += name1_lower.count("t") + name1_lower.count("r") + \
    name1_lower.count("u") + name1_lower.count("e")
total_love += name1_lower.count("l") + name1_lower.count("o") + \
    name1_lower.count("v") + name1_lower.count("e")
# second name
total_true += name2_lower.count("t") + name2_lower.count("r") + \
    name2_lower.count("u") + name2_lower.count("e")
total_love += name2_lower.count("l") + name2_lower.count("o") + \
    name2_lower.count("v") + name2_lower.count("e")
# sum points
score = str(total_love) + str(total_true)
score = int(score)
if(score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos")
if(score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your socre is {score}")
