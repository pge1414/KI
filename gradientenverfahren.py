import csv, matplotlib.pyplot as plt, numpy as np
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

liste = [0.3, 0.5, 0.8, 1, 1.2, 1.5, 1.8, 2]

def mittelwert(liste : list)-> int :
    return sum(liste)/ len(liste)

def kovarianz(liste_x : list, liste_y : list)-> int :
    liste_produkte = []
    for i in range(len(liste_x)):
        diff_x = liste_x[i] - sum(liste_x) / len(liste_x)
        diff_y = liste_y[i] - sum(liste_y) / len(liste_y)
        liste_produkte.append(diff_x*diff_y)
    return sum(liste_produkte)

def regression(prädiktoren, wert):
    pass