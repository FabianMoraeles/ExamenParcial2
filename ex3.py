vecinos = {
    0: [8],
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8],
    8: [0, 5, 7, 9],
    9: [6, 8]
}

def nokia(n):
    if n == 1:
        return 10
    
    comb = {d: 1 for d in range(10)}
    
    for j in range(2, n + 1):
        nuevo_comb = {}
        for d in range(10):
            nuevo_comb[d] = sum(comb[v] for v in vecinos[d])
        comb = nuevo_comb
    
    return sum(comb.values())

for n in [2, 3, 4]:
    total = nokia(n)
    print("n=" + str(n) + " -> " + str(total) + " combinaciones")