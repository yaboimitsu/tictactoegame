from turtle import *
from freegames import line
import random

def grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    color('blue')
    width(5)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

def drawo(x, y):
    color('red')
    width(5)
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)

def floor(value):
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0, 'board': [[''] * 3 for _ in range(3)], 'game_over': False}
players = [drawx, drawo]

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '':
            return row[0]
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != '':
            return check[0]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def check_draw(board):
    for row in board:
        if '' in row:
            return False
    return True

def computer_move():
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if state['board'][row][col] == '':
            return row, col

def tap(x, y):
    if state['game_over']:
        return
    x = floor(x)
    y = floor(y)
    row = int((y + 200) // 133)
    col = int((x + 200) // 133)
    if state['board'][row][col] != '':
        return
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['board'][row][col] = 'X' if player == 0 else 'O'
    winner = check_winner(state['board'])
    if winner:
        print(f"The winner is the {winner} player!")
        state['game_over'] = True
        return
    if check_draw(state['board']):
        print("Draw!")
        state['game_over'] = True
        return
    state['player'] = not player
    if player == 0: 
        row, col = computer_move()
        x = col * 133 - 200
        y = row * 133 - 200
        draw = players[state['player']]
        draw(x, y)
        update()
        state['board'][row][col] = 'X' if state['player'] == 0 else 'O'
        winner = check_winner(state['board'])
        if winner:
            print(f"The winner is the {winner} player!")
            state['game_over'] = True
            return
        if check_draw(state['board']):
            print("Draw!")
            state['game_over'] = True
            return
        state['player'] = not state['player']

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
