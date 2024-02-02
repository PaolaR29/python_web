import time
import pandas as pd
import matplotlib.pyplot as plt

def funcion1(n):
    return n*(n+1)//2

def funcion2(n):
    suma=0
    for i in range(1,n+1):
        suma+=1
    return suma

lista_numeros = [10,100,1000,10000]

tiempos = {'funcion1':[], 'funcion2':[]}

#medir tiempos de ejecucion
for n in lista_numeros:
    inicio = time.perf_counter()
    funcion1(n)
    fin = time.perf_counter()
    diferencia = fin - inicio
    tiempos['funcion1'].append(diferencia)

    inicio = time.perf_counter()
    funcion2(n)
    fin = time.perf_counter()
    diferencia = fin - inicio
    tiempos['funcion2'].append(diferencia)

#Imprimir los tiempos
for i in tiempos:
    print(f"Tiempos de ejecución de la función 1 ({i}):")
    for n, t in zip(lista_numeros, tiempos[i]): #Se esta recorriendo la lista de números y los tiempos
        #que se están accesando para la función 1, se asignan tanto para n como para tiempo
        print(f"n = {n}: {t} segundos")
    print()

#crear un dataframe
df = pd.DataFrame(tiempos,index=lista_numeros)
df.index.name = "n"
df.reset_index(inplace=True)

#mostrar el dataframe
print(df)

#Generar una gráfica
plt.plot(df['n'], df['funcion1'], label="Suma constante", marker='o')
plt.plot(df['n'], df['funcion2'], label="Suma lineal", marker='x')
plt.xlabel("n (Números de elementos)")
plt.ylabel("Tiempos de ejecución (s)")
plt.title("Comparación del tiempo de Ejecución: Suma Lineal vs Suma Constante")
plt.xscale('log')
plt.yscale('log')
plt.legend
plt.grid(True)
plt.savefig('Sumatorias.png')
