from typing import Generic, TypeVar

T = TypeVar('T')

class GrafoAdyacencia(Generic[T]):
  def __init__(self) -> None:
    self.lista_adyacencia: dict[T, set[T]] = {}

  def agregar_nodo(self, nodo: T) -> None:
    if nodo in self.lista_adyacencia:
      raise ValueError("Ya existe el nodo en el grafo")
    self.lista_adyacencia[nodo] = set()
    
  def agregar_arista(self, origen: T, destino: T) -> None:
    if not origen in self.lista_adyacencia:
      raise ValueError("No existe el nodo origen en el grafo")
    if not destino in self.lista_adyacencia:
      raise ValueError("No existe el nodo destino en el grafo")
    self.lista_adyacencia[origen].add(destino)
    self.lista_adyacencia[destino].add(origen)
  
  def eliminar_arista(self, origen: T, destino: T) -> None:
    if not origen in self.lista_adyacencia:
      raise ValueError("No existe el nodo origen en el grafo")
    if not destino in self.lista_adyacencia:
      raise ValueError("No existe el nodo destino en el grafo")
    if not destino in self.lista_adyacencia[origen]:
      raise ValueError("No existe una arista entre los nodos")
        
    self.lista_adyacencia[origen].remove(destino)
    self.lista_adyacencia[destino].remove(origen)
  
  def eliminar_nodo(self, nodo: T) -> None:
    if not nodo in self.lista_adyacencia:
      raise ValueError("No existe el nodo a eliminar")
    adyacentes = list(self.lista_adyacencia[nodo])
    for adyacente in adyacentes:
      self.eliminar_arista(nodo, adyacente)
    del self.lista_adyacencia[nodo]
    
  def es_vecino_de(self, nodo: T, otro_nodo: T) -> bool:
    if not nodo in self.lista_adyacencia:
      raise ValueError("No existe el nodo en el grafo")
    if not otro_nodo in self.lista_adyacencia:
      raise ValueError("No existe el otro_nodo en el grafo")
    return otro_nodo in self.lista_adyacencia(nodo)
  def vecinos_de(self, nodo: T) -> set[T]:
    if not nodo in self.lista_adyacencia:
      raise ValueError("No existe el nodo en el grafo")
    return self.lista_adyacencia[nodo]
  def __str__(self):
    # Verificamos que el diccionario no esté vacío
    if not self.lista_adyacencia:
        return "El diccionario está vacío.\n"
    
    resultado = "GrafoAdyacencia\n"
    for clave, valor in self.lista_adyacencia.items():
        resultado += "\t" + str(clave) + ": " + str([dato for dato in valor]) + "\n"
    return resultado
  def ver_grafo(self):
    for key, values in self.lista_adyacencia.items():
      print(key,":", values)

if __name__ == '__main__':
  grafo = GrafoAdyacencia()
  grafo.agregar_nodo(1)
  grafo.agregar_nodo(2)
  grafo.agregar_nodo(3)
  grafo.agregar_nodo(4)
  grafo.agregar_nodo(5)
  grafo.agregar_arista(1,2)
  grafo.agregar_arista(1,3)
  grafo.agregar_arista(3,5)
  grafo.agregar_arista(3,4)
  grafo.agregar_arista(4, 2)
  grafo.agregar_arista(4, 1)
  grafo.agregar_arista(4, 5)
  grafo.eliminar_arista(5, 3)
  grafo.ver_grafo()
  grafo.eliminar_nodo(1)
  print("Eliminamos el nodo 1")
  grafo.ver_grafo()
  print("vecinos de 4:", grafo.vecinos_de(4))