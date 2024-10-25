from collections.abc import Callable
from typing import Any, Generic, Optional, TypeVar
from functools import wraps
from copy import copy
from funciones_grafico import grafico_arbol_binario

T = TypeVar('T')

class NodoAB(Generic[T]):
    # Inicializador de la clase
    def __init__(self, dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None):
        # Almacena el dato en el nodo
        self.dato = dato
        # Inicializa el subárbol izquierdo (si) o crea un nuevo ArbolBinario si no se proporciona
        self.si: ArbolBinario[T] = ArbolBinario() if (si is None) else si
        # Inicializa el subárbol derecho (sd) o crea un nuevo ArbolBinario si no se proporciona
        self.sd: ArbolBinario[T] = ArbolBinario() if (sd is None) else sd

    def __str__(self):
        # Devuelve el dato del nodo como una cadena (dato)
        return self.dato
    
class ArbolBinario(Generic[T]):
    def __init__(self):
        # La raíz del árbol se inicializa como None, indicando que el árbol está vacío
        self.raiz: Optional[NodoAB[T]] = None
        
    class _Decoradores:
        
        @classmethod
        def valida_es_vacio(cls, f: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(f) # Mantiene la metadata del método original
            def wrapper(self, *args: Any, **kwargs: Any) -> Any:
                if self.es_vacio():
                    raise TypeError('Arbol Vacio')
                return f(self, *args, **kwargs) # Llama al método original si no está vacío
            return wrapper
        
    @staticmethod
    def crear_nodo(dato: T, si: "Optional[ArbolBinario[T]]" = None, sd: "Optional[ArbolBinario[T]]" = None) -> "ArbolBinario[T]":
        t = ArbolBinario() # Crea una nueva instancia de ArbolBinario
        t.raiz = NodoAB(dato, si, sd) # Asigna un nuevo nodo a la raíz con los subárboles proporcionados
        return t

    def es_vacio(self) -> bool:
        # Retorna True si la raíz del arbol es None
        return self.raiz is None
    
    @_Decoradores.valida_es_vacio # Aplica el decorador para validar si el árbol está vacío (si no tiene raiz)
    def si(self) -> "ArbolBinario[T]":
        # funcion que devuelve el subarbol izquierdo
        assert self.raiz is not None  # Asegura que la raíz no sea None
        return self.raiz.si  # Retorna el subárbol izquierdo
    
    @_Decoradores.valida_es_vacio # Aplica el decorador para validar si el árbol está vacío (si no tiene raiz)
    def sd(self) -> "ArbolBinario[T]":
        # funcion que devuelve el subarbol derecho
        assert self.raiz is not None  # Asegura que la raíz no sea None
        return self.raiz.sd  # Retorna el subárbol derecho
    
    # Método para verificar si el nodo es una hoja (sin hijos)
    def es_hoja(self) -> bool:
        # verifica que el nodo tenga una raiz y que no tenga subarboles izquierdo y derecho
        return not self.es_vacio() and self.si().es_vacio() and self.sd().es_vacio()

    @_Decoradores.valida_es_vacio # Aplica el decorador para validar si el árbol está vacío (si no tiene raiz)
    def dato(self) -> T:
        assert self.raiz is not None  # Asegura que la raíz no sea None
        return self.raiz.dato  # Retorna el dato del nodo raíz
    
    @_Decoradores.valida_es_vacio # Aplica el decorador para validar si el árbol está vacío (si no tiene raiz)
    def insertar_si(self, si: "ArbolBinario[T]"):
        assert self.raiz is not None  # Asegura que la raíz no sea None
        self.raiz.si = si  # Asigna un nuevo subárbol izquierdo

    @_Decoradores.valida_es_vacio # Aplica el decorador para validar si el árbol está vacío (si no tiene raiz)
    def insertar_sd(self, sd: "ArbolBinario[T]"):
        assert self.raiz is not None  # Asegura que la raíz no sea None
        self.raiz.sd = sd  # Asigna un nuevo subárbol derecho
    
    # Método para establecer la raíz del árbol con un nodo dado
    def set_raiz(self, nodo: NodoAB[T]):
        self.raiz = nodo
    
    # Método para calcular la altura del árbol (número de niveles)
    def altura(self) -> int:
        if self.es_vacio():
            return 0 # La altura de un árbol vacío es 0
        else:
            return 1 + max(self.si().altura(), self.sd().altura()) # Altura = 1 + altura del subárbol más alto
    
    # Método especial para obtener la cantidad de nodos en el árbol (longitud)
    def __len__(self) -> int:
        if self.es_vacio():
            return 0 # Si está vacío, retorna longitud 0
        else:
            return 1 + len(self.si()) + len(self.sd()) # Cuenta los nodos en los subárboles y el de la raiz
    
    def __str__(self):
        def mostrar(t: ArbolBinario[T], nivel: int):
            tab = '.' * 4
            indent = tab * nivel
            if t.es_vacio():
                return indent + 'AV\n'
            else:
                out = indent + str(t.dato()) + '\n'
                out += mostrar(t.si(), nivel + 1)
                out += mostrar(t.sd(), nivel + 1)
                return out   
        return mostrar(self, 0)

    def inorder(self) -> list[T]:
        if self.es_vacio():
            return []
        else:
            return self.si().inorder() + [self.dato()] + self.sd().inorder()
    
    def inorder_tail(self) -> list[T]:
        pass

    def preorder(self) -> list[T]:
        pass

    def posorder(self) -> list[T]:
        pass

    def bfs(self) -> list[T]:
        """Devuelve los nodos organizados por niveles en una sola lista usando BFS recursivo."""
        def recorrer(arbol: ArbolBinario[T], nivel = 0, diccionario = {}):
            if arbol.es_vacio():
                return
            if not arbol.es_vacio():
                if nivel in diccionario:
                    diccionario[nivel].append(arbol.dato())
                else:
                    diccionario[nivel] = [arbol.dato()]
                recorrer(arbol.si(), nivel + 1, diccionario)
                recorrer(arbol.sd(), nivel + 1, diccionario)
                           
        niveles = {}
        recorrer(self, 1, niveles)
        return [valor for lista in niveles.values() for valor in lista]

    def nivel(self, x: T) -> int:
        """Dado un valor, regrese el nivel en el que se encuentra en caso de no encontrar debe retornar un valor superior ala altura del arbol."""
        def recorrer(arbol: ArbolBinario[T], nivel = 0, diccionario = {}):
            if arbol.es_vacio():
                return
            if not arbol.es_vacio():
                if arbol.dato() == x:
                    diccionario["existe"] = nivel
                    return
                else:
                    diccionario["no existe"] = nivel + 2
                recorrer(arbol.si(), nivel + 1, diccionario)
                recorrer(arbol.sd(), nivel + 1, diccionario)
                           
        busqueda = {}
        recorrer(self, 1, busqueda)
        return busqueda['existe'] if "existe" in busqueda else busqueda["no existe"]
    def copy(self) -> "ArbolBinario[T]":
        if self.es_vacio():
            return ArbolBinario()
        else:
            arbol = ArbolBinario.crear_nodo(copy(self.dato()))
            arbol.insertar_si(self.si().copy())
            arbol.insertar_sd(self.sd().copy())
            return arbol

    def espejo(self) -> "ArbolBinario[T]":
        pass
        
    def sin_hojas(self):
        pass

    def graficar_arbol(self):
        def arbol_a_diccionario(arbol: ArbolBinario[T]) -> Optional[dict]:
            if arbol.es_vacio():
                return None
            return {
                'value': arbol.dato(),
                'left': arbol_a_diccionario(arbol.si()),
                'right': arbol_a_diccionario(arbol.sd())
            }
        binary_tree = arbol_a_diccionario(self) #Obtengo el diccionario
        grafico_arbol_binario(binary_tree)

def main():
    t = ArbolBinario.crear_nodo(1)
    n2 = ArbolBinario.crear_nodo(2)
    n3 = ArbolBinario.crear_nodo(3)
    n4 = ArbolBinario.crear_nodo(4)
    n5 = ArbolBinario.crear_nodo(5)
    n6 = ArbolBinario.crear_nodo(6)
    n7 = ArbolBinario.crear_nodo(7)
    n8 = ArbolBinario.crear_nodo(8)
    n2.insertar_si(n4)
    n2.insertar_sd(n5)
    n5.insertar_si(n8)
    n3.insertar_si(n6)
    n3.insertar_sd(n7)
    t.insertar_si(n2)
    t.insertar_sd(n3)
    
    #print(t)
    #t.graficar_arbol()
    print(f'Altura: {t.altura()}')
    print(f'Nodos: {len(t)}')
    print(f'BFS: {t.bfs()}')
    print(f'Nivel de 8: {t.nivel(8)}')
    t2 = t.copy()
    #print(t2)
    t2.graficar_arbol()
    """


    print(f'DFS inorder stack: {t2.inorder()}')
    print(f'DFS inorder tail:  {t2.inorder_tail()}')
    print(f'Nivel de 8: {t2.nivel(8)}')
    t3 = t2.espejo()
    print(t3)
    print(t3.sin_hojas())
    """

if __name__ == '__main__':
    main()