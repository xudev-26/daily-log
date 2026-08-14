import random #import the random tools to use it 

def casino(): #function responsible for randomization
    money = random.randint(100, 1000) #randomize money 100 up to 1000
    flip = random.choice(["tails", "heads"]) #choose between the two
    return money, flip #give the result to whoever need it

def display(money, bet): #function responsible for display and validation of money
    print(f"Remaining money {money}") #display the remaining money

    if bet <= money: #If bet is less than or equal to money, then do it again
        return True
    else:
        return False
    
def player(): #the main factory
    print("=" * 20)
    print("Welcome To Vegas Casino")
    print("=" * 20)
    money, flip = casino()  #calls the casino function and unpack the returned variable inside it
    failure_attempt = 0 #counter 
    while True:
        print("1. Proceed\n2. Leave")
        choice = input("Enter your choice: ")

        if choice == "2":
            print("You quitted, good financial decision")
            break

        if choice == "1":
            bet = int(input("Put your bet: "))

            if not display(money, bet):
                print("You don't have enough money for that bet!")
                continue #ask again, continue the loop

            guess = input("Enter your guess(heads/tails): ")

            if guess != flip:
                money -= bet #if player guess wrong, then minus the money with how much he bet
                print("You lose, the flip")
                failure_attempt += 1 #if fail, add 1 to the counter 

                if money <= 1:
                    print("You dont have enough money")
                    break
            else:
                money += bet #if player guess right. add the bet to the money
                print("Congratulations, the flip | Your money is doubled")
                print(money)
                break


player()





        



