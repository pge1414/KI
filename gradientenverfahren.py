import csv, matplotlib.pyplot as plt, numpy as np,math
from mpl_toolkits import mplot3d

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

datensatz_nach_art = {}    
for zeile in datensatz:
    if zeile[-1] not in datensatz_nach_art:
        datensatz_nach_art[zeile[-1]] = []
    datensatz_nach_art[zeile[-1]].append(zeile[:-1])  

gewichte = [0.8, 0.9, 0.9999, 1, 1.02, 1.5, 1.1, 1.25]

sx_setosa = [] #standartabweichung
sy_setosa = []
sx_virginica = []
sy_virginica = []
sx_versicolor = []
sy_versicolor = []

x_setosa = [] #mittelwert
y_setosa = []
x_virginica = []
y_virginica = []
x_versicolor = []
y_versicolor = []

s_x_setosa = [] #kovarianz
s_y_setosa = []
s_x_versicolor = []
s_y_versicolor = []
s_x_virginica = []
s_y_virginica =[]

rx_setosa = [] #korelation
ry_setosa = []
rx_versicolor = []
ry_versicolor = []
rx_virginica = []
ry_virginica =[]

for i in datensatz:
    if i[4] == "Iris-setosa":
        sx_setosa.append(i[0])
        sy_setosa.append(i[1])

        x_setosa.append(i[0])
        y_setosa.append(i[1])

        s_x_setosa.append(i[0])
        s_y_setosa.append(i[1])

        rx_setosa.append(i[0])
        ry_setosa.append(i[1])

    if i[4] == "Iris-versicolor":
        sx_versicolor.append(i[0])
        sy_versicolor.append(i[1])

        x_versicolor.append(i[0])
        y_versicolor.append(i[1])

        s_x_versicolor.append(i[0])
        s_y_versicolor.append(i[1])

        rx_versicolor.append(i[0])
        ry_versicolor.append(i[1])

    if i[4] == "Iris-virginica":
        sx_virginica.append(i[0])
        sy_virginica.append(i[1])

        x_virginica.append(i[0])
        y_virginica.append(i[1])

        s_x_virginica.append(i[0])
        s_y_virginica.append(i[1])

        rx_virginica.append(i[0])
        ry_virginica.append(i[1])


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

x_ = mittelwert(x_setosa)
y_ = mittelwert(y_setosa)

sx = standartabweichung(sx_setosa)
sy = standartabweichung(sy_setosa)

sxy = kovarianz(s_x_setosa, s_y_setosa) 

rxy = kovarianz(rx_setosa, ry_setosa)

a_ = a(sy, sx, rxy, x_, y_)
b_ = b(sy, sx, rxy)

# 4.3,3.0 ,,,, 5.2,3.5

# print(regression(4.7 , a_, b_))

setosa_list = []
for i in datensatz:
    if i[4] == "Iris-setosa":
        setosa_list.append(i)

ergebnisse = {}

def differenz(x, y):
    if x <= y:
        return y-x
    else:
        return x-y

for i in gewichte:
    for j in setosa_list:
        ergebnisse.update({differenz(j[1],regression(j[0]*i, a_*i, b_*i)) : i})

key = []
value = []

for i in ergebnisse.keys():
    key.append(i)
for i in ergebnisse.values():
    value.append(i)

print(ergebnisse)

print(min(key))
for i in range(len(key)): 
    if key[i] == min(key): print(value[i]) 
print(len(key))
print(len(value))
print(len(ergebnisse))
print(len(datensatz))

zahl0 = 0
zahl1 = 0
zahl2 = 0
zahl3 = 0
zahl4 = 0
zahl5 = 0
zahl6 = 0
zahl7 = 0

for i in range(len(value)):
    if value[i] == 0.8:
        zahl0+= key[i]





# gibt nur kleinstes ergebnis und dazu passendes gewicht zurück ... muss summe aller ergebnisse pro gewicht vergleichen

# TODO auf 1. Oktober 2024

# Lies nachfolgenden Artikel und verstehe das Konzept einer Fehlerfunktion nochmals genauer:
# https://e2eml.school/how_modeling_works_3
# Überlege dir weitere Szenarien mit quadratischre, absoluter, absoluter mit Sättigung oder quadratischer mit
# indifferenter Region Fehlerfunktionen.
