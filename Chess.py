"""
Chess Simulator
Author: Demitri Clark
"""

Board = [["r","h","b","q","k","b","h","r"],
         ["p","p","p","p","p","p","p","p"],
         ["_","_","_","_","_","_","_","_"],
         ["_","_","_","_","_","_","_","_"],
         ["_","_","_","_","_","_","_","_"],
         ["_","_","_","_","_","_","_","_"],
         ["P","P","P","P","P","P","P","P"],
         ["R","H","B","Q","K","B","H","R"]]

#================================================================================#

def move():
    pos2 = int(input("Enter X: ")) # Okay this is a little weird bc it the 2d array is read Y first, then X so keep in mind.
    pos1 = int(input("Enter Y: "))

    new2 = int(input("Enter X: ")) # same deal this is basically the y not the x.
    new1 = int(input("Enter Y: "))

    print(Board[pos1][pos2])

    if Board[pos1][pos2]=="k":
        move_knight(pos1,pos2,new1,new2)

    print(Board[0])
    print(Board[1])
    print(Board[2])
    print(Board[3])
    print(Board[4])
    print(Board[5])
    print(Board[6])
    print(Board[7])
    


def is_inbound(P1,P2,N1,N2):
    if((abs(N1-P1)>=0 and abs(N2-P2)>=0)and((abs(N1-P1)<=7 and abs(N2-P2)<=7))):
        return True
    return False

def is_friendly_piece(P1,P2,N1,N2): 
    if(ord(Board[P1][P2]>=97 and ord(Board[P1][P2]<=122))):  # Checking if og pos is lower case
        if(ord(Board[N1][N2]>=97 and ord(Board[N1][N2]<=122))): # checking if new pos is lower
            print("Cant move move to friendly piece")
            return True
        else:
             return False
    else:                                                      # Has to be upper case then.
        if(ord(Board[N1][N2]>=65 and ord(Board[N1][N2]<=90))): # checking if new pos is uppercase
            print("Cant move move to friendly piece")
            return True
        else:
             return False
        
    return False
       


def move_knight(P1,P2,N1,N2):
     # Pos1, Pos2, New1, New2

    if ((abs(N1-P1)==2 and abs(N2-P2)==1) or (abs(N1-P1)==1 and abs(N2-P2)==2)):
         if(is_friendly_piece(P1,P2,N1,N2)): # Checking if piece
            if(is_inbound(P1,P2,N1,N2)):
                #!!! check for inbounds
                Board[N1][N2] = "k"
                Board[P1][P2] = "_"
                print("Moved knight")
            else:
                print("out of bounds")
    else:
        print("invalid move")
    
       
#================================================================================#
     
move()
