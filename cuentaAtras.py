def cuentaAtras(x):
    while x > 0:
        print(x)
        x = x - 1
    return print(x)

def contador(x):
    print("{},".format(x),end="")
    if x > 0:
        contador(x-1)
