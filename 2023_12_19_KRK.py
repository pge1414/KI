# Idee
# Es entscheiden nun nicht mehr die k nächsten Nachbarn, sondern alle, die in einem bestimmten Radius zur Eingabe liegen

import csv, math

# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

def abstand(zeile1, zeile2):
    n = 0
    for i in range(len(zeile1)):
        n += (zeile1[i] - zeile2[i]) ** 2
    return math.sqrt(n)

datensatz = []
with open("iris_datensatz.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])
# print(datensatz)

# Transponiert datensatz, d.h. es werden Zeilen und Spalten vertauscht
# *datensatz entpackt datensatz, d.h. statt einer Liste von Listen stehen dort nun viele verschiedene, voneinander getrennte Listen
# zip fasst alle Einträge dieser Listen (150 Stück, da es 150 Einträge im Datensatz gibt) an der gleichen Stelle zu einem einzelnen Tupel zusammen
# Also werden alle ersten Einträge zu einem Tupel zusammengefasst, alle zweiten, alle dritten, alle vierten und alle fünften.
# Mittels list wird das so entstandene Objekt wieder zu einer gewöhnlichen Liste gemacht
datensatz_transponiert = list(zip(*datensatz)) # ???
# Wir speichern die Maxima aller Spalten bis auf der mit den Blumennamen ab
maxima = [max(datensatz_transponiert[0]), max(datensatz_transponiert[1]), max(datensatz_transponiert[2]), max(datensatz_transponiert[3])]
# Wir gehen die Indizes aller Zeilen durch
for i in range(len(datensatz)):
    # Wir gehen die Indizes aller Spalten bis auf der letzten durch
    for j in range(len(datensatz[i]) - 1):
        # Wir teilen den Eintrag durch das Maximum seiner Spalte
        datensatz[i][j] /= maxima[j]

test_datensatz = datensatz[:1]

trainings_datensatz = datensatz[1:]

k = 0.7

abstände = []
for zeile in trainings_datensatz:
    abstände.append([abstand(zeile[:-1], test_datensatz[0][:-1]), zeile[-1]])
# print(abstände)

radius_k = list(filter(lambda x: x[0] <= k, abstände))

vorhersage = max([abstand[1] for abstand in radius_k], key=radius_k.count)

print(vorhersage)

# TODO
# Schreibe eine Funktion normalisieren(datensatz)
# Die Funktion soll alle Werte in datensatz auf den Wertebereich 0 bis 1 normalisieren und dabei die Verhältnisse der Werte untereinander nicht verändern
# Annahme: datensatz ist eine zweidimensionale Liste ausschließlich numerischer Werte

# TODO
# Validierung