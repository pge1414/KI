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
        y_setosa.append(i[01])

print(term(m(x_setosa, y_setosa), )
      
#6.0,2.2,5.0,1.5,Iris-virginica