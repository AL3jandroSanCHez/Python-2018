

import random
import time



name = input("What's your name?")
print("Hello, %s" % name.title())
print("This is the Magic 8 Ball Game, "+ name.title()+ "!")

list_responses = [ "It's certain, %s." % name.title(), "Sure", "Completly not.", "That never is going to happen.",
                   "It's preferible that you never know the answer to this question.",
                   "Maybe not now, but then could be.","Don't count on it.",
                   "You already know the answer to this question.",
                   "That is totally false.","Completly true."]

while True:

    question = input("Do you want to know the trust? What is your question? If you want to exit, press x.")
    if question.strip() == "x":
        break                

    print("Just wait 5 seconds to know the TRUTH.")
    time.sleep(1)
    print(random.choice(list_responses))
    
                     

