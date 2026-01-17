import numpy as np

score_player=0
score_computer=0
round=0

for i in range(5,round +1):
    print("round:",i)
while True:

    player = int(input("Enter a number:"))
    computer =np.random.randint(0,5)

    if player == computer:
        print("player is win")
        score_player += 1

    else:
        print("computer is win")
        score_computer +=1

    print("player:",player)
    print("computer:",computer)
    choice = input("if you want to continue a game:yes/no:")
    if choice != "yes":
        print("final score is:")
        print("the final score of player  score:",score_player)
        print("the final score of computer score:",score_computer)
        if score_player > score_computer:
            print("player  is win :")
        elif score_player < score_computer:
            print("computer  is win :")

        else:
            print("match is draw")
            
        break