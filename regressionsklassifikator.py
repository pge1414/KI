import csv, matplotlib.pyplot as plt, numpy as np
from matplotlib import cm

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

x_wert_list_setosa = []
y_wert_list_setosa = []
t_wert_list_setosa = []
x_wert_list_versicolor = []
y_wert_list_versicolor = []
t_wert_list_versicolor = []
x_wert_list_virginica = []
y_wert_list_virginica = []
t_wert_list_virginica = []

for i in datensatz:
    if i[4]== "Iris-setosa":
        x_wert_list_setosa.append(i[2])
        y_wert_list_setosa.append(i[1])
        t_wert_list_setosa.append(i[3])
    if i[4]== "Iris-versicolor":
        x_wert_list_versicolor.append(i[2])
        y_wert_list_versicolor.append(i[1])
        t_wert_list_versicolor.append(i[3])
    if i[4]== "Iris-virginica":
        x_wert_list_virginica.append(i[2])
        y_wert_list_virginica.append(i[1])
        t_wert_list_virginica.append(i[3])

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

def t_mitte(t):
    t_wert = 0
    for i in t:
        t_wert += i
    return t_wert/len(t)

def gerade(x_y1, x_y2, x_y3, search):

    # die X-Werte:
    x1 = [0, x_y1[0]]
    # die Y-Werte:
    y1 = [0, x_y1[1]]

    x2 = [0, x_y2[0]]
    y2 = [0, x_y2[1]]

    x3 = [0, x_y3[0]]
    y3 = [0, x_y3[1]]

    plt.plot(x1, y1, color='black')
    plt.plot(x2, y2, color='green')
    plt.plot(x3, y3, color='red')
    plt.plot(search[0], search[1], "bo")
    plt.show()

x_y_setosa = mittelwert(x_wert_list_setosa, y_wert_list_setosa)
x_y_versicolor = mittelwert(x_wert_list_versicolor, y_wert_list_versicolor)
x_y_virginica = mittelwert(x_wert_list_virginica, y_wert_list_virginica)
t_setosa = t_mitte(t_wert_list_setosa)
t_versicolor = t_mitte(t_wert_list_versicolor)
t_virginica = t_mitte(t_wert_list_virginica)

def m(x_y) -> int:
    m = x_y[1]/x_y[0]
    return m

def REG_K(m_d, m_s : float, t_s : float):
    a = 100.0
    b = 100.0
    k = {"" : a}
    for i, j in m_d.items():
        if float(j[0]-m_s)**2 < a and float(j[1]-t_s)**2 < b:
            k = {i : j}
            a = float(j[0]-m_s)**2
            b = float(j[1]-t_s)**2
    return k
        
x = 1.5
y = 0.2

# print(REG_K({"setosa" : m(x_y_setosa), "versicolor" : m(x_y_versicolor), "virginica" : m(x_y_virginica)}, m((x, y))))
# gerade(x_y_setosa, x_y_versicolor, x_y_virginica, (x, y))

test_datensatz = []

for i in datensatz:
    test_datensatz.append(i)

def test(durchgänge):
    anzahl = 0
    for z in range(durchgänge):
        for i in test_datensatz:
            for a in REG_K({"Iris-setosa" : [m(x_y_setosa), t_setosa], "Iris-versicolor" : [m(x_y_versicolor), t_versicolor], "Iris-virginica" : [m(x_y_virginica), t_virginica]}, m((i[2], i[1])), i[3]).keys():
                if str(a) == i[4]:
                    anzahl += 1
    return anzahl, len(datensatz)*durchgänge, anzahl/(len(datensatz)*durchgänge)

print(test(1))



#6.3,2.3,4.4,1.3,Iris-versicolor
#5.0,3.3,1.4,0.2,Iris-setosa
#5.9,3.0,5.1,1.8,Iris-virginica

# raging: 2, 1, 3