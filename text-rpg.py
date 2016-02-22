def game():
    print ("MY PURELY TEXT RPG\n\n\n")
    print("Press CTRL + C to quit\n\n")
    print ("Game input is done using numbers only.")

    finish = ["GAME OVER!","YOU WIN!"]

    print ("You enter a cave.\n The path splits into two branches.\n Do you go left or right?")

    print ("1. left")
    print ("2. right")

    path = input("> ")

    if path == "1":
        print ("The path goes downhill.\n The cavern collapses behind you.\nBefore you appears a orc.\nWhat do you do?") 
        print ("1. Run")
        print ("2. Hide")
        print ("3. Attack with a nearby stone.")
        
        orc = input("> ")
        
        if orc =="1":
            print ("Nowhere to run. Nowhere to hide. The orc hears you and attacks with his sword.")
        elif orc == "2":
            print ("You die of starvation.")
        elif orc == "3":
            print ("You hit the orc. However the attack is not enough to finish him off. He attacks you with his sword.")
        else:
            print ("Well, {} got you nowhere").format(orc)
            
        return finish[0]
        game() 
        
    elif path == "2":
        print ("The path goes uphill.\nYou are exhausted by te time you reach the top.\n You hear the cavern collapse behind you.")
        print ("You reach a cliff. Below you can see a orc. The orc has a sword as well as a bow and arrow.")
        print ("You ponder on whether to navigate the narrow path next to the cliff to an opening on the other side, to jump across or to throw a stone at the orc...") 
        
        print ("1. Navigate the narrow path.")
        print ("2. Jump!")
        print ("3. Throw a stone.")
        
        cliff = input("> ")
        
        if cliff == "1":
            print ("As you move you stumble alerting the orc.\nThe orc notices you and shoots an arrow at you. It impales your knee as you enter the opening.")
            print ("Although you have an arrow in the knee you win")
            return finish[1]
        elif cliff == "2":
            print ("Epic fall!")
            return finish[0]
            game()  
        elif cliff == "3":
            print ("You hit the orc and knock it out.\nHowever, fear gets the better of you and you pass out.")
            return finish[0]
            game()
            
    else:
        print ("You're probably better off not entering the cave anyway.")
        return finish[0]
        game() 
        
def main():
    while game() != "YOU WIN!":
        game()

if __name__ == "__main__":
    main()
