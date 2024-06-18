import csv, matplotlib.pyplot as plt

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

def m(x : list, y : list):
    return sum(y) / sum(x)
        
def term(m : float, x : float):
    return m*x

x_setosa = []
y_setosa = []

for i in datensatz:
    if i[4] == "Iris-setosa":
        x_setosa.append(i[0])
    if i[4] == "Iris-setosa":
        y_setosa.append(i[1])

print(term(m(x_setosa, y_setosa), 5.4))

################################################################

################################################################

# for i in range(x_setosa):
#     term(m(x_setosa, y_setosa), x_setosa[i])

#5.4,3.7,1.5,0.2,Iris-setosa
#4.8,3.0,1.4,0.1,Iris-setosa
#5.0,3.3,1.4,0.2,Iris-setosa