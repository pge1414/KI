import csv, math

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

x_wert_list_setosa = []
y_wert_list_setosa = []
x_wert_list_versicolor = []
y_wert_list_versicolor = []
x_wert_list_virginica = []
y_wert_list_virginica = []

for i in datensatz:
    if i[4]== "Iris-setosa":
        x_wert_list_setosa.append(i[0])
        y_wert_list_setosa.append(i[1])

def mittelwert(x:list, y:list) -> int:
    x_wert = 0
    y_wert = 0
    for i in x:
        x_wert += i
    for i in y:
        y_wert += i
    durchschnitt_x = x_wert/len(x)
    durchschnitt_y = y_wert/len(y)
    return durchschnitt_x, durchschnitt_y

#def gerade()

print(x_wert_list)
print(y_wert_list)

print(mittelwert(x_wert_list, y_wert_list))