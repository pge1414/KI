import random

# spielfeld = [["1",2,3,4,5],[1,2,"2",4,5],[1,2,3,4,5],[1,2,3,4,"3"],[1,"4",3,4,5]]

# def finder(voc : str, liste : list) -> list:
#     for i in range(len(liste)):
#         for j in range(len(liste[i])):
#             if liste[i][j] == voc:
#                 return [i, j]

# def punktverteilung(liste : list) -> list:
#     punkt_passagier = str(random.randint(1,4))
#     punkt_ziel = str(random.randint(1,4))
#     if punkt_passagier != punkt_ziel:
#         pas = finder(punkt_passagier, liste)
#         ziel = finder(punkt_ziel, liste)
#         liste[pas[0]][pas[1]] = "p"
#         liste[ziel[0]][ziel[1]] = "z"
#     else:
#         punktverteilung(liste)

# punktverteilung(spielfeld)
# print(spielfeld)

# for i in range(len(spielfeld)):
#     for j in range(len(spielfeld[i])):
#         if spielfeld[i][j] == "4":
#             print(i , j)
liste = []
for i in range(500):
    liste.append(0)

print(liste)

# print(max(tuple([1,2,3])))

# def platzierung():
#     pos_passagier = random.choice([244,354,498,106])
#     ziel = random.choice([244,354,498,106])
#     if pos_passagier != ziel:
#         return [pos_passagier, ziel]
#     else:
#         return platzierung()

# print(platzierung())