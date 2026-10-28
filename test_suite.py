"""
Suite de Pruebas Unitarias y Benchmarks de Rendimiento
Para el Sistema de Gestión de Urgencias y Triage Hospitalario.
"""
import random
import time
from models import Paciente
from data_structures import ListaEnlazada, Pila, Cola, ColaPrioridad
from algorithms import (
    ordenamiento_burbuja,
    ordenamiento_seleccion,
    ordenamiento_insercion,
    ordenamiento_quicksort,
    busqueda_lineal,
    busqueda_binaria
)

def test_estructuras_datos():
    print("=== [1] PRUEBAS DE ESTRUCTURAS DE DATOS ===")
    
    # 1. Pila (Stack)
    pila = Pila()
    pila.apilar("Accion A: Asignar Cama 101")
    pila.apilar("Accion B: Inyectar Analgesico")
    pila.apilar("Accion C: Traslado a Rayos X")
    assert len(pila) == 3
    assert pila.desapilar() == "Accion C: Traslado a Rayos X"
    assert pila.ver_tope() == "Accion B: Inyectar Analgesico"
    assert len(pila) == 2
    print("  [OK] Pila (LIFO)")

    # 2. Cola (Queue)
    cola = Cola()
    cola.encolar("Paciente 1")
    cola.encolar("Paciente 2")
    cola.encolar("Paciente 3")
    assert len(cola) == 3
    assert cola.desencolar() == "Paciente 1"
    assert cola.ver_frente() == "Paciente 2"
    assert len(cola) == 2
    print("  [OK] Cola (FIFO)")

    # 3. Lista Enlazada
    lista = ListaEnlazada()
    lista.agregar_al_final(10)
    lista.agregar_al_final(20)
    lista.agregar_al_inicio(5)
    assert lista.a_lista() == [5, 10, 20]
    eliminado = lista.eliminar(lambda x: x == 10)
    assert eliminado == 10
    assert lista.a_lista() == [5, 20]
    print("  [OK] Lista Enlazada")

    # 4. Cola de Prioridad (Triage)
    cp = ColaPrioridad(key_prioridad=lambda p: p.prioridad)
    p1 = Paciente(1, "Carlos Gomez", 45, 4, 30, "Esguince de tobillo")
    p2 = Paciente(2, "Maria Ruiz", 68, 1, 5, "Paro cardiorrespiratorio")
    p3 = Paciente(3, "Jorge Soto", 29, 2, 12, "Dolor toracico agudo")
    p4 = Paciente(4, "Ana Perez", 34, 4, 15, "Fiebre moderada")
    
    cp.encolar(p1)
    cp.encolar(p2)
    cp.encolar(p3)
    cp.encolar(p4)

    # El orden debe ser prioridad 1, luego 2, luego 4 (p1 antes de p4 por FIFO)
    atendido1 = cp.desencolar()
    atendido2 = cp.desencolar()
    atendido3 = cp.desencolar()
    atendido4 = cp.desencolar()

    assert atendido1.id_paciente == 2  # Prioridad 1
    assert atendido2.id_paciente == 3  # Prioridad 2
    assert atendido3.id_paciente == 1  # Prioridad 4 (llegó primero)
    assert atendido4.id_paciente == 4  # Prioridad 4
    print("  [OK] Cola de Prioridad (Triage Manchester)")


def test_algoritmos_ordenamiento_y_busqueda():
    print("\n=== [2] PRUEBAS DE ALGORITMOS ===")
    datos = [45, 12, 89, 34, 25, 7, 60]
    esperado = sorted(datos)

    # Burbuja
    b_res, b_comp, b_swaps = ordenamiento_burbuja(datos)
    assert b_res == esperado
    print(f"  [OK] Burbuja: Orden correcto. Comp={b_comp}, Swaps={b_swaps}")

    # Selección
    s_res, s_comp, s_swaps = ordenamiento_seleccion(datos)
    assert s_res == esperado
    print(f"  [OK] Selección: Orden correcto. Comp={s_comp}, Swaps={s_swaps}")

    # Inserción
    i_res, i_comp, i_swaps = ordenamiento_insercion(datos)
    assert i_res == esperado
    print(f"  [OK] Inserción: Orden correcto. Comp={i_comp}, Desplazamientos={i_swaps}")

    # QuickSort
    q_res, q_comp, q_swaps = ordenamiento_quicksort(datos)
    assert q_res == esperado
    print(f"  [OK] QuickSort: Orden correcto. Comp={q_comp}, Intercambios={q_swaps}")

    # Búsqueda Lineal
    idx_lin, val_lin, comp_lin = busqueda_lineal(datos, 89)
    assert val_lin == 89 and idx_lin == 2
    print(f"  [OK] Búsqueda Lineal: Elemento 89 hallado en índice {idx_lin} con {comp_lin} comparaciones.")

    # Búsqueda Binaria
    idx_bin, val_bin, comp_bin = busqueda_binaria(esperado, 89)
    assert val_bin == 89 and idx_bin == 6
    print(f"  [OK] Búsqueda Binaria: Elemento 89 hallado en índice {idx_bin} con {comp_bin} comparaciones.")


def benchmark_algoritmos():
    print("\n=== [3] BENCHMARK Y EVALUACIÓN DE COMPLEJIDAD ===")
    tamanos = [50, 200, 800]
    
    print(f"{'N':>5} | {'Algoritmo':<12} | {'Tiempo (ms)':>11} | {'Comparaciones':>14} | {'Intercambios':>13}")
    print("-" * 65)

    for n in tamanos:
        random.seed(42)
        base = [random.randint(1, 10000) for _ in range(n)]

        # Burbuja
        t0 = time.perf_counter()
        _, b_comp, b_swaps = ordenamiento_burbuja(base)
        t_burbuja = (time.perf_counter() - t0) * 1000

        # Selección
        t0 = time.perf_counter()
        _, s_comp, s_swaps = ordenamiento_seleccion(base)
        t_seleccion = (time.perf_counter() - t0) * 1000

        # Inserción
        t0 = time.perf_counter()
        _, i_comp, i_swaps = ordenamiento_insercion(base)
        t_insercion = (time.perf_counter() - t0) * 1000

        print(f"{n:>5} | {'Burbuja':<12} | {t_burbuja:>11.3f} | {b_comp:>14} | {b_swaps:>13}")
        print(f"{n:>5} | {'Selección':<12} | {t_seleccion:>11.3f} | {s_comp:>14} | {s_swaps:>13}")
        print(f"{n:>5} | {'Inserción':<12} | {t_insercion:>11.3f} | {i_comp:>14} | {i_swaps:>13}")
        print("-" * 65)

    print("\n=== [4] BENCHMARK BÚSQUEDA (LINEAL VS BINARIA, N=1000) ===")
    n = 1000
    datos_ord = sorted([random.randint(1, 50000) for _ in range(n)])
    objetivo_existente = datos_ord[n // 2]
    objetivo_inexistente = -999

    # Lineal existente
    _, _, comp_lin_ex = busqueda_lineal(datos_ord, objetivo_existente)
    # Binaria existente
    _, _, comp_bin_ex = busqueda_binaria(datos_ord, objetivo_existente)
    # Lineal inexistente
    _, _, comp_lin_in = busqueda_lineal(datos_ord, objetivo_inexistente)
    # Binaria inexistente
    _, _, comp_bin_in = busqueda_binaria(datos_ord, objetivo_inexistente)

    print(f"Elemento Medio ({objetivo_existente}):  Lineal = {comp_lin_ex} comp  vs  Binaria = {comp_bin_ex} comp")
    print(f"Elemento Inexistente ({objetivo_inexistente}): Lineal = {comp_lin_in} comp  vs  Binaria = {comp_bin_in} comp")

if __name__ == "__main__":
    test_estructuras_datos()
    test_algoritmos_ordenamiento_y_busqueda()
    benchmark_algoritmos()
