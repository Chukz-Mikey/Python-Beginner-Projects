print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0


playagain = True

while playagain:
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!!!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct!!!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory":
        print("Correct!!!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does UPS stand for? ")
    if answer.lower() == "universal power supply":
        print("Correct!!!")
        score += 1
    else:
        print("Incorrect!")

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 4) * 100) + "%.")

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🙌🎉🎉")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye! 👋")
