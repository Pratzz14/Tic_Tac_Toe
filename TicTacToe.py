import itertools 

'''GOBAL VARIALBLES'''
#board
board=["1","2","3","4","5","6","7","8","9"]
game_on=True
winnner=None
player=itertools.cycle(["X","O"])
next_player="O"
count=0

'''**************'''

#display
def display_board():
    global next_player
    print(board[0]+" |",board[1]+" |",board[2])
    print(board[3]+" |",board[4]+" |",board[5])
    print(board[6]+" |",board[7]+" |",board[8])

    print("Player:",next_player)


#vertical
def vertical():
    global game_on
    col_1=board[0]==board[3]==board[6]
    col_2=board[1]==board[4]==board[7]
    col_3=board[2]==board[5]==board[8]
    if col_1 or col_2 or col_3:
        game_on=False
        winnner= not None
    if col_1:
        print(f"winnner: {board[0]}")
    if col_2:
        print(f"winnner: {board[1]}")
    if col_3:
        print(f"winnner: {board[2]}")

#horizontal
def horizontal():
    global game_on
    row_1=board[0]==board[1]==board[2]
    row_2=board[3]==board[4]==board[5]
    row_3=board[6]==board[7]==board[8]
    if row_1 or row_2 or row_3:
        game_on=False
        winnner= not None

    if row_1:
        print(f"winnner: {board[0]}")
    if row_2:
        print(f"winnner: {board[3]}")
    if row_3:
        print(f"winnner: {board[6]}")
    

#diagonals / \
def diagonal():
    global game_on
    dia_1=board[0]==board[4]==board[8]
    dia_2=board[2]==board[4]==board[6]
    
    if dia_1 or dia_2 :
        game_on=False
        winnner= not None

    if dia_1:
        print(f"winnner: {board[0]}")
    if dia_2:
        print(f"winnner: {board[2]}")


#check win
def check_win():
    global winner
    vertical()
    horizontal()
    diagonal()

    winnner=None

#check tie
def check_tie():
    global game_on
    global count
    if count==9:
        print("Tie")
        game_on=False
        winnner=not None
    

#to check if game is over
def check():
    check_win()
    check_tie()


#To get position and to flip the player
def handle_game():
    global next_player
    global count
    
    
    position=input("Enter a position between 1-9:" )
    position=int(position)-1
    if board[position] != "X" and board[position]!="O":
        board[position]=next_player
        next_player=next(player)
        count=count+1
    else:
        print("position already occupied !")
    
    display_board()

#play game
def play_game():
    global next_player
    display_board()
    while game_on:
        
        handle_game()
        check()



play_game()






