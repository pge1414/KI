import csv, math

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])



zeilen_nach_art = {}
for zeile in datensatz:
    if not zeile[-1] in zeilen_nach_art: 
        if not zeile[-1] in zeilen_nach_art:
            zeilen_nach_art[zeile[-1]] = []

        zeilen_nach_art[zeile[-1]].append(zeile[:-1])

def gauss(o,p,x):
    return 1/(o*math.sqrt(2*math.pi))*math.e**(-0.5((x-p)/o)**2)

def varianz(a : float, b : float, c : float, d : float) -> float:
    er = (a+b+c+d)/4
    return ((a-er)**2+(b-er)**2+(c-er)**2+(d-er)**2)/4

def standardverteilung(varianz : float) :
    return math.sqrt(varianz)

print(zeilen_nach_art)


#erstelle ein dict, dass für jede vorkommende art alle zugehörigen datenzeilen abspeichert
#erstelle im anschluss ein dict, das für jede kombination aus art und eingabeparameter (3*4 = 12 stück) die den datensatz entsprechende gauss verteilung enthält