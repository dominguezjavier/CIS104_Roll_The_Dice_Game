import random

# get random number step 1
def getRandomNumber ():
    return random.randint (1,101) #random.randit gives you an integer.

def compareNumbers (randNumber, userNumber):
    return userNumber - randNumber

randNumber = getRandomNumber ()

keepGoing = True

while(keepGoing):

# step 2 ask user for a number
    userNumber = input("Please choose a number between 1 and 100: ")
    try:
        intuserNumber = int(userNumber) # step 2.5 convert the user number to an integer
    except:
        print("Please try again with a number. ")
        continue # a continue option will let you stay in the loop and try again.
                 # a break will terminate the program completely.
# step 3 compare numbers
    difference = compareNumbers (randNumber, intuserNumber)

#print (str(randNumber) + " " + str(userNumber))

# step 4 give user feedback
    if(difference < 0):
        print("Your choice is too low. ")
    elif(difference > 0):
        print("Your choice is too high. ")
    else:
        print("Your choice is correct. ")
        keepGoing = False

print (" Game Over! Congratulations. ")