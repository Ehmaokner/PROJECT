import random

 
name = input("What is your name? ")

 
print("Best of Luck ! ", name)
 
words = ['scroll', 'momento', 'science', 'programming',
         'digit', 'mathematics', 'ronaldo', 'condition',
         'reverse', 'water', 'messi', 'robbery']
 

 
 
print("Guess the characters")
 
guesses = ''
 

turns = 6
 
 
while turns > 0:
     
   
    failed = 0
     
   
    for char in word:
         
       
        if char in guesses:
            print(char, end=" ")
             
        else:
            print("_")
            print(char, end=" ")
             
           
            failed += 1
             
 
    if failed == 0:
    
        print("You Win")
         
       
        print("The word is: ", word)
        break
  
    print()
    guess = input("guess a character:")
     

    guesses += guess
     
    
    if guess not in word:
         
        turns -= 1
         
       
        print("Wrong")
         
       
        print("You have", + turns, 'more guesses')
         
         
        if turns == 0:
            print("You Loose")
            