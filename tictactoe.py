computer='x'
human='o'

import random
board=['']*10

def display_board():
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[7]} | {board[8]} | {board[9]}')    
    print('-'*10)

def check_win():
    if board[1]==board[2]==board[3] and board[1]!='':
        return True
    if board[4]==board[5]==board[6] and board[4]!='':
        return True
    if board[7]==board[8]==board[9] and board[7]!='':
        return True
    if board[1]==board[4]==board[7] and board[1]!='':
        return True
    if board[2]==board[5]==board[8] and board[2]!='':
        return True
    if board[3]==board[6]==board[9] and board[3]!='':
        return True
    if board[1]==board[5]==board[9] and board[1]!='':
        return True
    if board[3]==board[5]==board[7] and board[3]!='':
        return True
    else:
        return False

def is_available(pos):
    if board[pos]=='':
        return True
    else:
        return False

def check_draw():
    if board.count('')<=1:
        return True
    else:
        return False

def insert(letter,pos):
    if is_available(pos):
        board[pos]=letter
        display_board()
        if check_win():
            if letter=='x':
                print('computer wins')
                exit()
            else:
                print('human wins')
                exit()
        if check_draw():
            print('draw')
            exit()

    else:
        if letter=='o':
            pos=int(input('not free,re enter another position'))
        else:
            pos=random.randint(1,9)
        insert(letter,pos)

def computer_move(letter):
    pos=random.randint(1,9)
    insert(letter,pos)

def human_move(letter):
    pos=int(input('enter the position 1-9: '))
    insert(letter,pos)





while not check_win():
    # display_board()
    computer_move(computer)
    human_move(human)
