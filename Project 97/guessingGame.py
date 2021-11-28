import random
number = random.randint(1, 9)
chanceCount = 0
print("THE NUMBER GUESSING GAME")
print("Guess a number between 1 and 9")
while (chanceCount < 5):
    guess= int(input("Enter your guess: "))
    if (guess> number):
        print("Your guess is too large")
        print("Hint:Guess a number lower than ",guess)
    elif (guess == number):
        print("Congratulation! You guessed it correct")
    else :
        print("Your number guess is too less")
        print("Hint:Guess a number higher than ",guess)
    chanceCount = chanceCount + 1
if not chanceCount < 5:
    print("You lose the number is",number)
