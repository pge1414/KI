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

rdm_zeile = random.randint(0, 149)

test_datensatz = datensatz[rdm_zeile]
trainings_datensatz = datensatz.remove(test_datensatz)

k = 1

abstände = []
for zeile in list(trainings_datensatz):
    abstände.append([euklidischer_abstand(zeile[:-1], test_datensatz[0][:-1]), zeile[-1]])

abstände.sort(key=lambda x: x[0])

top_k_abstände = []

vorhersage_Radius = (max([abstände[1] for abstände in list(filter(lambda x: x[0]<=k, abstände))], key=list(filter(lambda x: x[0]<=k, abstände)).count))

print(vorhersage_Radius)

# for i in abstände:
#     if i[0] <= k:
#         top_k_abstände.append(i)

# vorhersage = max([abstände[1] for abstände in top_k_abstände], key=top_k_abstände.count)

#print(vorhersage)

if vorhersage_Radius == test_datensatz[4]:
    print("Ja")