"""
Demostración del Caso Práctico:
Sistema de Gestión de Urgencias y Triage Hospitalario
"""
from models import Paciente
from data_structures import ListaEnlazada, Pila, ColaPrioridad
from algorithms import (
    ordenamiento_burbuja,
    ordenamiento_seleccion,
    ordenamiento_insercion,
    busqueda_lineal,
    busqueda_binaria
)

def ejecutar_simulacion():
    print("=" * 80)
    print("      SISTEMA DE GESTIÓN DE URGENCIAS Y TRIAGE HOSPITALARIO (SGU-TH)")
    print("=" * 80)

    # 1. Registro de pacientes en la Lista Enlazada
    registro_general = ListaEnlazada()
    pacientes_iniciales = [
        Paciente(1008, "Ana Morales", 34, 4, 25, "Cefalea leve y fiebre"),
        Paciente(1002, "Roberto Silva", 71, 1, 5, "Paro cardio-respiratorio"),
        Paciente(1015, "Clara Mendez", 28, 3, 40, "Fractura cerrada de muñeca"),
        Paciente(1005, "David Torres", 52, 2, 10, "Dolor precordial opresivo"),
        Paciente(1020, "Elena Vargas", 19, 5, 55, "Dolor de garganta"),
        Paciente(1003, "Felipe Castro", 63, 2, 18, "Dificultad respiratoria aguda"),
        Paciente(1011, "Gabriela Rios", 41, 3, 30, "Cólico renal agudo"),
    ]

    print("\n[PASO 1] Registrando pacientes entrantes en Lista Enlazada...")
    for p in pacientes_iniciales:
        registro_general.agregar_al_final(p)
    print(f"Total pacientes registrados en memoria: {len(registro_general)}")

    # 2. Cola de Prioridad para Atención Inmediata en Shock Room y Boxes
    print("\n[PASO 2] Asignando pacientes a la Cola de Prioridad (Protocolo de Triage)...")
    cola_triage = ColaPrioridad(key_prioridad=lambda p: (p.prioridad, -p.tiempo_espera_min))
    for p in registro_general:
        cola_triage.encolar(p)

    print("Orden de llamado médico según severidad y espera:")
    for idx, p in enumerate(cola_triage.a_lista(), 1):
        print(f"  {idx}. {p}")

    # 3. Pila para Auditoría y Deshacer de Asignaciones (Undo)
    print("\n[PASO 3] Flujo de atención y registro en Pila (LIFO) de auditoría:")
    pila_auditoria = Pila()
    
    # Atendemos los 2 pacientes más críticos
    for _ in range(2):
        paciente_atendido = cola_triage.desencolar()
        accion = f"Ingreso a Box de Reanimación: {paciente_atendido.nombre} (ID {paciente_atendido.id_paciente})"
        pila_auditoria.apilar(accion)
        print(f"  -> Atendiendo de inmediato: {paciente_atendido.nombre} [Nivel {paciente_atendido.prioridad}]")

    print(f"\nAcción en la cima de la Pila de auditoría: '{pila_auditoria.ver_tope()}'")
    accion_revertida = pila_auditoria.desapilar()
    print(f"Operación de Rollback/Deshacer ejecutada: Revertida '{accion_revertida}'")

    # 4. Ordenamiento para Reportes de Gestión Hospitalaria
    print("\n[PASO 4] Generación de Reportes mediante Algoritmos de Ordenamiento:")
    lista_pacientes = registro_general.a_lista()

    # A) Ordenamiento por Selección: Por Nivel de Gravedad (1 a 5)
    orden_gravedad, comp_s, swaps_s = ordenamiento_seleccion(
        lista_pacientes, key=lambda p: p.prioridad
    )
    print(f"\n--- A) Ordenados por Severidad (Selección) [Comp: {comp_s}, Swaps: {swaps_s}] ---")
    for p in orden_gravedad[:4]:
        print(f"  {p}")

    # B) Ordenamiento por Inserción: Por Tiempo de Espera Descendente
    orden_espera, comp_i, swaps_i = ordenamiento_insercion(
        lista_pacientes, key=lambda p: p.tiempo_espera_min, reverse=True
    )
    print(f"\n--- B) Ordenados por Mayor Tiempo de Espera (Inserción) [Comp: {comp_i}, Desplazamientos: {swaps_i}] ---")
    for p in orden_espera[:4]:
        print(f"  {p}")

    # C) Ordenamiento Burbuja: Por ID de Paciente (Ascendente) para indexación
    orden_id, comp_b, swaps_b = ordenamiento_burbuja(
        lista_pacientes, key=lambda p: p.id_paciente
    )
    print(f"\n--- C) Ordenados por ID de Paciente (Burbuja) [Comp: {comp_b}, Swaps: {swaps_b}] ---")
    for p in orden_id:
        print(f"  {p}")

    # 5. Algoritmos de Búsqueda
    print("\n[PASO 5] Búsquedas de Pacientes:")
    id_a_buscar = 1015
    print(f"Búsqueda Binaria por ID {id_a_buscar} sobre arreglo indexado:")
    idx, paciente_encontrado, comp_bin = busqueda_binaria(
        orden_id, id_a_buscar, key=lambda p: p.id_paciente
    )
    print(f"  -> Resultado: Encontrado en índice [{idx}] con SOLO {comp_bin} comparaciones: {paciente_encontrado.nombre}")

    sintoma_a_buscar = "Dificultad respiratoria aguda"
    print(f"\nBúsqueda Lineal por Síntoma '{sintoma_a_buscar}' sobre registro general no ordenado:")
    idx_l, p_sintoma, comp_lin = busqueda_lineal(
        lista_pacientes, sintoma_a_buscar, key=lambda p: p.sintoma
    )
    print(f"  -> Resultado: Encontrado en posición [{idx_l}] con {comp_lin} comparaciones: {p_sintoma.nombre}")

    print("\n" + "=" * 80)
    print("               SIMULACIÓN FINALIZADA EXITOSAMENTE")
    print("=" * 80)

if __name__ == "__main__":
    ejecutar_simulacion()
