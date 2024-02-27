import threading,time

def summieren(liste, von, bis):
    ergebnis = 0
    for i in range(von, bis):
        ergebnis += liste[i]
    return ergebnis

def sum_threads(liste, von, bis, ergebnisse, index):
    summe = sum(liste[von:bis])
    ergebnisse[index] = summe

def listensumme_multithreaded(liste, k):
    threads = []
    ergebnisse = [1 for i in range(k)]
    
    for i in range(k):
        t= threading.Thread(target=sum_threads, args= [liste, len(liste) // k * i, len(liste) // k * (i + 1), ergebnisse, i])
        threads.append(t)
        t.start()

    ergebnis = 0

    for i in range(k):
        threads[i].join()
        ergebnis += ergebnisse[i]

    return ergebnis

trainings_liste = []

for i in range(200000000):    trainings_liste.append(i)

start = time.time()

print(listensumme_multithreaded(trainings_liste, 8))
print(time.time() - start)

start2 = time.time()
print(sum(trainings_liste))
print(time.time() - start2)