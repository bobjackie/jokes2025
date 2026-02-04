
# the list of jokes 



# tells the code what to say basd on the users input 
# jokes = {
#     "tanks": ("Tanks", "You are welcome!"), #these are dictionary literals and seperate the KEY TERM from its values
#     "robbers": ("Calder", "Calder the police -I've been robbed"),
#     "pencils": ("Broken pencil", "Nevermind, it's pointless")
# }

#the code wil ask user if they want o hear a joke, if they respond with yes, the it will say "great, lets play" if they answer with no then the code will reply with "okay suit yourself".. if you relpy with anything else the it would remind the user that its a yes or no answer 

joke = input("Do you want to hear a joke? ")
if joke == "no":
    print("Okay suit yourself!")
elif joke == "yes":
    print("Great, Let's Play")
else:
    print("its a yes or no answer")
# the code will ask the user what joke they want to hear 
question = input("What joke do you choose? robbers, tanks, or pencils: ")

# # when the user chooses what joke thy want to hear, it will tell the joke then ask the user if they want to hear a new joke. if they do they have to say another joke they want to hear. once if they decid
# a ot netsil ot ton 
def rob():
        input("Knock Knock ")
        input("Calder")
        print("Calder police - I've been robbed!")
def pen():
    input("Knock Knock ")
    input("Broken pencil ")
    input("Nevermind, it's pointless! ")
def tank():
    one= input("Knock Knock ")
    two= input("Tank ")
    th= input("You are welcome! ")

# def jokelist():
#     if question == robbers:
#          return(rob)

if question == "robbers" :
        print(rob)
        # input("Knock Knock ")
        # input("Calder")
        # print("Calder police - I've been robbed!")
elif question == "tanks":
     print(tank)
    # input("Knock Knock ")
    # input("Tank ")
    # input("You are welcome! ")
elif question == "pencils":
        print(pen)
    # input("Knock Knock ")
    # input("Broken pencil ")
    # input("Nevermind, it's pointless! ")
joke = input("Do you want to hear another joke or are you finished? ")
# joke = input("Do you want to hear another joke or are you finished? ")

# after telling the jokes, the code will ask the user to rate the game out of ten, the give a percentage based on what the user rates the jokes
if joke == "finished":
    score = int(input("Rate the game 1-10"))
    print(str(score * 10) + " % out of 100%")

# after rating the jokes, the code will ask you if you enjoyed the jokes. the user has to anser yes or no or else the code will tell you that it is a yes or no answer

def satistifaction():
    answer = input("Did you enjoy the funny jokes? (yes/no)").lower()

    if answer == "yes":
        return "Yay! W manz"
    elif answer == "no":
        return "Bruh"
    else:
        return "idiot its a yes or no answer."
    


#      if joke == "no":
#      print("Okay suit yourself!")
#     elif joke == "yes":
#         print("Great, Let's Play")
#         question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#         if question == rob :
#             input("Knock Knock ")
#             input("Calder")
#             print("Calder police - I've been robbed!")
#             joke = input("Do you want to hear another joke or are you finished? ")
#         elif question == tank:
#             input("Knock Knock ")
#             input("Tank ")
#             input("You are welcome! ")
#             joke = input("Do you want to hear another joke or are you finished? ")
#         elif question == pen :
#             input("Knock Knock ")
#             input("Broken pencil ")
#             input("Nevermind, it's pointless! ")
#             joke = input("Do you want to hear another joke or are you finished? ")
#     if joke == "finished":
#         score = int(input("Rate the game 1-10"))
#         print(str(score * 10) + " % out of 100%")
       
# def satistifaction():
#     answer = input("Did you enjoy the funny jokes? (yes/no)").lower()

#     if answer =="yes":
#         return "Yay! W manz"
#     elif answer =="no":
#         return "Bruh"
#     else:
#         return "idiot its a yes or no answer."
    