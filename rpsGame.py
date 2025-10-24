# Rock, Paper, Scissors
# Displaying Wins, Losses, Ties
# player can enter the following move such as (r)ock, (p)aper (s)cissors or (q)uit
import random, sys, time
import matplotlib.pyplot as plt
import numpy as np

def main():
    wins = losses = ties = 0
    animation_display("""       Rock, Paper, Scissors""", "\n")
    
    while True:
        animation_display(f"""  | Wins: {wins}, Losses: {losses}, Ties: {ties} |""", "\n")
        animation_display("Enter you move (r)ock, (p)aper, (s)cissor or (q)uit: ")
        player_move = get_player_move(wins, losses, ties)
        computer_move = get_computer_move()
        
        animation_display("Both sides are picking their move", "\n")
        
        print_move(player_move, True)
        print_move(computer_move, False)
        
        result = determine_winner(player_move, computer_move, wins, losses, ties)
        wins, losses, ties = result

def get_player_move(wins, losses, ties):
    while True:
        move = input().lower()
        if move == "q":
            animation_display("Thanks for playing!")
            x = np.array(["wins", "losses", "ties"])
            y = np.array([wins, losses, ties])
            plt.bar(x,y, color = ["green", "red", "blue"])
            plt.show()
            sys.exit()
        if move in ("r", "p", "s"):
                return move
        animation_display("Please enter valid keys such as (r)ock, (p)aper, (s)cissor or (q)uit: ")

def get_computer_move():
    return random.choice(["r", "p", "s"])

def print_move(move, is_player = True):
    move_names = {"r": "Rock", "p": "Paper", "s": "Scissor"}
    animation_display(f"{"You" if is_player else "Computer"} choose {move_names[move]}", "\n")
    
    
def determine_winner(player, computer, wins, losses, ties):
    if player == computer:
        animation_display("It's a tie!", "\n")
        ties += 1
    elif (player, computer) in (("r", "s"), ("p", "r"), ("s", "p")):
        animation_display("You win!", "\n")
        wins += 1
    else:
        animation_display("You lose!", "\n")
        losses += 1
    return wins, losses, ties

def animation_display(load, print_end = ""):
    for i in range(len(load)):
        print(load[i], end="", flush=True)
        time.sleep(len(load)/ len(load) * 0.01)
    print(end=f"{print_end}")
        
if __name__ == "__main__":
    main()