import random
import os
# s = snake
# w = water
# g = gun
player_score = 0
com_score = 0
turns = 10
liste = None


rules ="""
__________________________________________
------------------------------------------
*Rules*
------------------------------------------
1)You will only get 10 chances
2)you can use s,w,g for snake, water, gun
  respectively
3)You can only use the character mentioned
  above
4)After when you use all the chances the 
  score of the player and computer will be 
  calculated, then winner will be declared
-------------------------------------------
"""


def find_highscore():
    with open('highscore.txt', 'r+') as fb:
        content = fb.readlines()
        if len(content) >= 1:
            f_highscore = max(content)
            print(f_highscore)
        else:
            None

def main_input():
    while True:
        try:
            print(f"""
______________________________
------------------------------
Snake, Water, Gun
------------------------------
[1]Start the game
[2]Learn how to play the game
[3]HighScore
[4]See rules to play
[x]exit
------------------------------
""")
            inp = input('>>')
            print(
                """
______________________________
------------------------------
""")
            if inp == '1':
                play()
            elif inp == '2':
                print('''
Introduction: Snake Water Gun This just like stone paper scissor.
Both the players should keep the gestures simultaneously. 
The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
                ''')
            elif inp == '3':
                find_highscore()
            elif inp == 'x':
                exit()
            elif inp == '4':
                print(rules)
            else:
                print("invalid input")

        except Exception as e:
            print(e)
""

def computer():
    liste = ['snake', 'water', 'gun']
    comp_cho = str(random.choice(liste))
    return comp_cho

def play():
    global liste, turns, player_score, com_score
    while True:
        computer_out = computer()
        user_input = str(input('Enter your attack: '))
        print('''__________________________\n
--------------------------''')

        if turns == 0:
            break
        elif computer_out == 'snake':
            if user_input == 'w':
                com_score += 1
                turns -= 1
            elif user_input == '':
                player_score += 1
                turns -= 1
            elif user_input == 's':
                None
            else:
                print('invalid input')
        elif computer_out == 'water':
            if user_input == 'g':
                com_score += 1
                turns -= 1
            elif user_input == 's':
                player_score += 1
                turns -= 1
            elif user_input == 'w':
                None
            else:
                print('invalid input')
        elif computer_out == 'gun':
            if user_input == 's':
                com_score += 1
                turns -= 1
            elif user_input == 'w':
                player_score += 1
                turns -= 1
            elif user_input == 'g':
                None
            else:
                print('invalid input')

        print(f"""
___________________________
---------------------------
Your score = {player_score}
Computer's score = {com_score}
Tries left = {turns}
Computer used = {computer_out}
---------------------------
""")
    if com_score > player_score:
        winner = False
        print('___________________________________________')
        print(f'\n\nYour score = {player_score}\nComputer score = {com_score}\n')
        print('-------------------------------------------')
        print("computer won this match")

    elif com_score == player_score:
        winner = None
        print('___________________________________________')
        print(f'\n\nYour score = {player_score}\nComputer score = {com_score}\n')
        print('-------------------------------------------')
        print("This match was a draw")

    else:
        winner = True
        print('___________________________________________')
        print(f'\n\nYour score = {player_score}\nComputer score = {com_score}\n')
        print('-------------------------------------------')
        print("you won this match")


    with open("highscore.txt", 'a+') as f:
        if winner == True:
            f.write(f"player_score = {player_score} >> com_score {com_score} >> score=={player_score - com_score} >> status = won\n")

        elif winner == False:
            f.write(f"player_score = {player_score} >> com_score {com_score} >> score=None >> status = lost \n")
        
        else:
            f.write(
                f"player_score = {player_score} >> com_score {com_score} >> score=None >> status = draw \n")

    while True:
        print("""
_________________________
-------------------------
[1]play again
[2]see high score
[3]exit
--------------------------
        """)
        input_last = input('>>')
        if input_last == '1': 
            player_score = 0
            com_score = 0
            turns = 10
            play()
        elif input_last == '2':
            find_highscore()
        elif input_last == '3':
            print('thanks for playing this game')
            exit()
        else:
            print('wrong input')

main_input()
