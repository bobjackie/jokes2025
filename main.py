def jokelist(robbers, tanks, pencils):
    rob = jokelist[0]
    tank = jokelist[1]
    pen = jokelist[2]
    joke = input("Do you want to hear a joke? ")
    if joke == "no":
     print("Okay suit yourself!")
    elif joke == "yes":
        print("Great, Let's Play")
        question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
        if question == rob :
            input("Knock Knock ")
            input("Calder")
            print("Calder police - I've been robbed!")
            joke = input("Do you want to hear another joke or are you finished? ")
        elif question == tank:
            input("Knock Knock ")
            input("Tank ")
            input("You are welcome! ")
            joke = input("Do you want to hear another joke or are you finished? ")
        elif question == pen :
            input("Knock Knock ")
            input("Broken pencil ")
            input("Nevermind, it's pointless! ")
            joke = input("Do you want to hear another joke or are you finished? ")
    if joke == "finished":
        score = int(input("Rate the game 1-10"))
        print(str(score * 10) + " % out of 100%")
       
def satistifaction():
    answer = input("Did you enjoy the funny jokes? (yes/no)").lower()

    if answer =="yes":
        return "Yay! W manz"
    elif answer =="no":
        return "Bruh"
    else:
        return "idiot its a yes or no answer."
    

print (jokelist)
