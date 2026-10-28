"""
Demostración y Benchmark de Algoritmos sobre Estructuras Desarrolladas:
- Burbuja, Inserción, QuickSort
- Búsqueda Lineal y Binaria
Aplicado a Pacientes y Estructuras (ListaEnlazada y Arreglos)
"""
import random
import time
from models import Paciente
from data_structures import ListaEnlazada
from algorithms import (
    ordenamiento_burbuja,
    ordenamiento_insercion,
    ordenamiento_quicksort,
    busqueda_lineal,
    busqueda_binaria
)

def generar_pacientes(n: int):
    nombres = ["Ana", "Carlos", "Beatriz", "David", "Elena", "Fernando", "Gloria", "Hugo", "Irene", "Juan"]
    sintomas = ["Fiebre", "Trauma", "Dolor toracico", "Cefalea", "Disnea", "Fractura", "Quemadura"]
    pacientes = []
    for i in range(1, n + 1):
        pacientes.append(Paciente(
            id_paciente=i,
            nombre=f"{random.choice(nombres)}_{i}",
            edad=random.randint(1, 90),
            prioridad=random.randint(1, 5),
            tiempo_espera_min=random.randint(0, 180),
            sintoma=random.choice(sintomas)
        ))
    return pacientes

def run_benchmarks():
    print("=" * 70)
    print("BENCHMARK DE ALGORITMOS SOBRE ESTRUCTURAS DESARROLLADAS")
    print("=" * 70)

    tamanos = [100, 500, 1000]
    for n in tamanos:
        pacientes = generar_pacientes(n)
        # Desordenar por tiempo de espera
        random.shuffle(pacientes)

        print(f"\n--- Probando con N = {n} pacientes (Ordenando por tiempo_espera_min) ---")

        # 1. Burbuja
        t0 = time.perf_counter()
        res_b, comp_b, swaps_b = ordenamiento_burbuja(pacientes, key=lambda p: p.tiempo_espera_min)
        t_burbuja = (time.perf_counter() - t0) * 1000
        print(f"Burbuja:    Tiempo: {t_burbuja:7.3f} ms | Comp: {comp_b:9d} | Swaps/Despl: {swaps_b:9d}")

        # 2. Inserción
        t0 = time.perf_counter()
        res_i, comp_i, swaps_i = ordenamiento_insercion(pacientes, key=lambda p: p.tiempo_espera_min)
        t_insercion = (time.perf_counter() - t0) * 1000
        print(f"Insercion:  Tiempo: {t_insercion:7.3f} ms | Comp: {comp_i:9d} | Swaps/Despl: {swaps_i:9d}")

        # 3. QuickSort
        t0 = time.perf_counter()
        res_q, comp_q, swaps_q = ordenamiento_quicksort(pacientes, key=lambda p: p.tiempo_espera_min)
        t_quick = (time.perf_counter() - t0) * 1000
        print(f"QuickSort:  Tiempo: {t_quick:7.3f} ms | Comp: {comp_q:9d} | Swaps/Despl: {swaps_q:9d}")

    # Búsquedas
    print("\n" + "=" * 70)
    print("COMPARACION DE BUSQUEDA LINEAL VS BUSQUEDA BINARIA")
    print("=" * 70)
    n_busqueda = 5000
    pacientes_busq = generar_pacientes(n_busqueda)
    # Ordenar por ID para búsqueda binaria
    pacientes_ordenados, _, _ = ordenamiento_quicksort(pacientes_busq, key=lambda p: p.id_paciente)

    objetivo_id = pacientes_busq[-1].id_paciente  # Peor caso o casi peor caso

    # Lineal
    t0 = time.perf_counter()
    idx_l, elem_l, comp_l = busqueda_lineal(pacientes_ordenados, objetivo_id, key=lambda p: p.id_paciente)
    t_lin = (time.perf_counter() - t0) * 1000
    print(f"Búsqueda Lineal  (N={n_busqueda}): Encontrado ID {objetivo_id} | Comp: {comp_l:5d} | Tiempo: {t_lin:.4f} ms")

    # Binaria
    t0 = time.perf_counter()
    idx_b, elem_b, comp_b = busqueda_binaria(pacientes_ordenados, objetivo_id, key=lambda p: p.id_paciente)
    t_bin = (time.perf_counter() - t0) * 1000
    print(f"Búsqueda Binaria (N={n_busqueda}): Encontrado ID {objetivo_id} | Comp: {comp_b:5d} | Tiempo: {t_bin:.4f} ms")

if __name__ == "__main__":
    run_benchmarks()
