# Idee
# Es entscheiden nun nicht mehr die k nächsten Nachbarn, sondern alle, die in einem bestimmten Radius zur Eingabe liegen

import csv, math, random, tqdm, matplotlib.pyplot as plt, threading

# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

def abstand(zeile1, zeile2):
    n = 0
    for i in range(len(zeile1)):
        n += (zeile1[i] - zeile2[i]) ** 2
    return math.sqrt(n)

def gewichtungen(datensatz): 
    for i in range(len(datensatz)): datensatz[i][1] *= 1; datensatz[i][2] *= 3; datensatz[i][0] *= 4
    return datensatz

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])
        #gewichtungen(datensatz)
# print(datensatz)

# Transponiert datensatz, d.h. es werden Zeilen und Spalten vertauscht
# *datensatz entpackt datensatz, d.h. statt einer Liste von Listen stehen dort nun viele verschiedene, voneinander getrennte Listen
# zip fasst alle Einträge dieser Listen (150 Stück, da es 150 Einträge im Datensatz gibt) an der gleichen Stelle zu einem einzelnen Tupel zusammen
# Also werden alle ersten Einträge zu einem Tupel zusammengefasst, alle zweiten, alle dritten, alle vierten und alle fünften.
# Mittels list wird das so entstandene Objekt wieder zu einer gewöhnlichen Liste gemacht
datensatz_transponiert = list(zip(*datensatz)) # ???
datensatz_transponiert
# Wir speichern die Maxima aller Spalten bis auf der mit den Blumennamen ab
maxima = [max(datensatz_transponiert[0]), max(datensatz_transponiert[1]), max(datensatz_transponiert[2]), max(datensatz_transponiert[3])]
# Wir gehen die Indizes aller Zeilen durch
for i in range(len(datensatz)):
    # Wir gehen die Indizes aller Spalten bis auf der letzten durch
    for j in range(len(datensatz[i]) - 1):
        # Wir teilen den Eintrag durch das Maximum seiner Spalte
        datensatz[i][j] /= maxima[j]


def krk(testdatenzeile, trainingsdaten, k):
    abstände = []
    for zeile in trainingsdaten:
        abstände.append([abstand(zeile[:-1], testdatenzeile), zeile[-1]])

    radius_k = list(filter(lambda x: x[0] <= k, abstände))

    if not radius_k:
        return ""

    vorhersage = max([abstand[1] for abstand in radius_k], key=radius_k.count)
    return vorhersage

# Gibt den Prozentsatz der richtig klassifizierten Blumen zurück (für ein festgelegtes k)
def validierung(p: float, k: float, h: int) -> float:
    treffer = 0
    
    for _ in range(h):
        random.shuffle(datensatz)
        testdaten = datensatz[:int(len(datensatz) * p)] # Von Anfang an
        trainingsdaten = datensatz[int(len(datensatz) * p):] # Bis zum Ende

        for testdatenzeile in testdaten:
            vermutung = krk(testdatenzeile[:-1], trainingsdaten, k) # krk bestimmt die Vorhersage, welcher Art testdatenzeile angehört
            if vermutung == testdatenzeile[-1]:
                treffer += 1

    return treffer / (len(testdaten) * h)

def k_optimierung(n: int):
    ks = []
    ergebnisse = []
    k_opt = 0
    erg_opt = 0
    for k in tqdm.tqdm(range(n)):
        ks.append(k / n)
        erg = validierung(0.2, k / n, n // 2)
        ergebnisse.append(erg)
        if erg > erg_opt:
            k_opt = k / n
            erg_opt = erg
    return ks, ergebnisse, k_opt, erg_opt

def execute(m):
    d = k_optimierung(m)
    plt.plot(d[0], d[1])
    plt.scatter(d[2], d[3], c="red", s=100, label="Optimum")
    plt.xlabel("k")
    plt.ylabel("Genauigkeit")
    plt.title(f"Optimum bei k={d[2]}, μ={(round(d[3], 4))}")
    plt.show()

def rune(m, n):
    sum_k = 0
    sum_p = 0
    all_list = []
    for i in range(m):
        d = k_optimierung(n)
        sum_k += d[2]
        sum_p += round(d[3], 3)
    all_list.append(float(sum_k)/float(m)) 
    all_list.append(float(sum_p)/float(m))
    return all_list

print(rune(20, 20))