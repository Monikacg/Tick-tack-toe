import sys
from termcolor import colored,cprint
import colorama

colorama.init()
listOfXandO = [['*', '*', '*'],['*', '*', '*'],['*', '*', '*']]
ColorMap = [['*', '*', '*'],['*', '*', '*'],['*', '*', '*']]

def printMap(listXO): #endre på denne! print i farger
    colors = [['white', 'white', 'white'], ['white', 'white', 'white'], ['white', 'white', 'white']]
    n = [0, 1, 2]
    for i in n:
        for j in n:
            if listXO[i][j] == 'x':
                colors[i][j] = 'red'
                #ColorMap[i][j] = listXO[i][j] # Kanskje dette løser problemet?
            elif listXO[i][j] == 'o':
                colors[i][j] = 'cyan'
        ColorMap[i] = [colored(listXO[i][0],colors[i][0]), colored(listXO[i][1],colors[i][1]), colored(listXO[i][2],colors[i][2])]
        print(*ColorMap[i]),

def choosePlayer(player):
    if player != 1:
        player = 1
    else:
        player = 2
    return player

def setInput(list, player, input):
    if player == 1:
        list[int(input[0])-1][int(input[1])-1] = 'x'
    else:
        list[int(input[0])-1][int(input[1])-1] = 'o'

def askForInput(playerNumber):
    print('')
    print('Player ', playerNumber)
    x,y = input('Select row: '), input('Select collumn: ')
    return x,y

def checkInput(x,y,l): #-1: quit, 0: try again, 1: good input
    if x.isalpha() or y.isalpha():
        return -1
    elif not x.isalnum() or not y.isalnum():
        return -1
    elif x.isalnum() and x.isalnum():
        x = int(x)
        y = int(y)
        if x > 3 or y > 3 or x < 1 or y < 1:
            print('Input must be 1, 2 or 3')
            printMap(l)
            return 0
        elif l[x-1][y-1] != '*':
            print('Square taken, try again')
            printMap(l)
            return 0
        else:
            return 1

def checkHorizontally(l):
    for i in l:
        if i[0] != '*':
            if i[0]==i[1] and i[0]==i[2]:
                return True
    return False

def checkVertically(l):
    for i in range(3):
        if l[0][i] != '*':
            if l[0][i] == l[1][i] and l[0][i] == l[2][i]:
                return True
    return False

def checkDiagonally(l):
    if l[1][1] != '*':
        if l[0][0] == l[1][1] and l[0][0] == l[2][2]:
            return True
        elif l[0][2] == l[1][1] and l[0][2] == l[2][0]:
            return True
    return False

def allSpacesTaken(l,p):
    a = 0
    for i in l:
        for j in i:
            if j == '*':
                a = a + 1
    return a

def check(l, p):
    if checkHorizontally(l) or checkVertically(l) or checkDiagonally(l):
        printMap(l)
        print('The winner is Player', p)
        return True
    if allSpacesTaken(l,p) == 0:
        printMap(l)
        print('All spaces taken. Draw.')
        return True
    else:
        return False

def oneTurn(l, p):
    badInput = True
    printMap(l)
    p = choosePlayer(p)
    while badInput:
        x,y = askForInput(p)
        a = checkInput(x,y,l)
        if a == -1:
            print('Player', p, 'ended the game.')
            return False, p
        elif a == 0:
            badInput = True
        elif a == 1:
            b = [x,y]
            setInput(l,p,b)
            return True, p

def main():
    list = listOfXandO
    player = 0
    play = True
    while play:
        play, player = oneTurn(list, player)
        if check(list,player):
            play = False

main()
