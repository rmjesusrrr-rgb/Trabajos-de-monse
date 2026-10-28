"""
Modelos de dominio para el Sistema de Gestión de Urgencias y Triage Hospitalario.
"""
from dataclasses import dataclass

@dataclass
class Paciente:
    id_paciente: int
    nombre: str
    edad: int
    prioridad: int  # 1: Resucitación (Rojo), 2: Emergencia (Naranja), 3: Urgente (Amarillo), 4: Menor (Verde), 5: No urgente (Azul)
    tiempo_espera_min: int
    sintoma: str

    def __repr__(self) -> str:
        prioridades_str = {
            1: "Nivel 1 (Crítico/Rojo)",
            2: "Nivel 2 (Emergencia/Naranja)",
            3: "Nivel 3 (Urgente/Amarillo)",
            4: "Nivel 4 (Menor/Verde)",
            5: "Nivel 5 (No Urgente/Azul)"
        }
        p_str = prioridades_str.get(self.prioridad, f"Nivel {self.prioridad}")
        return f"[ID:{self.id_paciente:04d} | {self.nombre:<14} | {p_str:<25} | Espera: {self.tiempo_espera_min:>2}m | {self.sintoma}]"
