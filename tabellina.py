'''
Stampa la tabellina di un numero intero positivo per mezzo di un'iterazione.
Contollare l'input
(ciclo while)
'''
n = int(input("Inserisci un numero: "))
i = 0

if n > 0:
    while i < 11:
        print(n * i)
        i += 1
else:
    print("Inserisci un numero positivo e intero!!")