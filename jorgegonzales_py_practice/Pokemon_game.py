# Turn Based Pokemon Style Game
#
#     Write a simple game that allows the user and the computer to take turns selecting moves to use against each other.
#     Both the computer and the player should start out at the same amount of health (such as 100), and should be able to choose between the three moves:
#         The first move should do moderate damage and has a small range (such as 18-25).
#         The second move should have a large range of damage and can deal high or low damage (such as 10-35).
#         The third move should heal whoever casts it a moderate amount, similar to the first move.
#     After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have.
#     Once the user or the computer's health reaches 0, the game should end.
#     Subgoals:
#         When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
#         When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
#         Give each move a name.
import random


class Pokemon:
    """The base class for the game - both player and AI has manipulate Pokemon class objects"""
    def __init__(self, name):  # constructor. Each Pokemon class object has a name and hp
        self.name = name
        self.hp = 100

    def weak_strike(self, pokemon):  # the weak strike method to deal low damage to pokemon passed as argument
        tmp = random.randint(18, 25)  # we find damage amount
        print(self.name, "decided to attack with weak strike for", tmp)
        pokemon.hp -= tmp  # target pokemon (that was passed to method as argument) = enemy pokemon has its health modified for damage amount
        if pokemon.hp < 0:  # we check to not let hp go negative
            pokemon.hp = 0

    def strong_strike(self, pokemon):  # strong strike, same as weak, just more risky
        tmp = random.randint(10, 35)
        print(self.name, "decided to attack with strong strike for", tmp)
        pokemon.hp -= tmp
        if pokemon.hp < 0:
            pokemon.hp = 0

    def heal(self):  # we do not pass any args to that method since we modify only our object's parameter (health)
        tmp = random.randint(18, 25)
        self.hp += tmp
        print(self.name, "Decided to heal and healed for", tmp, "hp")
        if self.hp > 100:
            tmp -= self.hp - 100
            self.hp = 100


def ai_move(ai_pokemon):  # function to define AI movement
    move_list = [[1, 2, 3] for i in range(10)]  # common movelist. Used when AI hp > 35%. We use generator to create it
    move_list_low_hp = [[1, 3, 3] for i in range(10)]  # low HP AI movelist
    if ai_pokemon.hp > 35:
        return move_list[random.randint(0, 9)][random.randint(0, 2)]  # we get AI move
    elif 35 > ai_pokemon.hp > 0:
        return move_list_low_hp[random.randint(0, 9)][random.randint(0, 2)]  # we get AI move


Player_Pokemon = Pokemon("Player")  # we create Pokemon class object for player
AI_Pokemon = Pokemon("AI")  # we create Pokemon class object for AI

while 1:
    if Player_Pokemon.hp <= 0:  # checking win condition
        print("AI has won the battle !")
        break
    elif AI_Pokemon.hp <= 0:  # checking win condition
        print("Player has won the battle !")
        break
    ai_action = ai_move(AI_Pokemon)  # we get AI move into variable
    while 1:  # we check if player in entering valid move(type and value)
        player_action = input("""Please enter your action!
        1 - Weak strike
        2 - Strong strike
        3 - Heal\n""")
        try:
            player_action = int(player_action)
        except:
            print("You have entered wrong value type! Please try again")
            continue
        if player_action in [1, 2, 3]:
            break
        else:
            print("You have entered wrong move! Please try again")
    if player_action == 1:  # we process player move
        Player_Pokemon.weak_strike(AI_Pokemon)
    elif player_action == 2:
        Player_Pokemon.strong_strike(AI_Pokemon)
    else:
        Player_Pokemon.heal()

    if ai_action == 1:  # we process AI move
        AI_Pokemon.weak_strike(Player_Pokemon)
    elif ai_action == 2:
        AI_Pokemon.strong_strike(Player_Pokemon)
    else:
        AI_Pokemon.heal()

    if Player_Pokemon.hp == 0 and AI_Pokemon.hp == 0:  # just in case we check if both are dead
        print("TIE!")
        break
    print("\nPlayer has ", Player_Pokemon.hp, "HP  AI has", AI_Pokemon.hp, " HP\n")
