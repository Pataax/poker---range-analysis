from pprint import pprint

d = {'azul': {'label': 'labelazul'}, 'amarelo': {'label': 'labelamarelo'}}

foo = 'azul'
path = d[foo]
if 'select_range' not in path:
    path['select_range'] = []

print(d)


