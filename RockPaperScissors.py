import random

def play():
    user= input("choose 'r' for Rock, 'p' for paper, 's' for scissors\n")
    computer= random.choice(['r', 's', 'p'])
    if user== computer: 
        return 'its  a tie'
    if player_win(user, computer):
            return 'yay!! you have won!!'
    else: 
            return "Im sorry try again"
def player_win(player, opponent):
    if(player=='r' and opponent== 's') or (player=='s' and opponent== 'p') or (player=='p' and opponent== 'p'):
        return True

print(play())
    
