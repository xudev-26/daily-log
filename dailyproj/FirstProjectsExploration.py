import random
import sys

HANGMAN_PICS = [r""" #list of pictures, the r in the beginning stands for raw strings. so any special character is ignored and treated as just string
    +---+

    |   |
        |
        |
        |
        |
=========""", r"""
    +---+

    |   |
    O   |
        |
        |
        |
=========""", r"""
    +---+

    |   |
    O   |

    |   |
        |
        |
=========""", r"""
    +---+

    |   |
    O   |
   /|   |
        |
        |
=========""", r"""
    +---+

    |   |
    O   |
   /|\  |
        |
        |
=========""", r"""
    +---+

    |   |
    O   |
   /|\  |
   /    |
        |
=========""", r"""
    +---+

    |   |
    O   |
   /|\  |
   / \  |
        |
========="""]

guillotine_pics = [r""" #Same as the first variable that contains the picture of hangman
    +---+

    |   |
    |   |
    |   |
    |   |
    |   |
=========""", r"""
    +---+

    |   |
    |   |
    |   |
    |   |
    |  /\

    |  ||
=========""", r"""
    +---+

    |   |
    |   |
    |   |
    |  /\

    |  O |
    |  ||
=========""", r"""
    +---+

    |   |
    |   |
    |  /\

    |  O |
    | /| |
    |  ||
=========""", r"""
    +---+

    |   |
    |  /\

    |  O |
    | /|\|
    | / |
=========""", r"""
    +---+

    |   |
    |  /\

    |  O |
    | /|\|
    | / \
=========""", r"""
    +---+

    |   |
    |  /\

    |  O |
    | /|\|
    | / \
    |  _
========="""]

animals = "ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA".split()
fruits = "APPLE BANANA CHERRY DATE FIG GRAPE KIWI LEMON MANGO ORANGE PAPAYA PEACH PEAR PLUM QUINCE RAISIN STRAWBERRY TANGERINE WATERMELON".split() #A string that is converted into list of substring because of split() function

def validation(): #function named validation, the job of this function is to get the user choice
    print("1. Animals\n2. Fruits")#display | instructions
    while True:
        category = { #Nested dictionary that contains the choice player can pick 
            "1": {#this key, no. 1 when accessed leads to the animal variable and HANGMAN_PICS
                "words": animals,
                "pics": HANGMAN_PICS
            },
            "2": { #the key 2 when accessed leads to the fruits variable and guillotine_pics
                "words": fruits,
                "pics": guillotine_pics
            }
        }
        user = input("Enter your choice: ").strip() #Get the user choice, strip() function is use to remove any possible whitespace 
        if user in category: #Checks if the input user variable is in the category dictionary  
            selected = category[user] #If the input is in the category dictionary, then get the keys using the user input. and then store it in the variable named selected
            return selected #return the data to where it is needed to be used

def draw_board(pics, missed, correct, word): #function that contains threee parameters, the job of this function is to display the chosen picture
    print(pics[len(missed)]) #get the list of picture, then get the given index using how many times player has missed
    blanks = ["_"] * len(word) #Display blanks using len() functionn base on how many word is in the given word, 
    for i in range(len(word)): #generate a sequence of letters base on how many letter is in the word
        if word[i] in correct: #now if the word in generated sequence of letter is in correct
            blanks[i] = word[i]#Replace the single blank with the correct letters 
    print(" ".join(blanks)) #Join them together so it doesnt look like a list 
    print("\nMissed letters:", " ".join(missed)) #Display the missed letter

def get_guess(already_guessed):#the job of this function is to get the player guess | the parameter acts as a checker 
    while True: #Keep running as long as the condition is true 
        guess = input("Enter your guess: ").upper() #converts the input into an uppercase letter using upper() function
        if guess in already_guessed: #Now if the input in guess is in already_guessed    
            print("You've already guessed that.")#Display this
        elif len(guess) != 1: #Player can only guess 1 letter, so if it os more than that. ask the player again
            print("Enter only one letter.")
        elif not guess.isalpha(): #Checks if the user input is not a letter 
            print("Letters only.")
        else:
            return guess #return the data to wherever it is needed 

def main():#This is where everythings gather, in this function 
    selected = validation() #call the validation function inside the selected variable()
    secret_word = random.choice(selected["words"])#get the value of word inside validation() then randomize it using random module
    missed_letters = [] #Storage for missed letter
    correct_letters = [] #for correct one

    while True:
        draw_board(selected["pics"], missed_letters, correct_letters, secret_word) #call the drawboard() function along with its parameters, because those parameter have data | 
        #we specifically accessed the picture by using the selected variable which has the value of the validation() function and get the value of the pics
        guess = get_guess(missed_letters + correct_letters) #call the get_guess() function and combine the missed and correct to check if the user already typed that letter, storing it in variable named guess

        if guess in secret_word: #If the guess actually inside secret_word, then add it to the empty list of correct
            correct_letters.append(guess)
        else: #opposite of the first one
            missed_letters.append(guess)

        if all(letter in correct_letters for letter in secret_word): #generate a sequence of letter that is in secret_word using the letter variable
            #then check if that letter is in correct
            print("\n" + secret_word)
            print("Congratulations! You guessed the word!") #display
            break #stop the loop
    
        if len(missed_letters) == len(selected["pics"]) - 1: #now if the missed letter has reached how many pictures in pics, then game ends and player lose 
            print(selected["pics"][len(missed_letters)])
            print("\nGame Over!")
            print("The word was:", secret_word)
            break


if __name__ == "__main__": #acts as a gate 
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
