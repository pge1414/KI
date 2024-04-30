import csv, math


def mu_f(daten):
    return sum(daten) / len(daten)

def sigma_f(daten):
    mu = mu_f(daten)
    return math.sqrt(sum([(x - mu) ** 2 for x in daten]) / (len(daten) - 1))

def gauss(x, mu, sigma):
    return (1/(sigma*math.sqrt(2*math.pi))) * math.e ** (-0.5 * ((x - mu) / sigma) ** 2)

datensatz = []
with open("iris.csv") as f:
    csv_reader = csv.reader(f)
    for zeile in csv_reader:
        datensatz.append([float(wert) for wert in zeile[:-1]] + [zeile[-1]])

def mu_sigma_nach_art_f():
    zeilen_nach_art = {}
    for zeile in datensatz:
        if not zeile[-1] in zeilen_nach_art:
            zeilen_nach_art[zeile[-1]] = []

        zeilen_nach_art[zeile[-1]].append(zeile[:-1])

    spalten_nach_art = {}
    for art in zeilen_nach_art:
        spalten_nach_art[art] = list(zip(*zeilen_nach_art[art]))

    ergebnis = {}
    for art in spalten_nach_art:
        ergebnis[art] = [(mu_f(spalte), sigma_f(spalte)) for spalte in spalten_nach_art[art]]

    return ergebnis

def nbk(daten):
    mu_sigma_nach_art = mu_sigma_nach_art_f()

    p_nach_art = dict.fromkeys(mu_sigma_nach_art.keys(), 1)
    art_max = None
    for art in mu_sigma_nach_art:
        p_nach_art[art] = 1
    
        for i in range(len(daten)):
            p_nach_art[art] *= p_nach_art[art] * gauss(daten[i], mu_sigma_nach_art[art][i][0] , mu_sigma_nach_art[art][i][1])

        # TODO Wo bei der Berechnung von p der Fehler?

        if not art_max or p_nach_art[art] > p_nach_art[art_max]:
            art_max = art

    return art_max

print(nbk([6.3,3.3,6.0,2.5]))
print(datensatz[0][-1])

# mehrdimensionale Gauss-Verteilung: https://de.wikipedia.org/wiki/Mehrdimensionale_Normalverteilung
