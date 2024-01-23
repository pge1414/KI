import csv, math, random, tqdm

# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

def abstand(zeile1, zeile2):
    n = 0
    for i in range(len(zeile1)):
        n += (zeile1[i] - zeile2[i]) ** 2
    return math.sqrt(n)

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])
#print(datensatz)
        
# def krk(zeile : list, gesamt : list):
#     primelist = []
#     k = 0.5
#     if abstand(zeile, gesamt) <= k:
#         primelist.append(gesamt[4])
#     return max(primelist.count("Iris-versicolor"), primelist.count("Iris-virginica"), primelist.count("Iris-setosa"))

def krk(testdatenzeile,trainingsdaten, k):
    abstände = []


datensatz_transponiert = list(zip(*datensatz)) # ???
maxima = [max(datensatz_transponiert[0]), max(datensatz_transponiert[1]), max(datensatz_transponiert[2]), max(datensatz_transponiert[3])]
for i in range(len(datensatz)):
    for j in range(len(datensatz[i]) - 1):
        datensatz[i][j] /= maxima[j]

def validierung(p: float) -> float:
    random.shuffle(datensatz)
    testdaten = datensatz[:int(len(datensatz)*p)]
    trainingsdaten = datensatz[int(len(datensatz)*p):]

    treffer = 0
    for testdatenzeile in testdaten:
        vermutung = krk(testdatenzeile[:-1], trainingsdaten)
        if vermutung == testdatenzeile[:-1]:
            treffer += 1
    
    return treffer / len(testdaten)

for k in tqdm.tqdm(range(10000)):
    print(validierung(0.2))

# test_datensatz = datensatz[:1]

# trainings_datensatz = datensatz[1:]

# k = 0.2

# abstände = []
# for zeile in trainings_datensatz:
#     abstände.append([abstand(zeile[:-1], test_datensatz[0][:-1]), zeile[-1]])
# # print(abstände)

# radius_k = list(filter(lambda x: x[0] <= k, abstände))

# vorhersage = max([abstand[1] for abstand in radius_k], key=radius_k.count)

