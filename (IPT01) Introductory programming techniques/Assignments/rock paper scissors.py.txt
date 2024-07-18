import random
import time
choices=("rock", "paper", "scissors")
times_played=0
player_wins=0
computer_wins=0
draws=0
rock=0
paper=0
scissors=0
#imported all relevent libraries and initialised all the needed variables
print("""
____________________________________________________________________________________________________________________________________________________________________________________________________________
|  _______                       __                            _______                                                               ______             __                                                  |
| /       \                     /  |                          /       \                                                             /      \           /  |                                                 |
| $$$$$$$  |  ______    _______ $$ |   __                     $$$$$$$  | ______    ______    ______    ______                      /$$$$$$  |  _______ $$/   _______  _______   ______    ______    _______ |
| $$ |__$$ | /      \  /       |$$ |  /  |       ______       $$ |__$$ |/      \  /      \  /      \  /      \        ______       $$ \__$$/  /       |/  | /       |/       | /      \  /      \  /       ||
| $$    $$< /$$$$$$  |/$$$$$$$/ $$ |_/$$/       /      |      $$    $$/ $$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |      /      |      $$      \ /$$$$$$$/ $$ |/$$$$$$$//$$$$$$$/ /$$$$$$  |/$$$$$$  |/$$$$$$$/ |
| $$$$$$$  |$$ |  $$ |$$ |      $$   $$<        $$$$$$/       $$$$$$$/  /    $$ |$$ |  $$ |$$    $$ |$$ |  $$/       $$$$$$/        $$$$$$  |$$ |      $$ |$$      \$$      \ $$ |  $$ |$$ |  $$/ $$      \ |
| $$ |  $$ |$$ \__$$ |$$ \_____ $$$$$$  \                     $$ |     /$$$$$$$ |$$ |__$$ |$$$$$$$$/ $$ |                          /  \__$$ |$$ \_____ $$ | $$$$$$  |$$$$$$  |$$ \__$$ |$$ |       $$$$$$  ||
| $$ |  $$ |$$    $$/ $$       |$$ | $$  |                    $$ |     $$    $$ |$$    $$/ $$       |$$ |                          $$    $$/ $$       |$$ |/     $$//     $$/ $$    $$/ $$ |      /     $$/ |
| $$/   $$/  $$$$$$/   $$$$$$$/ $$/   $$/                     $$/       $$$$$$$/ $$$$$$$/   $$$$$$$/ $$/                            $$$$$$/   $$$$$$$/ $$/ $$$$$$$/ $$$$$$$/   $$$$$$/  $$/       $$$$$$$/  |
|                                                                               $$ |                                                                                                                        |
|                                                                               $$ |                                                                                                                        |
|                                                                               $$/                                                                                                                         |
|___________________________________________________________________________________________________________________________________________________________________________________________________________|""")
print("""Welcome to rock paper scissors!
         here are the instructions:
         you pick 'rock' or 'paper' or 'scissors'
         (remember this is case sensitive!!!)
         The computer will then choose an option
         rock beats scissors
         paper beats rock
         scissor beats paper
         """)
#all the introduction to the game is here, the big title is made from an online ascii art generator (and the time.sleep bits of code are there to just give the player some time or else it would be all very fast paced)
time.sleep(5)
while True:
    print("")
    player = str(input("enter your choice: "))
    #player enters their choice
    computer = random.choice(choices)
    #computer generates a random choice
    print("you have chosen:", player)
    print("computer chose:", computer)
    #print statements for the player to see what they the computer and they have chosen
    time.sleep(1)
    if (player=="rock" and computer=="scissors") or (player=="scissors" and computer=="paper") or (player=="paper" and computer=="rock"):
     print("player wins")
     #the conditions for if the player has won
     player_wins = player_wins+1
     times_played = times_played+1
     #number of times the player has won and the number of times the player has played will increase here
    elif player==computer:
     print("its a draw")
     draws = draws+1
     times_played = times_played+1
     #the condition of draw where both of the inputs are equal
    elif (computer=="rock" and player=="scissors") or (computer=="scissors" and player=="paper") or (computer=="paper" and player=="rock"):
     print("you lost player!")
     #the conditions of when the player has lost
     computer_wins = computer_wins+1
     times_played = times_played+1
     #the win counter for the computer and times played plus 1 is also here since the previous one will be disregarded as per it not falling into its conditions
    else:
        print("incorrect input")
        #incorrect input to remove any false data input
    if player=="rock":
      rock=rock+1
    if player=="paper":
      paper=paper+1
    if player=="scissors":
      scissors=scissors+1
      #the counter for how many times the player has chosen each weapon
    time.sleep(2)
    print("you have played:", times_played, "times")
    play_again=str(input("would you like to play again? "))
    #checking if the player would like to play again
    if play_again=="no":
      #if the answer is no the code will output all the data
      time.sleep(2)
      print("""
      Thank you for playing""")
      print("you have played:", times_played, "times")
      print("you have won:", player_wins, "times")
      print("you have lost:", computer_wins, "times")
      print(draws, "draws")
      print(" ")
      print("you have used rock", rock, "times")
      print("you have used paper", paper, "times")
      print("you have used scissors", scissors, "times")
      print("Made by Mohamed Firas Faisal")
      time.sleep(10)
      break
      #and the code will finish up to here
    else:
      print("Okay")
      time.sleep(1)
      #the code goes back again