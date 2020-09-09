figuras = ['A', 'K'] # Ás 
naipes = ['d', 'h', 's', 'c'] # d = diamond (ouros), s = spade (espadas), h = hearts (copas), c = clubs(paus)

cartas = []
for figura in figuras:
    for naipe in naipes:
        cartas.append(figura+naipe)
# print(cartas)

hands = []
for figura1 in figuras:
    for figura2 in figuras:
        if figuras.index(figura1) < figuras.index(figura2):
            hands.append(figura1+figura2)
        else:
            hands.append(figura2+figura1)


print(hands)