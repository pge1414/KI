import csv, matplotlib.pyplot as plt

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

x1_setosa = []
x2_setosa = []
x3_setosa = []
x4_setosa = []

x1_versicolor = []
x2_versicolor = []
x3_versicolor = []
x4_versicolor = []

x1_virginica = []
x2_virginica = []
x3_virginica = []
x4_virginica = []


for i in datensatz:
    if i[4] == "Iris-setosa":
        x1_setosa.append(i[0])
    if i[4] == "Iris-setosa":
        x2_setosa.append(i[1])
    if i[4] == "Iris-setosa":
        x3_setosa.append(i[2])
    if i[4] == "Iris-setosa":
        x4_setosa.append(i[3])

    if i[4] == "Iris-setosa":
        x1_setosa.append(i[0])
    if i[4] == "Iris-setosa":
        x2_setosa.append(i[1])
    if i[4] == "Iris-setosa":
        x3_setosa.append(i[2])
    if i[4] == "Iris-setosa":
        x4_setosa.append(i[3])
        
    if i[4] == "Iris-setosa":
        x1_setosa.append(i[0])
    if i[4] == "Iris-setosa":
        x2_setosa.append(i[1])
    if i[4] == "Iris-setosa":
        x3_setosa.append(i[2])
    if i[4] == "Iris-setosa":
        x4_setosa.append(i[3])



################################################################

################################################################

# for i in range(x_setosa):
#     term(m(x_setosa, y_setosa), x_setosa[i])

#5.4,3.7,1.5,0.2,Iris-setosa
#4.8,3.0,1.4,0.1,Iris-setosa
#5.0,3.3,1.4,0.2,Iris-setosa