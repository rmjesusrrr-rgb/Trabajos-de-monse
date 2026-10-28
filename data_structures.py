"""
Implementación desde cero de Estructuras de Datos Básicas:
- Lista Enlazada Simple (Linked List)
- Pila (Stack - LIFO)
- Cola (Queue - FIFO)
- Cola de Prioridad (Priority Queue para Triage)
"""
from typing import Any, Optional, List, Generator

class Nodo:
    """Nodo elemental para estructuras enlazadas en memoria dinámica."""
    def __init__(self, dato: Any):
        self.dato = dato
        self.siguiente: Optional['Nodo'] = None

    def __repr__(self) -> str:
        return f"Nodo({self.dato})"


class ListaEnlazada:
    """Lista simplemente enlazada con soporte para operaciones básicas."""
    def __init__(self):
        self.cabeza: Optional[Nodo] = None
        self.tamanio: int = 0

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def agregar_al_inicio(self, dato: Any) -> None:
        """Inserción en la cabeza - O(1) tiempo."""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamanio += 1

    def agregar_al_final(self, dato: Any) -> None:
        """Inserción al final - O(n) tiempo sin puntero de cola."""
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamanio += 1

    def eliminar(self, criterio_func) -> Optional[Any]:
        """Elimina el primer nodo que cumpla con el criterio booleano - O(n)."""
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if criterio_func(actual.dato):
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamanio -= 1
                return actual.dato
            anterior = actual
            actual = actual.siguiente
        return None

    def a_lista(self) -> List[Any]:
        """Convierte la lista enlazada a una lista indexada nativa."""
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    def __len__(self) -> int:
        return self.tamanio

    def __iter__(self) -> Generator[Any, None, None]:
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Pila:
    """Pila (LIFO: Last-In, First-Out) implementada con nodos enlazados."""
    def __init__(self):
        self.tope: Optional[Nodo] = None
        self.tamanio: int = 0

    def esta_vacia(self) -> bool:
        return self.tope is None

    def apilar(self, dato: Any) -> None:
        """Push: Inserta un elemento en la cima - O(1)."""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamanio += 1

    def desapilar(self) -> Optional[Any]:
        """Pop: Extrae y retorna el elemento en la cima - O(1)."""
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return dato

    def ver_tope(self) -> Optional[Any]:
        """Peek: Retorna el elemento en la cima sin extraerlo - O(1)."""
        return None if self.esta_vacia() else self.tope.dato

    def __len__(self) -> int:
        return self.tamanio


class Cola:
    """Cola (FIFO: First-In, First-Out) implementada con punteros a frente y final."""
    def __init__(self):
        self.frente: Optional[Nodo] = None
        self.final: Optional[Nodo] = None
        self.tamanio: int = 0

    def esta_vacia(self) -> bool:
        return self.frente is None

    def encolar(self, dato: Any) -> None:
        """Enqueue: Inserta al final de la fila - O(1)."""
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.tamanio += 1

    def desencolar(self) -> Optional[Any]:
        """Dequeue: Extrae el elemento al frente de la fila - O(1)."""
        if self.esta_vacia():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamanio -= 1
        return dato

    def ver_frente(self) -> Optional[Any]:
        return None if self.esta_vacia() else self.frente.dato

    def __len__(self) -> int:
        return self.tamanio


class ColaPrioridad:
    """
    Cola de Prioridad ordenada para Triage Médico.
    Los elementos con menor valor numérico de prioridad (1 = Resucitación)
    se ubican antes en la cola. En caso de igual prioridad, se preserva FIFO (tiempo).
    """
    def __init__(self, key_prioridad=lambda x: x.prioridad):
        self.cabeza: Optional[Nodo] = None
        self.tamanio: int = 0
        self.key_prioridad = key_prioridad

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def encolar(self, dato: Any) -> None:
        """Inserción ordenada por severidad - O(n)."""
        nuevo = Nodo(dato)
        prio_nuevo = self.key_prioridad(dato)

        if self.esta_vacia() or prio_nuevo < self.key_prioridad(self.cabeza.dato):
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            # Mantener orden FIFO para igual prioridad (< en lugar de <=)
            while actual.siguiente is not None and self.key_prioridad(actual.siguiente.dato) <= prio_nuevo:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        self.tamanio += 1

    def desencolar(self) -> Optional[Any]:
        """Extrae el paciente más crítico - O(1)."""
        if self.esta_vacia():
            return None
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self.tamanio -= 1
        return dato

    def __len__(self) -> int:
        return self.tamanio

    def a_lista(self) -> List[Any]:
        res = []
        actual = self.cabeza
        while actual is not None:
            res.append(actual.dato)
            actual = actual.siguiente
        return res
