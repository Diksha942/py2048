import random as rm
import os
import time
import copy
import math

def print_game(game_map): #print the game map
    print("\n")
    for i in range(n):
        for j in range(n):
            if game_map[i][j]==0:
                print(game_map[i][j], end="     ")
            elif math.log(game_map[i][j],10)<1 and math.log(game_map[i][j],10)>0:
                print(game_map[i][j], end="     ")
            elif math.log(game_map[i][j],10)<2 and math.log(game_map[i][j],10)>1:
                print(game_map[i][j], end="    ")
            elif math.log(game_map[i][j],10)<3 and math.log(game_map[i][j],10)>2:
                print(game_map[i][j], end="   ")
            elif math.log(game_map[i][j],10)<4 and math.log(game_map[i][j],10)>3:
                print(game_map[i][j], end="  ")
        print(end="\n")

def adj_same(g): #check if adjacents are same
    for i in range(len(g)-1):
        for j in range(len(g)-1):
            if j==0 and i!=j:
                if g[i][j]==g[i-1][j] or g[i][j]==g[i+1][j] or g[i][j]==g[i][j+1]:
                    return(g,True)
                else:
                    continue
            elif i==(n-1) and j!=0:
                if g[i][j]==g[i][j-1] or g[i][j]==g[i][j+1] or g[i][j]==g[i-1][j]:
                    return(g,True)
                else:
                    continue
            elif j==(n-1) and i!=j:
                if g[i][j]==g[i-1][j] or g[i][j]==g[i+1][j] or g[i][j]==g[i][j-1]:
                    return(g,True)
                else:
                    continue
            elif i==0 and j!=(n-1):
                if g[i][j]==g[i][j-1] or g[i][j]==g[i][j+1] or g[i][j]==g[i+1][j]:
                    return(g,True)
                else:
                    continue
            else:
                if g[i][j]==g[i][j-1] or g[i][j]==g[i][j+1] or g[i][j]==g[i+1][j] or g[i][j]==g[i-1][j]:
                    return(g,True)  
                else:
                    return(g,False)
    return(g,False)

def generate_2(game_map): #generate a random 2
    a=rm.randint(0,n-1)
    b=rm.randint(0,n-1)
    if game_map[a][b]==0:
        game_map[a][b]=2
    else:
        s=0
        for row in game:
            s=s+row.count(0)          
        if (s!=0):
            while(game_map[a][b]!=0):
                a=rm.randint(0,n-1)
                b=rm.randint(0,n-1) 
            game_map[a][b]=2
            return(game_map,True)
        else:
            return(game_map,False)
    return(game_map,True)


def move_up(game_b):  #The Move up command
    for i in range(len(game_b)):
        a=[]
        b=[]
        for j in range(len(game_b)):
            if game_b[j][i]!=0:   
                a.append(game_b[j][i])
        myiter=iter(range(len(a)))    
        for j in myiter:
            if j<len(a)-1 and a[j]==a[j+1]:
                s=a[j+1]+a[j]
                b.append(s)
                next(myiter,None)
            else:
                b.append(a[j])
        for j in range(len(game_b)):
            game_b[j][i]=0
        for j in range(len(b)):
            game_b[j][i]=b[j]
    return(game_b)

def clear():
    os.system('cls')

def move_down(game_b): #The move down command
    for i in range(len(game_b)):
        a=[]
        b=[]
        for j in range(len(game_b)):
            if game_b[j][i]!=0:   
                a.append(game_b[j][i])
        myiter=iter(range(len(a)))    
        for j in myiter:
            if j<len(a)-1 and a[j]==a[j+1]:
                s=a[j+1]+a[j]
                b.append(s)
                next(myiter,None)
            else:
                b.append(a[j])
        for j in range(len(game_b)):
            game_b[j][i]=0
        for j in range(len(b)):
            game_b[len(game_b)-j-1][i]=b[len(b)-j-1]
    return(game_b)

def move_left(game_b): #The move left command
    game=copy.deepcopy(game_b)
    for row in game:
        a=[]
        b=[]
        for j in range(len(row)):
            if row[j]!=0:   
                a.append(row[j])
        myiter=iter(range(len(a)))    
        for j in myiter:
            if j<len(a)-1 and a[j]==a[j+1]:
                s=a[j+1]+a[j]
                b.append(s)
                next(myiter,None)
            else:
                b.append(a[j])
        for j in range(len(game)):
            row[j]=0
        for j in range(len(b)):
            row[j]=b[j]
    return(game)
               
def move_right(game_b): #The move right command
    game=copy.deepcopy(game_b)
    for row in game:
        a=[]
        b=[]
        for j in range(len(row)):
            if row[j]!=0:   
                a.append(row[j])
        myiter=iter(range(len(a)))    
        for j in myiter:
            if j<len(a)-1 and a[j]==a[j+1]:
                s=a[j+1]+a[j]
                b.append(s)
                next(myiter,None)
            else:
                b.append(a[j])
        for j in range(len(game)):
            row[j]=0
        for j in range(len(b)):
            row[len(row)-j-1]=b[len(b)-j-1]
    return(game)
               
        
def keys(game_brd): #inputting the keys
    k=input()
    if k.lower()=="w":
        clear()
        game_brd=move_up(game_brd)
        return(game_brd,True)
    elif k.lower()=="s":
        clear()
        game_brd=move_down(game_brd)
        return(game_brd,True)
    elif k.lower()=="a":
        clear()
        game_brd=move_left(game_brd)
        return(game_brd,True)
    elif k.lower()=="d":
        clear()
        game_brd=move_right(game_brd)
        return(game_brd,True)
      
    else:
        print("Invalid Input. Please press \n w for up\n s for down\n a for left\n d for right")
        return(game_brd,False)
        
global n, game, w
n=int(input("Enter size "))
w=int(input("Enter the no. till which u wish to play "))
game = [[0 for i in range(n)] for i in range(n)]
test_game=[[] for i in range(n)]
play=True
while play:
    #generating a random 2
    game,value=(generate_2(game))
    #if not space to generate a 2, then checking if it hass got any adjacent same no.
    if  not value:
        game,val = adj_same(game)
        if not val:
            print_game(game)
            print("Game Over")
            time.sleep(10)
            play=False
    print_game(game)
    #getting a copy to check for invalid move
    test_game=copy.deepcopy(game)
    game,key=keys(game)
    if not key:
        print_game(game)
        game,_=keys(game)
    if key:
        if game==test_game:
            _,value=(generate_2(game))
            if  not value:
                game,val = adj_same(game)
                if not val:
                    print_game(game)
                    print("Game Over")
                    time.sleep(10)
                    play=False
            else:
                print("Invalid Move")
                print_game(game)
                game,_=keys(game)
    for i in range(n):
        for j in range(n):
            if game[i][j]==w:
                print_game(game)
                print("You win")
                time.sleep(6)
                play=False
                break
            else:
                continue
            