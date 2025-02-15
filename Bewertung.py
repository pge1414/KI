import csv, random

def euklidischer_abstand(p, q):
    a = 0
    for i in range(0, 3):
        a += (float(p[i]) - float(q[i]))**2
    return a**0.5

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]]+ [zeile[-1]])

test_datensatz = datensatz[:1]
trainings_datensatz = datensatz[1:]

k = 1

abstände = []
for zeile in trainings_datensatz:
    abstände.append([euklidischer_abstand(zeile[:-1], test_datensatz[0][:-1]), zeile[-1]])

abstände.sort(key=lambda x: x[0])

top_k_abstände = []

print(max([abstände[1] for abstände in list(filter(lambda x: x[0]<=k, abstände))], key=list(filter(lambda x: x[0]<=k, abstände)).count))

datensatz_transponiert = list(zip(*datensatz))
maxi = [max(datensatz_transponiert[0]), max(datensatz_transponiert[1]), max(datensatz_transponiert[2]), max(datensatz_transponiert[3])]
superd = []
print(maxi)
for i in range(len(datensatz)):
    for j in range(len(datensatz[i])-1):
        datensatz[i][j] /= maxi[j]
print(datensatz)

# for i in abstände:
#     if i[0] <= k:
#         top_k_abstände.append(i)

# vorhersage = max([abstände[1] for abstände in top_k_abstände], key=top_k_abstände.count)

#print(vorhersage)