namesofjokes = ["robbers", "tanks", "pencils"]



def rob():
    input("Knock Knock... ")
    input("Calder... ")
    print("Calder police - I've been robbed!")
    namesofjokes.remove("robbers")

def pen():
    input("Knock Knock... ")
    input("Broken pencil... ")
    print("Nevermind, it's pointless!")
    namesofjokes.remove("pencils")

def tank():
    input("Knock Knock... ")
    input("Tank... ")
    print("You are welcome!")
    namesofjokes.remove("robbers")
def main2():
    print("Welcome to 6036 s kolmar ave, where we joke!")

    while True:
        joke = input("Do you want to hear a joke? yes or no: ")

        if joke == "no":
            print("Okay suit yourself!")
            break
        elif joke != "yes":
            print("It's a yes or no answer")
            continue

        # User picks a joke from the CURRENT list
        outcomes()

        # If no jokes left, end the program
        if len(namesofjokes) == 0:
            print("No more jokes left!")
            break

        again = input("Do you want to hear another joke or are you finished? yes or no: ")

        if again == "yes":
            print("Remaining jokes:", namesofjokes)   # ⭐ THIS IS WHAT YOU WANTED
            continue

        if again == "no":
            score = int(input("Rate the game 1-10: "))
            print(str(score * 10) + "% out of 100%")
            answer = input("Did you enjoy the funny jokes? yes or no: ")
            satisfaction(answer)
            break


def outcomes():
    question = input("What joke do you choose? Jokes " + str(namesofjokes) + ": ")

    if question == "robbers":
        rob()
    elif question == "tanks":
        tank()
    elif question == "pencils":
        pen()
    else:
        print("That joke does not exist.")
outcomes()