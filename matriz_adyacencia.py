from typing import Generic, TypeVar
from funciones_grafico import grafico_grafo
T = TypeVar('T')

class MatrizAdyacencia(Generic[T]):
  def __init__(self) -> None:
    self.matriz_adyacencia: list[list[int]] = []
    self.nodos: set[T] = set()
  
  def index_nodo(self, nodo) -> int:
    return list(self.nodos).index(nodo)

  def agregar_nodo(self, nodo: T) -> None:
    if nodo in self.nodos:
      raise ValueError("Ya existe el nodo en la matriz")
    self.nodos.add(nodo)
    matriz = [ [0]*len(self.nodos) for _ in self.nodos]
    self.matriz_adyacencia = matriz
    
  def agregar_arista(self, origen: T, destino: T) -> None:
    if not origen in self.nodos:
      raise ValueError("No existe el nodo origen en la matriz")
    if not destino in self.nodos:
      raise ValueError("No existe el nodo destino en la matriz")
     
    pos_o = self.index_nodo(origen)
    pos_d = self.index_nodo(destino)
    self.matriz_adyacencia[pos_o][pos_d] = 1
    self.matriz_adyacencia[pos_d][pos_o]= 1
  
  def eliminar_arista(self, origen: T, destino: T) -> None:
    if not origen in self.nodos:
      raise ValueError("No existe el nodo origen en la matriz")
    if not destino in self.nodos:
      raise ValueError("No existe el nodo destino en la matriz")
    
    pos_o = self.index_nodo(origen)
    pos_d = self.index_nodo(destino)
    self.matriz_adyacencia[pos_o][pos_d] = 0
    self.matriz_adyacencia[pos_d][pos_o]= 0  
  def eliminar_nodo(self, nodo: T) -> None:
      if nodo not in self.nodos:
          raise ValueError("No existe el nodo en la matriz")
        
      pos_n = self.index_nodo(nodo)
      self.nodos.remove(nodo)
      self.matriz_adyacencia.pop(pos_n)
      for fila in self.matriz_adyacencia:
          fila.pop(pos_n)

  def es_vecino_de(self, nodo: T, otro_nodo: T) -> bool:
      if nodo not in self.nodos or otro_nodo not in self.nodos:
          raise ValueError("Uno o ambos nodos no existen en la matriz")
        
      pos_n = self.index_nodo(nodo)
      pos_otro = self.index_nodo(otro_nodo)
      return self.matriz_adyacencia[pos_n][pos_otro] == 1

  def vecinos_de(self, nodo: T) -> set[T]:
    if nodo not in self.nodos:
      raise ValueError("El nodo no existe en la matriz")
        
    pos_n = self.index_nodo(nodo)
    vecinos = set()
    for idx, valor in enumerate(self.matriz_adyacencia[pos_n]):
      if valor == 1:
        vecinos.add(list(self.nodos)[idx])
      return vecinos
    
  def mostrar_matriz(self):
    print("   ", end='')
    for nodo in self.nodos:
      print(nodo, end=" ")
    print()
    max_longitud_fila = max(len(fila) for fila in self.matriz_adyacencia)
    for i, fila in enumerate(self.matriz_adyacencia):
      fila_str = str(list(self.nodos)[i]) + ": "
      for elemento in fila:
        fila_str += str(elemento) + " "
      print(fila_str.ljust(max_longitud_fila*2))

  def mostrar(self):
    grafico_grafo(self.matriz_adyacencia, list(self.nodos))
      
if __name__ == '__main__':
  m = MatrizAdyacencia()
  m.agregar_nodo(1)
  m.agregar_nodo(2)
  m.agregar_nodo(3)
  m.agregar_nodo(4)
  m.agregar_nodo(5)
  
  m.agregar_arista(1,2)
  m.agregar_arista(2,3)
  m.agregar_arista(3,4)
  m.agregar_arista(4,1)
  m.agregar_arista(1,5)
  m.agregar_arista(2,5)
  m.agregar_arista(3,5)
  m.agregar_arista(4,5)

  m.mostrar()
  
  m.eliminar_nodo(3)
  
  print("Vecinos de 2:", m.vecinos_de(2))

  m.mostrar()