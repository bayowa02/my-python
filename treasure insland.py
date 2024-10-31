print("welcome to Treasure island.")
print("Your mission is to find the treasure.")


step1 = input("you're at a cross road , where do you want to go? \n type 'left', 'right':")
if step1 == "right":
    step2 = input("you've come to a lake , there is an island in the middle of the late \n type 'wait' to wait for a boat , type 'swim' to swim across.")
   
    if step2 == "wait":
        step3 = input("you've arrive at the island unharmed. there is a house with 3 doors. \n one red,  one yellow, one blue. choose a colour")
        
        if step3 == "red":
            print("its a room full of fire. game over ")
        elif step3 == "yellow":
            print("congratulation you are safe")
        else:
            print("you where eating. game over")
    
    else:
        print("you where eating buy a crocodie. game over")   

else:
    print("you where killed by the montin gorilars. game over")            