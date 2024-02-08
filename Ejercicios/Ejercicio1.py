#def busqueda(lista, objetivo):

def busqueda(lista,objetivo):
  for e in range(0,len(lista)):
    for j in range(e+1,len(lista)):
      res = lista[e]+lista[j]
      if res == objetivo:
        print (lista[e] ,", ",lista[j])
        break

#lectura de números
lista = [ 1,9,5,0,20,-4,12,16,7]
objetivo = 10

busqueda(lista,objetivo)