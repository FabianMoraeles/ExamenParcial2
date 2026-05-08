pruebas = [
    (50, [(60,10),(100,20),(120,30)]),  
    (30, [(500,5),(400,10),(300,15)]),
    (15, [(10,2),(5,3),(15,5),(7,1)])
]

def knapsack_fraccionado(W, articulos):
    
    articulos = sorted(articulos, key=lambda x: x[0]/x[1], reverse=True)
    
    valor_total = 0
    capacidad = W
    seleccion = []
    
    for precio, peso in articulos:
        if capacidad == 0:
            break
        tomar = min(peso, capacidad)
        valor = tomar * (precio / peso)
        valor_total += valor
        capacidad -= tomar
        seleccion.append((precio, peso, tomar))
    
    return valor_total, seleccion




for W, items in pruebas:
    val, sel = knapsack_fraccionado(W, items)
    print("W=" + str(W))
    for p,w,t in sel:
        print("  item(p=" + str(p) + ",w=" + str(w) + ") - " + str(t))
    print("  Valor total: " + str(round(val, 2)) + "\n")