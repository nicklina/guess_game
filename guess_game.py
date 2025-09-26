import random

print("To stop anytime, enter: q")
score = 0

while True:  # "True" must be capitalized
    num = random.randint(0, 10)  # spelling: randint not randit
    guess = input("Guess a number between 0 to 10: ")

    if guess == "q":
        print("Game over")
        break

    guess_num = int(guess)

    if guess_num == num:  # use == for comparison, not "is"
        print("CONGRATS, you guessed it correct")
        score += 10
        print("Your new score:", score)
    else:
        print("Your guess didn't match")
        print("The number was:", num)
