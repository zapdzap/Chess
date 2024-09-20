"""
Chess Simulator
Author: Demitri Clark
"""

Board = [["r","h","b","q","k","b","h","r"],
         ["p","p","p","p","p","p","p","p"],
         ["_","_","_","_","_","_","_","_"],
         ["_","_","_","_","_","_","_","_"],
         ["P","P","_","r","_","_","P","P"],
         ["_","_","_","_","_","_","_","_"],
         ["P","P","P","P","P","P","P","P"],
         ["R","H","B","Q","K","B","H","R"]]

#================================================================================#

def move():
    print_board()

    pos2 = int(input("Enter X: ")) # Okay this is a little weird bc it the 2d array is read Y first, then X so keep in mind.
    pos1 = int(input("Enter Y: "))

    new2 = int(input("Enter X: ")) # same deal this is basically the y not the x.
    new1 = int(input("Enter Y: "))

    print(Board[pos1][pos2])
    print("next")

    if Board[pos1][pos2]=="h" or Board[pos1][pos2]=="H":
        move_knight(pos1,pos2,new1,new2)

    elif Board[pos1][pos2]=="p" or Board[pos1][pos2]=="P":
        move_pawn(pos1,pos2,new1,new2)

    elif Board[pos1][pos2]=="k" or Board[pos1][pos2]=="K":
        move_king(pos1,pos2,new1,new2)
    
    elif Board[pos1][pos2]=="r" or Board[pos1][pos2]=="R":
        move_rook(pos1,pos2,new1,new2)


    print_board()
    
def print_board():
    print(Board[0],"0")
    print(Board[1],"1")
    print(Board[2],"2")
    print(Board[3],"3")
    print(Board[4],"4")
    print(Board[5],"5")
    print(Board[6],"6")
    print(Board[7],"7")
    print()
    print('["0", "1", "2", "3", "4", "5", "6", "7"]')


def is_inbound(N1,N2):                                # Checks if new position is on the board.
    if((N1>=0 and N1<=7)and(N2>=0 and N2<=7)):
        return True
    return False


def is_friendly_piece(P1,P2,N1,N2): 
    if(ord(Board[P1][P2])>=97 and ord(Board[P1][P2])<=122):  # Checking if og pos is lower case
        if(ord(Board[N1][N2])>=97 and ord(Board[N1][N2])<=122): # checking if new pos is lowercase
            print("Cant move move to friendly piece")
            return True
        else:
             return False
    else:                                                      # Has to be upper case then.
        if(ord(Board[N1][N2])>=65 and ord(Board[N1][N2])<=90): # checking if new pos is uppercase
            print("Cant move move to friendly piece")
            return True
        else:
             return False
        
#================================================================================#        

def move_pawn(P1,P2,N1,N2):
    if Board[P1][P2]=="p":   # check for lowercase
        if(abs(N2-P2)==1 and N1-P1==1): # If move is diagonal attack
            if(not(Board[N1][N2]=="_")):     # checking for piece on diagonal
                if(not is_friendly_piece(P1,P2, N1,N2)):
                    Board[N1][N2] = Board[P1][P2]
                    Board[P1][P2] = "_"
                else:
                    print("friendly piece")
            print("no piece on diagonal")
        elif(N2==P2 and N1-P1==1):                          # If move is forward move
            if(Board[N1][N2]=="_"):
                Board[N1][N2] = Board[P1][P2]
                Board[P1][P2] = "_"
            else:
                print("cant move pawn to occupied spot")
        else:
            print("Pawns cannot make this move")
   
   
    # else uppercase move
   
   
    else:  
        if(abs(P2-N2)==1 and P1-N1==1): # If move is diagonal attack
            if(not(Board[N1][N2]=="_")):     # checking for piece on diagonal
                if(not is_friendly_piece(P1,P2, N1,N2)):
                    Board[N1][N2] = Board[P1][P2]
                    Board[P1][P2] = "_"
                else:
                    print("friendly piece")
            print("no piece on diagonal")
        elif(N2==P2 and P1-N1==1):                          # If move is forward move
            if(Board[N1][N2]=="_"):
                Board[N1][N2] = Board[P1][P2]
                Board[P1][P2] = "_"
            else:
                print("cant move pawn to occupied spot")
        else:
            print("Pawns cannot make this move")

    move()




#================================================================================#
       
def move_knight(P1,P2,N1,N2):
     # Pos1, Pos2, New1, New2

    if ((abs(N1-P1)==2 and abs(N2-P2)==1) or (abs(N1-P1)==1 and abs(N2-P2)==2)):
        if(is_inbound(N1,N2)):
            if( not (is_friendly_piece(P1,P2,N1,N2))): # As long as the move is not onto a friendly piece the following code will run
                Board[N1][N2] = Board[P1][P2]
                Board[P1][P2] = "_"
                print("Moved knight")
                
        else:
            print("out of bounds")
   
    else:
        print("invalid move")
    move()
    
       
#================================================================================#

def move_king(P1,P2,N1,N2):

    # ADD A CHECK WHICH COMBINES ALL OTHER PIECES MOVING ABILITIES BACKWARDS TO SEE IF KING IS STILL IN 'CHECK'

    if((abs(N1-P1)==1) or (abs(N2-P2)==1) or ((abs(N2-P2)==1)and(abs(N1-P1)==1))):
        if(is_inbound(N1,N2) and not is_friendly_piece(P1,P2,N1,N2)):
            Board[N1][N2] = Board[P1][P2]
            Board[P1][P2] = "_"
        else:
            print("not inbound or trying to move onto friendly piece ")
    else:
        print("invalid king movement")

    move()


#================================================================================#

def move_rook(P1,P2,N1,N2):
    canmove= True

    if(P1==N1): # HORIZONAL!! => This means there is no vertical change
        if(N2>P2)and(N2-P2>1): # MOVING RIGHT!! ------->  moving more than 1 spot!
            for index in range(P2+1,N2):
                print(Board[P1][index])
                if not (Board[P1][index] == "_"): # If the current space inbetween the current pos and new pos isnt a "_" 
                    canmove = False
        
        # MOVING RIGHT WORKS AS INTENTED, MOVING LEFT RIGHT NOW LETS USER SKIP PIECES

        #elif(N2<P2)and(P2-N2>1): # MOVING LEFT!! <-------  moving more than 1 spot!
        #    for index in range(P2+1,N2):
        #        if not (Board[P1][index] == "_"): # If the current space inbetween the current pos and new pos isnt a "_" 
        #            canmove = False
    

    if(canmove):
        Board[N1][N2] = Board[P1][P2]
        Board[P1][P2] = "_"

    (move)



#================================================================================#
     
move()
