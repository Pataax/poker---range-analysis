figures_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
naipes_list = [('d','#014082'), ('h','#CC0000'), ('s','#000000'), ('c','#00732B')]

cards = [[figure + naipe[0] for figure in figures_list] for naipe in naipes_list]
hands = [[figure1 + figure2 for figure1 in figures_list] for figure2 in figures_list]

for i in cards:
    print(i)
print('-'*100)
for i in hands:
    print(i)