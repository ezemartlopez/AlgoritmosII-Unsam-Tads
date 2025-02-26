from typing import TypeVar, Optional, Protocol
from arbol_binario import ArbolBinario, NodoAB

class Comparable(Protocol):
    def __lt__(self: 'T', otro: 'T') -> bool: ...
    def __le__(self: 'T', otro: 'T') -> bool: ...
    def __gt__(self: 'T', otro: 'T') -> bool: ...
    def __ge__(self: 'T', otro: 'T') -> bool: ...
    def __eq__(self: 'T', otro: 'T') -> bool: ...
    def __ne__(self: 'T', otro: 'T') -> bool: ...

T = TypeVar('T', bound=Comparable)


class NodoABO(NodoAB[T]):
    def __init__(self, dato: T):
        super().__init__(dato, ArbolBinarioOrdenado(), ArbolBinarioOrdenado())
    
    def __lt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato < otro.dato
    
    def __gt__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato > otro.dato

    def __eq__(self, otro: "NodoABO[T]") -> bool:
        return isinstance(otro, NodoABO) and self.dato == otro.dato
    
    
class ArbolBinarioOrdenado(ArbolBinario[T]):
    @staticmethod
    def crear_nodo(dato: T) -> "ArbolBinarioOrdenado[T]":
        nuevo = ArbolBinarioOrdenado()
        nuevo.set_raiz(NodoABO(dato))
        return nuevo
    
    def es_ordenado(self) -> bool:
        def es_ordenado_interna(
            arbol: "ArbolBinarioOrdenado[T]", 
            minimo: Optional[T] = None, 
            maximo: Optional[T] = None
        ) -> bool:
            if arbol.es_vacio():
                return True
            if (minimo is not None and arbol.dato() <= minimo) or (maximo is not None and arbol.dato() >= maximo):
                return False
            return es_ordenado_interna(arbol.si(), minimo, arbol.dato()) and es_ordenado_interna(arbol.sd(), arbol.dato(), maximo)
        
        return es_ordenado_interna(self)
    
    def insertar_si(self, arbol: "ArbolBinarioOrdenado[T]"):
        si = self.si()
        super().insertar_si(arbol)
        if not self.es_ordenado():
            super().insertar_si(si)
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")
    
    def insertar_sd(self, arbol: "ArbolBinarioOrdenado[T]"):
        sd = self.sd()
        super().insertar_sd(arbol)
        if not self.es_ordenado():
            super().insertar_sd(sd)
            raise ValueError("El árbol a insertar no es ordenado o viola la propiedad de orden del árbol actual")
    
    def insertar(self, valor: T):
        if self.es_vacio():
            self.set_raiz(NodoABO(valor))
        elif valor < self.dato():
            self.si().insertar(valor)
        else:
            self.sd().insertar(valor)
    def graficar_arbol(self):
        return super().graficar_arbol()
    def pertenece(self, valor: T) -> bool:
        if self.es_vacio():
            return False
        else:
            if self.dato() == valor:
                return True
            
            if self.dato() < valor:
                return self.sd().pertenece(valor)
            else:
                return self.si().pertenece(valor)
    def minimo(self) -> Optional[T]:
        if self.es_vacio():
            return None
        else:
            dato = self.dato()
            if self.es_hoja():
                return dato
            if self.si():
                return self.si().minimo()
                    
    def maximo(self) -> Optional[T]:
            if self.es_vacio():
                return None
            else:
                dato = self.dato()
                if self.es_hoja():
                    return dato
                if self.sd():
                    return self.sd().maximo() 
    def valores_menores_a(self, valor: T) -> list[T]:
        def recorrer(a: ArbolBinario[T], lista = []):
            if a.es_vacio():
                return []
            else:
                if a.dato() < valor:
                    lista.append(a.dato())
                if a.si():
                    recorrer(a.si(), lista)
                if a.sd():
                    recorrer(a.sd(), lista)
        lista = []
        recorrer(self, lista)
        return lista
            
    @staticmethod
    def convertir_ordenado(arbol_binario: ArbolBinario[T]) -> "ArbolBinarioOrdenado[T]":
        pass
        

def main():
    t: ArbolBinarioOrdenado[int] = ArbolBinarioOrdenado()
    t.insertar(10)
    t.insertar(5)
    t.insertar(15)
    t.insertar(2)
    t.insertar(7)
    t.insertar(12)
    t.insertar(17)
    t.insertar(20)
    t.insertar(13)
    print(t.es_ordenado())
    #print(t)

    t2: ArbolBinarioOrdenado[int] = ArbolBinarioOrdenado()
    t2.insertar(8)
    # t2.insertar(11)   # Descomentar para probar la excepción al violar el orden
    t2.insertar(6)
    t.insertar_si(t2)
    #print(t)
    t.graficar_arbol()
    print(f'Ordenado?: {t.es_ordenado()}')
    print(f'Tiene 12: {t.pertenece(12)}')
    print(f'minimo: {t.minimo()}')
    print(f'maximo: {t.maximo()}')
    print(f'Valores menores a 13: {t.valores_menores_a(13)}')
    """
    """

if __name__ == "__main__":
    main()