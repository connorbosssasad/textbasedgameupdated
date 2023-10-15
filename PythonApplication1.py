import time
count = 3
restart = True
while restart == True:
    # Receiving messages from strangers
    print("Uh-oh! You're exploring the digital world on your computer, and you've just received a message from a character you've never met before. They look a bit suspicious, and they're asking for personal information. What should you do to stay safe and make the right choice? Type your next move to continue the adventure!")
    time.sleep(1)
    print("Type 1: to reply to the suspicious person", " or type 2: to block the suspicious character")
    choice = input("1 or 2: ")
    if choice == "1":
        print("Uh-oh! You decided to share your personal information with the mysterious character. Suddenly, your computer screen starts acting strange, and a spooky laugh echoes through your speakers. It looks like you might be in trouble!")
        count -=1
        
    elif choice == "2":
        print("Great job! You didn't share any personal information with the suspicious character. Continue forth with the adventure!")
        
        print("Great! You've learned the importance of online safety.")
        time.sleep(1)

    # Dont give name to strangers
    name = input("Out of curiosity... What is your name?: ")
    print(f"Okay, {name} have you learned nothing! You just gave me your name... you are lucky im trustworthy.")
    time.sleep(1)
        
    # Choose secure username
    print(f"Choose an online username from the following; 1: {name}dogross, 2: MyName{name}IsAwesome, 3: UnsquashedBerry23")
    time.sleep(1)
    choiceofname = input("Choose either: 1, 2, or 3:  ")
    time.sleep(1)
    if choiceofname == "1":
        print("WRONG CHOICE! THAT HAS YOUR NAME IN IT")
        count -= 1

    elif choiceofname == "2":
        print("WRONG CHOICE! THAT ALSO HAS YOUR NAME IN IT!!!")
        count -= 1

    elif choiceofname == "3":
        print("Wow, that is an excellent choice! Very private and secure.")

    # Receiving strange email
    time.sleep(1)
    print("Uh-oh! As you continue your e-safety adventure, you check your email and notice a strange message from an unknown sender. The subject line says, 'You've won a million dollars! How will you reply?")
    time.sleep(1)
    print("1: Open the email and see what it is all about, 2: Delete the email without opening it, 3:Report the email as spam to your email provider ")
    reply = input("1, 2 or 3: ")
    if reply == "1":
        print("WRONG CHOICE! YOU HAVE MALWARE DOWNLOADING AT THIS CURRENT MOMENT!")
        count -= 1
        
    elif reply == "2":
        print("That is a good choice, but not the one i was looking for...")
        count -= 1

    elif reply == "3":
        print("Fantastic! That is an excellent choice!!! You made the right decision.")
        
    # Meeting online player
    time.sleep(1)
    print("Uh-oh! While playing your favorite online game, you meet another player who seems friendly at first. They start asking for very personal details like your full name, home address, and even your phone number. You remember the important rule: 'Never share personal information with strangers online")
    time.sleep(1)
    print("1: Share the information because they seem nice. 2: Politely refuse and remind them it's not safe. 3: Report the player to the game moderators.")
    reply2 = input("1, 2 or 3: ")
    if reply2 == "1":
        print("WRONG CHOICE! NOW THEY ARE COMING TO YOUR ADDRESS")
        count -= 1
        
    elif reply2 == "2":
        print("That is a good choice, but it is not the one i wanted!!!!")
        count -= 1

    elif reply2 == "3":
        print("Good job! that is the answer i was looking for.")
        
    # Unknown friend request
    time.sleep(1)
    print("Uh-oh! You recieve a friend request from someone you have no mutual friends with. They seem to be new to the social media website")
    time.sleep(1)
    print("1: Accept the strangers friend request. 2: Deny the friend request and block the strange person. ")
    reply3 = input("Choose either option 1 or 2: ")
    if reply3 == "1":
        print("WRONG CHOICE! THEY NOW HAVE ACCESS TO ALL OF YOUR DATA")
        count -= 1
        
    elif reply3 == "2":
        print("Correct choice!")    

    # Posting photos online
    time.sleep(1)
    print("Uh-oh! You have a public account on social media and decided to post images of you and some friends. These images can be seen by anyone, what steps should you take to make these photos private")
    time.sleep(1)
    print("1: Delete the photos. 2: Make your account private. 3: Do nothing")
    reply4 = input("Choose either option 1, 2 or 3:  ")
    if reply4 == "1":
        print("Good choice, but there is a much simpler way to secure these photos")
    if reply4 == "2":
        print("Correct choice!")
    if reply4 == "3":
        print("Wrong choice! your images are still available to the public")        
        count -= 1
    
    
    if count <= 0:
        print(f"You lost the game, your points are at {count}.")
    elif count > 0:
        print(f"You won the game with {count} lives left!")
            
    choice4 = input("Do you want to restart? (yes/no) ").lower()
    if choice4 == "yes":
        restart = True
        count = 3
    elif choice4 == "no":
        restart = False
    else:
        print("That was not a choice buddy.")



        








          
  