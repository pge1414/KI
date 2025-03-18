def regelkonform(move: str, figur: str, feld : list) -> bool:
    if figur == 'x1' or figur == 'x2' or figur == 'x3':
        key = [key for key, val in feld.items() if figur in val]
        print(key[0])
        if move == 'forward' and feld[key[0]-1][feld[key[0]].index(figur)] == ' ':
            return True
        if move == 'right' and feld[key[0]-1][feld[key[0]].index(figur)+1] != ' ':
            return True
        if move == 'left' and feld[key[0]-1][feld[key[0]].index(figur-1)] != ' ':
            return True
        else: return False
        
    if figur == 'x1' or figur == 'x2' or figur == 'x3':
        key = [key for key, val in feld.items() if figur in val]
        print(key[0])
        if move == 'forward' and feld[key[0]+1][feld[key[0]].index(figur)] == ' ':
            return True
        if move == 'right' and feld[key[0]+1][feld[key[0]].index(figur)+1] != ' ':
            return True
        if move == 'left' and feld[key[0]+1][feld[key[0]].index(figur-1)] != ' ':
            return True
        else: return False


def game():
    feld = {1 : ['y1', 'y2', 'y3'],2 : [' ', ' ', ' '],3 : ['x1', 'x2', 'x3']}
    game = True
    while game == True:
        print(f" {feld[1][0]} | {feld[1][1]} | {feld[1][2]}")
        print("--------------")
        print(f" {feld[2][0]} | {feld[2][1]} | {feld[2][2]}")
        print("--------------")
        print(f" {feld[3][0]} | {feld[3][1]} | {feld[3][2]}")

        move = input('1 where do you wanna go   ')
        figur = input('1 who will fight   ')
        feld = {1 : ['y1', 'y2', 'y3'],2 : [' ', ' ', ' '],3 : ['x1', 'x2', 'x3']}
        if regelkonform(move, figur, feld):
            key = [key for key, val in feld.items() if figur in val]
            print(key[0])
            if move == 'forward':
                feld[key[0]-1][feld[key[0]].index(figur)] = figur
                feld[key[0]][feld[key[0]].index(figur)] = ' '
            if move == 'right':
                feld[key[0]-1][feld[key[0]].index(figur)+1] = figur
                feld[key[0]][feld[key[0]].index(figur)] = ' '
            if move == 'left':
                feld[key[0]-1][feld[key[0]].index(figur-1)] = figur
                feld[key[0]][feld[key[0]].index(figur)] = ' '
            print(feld)

        
print(regelkonform('right', 'x1', {1 : ['y1', 'y2', 'y3'],2 : [' ', ' ', ' '],3 : ['x1', 'x2', 'x3']}))
game()