import random

while True:
        choices =["rock","paper","scissors"]
        computer = random.choice(choices)
        player = None
        while player not in choices:
                player = input("rock,paper,scissors?:" ).lower()
                if player ==computer:
                        print("player :",player)
                        print("computer :",computer)
                        print("tie")
                elif player == "rock":
                        if computer=="paper":
                                print("player :",player)
                                print("computer :",computer)
                                print("you lose")
                        elif  computer=="scissors":
                                print("player :",player)
                                print("computer :",computer)
                                print("you win")
                elif player == "scissors":
                        if computer=="paper":
                                print("player :",player)
                                print("computer :",computer)
                                print("you win")
                        elif  computer=="rock":
                                print("player :",player)
                                print("computer :",computer)
                                print("you lose!")           
                        elif player == "paper":
                                if computer=="scissors":
                                        print("player :",player)
                                        print("computer :",computer)
                                        print("you lose")
                                elif  computer=="rock":
                                        print("player :",player)
                                        print("computer :",computer)
                                        print("you win")
        play_again = input("enter y/n: ").lower()
        if play_again == 'n':
                break                                                                                   
                                                