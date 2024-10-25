from funciones_grafico import grafico_grafo_simple
from typing import Generic, TypeVar

T = TypeVar('T')


class Nodo(Generic[T]):
    def __init__(self, dato: T) -> None:
        self.dato = dato

    def __eq__(self, otro) -> bool:
        if otro is None or not isinstance(otro, Nodo):
            return False
        return self.dato == otro.dato

    def __hash__(self) -> int:
        return hash(self.dato)
      
    def __str__(self):
       return str(self.dato)
    def __repr__(self):
        return f"{self.dato}"

class Grafo(Generic[T]):
    def __init__(self) -> None:
        self.nodos: set[Nodo[T]] = set()
        self.aristas: set[tuple[Nodo[T], Nodo[T]]] = set()
        
    def agregar_nodo(self, nodo: Nodo[T]):
      if nodo in self.nodos:
        raise ValueError("El nodo ya se encuentra en el set.")
      self.nodos.add(nodo)
    
    def agregar_arista(self, origen: T, destino: T) -> None:
      if (origen, destino) in self.aristas or (destino, origen) in self.aristas:
        raise ValueError("La arista ya se encuentra en el set.")
      self.aristas.add((origen, destino))
    
    def eliminar_nodo(self, nodo: T) -> None:
      if not nodo in self.nodos:
        raise ValueError("No existe el nodo a eliminar")
      self.nodos = set(filter(lambda x: x.dato != nodo.dato, self.nodos))
      self.aristas = set(filter(lambda arista: not nodo in arista, self.aristas))
    
      
    def eliminar_arista(self, origen: T, destino: T) -> None:
      arista_eliminar = (origen, destino)
      arista_eliminar_r = (destino, origen)
      if not (arista_eliminar in self.aristas or arista_eliminar_r in self.aristas):
          raise ValueError("No existe la arista a eliminar.")
      self.aristas = set(filter(lambda arista: arista != arista_eliminar and arista != arista_eliminar_r, self.aristas))

      
    def es_vecino_de(self, nodo: T, otro_nodo: T) -> bool:
      return (nodo, otro_nodo) in self.aristas or (otro_nodo, nodo) in self.aristas
    
    def vecinos_de(self, nodo: T) -> set[T]:
      return set(map(lambda arista: arista[0] if arista[0]!=nodo else arista[1],filter(lambda arista: nodo in arista, self.aristas)))
    
    def ver_grafo(self):
      return f"nodos: {str(self.nodos)}\naristas: {str(self.aristas)}"
    def mostrar(self):
      grafico_grafo_simple(self.nodos, self.aristas)
    
if __name__ == '__main__':
  gs = Grafo()
  n1 = Nodo(1)
  n2 = Nodo(2)
  n3 = Nodo(3)
  n4 = Nodo(4)
  n5 = Nodo(5)
  n6 = Nodo(6)
  
  gs.agregar_nodo(n1)
  gs.agregar_nodo(n2)
  gs.agregar_nodo(n3)
  gs.agregar_nodo(n4)
  gs.agregar_nodo(n5)
  gs.agregar_nodo(n6)
  
  gs.agregar_arista(n1, n2)
  gs.agregar_arista(n2, n3)
  gs.agregar_arista(n3, n1)
  gs.agregar_arista(n3, n4)
  gs.agregar_arista(n4, n5)
  gs.agregar_arista(n5, n6)
  gs.agregar_arista(n6, n4)
  gs.mostrar()
  
  gs.eliminar_nodo(n1)
  print("Eliminamos nodo n1")
  print(gs.ver_grafo())
  
  print("Elminamos la arista (n2, n3)")
  gs.eliminar_arista(n2,n3)
  print(gs.ver_grafo())
  
  print("n4 es vecino de n3:", gs.es_vecino_de(n4, n3))
  
  print("Vecinos de n4:", gs.vecinos_de(n4))
  gs.mostrar()