import itertools


# creates the matrix with all the cards
figures_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
naipes_list = [('d','#014082'), ('h','#ce0e0e'), ('s','#000000'), ('c','#00732b')]
cards_matrix = [[figure + naipe[0] for figure in figures_list] for naipe in naipes_list]


# creates a list with all hands
hands = []
for f1 in figures_list:
    for f2 in figures_list:
        if f1 == f2:
            if f1+f2 not in hands:
                hands.append(f1+f2)
        elif figures_list.index(f1) < figures_list.index(f2):
            if f1+f2+'s' not in hands:
                hands.append(f1+f2+'s')
        elif f1+f2+'o' not in hands:
                hands.append(f2+f1+'o')

# separate hands into pairs, suiteds and off-suiteds to make the combinations
pairs = []
suiteds = []
off_suiteds = []

for hand in hands:
    if hand[0] == hand[1]:
        pairs.append(hand)
    elif 's' in hand:
        suiteds.append(hand)
    elif 'o' in hand:
        off_suiteds.append(hand)

combinations = {}
naipes = "dhsc"
for hand in pairs:
    combinations[hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
    for naipe in itertools.combinations(naipes, len(hand))]

for hand in suiteds:
    combinations[hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
    for naipe in list(itertools.product(naipes, repeat=2))]

# gambiarra pra deixar somente as mãos suited
for hand in suiteds:
    for combo in combinations[hand][:]:
        if combo[0][1] != combo[1][1]:
            combinations[hand].remove(combo)

for hand in off_suiteds:
    combinations[hand] = [(hand[0] + naipe[0], hand[1] + naipe[1],)
    for naipe in list(itertools.product(naipes, repeat=2))]

# gambiarra pra deixar somente as mãos 0ff-suiteds
for hand in off_suiteds:
    for combo in combinations[hand][:]:
        if combo[0][1] == combo[1][1]:
            combinations[hand].remove(combo)


default_color_buttons = {
'1': {'color': '#B2301E'}, '2': {'color' : '#BE6EAE'}, '3': {'color': '#EA8376'}, 
'4': {'color': '#4572A9'}, '5': {'color': '#81ACDF'}, '6': {'color': '#E8950F'},
'7': {'color': '#FFCD69'}, 'SPLIT': {'color': '#27A2A1'}}


color_button_control = {
    'pf1': {'buttons': [], 'color': ''}, 'pf2': {'buttons': [], 'color': ''}, 
    'f1': {'buttons': [], 'color': ''}, 'f2': {'buttons': [], 'color': ''}, 
    'f3': {'buttons': [], 'color': ''}, 't1': {'buttons': [], 'color': ''}, 
    't2': {'buttons': [], 'color': ''}, 't3': {'buttons': [], 'color': ''},
    'r1': {'buttons': [], 'color': ''}, 'r2': {'buttons': [], 'color': ''}, 
    'r3': {'buttons': [], 'color': ''}, 
}
