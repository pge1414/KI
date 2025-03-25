feld = {1 : ['y1', 'y2', 'y3'],2 : ['  ', '  ', '  '],3 : ['x1', 'x2', 'x3']}


def regelkonform(move: str, figur: str) -> bool:
    if figur == 'x1' or figur == 'x2' or figur == 'x3':
        key = [key for key, val in feld.items() if figur in val]
        if move == 'forward' and feld[key[0]-1][feld[key[0]].index(figur)] == '  ':
            return True
        if move == 'right' and feld[key[0]-1][feld[key[0]].index(figur)+1] != '  ':
            return True
        if move == 'left' and feld[key[0]-1][feld[key[0]].index(figur)-1] != '  ':
            return True
        if IndexError == "list index out of range": return False
        else: return False
        
    if figur == 'y1' or figur == 'y2' or figur == 'y3':
        key = [key for key, val in feld.items() if figur in val]
        if move == 'forward' and feld[key[0]+1][feld[key[0]].index(figur)] == '  ':
            return True
        if move == 'right' and feld[key[0]+1][feld[key[0]].index(figur)+1] != '  ':
            return True
        if move == 'left' and feld[key[0]+1][feld[key[0]].index(figur)-1] != '  ':
            return True
        if IndexError: return False
        else: return False

def bewegen(move, figur):
    if regelkonform(move, figur):
            key = [key for key, val in feld.items() if figur in val]
            if figur == 'x1' or figur == 'x2' or figur == 'x3':            
                if move == 'forward':
                    feld[key[0]-1][feld[key[0]].index(figur)] = figur
                    feld[key[0]][feld[key[0]].index(figur)] = '  '
                if move == 'right':
                    feld[key[0]-1][feld[key[0]].index(figur)+1] = figur
                    feld[key[0]][feld[key[0]].index(figur)] = '  ' 
                if move == 'left':
                    feld[key[0]-1][feld[key[0]].index(figur)-1] = figur
                    feld[key[0]][feld[key[0]].index(figur)] = '  '
            
            if figur == 'y1' or figur == 'y2' or figur == 'y3':
                if move == 'forward':
                    feld[key[0]+1][feld[key[0]].index(figur)] = figur
                    feld[key[0]][feld[key[0]].index(figur)] = '  '
                if move == 'right':
                    feld[key[0]+1][feld[key[0]].index(figur)+1] = figur
                    feld[key[0]][feld[key[0]].index(figur)] = '  ' 
                if move == 'left':
                    feld[key[0]+1][feld[key[0]].index(figur)-1] = figur
                    feld[key[0]][feld[key[0]].index(figur)] = '  '
    
    else: print("Invalid move")

def wincheck(player):
    print(player)
    if player == 1 and regelkonform('forward', 'x1') != True and regelkonform('left', 'x1') != True and regelkonform('right', 'x1') != True and regelkonform('forward', 'x2') != True and regelkonform('left', 'x2') != True and regelkonform('right', 'x2') != True and regelkonform('forward', 'x3') != True and regelkonform('left', 'x3') != True and regelkonform('right', 'x3') != True:
        return True
    if player == 1 and regelkonform('forward', 'y1') != True and regelkonform('left', 'y1') != True and regelkonform('right', 'y1') != True and regelkonform('forward', 'y2') != True and regelkonform('left', 'y2')!= True and regelkonform('right', 'y2') != True and regelkonform('forward', 'y3') != True and regelkonform('left', 'y3') != True and regelkonform('right', 'y3') != True:
        return True

def game():
    while True:

        print(f" {feld[1][0]} | {feld[1][1]} | {feld[1][2]}")
        print("--------------")
        print(f" {feld[2][0]} | {feld[2][1]} | {feld[2][2]}")
        print("--------------")
        print(f" {feld[3][0]} | {feld[3][1]} | {feld[3][2]}")

        player = 1
        if wincheck(player):
            break

        move = input(f'{player} where do you wanna go   ')
        figur = input(f'{player} who will fight   ')
        
        bewegen(move, figur)

        print(f" {feld[1][0]} | {feld[1][1]} | {feld[1][2]}")
        print("--------------")
        print(f" {feld[2][0]} | {feld[2][1]} | {feld[2][2]}")
        print("--------------")
        print(f" {feld[3][0]} | {feld[3][1]} | {feld[3][2]}")

        player = 2

        if wincheck(player):
            break

        move = input(f'{player} where do you wanna go   ')
        figur = input(f'{player} who will fight   ')
        
        bewegen(move, figur)

    print(f"Glückwunsch {player}")

        

game()