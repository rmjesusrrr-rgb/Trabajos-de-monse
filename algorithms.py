"""
Implementación desde cero de Algoritmos de Ordenamiento y Búsqueda con métricas de rendimiento:
- Ordenamiento Burbuja (Bubble Sort)
- Ordenamiento por Selección (Selection Sort)
- Ordenamiento por Inserción (Insertion Sort)
- Búsqueda Lineal (Linear Search)
- Búsqueda Binaria (Binary Search)
"""
from typing import List, Any, Callable, Tuple, Optional

# ============================================================================
# ALGORITMOS DE ORDENAMIENTO
# ============================================================================

def ordenamiento_burbuja(
    arr: List[Any],
    key: Callable[[Any], Any] = lambda x: x,
    reverse: bool = False
) -> Tuple[List[Any], int, int]:
    """
    Ordenamiento Burbuja con bandera de corte temprano.
    Retorna: (arreglo_ordenado, comparaciones, intercambios)
    """
    a = list(arr)
    n = len(a)
    comparaciones = 0
    intercambios = 0

    for i in range(n):
        hubo_intercambio = False
        for j in range(0, n - i - 1):
            comparaciones += 1
            condicion = (key(a[j]) < key(a[j + 1])) if reverse else (key(a[j]) > key(a[j + 1]))
            if condicion:
                # Intercambio de 3 pasos en memoria
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                intercambios += 1
                hubo_intercambio = True
        if not hubo_intercambio:
            break

    return a, comparaciones, intercambios


def ordenamiento_seleccion(
    arr: List[Any],
    key: Callable[[Any], Any] = lambda x: x,
    reverse: bool = False
) -> Tuple[List[Any], int, int]:
    """
    Ordenamiento por Selección.
    Retorna: (arreglo_ordenado, comparaciones, intercambios)
    """
    a = list(arr)
    n = len(a)
    comparaciones = 0
    intercambios = 0

    for i in range(n):
        idx_extremo = i
        for j in range(i + 1, n):
            comparaciones += 1
            condicion = (key(a[j]) > key(a[idx_extremo])) if reverse else (key(a[j]) < key(a[idx_extremo]))
            if condicion:
                idx_extremo = j

        if idx_extremo != i:
            # Un solo intercambio por pasada externa
            temp = a[i]
            a[i] = a[idx_extremo]
            a[idx_extremo] = temp
            intercambios += 1

    return a, comparaciones, intercambios


def ordenamiento_insercion(
    arr: List[Any],
    key: Callable[[Any], Any] = lambda x: x,
    reverse: bool = False
) -> Tuple[List[Any], int, int]:
    """
    Ordenamiento por Inserción.
    Retorna: (arreglo_ordenado, comparaciones, desplazamientos)
    """
    a = list(arr)
    n = len(a)
    comparaciones = 0
    desplazamientos = 0

    for i in range(1, n):
        clave_elem = a[i]
        clave_val = key(clave_elem)
        j = i - 1

        while j >= 0:
            comparaciones += 1
            condicion = (key(a[j]) < clave_val) if reverse else (key(a[j]) > clave_val)
            if condicion:
                a[j + 1] = a[j]
                desplazamientos += 1
                j -= 1
            else:
                break
        a[j + 1] = clave_elem

    return a, comparaciones, desplazamientos


def ordenamiento_quicksort(
    arr: List[Any],
    key: Callable[[Any], Any] = lambda x: x,
    reverse: bool = False
) -> Tuple[List[Any], int, int]:
    """
    Ordenamiento Rápido (QuickSort) con particionamiento in-place (Lomuto).
    Estrategia Divide y Vencerás.
    Retorna: (arreglo_ordenado, comparaciones, intercambios)
    """
    a = list(arr)
    comparaciones = 0
    intercambios = 0

    def _partition(bajo: int, alto: int) -> int:
        nonlocal comparaciones, intercambios
        # Estrategia de pivote central para evitar el peor caso O(n^2) en datos ordenados
        medio = (bajo + alto) // 2
        a[medio], a[alto] = a[alto], a[medio]
        intercambios += 1

        pivote_val = key(a[alto])
        i = bajo - 1

        for j in range(bajo, alto):
            comparaciones += 1
            condicion = (key(a[j]) > pivote_val) if reverse else (key(a[j]) < pivote_val)
            if condicion:
                i += 1
                if i != j:
                    a[i], a[j] = a[j], a[i]
                    intercambios += 1

        if i + 1 != alto:
            a[i + 1], a[alto] = a[alto], a[i + 1]
            intercambios += 1
        return i + 1

    def _quicksort_rec(bajo: int, alto: int):
        if bajo < alto:
            pi = _partition(bajo, alto)
            _quicksort_rec(bajo, pi - 1)
            _quicksort_rec(pi + 1, alto)

    if len(a) > 1:
        _quicksort_rec(0, len(a) - 1)

    return a, comparaciones, intercambios


# ============================================================================
# ALGORITMOS DE BÚSQUEDA
# ============================================================================

def busqueda_lineal(
    arr: List[Any],
    valor_buscado: Any,
    key: Callable[[Any], Any] = lambda x: x
) -> Tuple[Optional[int], Optional[Any], int]:
    """
    Búsqueda Lineal / Secuencial.
    Retorna: (indice_encontrado, elemento, comparaciones_realizadas)
    """
    comparaciones = 0
    for idx, elem in enumerate(arr):
        comparaciones += 1
        if key(elem) == valor_buscado:
            return idx, elem, comparaciones
    return None, None, comparaciones


def busqueda_binaria(
    arr_ordenado: List[Any],
    valor_buscado: Any,
    key: Callable[[Any], Any] = lambda x: x
) -> Tuple[Optional[int], Optional[Any], int]:
    """
    Búsqueda Binaria (Divide y Vencerás) sobre arreglo ordenado ascendentemente.
    Retorna: (indice_encontrado, elemento, comparaciones_realizadas)
    """
    inicio = 0
    fin = len(arr_ordenado) - 1
    comparaciones = 0

    while inicio <= fin:
        medio = (inicio + fin) // 2
        val_medio = key(arr_ordenado[medio])
        comparaciones += 1

        if val_medio == valor_buscado:
            return medio, arr_ordenado[medio], comparaciones
        elif val_medio < valor_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None, None, comparaciones
