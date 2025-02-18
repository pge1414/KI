def adalinelerning(eta, x : list, w : list, y : int):
    while True:
        for i in range(len(x)):
            y_ = 1 + w[i] * x[i]
            error = abs(y_ - y) ** 2
            w[i] = w[i] - eta*(2*error)*x[i]
            print(y_)
            print(error)
        if error < 0.0001:
            print(f"error : {error}")
            print(w)
            False
            return w

#print(adalinelerning(0.0001, [1,1,1], [0.1,0.1,0.1], 1))

w = adalinelerning(1, [1,1,1], [0.1,0.1,0.1], 1)

def AndII(x : list, w : list):
    y = 0
    for i in range(len(w)):
        y += w[i] * x[i]
    if y - (len(w) - 2) > 0:
        return 1
    else:
        return 0
        
print(f"y : {AndII([1,1,1], w)}")
