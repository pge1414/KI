import csv, math, random, tqdm, matplotlib.pyplot as plt, threading

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])



datensatz_transponiert = list(zip(*datensatz)) # ???
datensatz_transponiert

maxima = [max(datensatz_transponiert[0]), max(datensatz_transponiert[1]), max(datensatz_transponiert[2]), max(datensatz_transponiert[3])]
for i in range(len(datensatz)):
    for j in range(len(datensatz[i]) - 1):
        datensatz[i][j] /= maxima[j]

zeilen_nach_art = {}

for i in range(len(datensatz)):
    if not datensatz[i][:-1] in zeilen_nach_art:
        zeilen_nach_art[datensatz[i][:-1]].append(datensatz[i])

#erstelle ein dict, dass für jede vorkommende art alle zugehörigen datenzeilen abspeichert
#erstelle im anschluss ein dict, das für jede kombination aus art und eingabeparameter (3*4 = 12 stück) die den datensatz entsprechende gauss verteilung enthält