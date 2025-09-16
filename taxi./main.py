spielfeld_taxi = [[1,2,"c",4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
spielfeld = [[1,2,3,4,5],[1,2,"m",4,5],[1,2,3,4,5],[1,2,3,4,5],[1,"z",3,4,5]]
lvl = 0
passagier = False

#findet den Index des Objektes in der Liste
def finder(voc : str, liste : list) -> list:
    for i in liste:
        for j in liste[i]:
            if voc in liste[i]:
                return [i,j]

#je höher das lvl desto schlechter der Weg (kleinere Bestrafungen pro Zug / größere wenn er den Fahrgast falsch absetzt)
def bestrafung(höhe : int) -> int:
    lvl += höhe

#bewegt das Objekt in horizontale und vertikale Richtung "R" "L" "O" "U"
def bewegung(r : str, liste : list) -> list:
    plz = finder["c", liste]
    if r == "R":
        liste[plz[0]][plz[1]] = plz[1] + 1
        plz[1] += 1
        liste[plz[0]][plz[1]] = "c"
    if r == "L":
        liste[plz[0]][plz[1]] = plz[1] + 1
        plz[1] -= 1
        liste[plz[0]][plz[1]] = "c"
    if r == "O":
        liste[plz[0]][plz[1]] = plz[1] + 1
        plz[0] -= 1
        liste[plz[0]][plz[1]] = "c"
    if r == "U":
        liste[plz[0]][plz[1]] = plz[1] + 1
        plz[0] += 1
        liste[plz[0]][plz[1]] = "c"


def vorwärts(liste : list) -> list:
    bewegung("O", liste)
    bestrafung(1)

def rückwärts(liste : list) -> list:
    bewegung("O", liste)
    bestrafung(1)

def rechts(liste : list) -> list:
    bewegung("O", liste)
    bestrafung(1)

def links(liste : list) -> list:
    bewegung("O", liste)
    bestrafung(1)

#checker ob car auf man -> Aufnahme der Person -> Belohnung oder nicht -> Bestrafung
def aufnahme(liste1 : list, liste2 : list):
    car = finder("c", liste1)
    man = finder("m", liste2)
    if car == man:
        bestrafung(-2)
        passagier = True
    else:
        bestrafung(5)

#checker ob car auf ziel mit oder ohne man -> bestrafung / belohnung je nachdem
def absetzen(liste1 : list, liste2: list):
    car = finder("c", liste1)
    ziel = finder("z", liste2)
    if car == ziel:
        if passagier:
            bestrafung(-3)
        else:
            bestrafung(7)
    else:
        bestrafung(5)