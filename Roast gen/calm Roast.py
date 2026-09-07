import random
from roasts import ROASTS
def Roaster():

    while True:
        user_input = input("Do you want to generate a roast?").lower()
        if user_input == 'no':
            print("Bye")
            break
        elif user_input == 'yes':
            print(random.choice(ROASTS))
        else:
            print("I didnt get that!")
Roaster()
      
