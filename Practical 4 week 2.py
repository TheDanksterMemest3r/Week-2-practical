money = 1000

while money > 0:
    print("You have",money,"pounds")
    cost = int(input("How much will you spend?"))
    if cost <= 0:
        print("Please enter a positive number")
    else:
        money -= cost

print("You are out of money")
