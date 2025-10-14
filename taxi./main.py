import random
spielfeld_taxi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, "t", 21, 22, 23, 24, 25]
zustands_tabelle = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#findet den Index des Objektes in der Liste
def finder(voc : str, liste : list) -> list:
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j] == voc:
                return [i, j]

#checker ob car auf ziel mit oder ohne man -> bestrafung / belohnung je nachdem

# Angabe welcher zustand es ist
# Möglichkeiten: 
# zeile_auto : [0,1,2,3,4]; spalte_auto : [0,1,2,3,4] -> feld ist 5x5; 
# pos_passagier : [0,1,2,3,4] -> fünf mögl. Positionen (einer der vier Pkte oder im Taxi); 
# ziel : [0,1,2] -> alle Zielpunkte außer des Startpkts sind mögl.
def zustandskodierung(zeile_auto : int, spalte_auto : int, pos_passagier : int, ziel : int) -> int:
    taxiposition = zeile_auto * 5 + spalte_auto
    return (taxiposition * 5 + pos_passagier) *4 + ziel

# https://en.wikipedia.org/wiki/Q-learning
# errechnet den wert der in die tabelle eingetragen wird
def formel(a : float, q : list, st : int, at : int, rt : int, l : float) -> float:
    return (1 - a) * q[st][at] + a * (rt + l * max(tuple(q[st+1])))

# dekodiert die zustandskodierung (mom_pos) -> siehe zustandskodierung
# f a,b = 5a + b -> b = f a,b - 5a -> a + b = 10 => 10 = f a,b - 5a + a ==> a = (10 - f a,b) / 4  
def zustandsdekodierung(mom_pos : int, pos_passagier : int, ziel : int) -> list:
    taxiposition = ((mom_pos - ziel) / 4 - pos_passagier) / 5
    zeile_auto = (10 - taxiposition) / 4
    spalte_auto = taxiposition - 5 * zeile_auto
    return [spalte_auto, zeile_auto]

def platzierung():
    pos_passagier = random.choice([1,3,7,11])
    ziel = random.choice([1,3,7,11])
    if pos_passagier != ziel:
        return [pos_passagier, ziel]
    else:
        return platzierung()
    
def reward(taxi_pos : int, pos_passagier : int, ziel : int, passagier : bool):
    if not passagier and taxi_pos == pos_passagier: # muss noch angepasst werden 25 : 500
        return 50
    if passagier and taxi_pos == ziel:
        return 100
    return -1

def updater(pos):
    return (zustandsdekodierung(pos)[0] + 1)  * zustandsdekodierung[1]

def angabe_pos_passagier(passagier_drin : int):
    if passagier_drin:
        return 5
    if spielfeld_taxi[1] == "p":
        return 1
    if spielfeld_taxi[3] == "p":
        return 2
    if spielfeld_taxi[7] == "p":
        return 3
    if spielfeld_taxi[11] == "p":
        return 4

def main():
    taxi_pos = finder("t", spielfeld_taxi)
    posi = platzierung()
    pos_passagier = posi[0]
    ziel = posi[1]
    spielfeld_taxi[pos_passagier] = "p"
    spielfeld_taxi[ziel] = "z"
    passagier_drin = 0
    if spielfeld_taxi("t") == spielfeld_taxi("p"):
        passagier_drin = 1
    zustand = zustandskodierung(taxi_pos[0], taxi_pos[1], angabe_pos_passagier(passagier_drin), ziel)
    formel(0.6, zustands_tabelle, zustand, random.randint(0, 5), reward(taxi_pos, pos_passagier, ziel, passagier_drin), 0.5)