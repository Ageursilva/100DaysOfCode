from collections import OrderedDict

def remove_duplicatas():
    lista_original = [5, 5, 1, 2, 2, 3, 4]
    lista_sem_repeticao  = list(OrderedDict.fromkeys(lista_original))
    print(lista_sem_repeticao )
    
remove_duplicatas()