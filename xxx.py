def f1():
    print('1')

def f2():
    print('2')

f_list = [f1, f2]

for f in f_list:
    f()