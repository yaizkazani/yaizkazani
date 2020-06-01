# Rock Paper Scissors Game
#
#     Create a rock-paper-scissors game.
#     Ask the player to pick rock, paper or scissors.
#     Have the computer chose its move.
#     Compare the choices and decide who wins.
#     Print the results.
#     Subgoals:
#         Give the player the option to play again.
#         Keep a record of the score (e.g. Player: 3 / Computer: 6).
import random, time


def game_rps(player_move):
    ai_move_list = ["rock", "paper", "scissors"]  # create all AI move possibilities
    ai_move = ai_move_list[random.randint(0, 2)]  # getting current AI move
    if str(player_move).isalpha():  # check if move is made of letters
        player_move = str(player_move).lower()  # process possible commands
        if player_move == "rules":
            return "Rules"
        elif player_move == "reset":
            return "Reset"
        elif player_move == "exit":
            return "Exit"
        if "rock" in player_move or "paper" in player_move or "scissors" in player_move:  # check if move value is correct
            if (player_move == "rock" and ai_move == "paper") or (player_move == "paper" and ai_move == "scissors") or (
                    player_move == "scissors" and ai_move == "rock"):
                return "ai_win", ai_move  # check if ai has won
            elif (player_move == "rock" and ai_move == "scissors") or (
                    player_move == "paper" and ai_move == "rock") or (player_move == "scissors" and ai_move == "paper"):
                return "player_win", ai_move  # check if player has won
            else:
                return "Draw", ai_move
        else:
            return str("Incorrect input value!"), ai_move
    else:
        return str("Incorrect input type!"), ai_move


player_wins = 0
ai_wins = 0
counter = 0
while True:
    if counter == 0:  # we show rules only for the first time
        print("Welcome to the Rock-Paper-Scissors game!", "\n \n",
              "The rules are: Rock beats Scissors, but lose to Paper",
              "\n", "Scissors beats Paper but loses to Rock", "\n", "Paper beats Rock, but loses to Scissors \n",
              "Rules to read Rules, Exit to exit, Reset to reset scores",
              sep="")
    time.sleep(1)
    print("Player score: ", player_wins, "\n", "AI score: ", ai_wins, "\n", sep="")
    game_result = game_rps(input("Please enter your move!"))  # we get game result and process it↓
    if game_result[0] == "player_win":
        print("AI move is:  ", game_result[1], "\nPlayer wins! \n", sep="")
        player_wins += 1
        time.sleep(2)
    elif game_result[0] == "ai_win":
        print("AI move is:  ", game_result[1], "\nAI wins! \n", sep="")
        ai_wins += 1
        time.sleep(2)
    elif game_result[0] == "Incorrect input value!":
        print("Incorrect value! please enter Paper or Rock or Scissors ! (Rules,Exit,Reset) \n")
    elif game_result[0] == "Incorrect input type!":
        print("Incorrect input type, please enter Paper or Rock or Scissors ! (Rules,Exit,Reset) \n")
    elif game_result == "Rules":
        print("Welcome to the Rock-Paper-Scissors game!", "\n \n",
              "The rules are: Rock beats Scissors, but lose to Paper",
              "\n", "Scissors beats Paper but loses to Rock", "\n", "Paper beats Rock, but loses to Scissors \n",
              "Rules to read Rules, Exit to exit, Reset to reset scores",
              sep="")
    elif game_result == "Reset":
        player_wins = 0
        ai_wins = 0
        print("Scores were reset!")
    elif game_result == "Exit":
        break
    elif game_result[0] == "Draw":
        print("AI move is: ", game_result[1].capitalize())
        time.sleep(1)
        print("It's a draw ! \n")
        time.sleep(2)
    counter += 1
