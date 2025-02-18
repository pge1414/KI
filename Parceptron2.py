import random,time,math, numpy as np
def Not(x : int):
    return x - x + 1

def And(x : int, y : int):
    return x * y

def AndII(x : int, y : int):
    return x + y - 1

def Or(x : int, y : int):
    return x + y

# def and_lernen():
#     x = [[0,0],[1,0],[0,1],[1,1]]
#     erg = [0,0]
#     x1g = erg[0]
#     x2g = erg[1]
#     while True:
#         for i in x:
#             if x1g*i[0] + x2g*i[1]-1 == AndII(i[0], i[1]):
#                 True
#             if x1g*i[0] + x2g*i[1]-1 < AndII(i[0], i[1]):
#                 x1g += 0.1
#                 x2g += 0.1
#                 print("a")
#             if x1g*i[0] + x2g*i[1]-1 > AndII(i[0], i[1]):
#                 x1g -= 0.01
#                 x2g -= 0.01
#             erg[0] = x1g
#             erg[1] = x2g
#             print(x1g, x2g)
#             a = [x1g*x[0][0] + x2g*x[0][1]-1, x1g*x[1][0] + x2g*x[1][1]-1, x1g*x[2][0] + x2g*x[2][1]-1, x1g*x[3][0] + x2g*x[3][1]-1]
#             b = [AndII(x[0][0],x[0][1]),AndII(x[1][0],x[1][1]),AndII(x[2][0],x[2][1]),AndII(x[3][0],x[3][1])]
#             if a == b:
#                 False
#                 return x1g, x2g


# print(and_lernen())

def classification(v,w,x,y):
    if v*x + w*y-1 <= 0:
        return 0
    else:
        return 1

def perceptronlearning(daten : list, w,v):
    lernrate = 0.5
    while True:
        for i in range(len(daten[1])-1):
            time.sleep(5)
            x = daten[i][0]
            y = daten[i][1]
            print(x,y)
            if classification(v,w,x,y) != AndII(x,y):
                print("x")
                print(i, w,v, "x: ", x, "y: ", y, "/-----", classification(v,w,x,y), "-----", AndII(x,y))
                w += lernrate    
                v += lernrate
                
            else:
                print(i, w,v,x,y,classification(v,w,x,y), AndII(x,y))
                if i == 2:
                    print("y")
                    False
                    return w, v
#print (perceptronlearning([[1,1,1],[0,1,0]],0,0))

# nginx & https & dns server





def mittelwert(liste : list)-> int:
    return sum(liste)/ len(liste)

def kovarianz(liste_x : list, liste_y : list)-> int:
    liste_produkte = []
    for i in range(len(liste_x)):
        diff_x = liste_x[i] - sum(liste_x) / len(liste_x)
        diff_y = liste_y[i] - sum(liste_y) / len(liste_y)
        liste_produkte.append(diff_x*diff_y)
    return sum(liste_produkte)




def korelation(liste_x : list, liste_y : list):
    return int(np.correlate(liste_x, liste_y))




def standartabweichung(liste : list):
    o = []
    for i in range(len(liste)):
        o.append(math.sqrt((liste[i]-mittelwert(liste))**2 * 1/3)) # 1/3 weil alle blumen gleich of vorkommen
    return sum(o)




def b(sy, sx, rxy):
    return (sy/sx) *rxy





def a(sy, sx, rxy, x, y):
    return -(sy/sx) * rxy * x + y





def regression(prädiktor, a, b):
    return b*prädiktor + a





def adalinelearning(x: list, w : list, o : list):
    ergebnis = []
    while True:
        for i in range(len(x)):
            #time.sleep(1)
            #print(w)
            if w[i] * x[i] != o[i]:
                eta=1/(x[i]**2)
                w[i] += eta*(o[i]-(w[i] * x[i]))*x[i]
            else:
                continue
            ergebnis.clear()
        for i in range(len(x)):
            ergebnis.append(w[i] * x[i])
        if ergebnis == o:
            return w
        else:
            True

def adaline(x : list, y : list):
    ergebniss = []
    for i in range(len(x)):
        print(adalinelearning(x[i], [0,0,0,0,0], y[i]))
        ergebniss.append(adalinelearning(x[i], [0,0,0,0,0], y[i]))
        return ergebniss


x = [[0,1,0,0,1],[1,1,1,0,1],[1,1,1,1,1],[0,0,0,0,1],[1,1,0,0,1],[0,0,0,0,0],[0,1,1,0,1],[0,1,0,0,0]]
y = [[0,1,0,0,1],[1,1,1,0,1],[1,1,1,1,1],[0,0,0,0,1],[1,1,0,0,1],[0,0,0,0,0],[0,1,1,0,1],[0,1,0,0,0]]

print(x[1])

datensatz = adaline(x,y)

print(datensatz)
x_datensatz_m = []
x_datensatz_s = []
datensatz_kov = []
datensatz_kor = []

g_datensatz_m = []
g_datensatz_s = []



for i in range(len(datensatz)):
    x_datensatz_m.append(mittelwert(x[i]))
    x_datensatz_s.append(standartabweichung(x[i]))
    datensatz_kov.append(kovarianz(x[i],datensatz[i]))
    datensatz_kor.append(korelation(x[i],datensatz[i]))
    g_datensatz_m.append(mittelwert(datensatz[i]))
    g_datensatz_s.append(standartabweichung(datensatz[i]))

print(x_datensatz_m, x_datensatz_s, datensatz_kov, datensatz_kor, g_datensatz_m, g_datensatz_s)

x_ = mittelwert(x_datensatz_m)
y_ = mittelwert(g_datensatz_m)

sx = standartabweichung(x_datensatz_s)
sy = standartabweichung(g_datensatz_s)

f = []
for i in range(len(datensatz_kor)):
    f.append(1)

sxy = kovarianz(datensatz_kov, f) 

rxy = korelation(datensatz_kor, f)

a_ = a(sy, sx, rxy, x_, y_)
b_ = b(sy, sx, rxy)

print(regression(1, a_, b_))



