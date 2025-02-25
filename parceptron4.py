import matplotlib.pyplot as plt, time, numpy as np, math

class Adaline:
    
    #errors = []

    def adalinelerning(eta, x : list, w : list, y : int):
        while True:
            for i in range(len(x)):
                y_ = 1 + w[i] * x[i]
                error = abs(y_ - y) ** 2
                w[i] = w[i] - eta*(2*error)*x[i]
                #errors.append(error)
                print(f"error : {error}")
                print(f"w : {w}")
            if error < 0.0001:
                False
                return w

    def Or(x : list,w : list):
        y = 0
        for i in range(len(x)):
            y += w[i] * x[i]
        if y > 0:
            return 1
        else:
            return 0

        
# w = Adaline.adalinelerning(0.1, [1,1,2,1], [0.1,0.1,0.1,0.1], 1)
        
# print(f"y : {Adaline.Or([0,0,0,0], w)}")

class Test:

    gewichte = []
    
    def tester(eta, x : list, w : list, y : list):
        for i in range(len(y)):
            print(i)
            Test.gewichte.append(Adaline.adalinelerning(eta, x[i], w[i], y[i]))
            print(Test.gewichte)
        return Test.gewichte
    
    def supporter(erg : list):
        list1 = []
        list2 = []
        list3 = []
        liste = [1,2,3,4,5]
        for i in erg:
            list1.append(i[0])
            list2.append(i[1])
            list3.append(i[2])
        return[list1, list2, list3]
        # fig, ax = plt.subplots()
        # ax.plot(liste,list1)
        # ax.plot(liste,list2)
        # ax.plot(liste,list3)
        # plt.show()


class Regression:

    def mittelwert(liste : list)-> int:
        return sum(liste)/ len(liste)

    def kovarianz(liste_x : list, liste_y : list)-> int:
        liste_produkte = []
        for i in range(len(liste_x)):
            diff_x = liste_x[i] - sum(liste_x) / len(liste_x)
            diff_y = liste_y[i] - sum(liste_y) / len(liste_y)
            liste_produkte.append(diff_x*diff_y)
        return sum(liste_produkte)

    def korelation(liste_x : list, liste_y : list):
        return int(np.correlate(liste_x, liste_y))

    def standartabweichung(liste : list):
        o = []
        for i in range(len(liste)):
            o.append(math.sqrt((liste[i]-Regression.mittelwert(liste))**2 * 1/3)) # 1/3 weil alle blumen gleich of vorkommen
        return sum(o)

    def b(sy, sx, rxy):
        return (sy/sx) *rxy

    def a(sy, sx, rxy, x, y):
        return -(sy/sx) * rxy * x + y

    def regression(prädiktor, a, b):
        return b*prädiktor + a

    def final(w : list,x : list ,y : list):
        werte = []
        x_ = Regression.mittelwert(x)
        y_ = Regression.mittelwert(y)

        sx = Regression.standartabweichung(x)
        sy = Regression.standartabweichung(y)

        sxy = Regression.kovarianz(x, y) 

        rxy = Regression.kovarianz(x, y)

        a_ = Regression.a(sy, sx, rxy, x_, y_)
        b_ = Regression.b(sy, sx, rxy)

        for i in range(len(w)):
            # print(f"Wert: {w[i]}")
            # print(f"Regresseionsgerade: {Regression.regression(w[i], a_, b_)}")
            # print("----------------------------------------")
            werte.append(Regression.regression(w[i], a_, b_))
        return werte







testerg = Test.tester(0.2, [[1,0,0],[0,1,0],[0,1,0],[1,0,1],[0,1,1]], [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]], [1,1,1,1,1])
# print(f"Ergebnis: {testerg}")
# Test.supporter(testerg)

print(Regression.final(Test.supporter(testerg)[2], Test.supporter(testerg)[0], Test.supporter(testerg)[1]))



