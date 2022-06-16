
# https://edube.org/learn/pe-1/project-tic-tac-toe-4

# 4.7.2.1 PROJEKT: Tic-Tac-Toe

# 4.7.2.1 PROJECT: Tic-Tac-Toe



#from random import randrange as rr

#from random import randrange as rr


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    # Funkcija prihvaća jedan parametar koji sadrži trenutni status ploče
    # i ispisuje ga na konzolu.
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ",  end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    # Funkcija prihvaća trenutni status ploče, pita korisnika o njegovom potezu,
    # provjerava unos i ažurira ploču prema odluci korisnika.
    global change_number
    ok = False # fake assumption - we need it to enter the loop
               # lažna pretpostavka - potrebna nam je za ulazak u petlju
    while not ok:
        move = input("Enter your move: ") 
        ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
        if not ok:
            print("Bad move - repeat your input!") # no, it isn't - do the input again
            continue
        change_number = int(move)
        move = int(move) - 1        # cell's number from 0 to 8
        row = move // 3             # cell's row
        col = move % 3              # cell's column
        sign = board[row][col]      # check the selected square
        ok = sign not in ['O','X'] 
        if not ok:                  # it's occupied - to the input again
            print("Field already occupied - repeat your input!")
            continue
    board[row][col] = 'O'  # set '0' at the selected square


def make_list_of_free_fields(board , board_move):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    # Funkcija pregledava ploču i pravi popis svih slobodnih kvadrata;
    # popis se sastoji od torki, dok je svaki tuple par brojeva redaka i stupca.
    free = []  # the list is empty initially
    for row in range(3): # iterate through rows   # iterirati kroz redove
        for col in range(3): # iterate through columns   # iterirati kroz stupce
            if board[row][col] in ['X']: # it's occupied or is the cell free?
                sign = "X"
                change_numberX = row*3+col+1
                # print("change_numberX" , change_numberX)
                change_board(board_move, change_numberX ,sign)
    for row in range(3): # iterate through rows   # iterirati kroz redove
        for col in range(3): # iterate through columns   # iterirati kroz stupce
            if board[row][col] not in ['O','X']: # is the cell free or it's occupied
                free.append((row,col)) # yes, it is - append new tuple to the list
    return free


def victory_for(board, sgn):     # sign rename in sgn
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # Funkcija analizira status ploče kako bi provjerila je li
    # igrač koji koristi 'O' ili 'X' je pobijedio u igri
    #if human_turn:
        #enter_move(board)
        #victor = victory_for(board,'O')
    if sgn == "X": # are we looking for X?      # line 72, in victory_for
                   # if sgn == "X": # are we looking for X?
                   # NameError: name 'sgn' is not defined
        who = 'me' # yes - it's computer's side
    elif sgn == "O": # ... or for O?
        who = 'you' # yes - it's our side
    else:
        who = None # we should not fall here!
    cross1 = cross2 = True  # for diagonals
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn: # check row rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
            return who
        if board[rc][rc] != sgn: # check 1st diagonal
            cross1 = False
        if board[2 - rc][rc] != sgn: # check 2nd diagonal   # originall is --->>> if board[2 - rc][2 - rc] != sgn
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def think_next_position(board_move):
    for i ,element in enumerate(board_move):
        if element.count("X")==2 and element.count("O")==0:
            for number in element:
                if isinstance(number ,int):
                    return number
    for i ,element in enumerate(board_move):
        if element.count("O")==2:
            for number in element:
                if isinstance(number ,int):
                    return number
    for i ,element in enumerate(board_move):
        if element.count("X")==1 and element.count("O")==0:
            for number in element:
                if isinstance(number ,int):
                    return number
    for i ,element in enumerate(board_move):
        if element.count("X")==0 and element.count("O")==0:
            for number in element:
                if isinstance(number ,int):
                    return number
        else:
            continue
         
    return None
   
        
def draw_move(board , board_move ):
    # The function draws the computer's move and updates the board.
    # Funkcija crta potez računala i ažurira ploču.
    number = 0            
    free = make_list_of_free_fields(board , board_move) # make a list of free fields
    cnt = len(free)
    if cnt > 0: # if the list is not empty, choose a place for 'X' and set it
        if cnt > 1:
            number = think_next_position(board_move)
            if number != None:
                number -=1        # cell's number from 0 to 8
                row = number // 3             # cell's row
                col = number % 3              # cell's column
        else:
            cnt -=1
            row, col = free[0]
        board[row][col] = 'X'
    return cnt
        
    
def change_board(board_move, new_number , sign):
    for element in board_move:
        for i ,pic in enumerate(element):
            if pic == new_number:
                element[i]= sign
    return board_move
    
          
          

# Testen
#if __name__ == "__main__":
#    display_board(3)


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # make an empty board

board_move =  [[1, 5, 9], [3, 5, 7],[1, 2, 3],[1, 4, 7], [2, 5, 8],[3, 6, 9],[4, 5, 6], [7, 8, 9] ]

board[1][1] = 'X' # set first 'X' in the middle
free = make_list_of_free_fields(board , board_move)

print(free)       # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
                  # 'X' # this is set first 'X' in the middle   (1,1)
                  
                  
        
                  
                  
human_turn = True # which turn is it now?  # Tko je sada na redu ?

cnt = 1
    
while len(free):
    display_board(board)
    if human_turn:
        sign = "O"
        enter_move(board)
        change_board(board_move ,change_number , sign)
        victor = victory_for(board,'O')
    else:
        cnt = draw_move(board , board_move )
        victor = victory_for(board,'X')
    if victor != None:
        display_board(board)
        print(f"{victor} have win")
        break
    if victor == None and cnt == 0:
        display_board(board)
        print("Remi")
        exit()
    human_turn = not human_turn
    free = make_list_of_free_fields(board,board_move)
    

    
