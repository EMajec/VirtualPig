#author: Ethan Turner
#date: 09/20/16
#description: This code allows for a two player version of pig, the dice game.
#proposed points (15 of 15): My assignment efficiently accomplishes all of the tasks



import random #you'll need this for the roll_die function


def main():
    p1_name = get_name() #creates the name for player one after calling my function
    p2_name = get_name() #cretaes the name for player 2 after calling my function
    p1_score = 0 #keeps track of Player 1's score
    p2_score = 0 #keeps track of Player 2's score
    whose_turn = 1 #keeps track of which player's turn it is

    #the game keeps going until one of the players reaches 100 points
    while p1_score < 100 and p2_score < 100:

        #print the score board
        print_score(p1_name,p1_score,p2_name,p2_score)

        #call take turn and update the score
        # for the correct player
        if whose_turn == 1: #check if it's Player 1's turn
            p1_score += take_turn(p1_name)
            whose_turn = 2 #next time through the loop, it will be Player 2's turn
        else:
            p2_score += take_turn(p2_name)
            whose_turn = 1 #next time through the loop, it will be Player 1's turn


    game_end_message(p1_name,p1_score,p2_name,p2_score) #when score gets above 100 we call this function below



#This function allows the user to take turns in the game
#track score for the round and each roll.
def take_turn(player_name):
    round_score = 0 #initializes counter for the round score
    roll_die()      #Rolls the dice for the turn
    score = roll_die() #Sets the score of each roll
    while score != 1:  # Allows the roller to continue rolling until they roll a pig
        round_score += score #adds the score from each roll to the total round score
        print(player_name, "rolled a ", score) #Tells the player what they rolled
        print("Turn Total: ",round_score) #Tells the player how much they rolled in the round counter.
        again = str(input("Roll again? y/n: ")) #asks the user to roll again
        if again is "y": #if yes then the program will call the random die function
            roll_die() #calls the random die function
            score = roll_die() #changes the number of the score to be the new random number
        if again is "n": #switches the turn of the individual
            return round_score #tallys up the round score and puts the number into the scoreboard
    if score == 1: #if the player rolls a one it is a pig
            print(player_name, " rolled a Pig!") #tells them its a pig
            return 0 #returns a score of 0 to their round score


#This creates a formatted scoreboard in order to tell the score of the game.
def print_score(p1n,p1s,p2n,p2s):
    print("----------------")
    print("  Score Board")
    print(p1n,':', p1s)
    print(p2n,':', p2s)
    print("----------------")


#This function will create a six sided die and roll it.
def roll_die():
    die = random.randint(1,6) #makes the die six sided
    return die #returns the number that was rolled


#his function tells the game to print the score of each player and who won the game
def game_end_message(p1_name,p1_score,p2_name,p2_score):
    if p1_score >= 100: #if player one wins, prints that player one is the winner
        print("--------------------------")
        print("*** The winner is ", p1_name,"***")
        print("--------------------------")
    if p2_score >= 100: #if player two wins, prints that player two is the winner
        print("--------------------------")
        print("*** The winner is ", p2_name,"***")
        print("--------------------------")
    print_score(p1_name,p1_score,p2_name,p2_score) #prints the final score of the game

#This function will allow both players to create a name for the game
def get_name():
    player_name = input("Enter a player name? ")
    return player_name



main() #Initiates the program
