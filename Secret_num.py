secret_number = 20

guesses = 0
while True:
    guesses += 1
    number = input("Guess the number: ")

    try:
        number = int(number)
    except:
        print("Sorry that is not a number")
        continue

    if number != secret_number:
        if number > secret_number:
            print(number, "is greater than the secret number")

        elif number < secret_number:
            print(number, "is less than the secret number")
    else:
        print("You guessed the number:", secret_number)
        break

print("You got it in", guesses, "guesses")
