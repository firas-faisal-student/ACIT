import random
import time
choices=["rock", "paper", "scissors"]
times_played=0
player_wins=0
computer_wins=0
draws=0
print("""
      
 _______                       __                            _______                                                               ______             __
/       \                     /  |                          /       \                                                             /      \           /  |
$$$$$$$  |  ______    _______ $$ |   __                     $$$$$$$  | ______    ______    ______    ______                      /$$$$$$  |  _______ $$/   _______  _______   ______    ______    _______
$$ |__$$ | /      \  /       |$$ |  /  |       ______       $$ |__$$ |/      \  /      \  /      \  /      \        ______       $$ \__$$/  /       |/  | /       |/       | /      \  /      \  /       |
$$    $$< /$$$$$$  |/$$$$$$$/ $$ |_/$$/       /      |      $$    $$/ $$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |      /      |      $$      \ /$$$$$$$/ $$ |/$$$$$$$//$$$$$$$/ /$$$$$$  |/$$$$$$  |/$$$$$$$/
$$$$$$$  |$$ |  $$ |$$ |      $$   $$<        $$$$$$/       $$$$$$$/  /    $$ |$$ |  $$ |$$    $$ |$$ |  $$/       $$$$$$/        $$$$$$  |$$ |      $$ |$$      \$$      \ $$ |  $$ |$$ |  $$/ $$      \
$$ |  $$ |$$ \__$$ |$$ \_____ $$$$$$  \                     $$ |     /$$$$$$$ |$$ |__$$ |$$$$$$$$/ $$ |                          /  \__$$ |$$ \_____ $$ | $$$$$$  |$$$$$$  |$$ \__$$ |$$ |       $$$$$$  |
$$ |  $$ |$$    $$/ $$       |$$ | $$  |                    $$ |     $$    $$ |$$    $$/ $$       |$$ |                          $$    $$/ $$       |$$ |/     $$//     $$/ $$    $$/ $$ |      /     $$/
$$/   $$/  $$$$$$/   $$$$$$$/ $$/   $$/                     $$/       $$$$$$$/ $$$$$$$/   $$$$$$$/ $$/                            $$$$$$/   $$$$$$$/ $$/ $$$$$$$/ $$$$$$$/   $$$$$$/  $$/       $$$$$$$/
                                                                               $$ |
                                                                               $$ |
                                                                               $$/                                                                                                                       
      
       """)

print("""Welcome to rock paper scissors!
         here are the instructions:
         you pick 'rock' or 'paper' or 'scissors'
         (remember this is case sensitive!!!)
         The computer will then choose an option
         rock beats scissors
         paper beats rock
         scissors beats paper """)
print ("""           !!Good Luck!!""")
print(""" 
      
      
             """)
time.sleep(5)
while True:
  player = str(input("enter your choice: "))
  computer = random.choice(choices)
  print("computer chose:", computer)
  time.sleep(1)
  if (player=="rock" and computer=="scissors") or (player=="scissors" and computer=="paper") or (player=="paper" and computer=="rock"):
   print("player wins")
   player_wins = player_wins+1
   times_played = times_played+1
  elif player==computer:
   print("its a draw")
   draws = draws+1
   times_played = times_played+1
  else:
   print("you lost player!")
   computer_wins = computer_wins+1
   times_played = times_played+1
  time.sleep(1)
  print("you have played:", times_played, "times")
  play_again=str(input("would you like to play again? "))
  if play_again=="no":
    print("thank you for playing")
    print("you have played:", times_played, "times")
    print("you have won:", player_wins, "times")
    print("you have lost:", computer_wins, "times")
    print(draws, "draws")
    break
  else:
    print("Okay")
    time.sleep(1)
