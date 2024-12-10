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
    x1g = 0
    x2g = 0
    x = [[0,0],[1,0],[0,1],[1,1]]
    while True:
        for i in x:
            if x1g*i[0] + x2g*i[1] == AndII(i[0], i[1]):
                return x1g, x2g
            if x1g*i[0] + x2g*i[1] < AndII(i[0], i[1]):
                x1g += 0.1
                x2g += 0.1
            if x1g*i[0] + x2g*i[1] > AndII(i[0], i[1]):
                x1g -= 0.01
                x2g -= 0.01

print(and_lernen())