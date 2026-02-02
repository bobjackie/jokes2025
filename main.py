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
        rate = int(input("Please rate our game 1-10! "))
        final_score = int(rate * 10)
        print(str(final_score) + " percent satisfaction rate")
       
def satistifaction():
        satistifaction = input("Did you enjoy the jokes? ")

        userinput= input("Please enter 'yes' or 'no': ").lower()
        if satistifaction == "yes":
            return "Yay! We are glad you enjoyed it!"
        elif satistifaction == "no":
            return "We're sorry you didn't enjoy it.".upper()
        else:
            return "Invalid response. Please answer with 'yes' or 'no'."
