import time
import pandas as pd
import matplotlib.pyplot as plt

def buscar_suma(arreglo, sum):
  parejas=[]
  for i in range(len(arreglo)):
    for j in range(i+1, len(arreglo)):
      if arreglo[i]+arreglo[j]==sum:
        parejas.append((arreglo[i], arreglo[j]))
  return parejas

def parejas(arreglo, sum):
  arreglo.sort()
  print(arreglo)
  (menor, mayor) = (0, len(arreglo) - 1)
  while menor < mayor:
    if arreglo[menor]+arreglo[mayor] == sum:
      print((arreglo[menor],arreglo[mayor]))
    if arreglo[menor] + arreglo[mayor] < sum:
      menor = menor + 1
    else:
      mayor = mayor - 1

def main():
  df = pd.DataFrame(columns = ["n", "suma", "t_lineal", "t_constante"])
  n = []
  t_lineal= []
  t_constante = []
  suma = []
  
  arreglo = [1,9,5,0,20,-4,12,16,7]
  sum = 12
  for i in buscar_suma(arreglo, sum):
    print (i)
  t0=time.perf_counter()
  print(t0)
  print("---------------------------------")
  print(parejas(arreglo, sum))
  t1=time.perf_counter()
  print(t1)

  n.append(parejas(arreglo,sum))
  #t_lineal.append(t1-t0)
  #t_constante.append(t2-t1)
  #suma.append(suma1)
  
  df['n'] = n
  df['suma'] = suma
  df['t_lineal'] = t_lineal
  df['t_constante'] = t_constante

  df.plot(x='n', y=['t_lineal', 't_constante'])
  plt.show()

if __name__ == "__main__":
  main()

