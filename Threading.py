import threading,time,math

# def summieren(liste, von, bis):
#     ergebnis = 0
#     for i in range(von, bis):
#         ergebnis += liste[i]
#     return ergebnis

# def sum_threads(liste, von, bis, ergebnisse, index):
#     summe = sum(liste[von:bis])
#     ergebnisse[index] = summe

# def listensumme_multithreaded(liste, k):
#     threads = []
#     ergebnisse = [1 for i in range(k)]
    
#     for i in range(k):
#         t= threading.Thread(target=sum_threads, args= [liste, len(liste) // k * i, len(liste) // k * (i + 1), ergebnisse, i])
#         threads.append(t)
#         t.start()

#     ergebnis = 0

#     for i in range(k):
#         threads[i].join()
#         ergebnis += ergebnisse[i]

#     return ergebnis

# trainings_liste = []

# for i in range(200000000):    trainings_liste.append(i)

# start = time.time()

# print(listensumme_multithreaded(trainings_liste, 8))
# print(time.time() - start)

# start2 = time.time()
# print(sum(trainings_liste))
# print(time.time() - start2)

# def liste_enthält_not_multithreaded(liste, x):
#     if x in liste: return True
# ergebnisse = []

# def liste_enthält(liste, x, von, bis):
#     if x in liste[von:bis]:ergebnisse.append(True)

# def enthält_multithreaded(liste, x, k):
#     threads = []

#     for i in range(k):
#         t= threading.Thread(target=liste_enthält, args= [liste, x, len(liste) // k * i, len(liste) // k * (i + 1)])
#         threads.append(t)
#         t.start()

#     for i in range(k):
#         threads[i].join()

#     for i in ergebnisse:
#         if i == True:
#             return True
        
# trainings_liste = []

# for i in range(900000000):    trainings_liste.append(i)

# start = time.time()

# print(enthält_multithreaded(trainings_liste,899999999, 8))
# print(time.time() - start)

# start2 = time.time()
# print(liste_enthält_not_multithreaded(trainings_liste,899999999))
# print(time.time() - start2)


ergebnisse_max = []

def max_singlethreaded(liste,von,bis):
    max = -math.inf
    for i in liste[von:bis]:
        if i > max:
            max = i
    ergebnisse_max.append(max)

def max_multithreaded(liste, k):
    threads = []

    for i in range(k):
        t= threading.Thread(target=max_singlethreaded, args= [liste, len(liste) // k * i, len(liste) // k * (i + 1)])
        threads.append(t)
        t.start()

    for i in range(k):
        threads[i].join()

    return max(ergebnisse_max)

start = time.time()

trainings_liste = []

for i in range(1000):    trainings_liste.append(i)

print(max_multithreaded(trainings_liste, 8))
print(time.time() - start)

start2 = time.time()
print(max(trainings_liste))
print(time.time() - start2)