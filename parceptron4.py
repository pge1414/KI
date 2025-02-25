import matplotlib.pyplot as plt

class Adaline:
    
    #errors = []

    def adalinelerning(eta, x : list, w : list, y : int):
        while True:
            for i in range(len(x)):
                y_ = 1 + w[i] * x[i]
                error = abs(y_ - y) ** 2
                w[i] = w[i] - eta*(2*error)*x[i]
                print(error)
                #errors.append(error)
            if error < 0.0001:
                print(f"error : {error}")
                print(w)
                False
                return w

    def half(x : list,w : list):
        for i in range(len(x)-1):
            y += w[i] * x[i]
        if y == len(x)/2:
            return 1
        else:
            return 0

        
    w = adalinelerning(0.1, [0,0,1,1], [0.1,0.1,0.1, 0.1], 2 )
            
    print(f"y : {half([1,1,0,0], w)}")

    #fig, ax = plt.subplots()
    #ax.scatter(gewichte, zahlen)
    #ax.plot(errors)
    #plt.show()

class Test:

    gewichte = []
    
    def tester(eta, x : list, w : list, y : list):
        for i in range(len(y)-1):
            print(i)
            Test.gewichte.append(Adaline.adalinelerning(eta, x[i], w[i], y[i]))
            print(Test.gewichte)
        return Test.gewichte
    
#print(Test.tester(1, [[1,0,0],[0,1,0],[0,1,0],[1,0,1]], [[0,0,0],[0,0,0],[0,0,0],[0,0,0]], [1,1,1,1]))
