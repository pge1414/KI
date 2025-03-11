def belohnung():
    return 1
def bestrafung():
    return 0

def zug_verifikation_x(zug, figur):
    if zug == "forward" and str(liste3[liste3.index(figur)- 3]).isnumeric():
        return True
    if zug == "diagonal_right" and str(liste3[liste3.index(figur)- 2]).isnumeric():
        return True
    if zug == "diagonal_left" and str(liste3[liste3.index(figur)- 4]).isnumeric():
        return True
    else: return False

def zug_verifikation_y(zug, figur):
    if zug == "forward" and str(liste3[liste3.index(figur)+ 3]).isnumeric():
        return True
    if zug == "diagonal_right" and str(liste3[liste3.index(figur)+ 2]).isnumeric():
        return True
    if zug == "diagonal_left" and str(liste3[liste3.index(figur)+ 4]).isnumeric():
        return True
    else: return False

def game():
    liste3 = ['y1','y2','y3',4,5,6,'x1',"x2","x3"]
    print("Game starting...")
    print("Player 1: x, Player 2: y")
    print("Player 1 start...")
    play = 1
    while play == True:
        print("Player1")
        zug = input("Where do you want to move: ")
        figur = input("Figure you want to move: ")
        if zug == "forward" and str(liste3[liste3.index(figur)- 3]).isnumeric():
            liste3[liste3.index(figur)] = liste3.index(figur)
            liste3[liste3.index(figur)- 3] = figur
        if zug == "diagonal_right" and str(liste3[liste3.index(figur)- 2]).isnumeric():
            liste3[liste3.index(figur)] = liste3.index(figur)
            liste3[liste3.index(figur)-2] = figur
        if zug == "diagonal_left" and str(liste3[liste3.index(figur)- 4]).isnumeric():
            liste3[liste3.index(figur)] = liste3.index(figur)
            liste3[liste3.index(figur)- 4] = figur
        else: 
            play = 0

        print(f" {liste3[0]} | {liste3[1]} | {liste3[2]}")
        print("-----------")
        print(f" {liste3[3]} | {liste3[4]} | {liste3[5]}")
        print("-----------")
        print(f" {liste3[6]} | {liste3[7]} | {liste3[8]}")
                
        print("Player2")
        zug = input("Where do you want to move: ")
        figur = input("Figure you want to move: ")
        if zug == "forward" and str(liste3[liste3.index(figur)+ 3]).isnumeric():
            liste3[liste3.index(figur)] = liste3.index(figur)
            liste3[liste3.index(figur)+ 3] = figur
        if zug == "diagonal_right" and str(liste3[liste3.index(figur)+ 2]).isnumeric():
            liste3[liste3.index(figur)] = liste3.index(figur)
            liste3[liste3.index(figur)+2] = figur
        if zug == "diagonal_left" and str(liste3[liste3.index(figur)+ 4]).isnumeric():
            liste3[liste3.index(figur)] = liste3.index(figur)
            liste3[liste3.index(figur)+ 4] = figur
        else: 
            play = 0

        print(f" {liste3[0]} | {liste3[1]} | {liste3[2]}")
        print("-----------")
        print(f" {liste3[3]} | {liste3[4]} | {liste3[5]}")
        print("-----------")
        print(f" {liste3[6]} | {liste3[7]} | {liste3[8]}")


# liste = [['y1', 'y2', 'y3'],[' ',' ',' '],['x1','x2','x3']]
# liste2 = [1,2,3,4,5,6,7,8,9]
# liste3 = ['y1','y2','y3',4,5,6,'x1',"x2","x3"]
# print(f" {liste[0][0]} | {liste[0][1]} | {liste[0][2]}")
# print("-----------")
# print(f" {liste[1][0]} | {liste[1][1]} | {liste[1][2]}")
# print("-----------")
# print(f" {liste[2][0]} | {liste[2][1]} | {liste[2][2]}")
# print(' ')
# print(' ')
# print(' ')
# print(f" {liste2[0]} | {liste2[1]} | {liste2[2]}")
# print("-----------")
# print(f" {liste2[3]} | {liste2[4]} | {liste2[5]}")
# print("-----------")
# print(f" {liste2[6]} | {liste2[7]} | {liste2[8]}")
# print(" ")
# print(" ")
# print(" ")
# print(f" {liste3[0]} | {liste3[1]} | {liste3[2]}")
# print("-----------")
# print(f" {liste3[3]} | {liste3[4]} | {liste3[5]}")
# print("-----------")
# print(f" {liste3[6]} | {liste3[7]} | {liste3[8]}")

# print(zug_verifikation_x("diagonal_right", "x3"))


game()