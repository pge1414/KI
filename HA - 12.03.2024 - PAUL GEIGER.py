import threading, time, math

def aufsteigend_sortiert(liste, von, bis):
    liste = liste[von:bis].sort()

def aufsteigend_sortiert_multithreading(liste, k):
    threads = []

    for i in range(k):
        t= threading.Thread(target=aufsteigend_sortiert, args= [liste, len(liste) // k * i, len(liste) // k * (i + 1)])
        threads.append(t)
        t.start()

    for i in range(k):
        threads[i].join()

    liste.sort()

test = []

for i in range(100000000):
    test.append(-i)

start = time.time()
print(aufsteigend_sortiert_multithreading(test,4))
print(time.time()-start)

start2 = time.time()
print(test.sort())
print(time.time()-start2)

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