def foo():
    return 'arroz', 'feijao'

x, *y = foo()
print(y)