import random 
 
def main() :
    print ("guess some random number between 10 and 100 ")
    random_number =random.randint(0,9)
    print(random_number)
    found = False 
    while  not found :
        user_guess = int(input("your guess : "))
        if user_guess ==  random_number :
            print ("you\'re  correct")
            found = True
        else :
            print ("you're a good  , guess again ")
        
        

 
    
main() 
