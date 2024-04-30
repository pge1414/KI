
import csv, math, random, tqdm, matplotlib.pyplot as plt, threading

def abstand(zeile1, zeile2, gewichte):
    n = 0
    for i in range(len(zeile1)):
        n += (zeile1[i] * gewichte[i] - zeile2[i] * gewichte[i]) ** 2
    return math.sqrt(n)

def gewichtungen(datensatz, g1, g2, g3, g4): 
    for i in range(len(datensatz)): datensatz[i][1] *= g2; datensatz[i][2] *= g3; datensatz[i][0] *= g1; datensatz[i][3] *= g4
    return datensatz

def gewichte_optimizer(gewichte_0, gewichte_1, gewichte_2,gewichte_3):
    d_opt = 0
    for g_0 in gewichte_0:
        for g_1 in gewichte_1:
            for g_2 in gewichte_2:
                for g_3 in gewichte_3:
                    for i in range(len(datensatz)):
                        datensatz[i][0] *= g_0
                        datensatz[i][1] *= g_1
                        datensatz[i][2] *= g_2
                        datensatz[i][3] *= g_3
                    d = k_optimierung(25)
                    for i in range(len(datensatz)):
                        datensatz[i][0] /= g_0
                        datensatz[i][1] /= g_1
                        datensatz[i][2] /= g_2
                        datensatz[i][3] /= g_3
                    if d[3] > d_opt:
                        d_opt = d[3]
                        g_0_opt = g_0
                        g_1_opt = g_1
                        g_3_opt = g_2
                        g_4_opt = g_3
    return d_opt, g_0_opt, g_1_opt, g_3_opt, g_4_opt

def gewichte_optimizer_multithreaded(gewichte_1, gewichte_2, gewichte_3, gewichte_4):
    gewichte = [(i,j) for i in gewichte_3 for j in gewichte_4]
    trenn_indizes = [i for i in range(0,len(gewichte)+1)]

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])
        gewichtungen(datensatz, 70, 40, 1,1)
# print(datensatz)


datensatz_transponiert = list(zip(*datensatz)) # ???
datensatz_transponiert

maxima = [max(datensatz_transponiert[0]), max(datensatz_transponiert[1]), max(datensatz_transponiert[2]), max(datensatz_transponiert[3])]
for i in range(len(datensatz)):
    for j in range(len(datensatz[i]) - 1):
        datensatz[i][j] /= maxima[j]


def krk(testdatenzeile, trainingsdaten, k, gewichte : list):
    abstände = []
    for zeile in trainingsdaten:
        abstände.append([abstand(zeile[:-1], testdatenzeile, gewichte), zeile[-1]])

    radius_k = list(filter(lambda x: x[0] <= k, abstände))

    if not radius_k:
        return ""

    vorhersage = max([abstand[1] for abstand in radius_k], key=radius_k.count)
    return vorhersage

def validierung(p: float, k: float, h: int, gewichte : list) -> float:
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
    for k in tqdm.tqdm(range(n)):
        ks.append(k / n)
        erg = validierung(0.2, k / n, n // 2 ,gewichte)
        ergebnisse.append(erg)
        if erg > erg_opt:
            k_opt = k / n
            erg_opt = erg
    return ks, ergebnisse, k_opt, erg_opt

# def execute(m):
#     d = k_optimierung(m)
#     plt.plot(d[0], d[1])
#     plt.scatter(d[2], d[3], c="red", s=100, label="Optimum")
#     plt.xlabel("k")
#     plt.ylabel("Genauigkeit")
#     plt.title(f"Optimum bei k={d[2]}, μ={(round(d[3], 4))}")
#     plt.show()

# def rune(m, n):
#     sum_k = 0
#     sum_p = 0
#     all_list = []
#     for i in range(m):
#         d = k_optimierung(n)
#         sum_k += d[2]
#         sum_p += round(d[3], 3)
#     all_list.append(float(sum_k)/float(m)) 
#     all_list.append(float(sum_p)/float(m))
#     return all_list

print(gewichte_optimizer([40, 20, 0.2, 1],[40, 20, 0.2, 1],[40, 20, 0.2, 1],[40, 20, 0.2, 1] ))
# g_2_opt = 0
# g_3_opt = 0
# d_opt = 0
# for g_2 in range(1, 10, 2):
#     for g_3 in range(1, 10, 2):
#         for i in range(len(datensatz)):
#             datensatz[i][0] *= 1
#             datensatz[i][1] *= 1
#             datensatz[i][2] *= g_2
#             datensatz[i][3] *= g_3
#         d = k_optimierung(25)
#         for i in range(len(datensatz)):
#             datensatz[i][0] /= 1
#             datensatz[i][1] /= 1
#             datensatz[i][2] /= g_2
#             datensatz[i][3] /= g_3
#         if d[3] > d_opt:
#             d_opt = d[3]
#             g_2_opt = g_2
#             g_3_opt = g_3
# print(d_opt, g_2_opt, g_3_opt)