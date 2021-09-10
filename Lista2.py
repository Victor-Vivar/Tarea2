lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def mid(lista):
    if len(lista) % 2 == 0:
        if len(lista) == 2:
            lista.pop(1)
            return lista
        lista.pop(0)
        lista.pop()
        return mid(lista)
    if len(lista) == 1:
        return lista
    lista.pop(0)
    lista.pop(-1)

    return mid(lista)
print(mid(lista))