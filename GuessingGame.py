secretNumber = 15

print("You Have 3 Chances To Guess The Number ")
print("Hint : Number Is Less Than 25...")

i = 1
guessLimit = 3
while i <= guessLimit:
    guessedNumber = int(input("Enter Number : "))
    if guessedNumber == secretNumber:
        print("You Win...")
        break
    if i == 3:
        print("You Failed...")
    i += 1