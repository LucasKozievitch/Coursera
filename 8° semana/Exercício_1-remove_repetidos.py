def remove_repetidos(lista):
    lista_nova = []

    for i in lista:
        exists = False
        for j in lista_nova:
            if i == j:
                exists = True
                break

        if exists == False:
            lista_nova.append(i)

    return sorted(lista_nova)