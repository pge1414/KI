import multiprocessing, math, time

def listen_teiler(liste, n : int):
    if n <= 0:
        raise ValueError("n nicht pos")
    liste_von_teillisten = [[]]*n
    for i in range(len(liste)):
        liste_von_teillisten[i%n].append(liste[i])
    return liste_von_teillisten

def maximum_single(liste):
    max = -math.inf
    for i in range(0, len(liste)):
        if liste[i] > max:
            max = liste[i]
    return max

def maximum_multi(liste, k):
    #trenn_indizes = [(liste, i, i+len(liste) // k) for i in range(0, len(liste)+1, len(liste) // k)]

    with multiprocessing.Pool(k) as pool:
        liste_geteilt = listen_teiler(liste, 8)
        ergebnisse = pool.map(max, liste_geteilt)

    return maximum_single(ergebnisse)

if __name__ == '__main__':

    zufallsliste = [i for i in range(10000000)]

    t1 = time.time()
    print(maximum_multi(zufallsliste, 8))
    print(time.time() - t1)

    t2 = time.time()
    print(max(zufallsliste))
    print(time.time() - t2)