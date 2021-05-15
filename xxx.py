rsw_slots = {'pf1': '', 'pf2': '', 
    'f1': '','f2': '', 'f3': '',
    't1': '', 't2': '', 't3': '', 
    'r1': '', 'r2': '', 'r3': ''}

slot_name = 'pf2'
keys = list(rsw_slots)

current_slot_first_char = keys[keys.index(slot_name)][0]
next_slot_first_char = keys[((keys.index(slot_name)) + 1)][0]

if next_slot_first_char == current_slot_first_char:
    next_street = keys[keys.index(slot_name) + 2]
else:
    next_street = keys[keys.index(slot_name) + 1]
print(next_street)

# rsw_slots[next_street].show()