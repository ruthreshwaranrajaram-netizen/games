# stone paper sceccor game
def game():
   
   player1_score = 0
   player2_score = 0


   while True: 
    player_1 = input("player 1 your turn:").lower()
    player_2 = input("player 2 your turn:").lower()
    

    if player_1=="stone" and player_2=="sceccor":
        print("player 1 is win")
        player1_score += 1

    elif player_1=="stone" and player_2=="paper":
        print("player 2 in win")
        player2_score += 1

    elif player_1=="paper" and player_2=="sceccor":
        print("player 2 is win")
        player2_score += 1


    elif player_1=="paper" and player_2=="stone":
        print("player 1 in win")
        player1_score += 1


    elif player_1=="sceccor" and player_2=="stone":
        print("player 2 is win")
        player2_score += 1

    elif player_1=="sceccor" and player_2=="paper":
        print("player 1 in win")
        player1_score += 1

    
    elif player_1=="sceccor" and player_2=="sceccor":
        print("match draw")
     
    elif player_1=="paper" and player_2=="paper":
        print("match draw")
        
    elif player_1=="stone" and player_2=="stone":
        print("match draw")

    print("score board:")

    print("player 1 score:",player1_score)
    print("player 2 score:",player2_score)
    
    choice = input("if you want to continue a game:yes/no:")
    if choice != "yes":
        print("final score is:")
        print("the final score of player 1 score:",player1_score)
        print("the final score of player 2 score:",player2_score)
        if player1_score > player2_score:
            print("player 1 is win :")
        elif player1_score < player2_score:
            print("player 2 is win :")

        else:
            print("match is draw")
            
        break
        
        
    
    
        
       
game()
