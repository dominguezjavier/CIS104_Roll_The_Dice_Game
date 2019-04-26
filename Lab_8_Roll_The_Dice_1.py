import random


# get random number rolled from the dice step 1
def rollRandomNumber ():
    return random.randint (1, 7) #random.randit gives you an integer.


keepRolling = True


while(keepRolling):

    
    print(" This is the number you rolled " + str(rollRandomNumber()) + " .Would you like to roll again? ")

    playersChoice = input("If you would like to roll again press y to continue or n to stop. ")

    
    
    if playersChoice == 'y':
       rollRandomNumber()

    else:
        print (" Thank you for playing. Keep it rolling. ")
        keepRolling = False


