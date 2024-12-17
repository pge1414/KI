import random
def Not(x : int):
    return x - x + 1

def And(x : int, y : int):
    return x * y

def AndII(x : int, y : int):
    return x + y - 1

def Or(x : int, y : int):
    return x + y

def and_lernen():
    x = [[0,0],[1,0],[0,1],[1,1]]
    erg = [0,0]
    x1g = erg[0]
    x2g = erg[1]
    while True:
        for i in x:
            if x1g*i[0] + x2g*i[1]-1 == AndII(i[0], i[1]):
                True
            if x1g*i[0] + x2g*i[1]-1 < AndII(i[0], i[1]):
                x1g += 0.1
                x2g += 0.1
                print("a")
            if x1g*i[0] + x2g*i[1]-1 > AndII(i[0], i[1]):
                x1g -= 0.01
                x2g -= 0.01
            erg[0] = x1g
            erg[1] = x2g
            print(x1g, x2g)
            a = [x1g*x[0][0] + x2g*x[0][1]-1, x1g*x[1][0] + x2g*x[1][1]-1, x1g*x[2][0] + x2g*x[2][1]-1, x1g*x[3][0] + x2g*x[3][1]-1]
            b = [AndII(x[0][0],x[0][1]),AndII(x[1][0],x[1][1]),AndII(x[2][0],x[2][1]),AndII(x[3][0],x[3][1])]
            if a == b:
                False
                return x1g, x2g


print(and_lernen())