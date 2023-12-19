import csv

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

k = 23

abstände = []
for zeile in trainings_datensatz:
    abstände.append([euklidischer_abstand(zeile[:-1], test_datensatz[0][:-1]), zeile[-1]])

abstände.sort(key=lambda x: x[0])

top_k_abstände = abstände[:k]

vorhersage = max([abstände[1] for abstände in top_k_abstände], key=top_k_abstände.count)

print(top_k_abstände)
print(vorhersage)