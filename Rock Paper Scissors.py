import random

def play():
    user = input("あなたの選択は? グーの場合は 'r', パーの場合は 'p', チョキの場合は's'を記載してください\n" )
    computer = random.choice(['r', 'p', 's'])


    if user == computer:
        return '同点'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return '勝ちました!'
    
    return '負けちゃった!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or ( player == 's' and opponent =='p') \
        or (player == 'p' and opponent == 'r'):
        return True 

print(play())
