import csv, math, random, matplotlib.pyplot as plt, multiprocessing, numpy as np
from matplotlib import cm


def abstand(zeile1, zeile2, gewichte):
    n = 0
    for i in range(len(zeile1)):
        n += (zeile1[i] * gewichte[i] - zeile2[i] * gewichte[i]) ** 2
    return math.sqrt(n)

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])


datensatz_transponiert = list(zip(*datensatz))
maxima = [max(datensatz_transponiert[0]), max(datensatz_transponiert[1]), max(datensatz_transponiert[2]), max(datensatz_transponiert[3])]
minima = [min(datensatz_transponiert[0]), min(datensatz_transponiert[1]), min(datensatz_transponiert[2]), min(datensatz_transponiert[3])]
for i in range(len(datensatz)):
    for j in range(len(datensatz[i]) - 1):
        datensatz[i][j] /= maxima[j]

def krk(testdatenzeile, trainingsdaten, k, gewichte):
    abstände = []
    for zeile in trainingsdaten:
        abstände.append([abstand(zeile[:-1], testdatenzeile, gewichte), zeile[-1]])

    radius_k = list(filter(lambda x: x[0] <= k, abstände))

    if not radius_k:
        return ""

    vorhersage = max([abstand[1] for abstand in radius_k], key=radius_k.count)
    return vorhersage

def validierung(p: float, k: float, h: int, gewichte: list) -> float:
    treffer = 0
    
    for _ in range(h):
        random.shuffle(datensatz)
        testdaten = datensatz[:int(len(datensatz) * p)]
        trainingsdaten = datensatz[int(len(datensatz) * p):]

        for testdatenzeile in testdaten:
            vermutung = krk(testdatenzeile[:-1], trainingsdaten, k, gewichte)
            if vermutung == testdatenzeile[-1]:
                treffer += 1

    return treffer / (len(testdaten) * h)

def k_optimierung(n: int, gewichte: list):
    ks = []
    ergebnisse = []
    k_opt = 0
    erg_opt = 0
    for k in range(n):
        ks.append(k / n)
        erg = validierung(0.2, k / n, n // 2, gewichte)
        ergebnisse.append(erg)
        if erg > erg_opt:
            k_opt = k / n
            erg_opt = erg
    return ks, ergebnisse, k_opt, erg_opt

def gewichte_optimierung(gewichte_3_4):
    d_s = []
    d_opt = 0
    g_3_opt = 0
    g_4_opt = 0
    for g_3, g_4 in gewichte_3_4:
            d = k_optimierung(25, [1, 1, g_3, g_4])
            d_s.append([g_3, g_4, d[3]])
            if d[3] > d_opt:
                d_opt = d[3]
                g_3_opt = g_3
                g_4_opt = g_4

    return d_opt, g_3_opt, g_4_opt, d_s

def gewichte_optimierung_multithreaded(gewichte_3, gewichte_4, k):

    gewichte = [(i, j) for i in gewichte_3 for j in gewichte_4]
    trenn_indizes = [i for i in range(0, len(gewichte) + 1, len(gewichte) // k)]
    trenn_indizes[-1] = len(gewichte)
    gewichte_liste = [gewichte[trenn_indizes[i]:trenn_indizes[i + 1]] for i in range(k)]

    with multiprocessing.Pool(k) as pool:
        ergebnisse = pool.map(gewichte_optimierung, gewichte_liste)

    d_s = []
    d_opt = 0
    g_3_opt = 0
    g_4_opt = 0
    for ergebnis in ergebnisse:
        d_s += ergebnis[3]
        if ergebnis[0] > d_opt:
            d_opt = ergebnis[0]
            g_3_opt = ergebnis[1]
            g_4_opt = ergebnis[2]
    
    return d_opt, g_3_opt, g_4_opt, d_s

if __name__ == '__main__':
    anzahl_t = 8
    d = gewichte_optimierung_multithreaded([i / 4 for i in range(1, 20)], [i / 4 for i in range(1, 20)], anzahl_t)
    print(f"Beste Genauigkeit: {d[0]} bei g_3={d[1]} und g_4={d[2]}")
    fig = plt.figure("K-Radius-Klassifikator")
    ax = fig.add_subplot(projection="3d")
    ax.plot_trisurf(np.array(list(zip(*d[3]))[0]), np.array(list(zip(*d[3]))[1]), np.array(list(zip(*d[3]))[2]), cmap=cm.coolwarm)
    ax.set_xlabel("g_3")
    ax.set_ylabel("g_4")
    ax.set_zlabel("Anteil korrekt klassifiziert")
    ax.scatter(d[1], d[2], d[0], color="green", s=100)
    ax.text(d[1], d[2], d[0]+0.03, s=f"({d[1]}, {d[2]}, {round(d[0],3)})")
    plt.show()