#Adrian Marquez, Breanna Tapia and Jacqueline Sandoval 
def rob():
    input("Knock Knock... ")
    input("Calder...")
    print("Calder police - I've been robbed!")
def pen():
    input("Knock Knock.... ")
    input("Broken pencil... ")
    print("Nevermind, it's pointless! ")

def tank():
    input("Knock Knock... ")
    input("Tank... ")
    print("You are welcome! ")

def satistifaction():
    answer = input("Did you enjoy the funny jokes? yes or no ")
    if answer == "yes":
        print("Yay! W manz")
    elif answer == "no":
        print("Bruh")
    else:
        print("Type yes or no")

satistifaction()

#the code wil ask user if they want o hear a joke, if they respond with yes, the it will say "great, lets play" if they answer with no then the code will reply with "okay suit yourself".. if you relpy with anything else the it would remind the user that its a yes or no answer 
print ("Welcome to narnia, where we joke.")
while True: # will make it so that the code can loop again if they user says they want to hear another joke
    joke = input("Do you want to hear a joke? ")
    if joke == "no":
        print("Okay suit yourself!")
        break #stops the program since they said no
    elif joke == "yes":
            print("Great, Let's Play")
    else:
        print("its a yes or no answer")
        continue #restarts the loop if the user does not answer with yes or no
    # the code will ask the user what joke they want to hear 
    question = input("What joke do you choose? robbers, tanks, or pencils: ")

    # # when the user chooses what joke thy want to hear, it will tell the joke then ask the user if they want to hear a new joke. if they do they have to say another joke they want to hear. once if they decid
 
    if question == "robbers" :
        rob()

    elif question == "tanks":
        tank()

    elif question == "pencils":
        pen()
    else:
        print("That joke not exist")


    # joke = input("Do you want to hear another joke or are you finished? ")

    # after telling the jokes, the code will ask the user to rate the game out of ten, the give a percentage based on what the user rates the jokes
    joke = input("Do you want to hear another joke or no ")

    if joke == "no":
        score = int(input("Rate the game 1-10: "))
        print(str(score * 10) + "% out of 100%")
        break #stops the program since they said and rated the jokes
# after rating the jokes, the code will ask you if you enjoyed the jokes. the user has to anser yes or no or else the code will tell you that it is a yes or no answer
