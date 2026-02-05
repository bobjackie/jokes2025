#Adrian Marquez, Breanna Tapia and Jacqueline Sandoval 


namesofjokes = ["robbers", "tanks", "pencils"]
# this is a list of the jokes that the user can choose from, it is used to
def rob():
    input("Knock Knock... ")
    input("Calder... ")
    print("Calder police - I've been robbed!")

def pen():
    input("Knock Knock... ")
    input("Broken pencil... ")
    print("Nevermind, it's pointless!")

def tank():
    input("Knock Knock... ")
    input("Tank... ")
    print("You are welcome!")
# These fucntions are what the, after the user picks a joke, will display
# The first two tine of the fucntion say input as the user has to press enter in order to continue 
#and the last line, so the print statement, is the last line of the joke so the user does not have to input anything to continue.
def satisfaction(answer):
    if answer == "yes":
        print("Yay! W manz")
    elif answer == "no":
        print("Bruh")
    else:
        print("Type yes or no")
# This function makes it so that after the user can input yes or no to if they enjoyed the jokes or not
# these fucntions are outside of the while True: statement because if they are inputed 
# inside of the fucntion, the program has to loop through the fucntion over and over again 
# aswell, the satistfaction function is after the user says they do not want to hear another joke because if it was before, the user would have to rate the jokes before they even heard them.

print("Welcome to Narnia, where we joke!")


while True:  # will make it so that the code can loop again if they user says they want to hear another joke
    joke = input("Do you want to hear a joke? yes or no: ")

    if joke == "no":
        print("Okay suit yourself!")
        break  # #stops the program since they said no
    elif joke != "yes":
        print("It's a yes or no answer")
        continue  # makes it so that the code can restrat since the user did not answer with a yes or no

# the code will ask the user what joke they want to hear 
    question = input("What joke do you choose? Jokes" + str(namesofjokes) + ": ")
# when the user chooses what joke thy want to hear, it will tell the joke then ask the user if they want to hear a new joke. if they do they have to say another joke they want to hear. once if they decid
    if question == "robbers":
        rob()
    elif question == "tanks":
        tank()
    elif question == "pencils":
        pen()
    else:
        print("That joke does not exist.")
# these codes are calling the fucntions that are above the while True: statement to print them out. 
    # Ask if they want another joke or finish
    again = input("Do you want to hear another joke or are you finished? yes or no: ")

    if again == "no": # this goes at the end of the program, and is done so that when the user is done with the program, they starts to rate it
        score = int(input("Rate the game 1-10: ")) # after telling the jokes, the code will ask the user to rate the game out of ten, the give a percentage based on what the user rates the jokes
        print(str(score * 10) + "% out of 100%")
        answer = input("Did you enjoy the funny jokes? yes or no: ")
        satisfaction(answer)
        break #stops the program since they said and rated the jokes