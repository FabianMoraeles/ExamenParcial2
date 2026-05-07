prueba = [293, 100, 41]

def sencillo(m):
    denominaciones=[25, 10, 5, 1]
    resultado = {}
    
    for d in denominaciones:
        if m >= d:
            cantidad = m // d
            resultado[d] = cantidad
            m -= cantidad * d
    
    return resultado



for monto in prueba:
    monedas = sencillo(monto)
    total = sum(monedas.values())
    print("Monto: Q" + str(monto // 100) + "." + str(monto % 100))
    for den, cant in monedas.items():
        if cant > 0:
            print(str(cant) + " monedas de Q0." + str(den))
    print("Total monedas: " + str(total) + "\n")