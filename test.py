combinations = {'AKs': [('Ad', 'Kd'), ('Ad', 'Kh'), ('Ad', 'Ks'), ('Ad', 'Kc'), ('Ah', 'Kd'), ('Ah', 'Kh'), ('Ah', 'Ks'), ('Ah', 'Kc'), ('As', 'Kd'), ('As', 'Kh'), ('As', 'Ks'), ('As', 'Kc'), ('Ac', 'Kd'), ('Ac', 'Kh'), ('Ac', 'Ks'), ('Ac', 'Kc')]}

for combo in combinations['AKs'][:]:
    if combo[0][1] != combo[1][1]:
        combinations['AKs'].remove(combo)
    else:
        print(combo)
print(combinations['AKs'])

