# Trabajos de Monse: Estructuras de Datos, Algoritmos y Complejidad Asintótica (Big-O)

Repositorio dedicado a la investigación teórica, desarrollo e instrumentación de algoritmos fundamentales de ciencias de la computación sobre estructuras de datos dinámicas y modelos orientados a objetos.

---

## 📚 Contenido del Proyecto

1. **Investigación Teórica en Cuaderno:**
   * Notación Asintótica: Big-O ($\mathcal{O}$), Big-Omega ($\Omega$), Big-Theta ($\Theta$).
   * Algoritmos de Ordenamiento: **Burbuja (Bubble Sort)**, **Inserción (Insertion Sort)** y **QuickSort**.
   * Algoritmos de Búsqueda: **Búsqueda Lineal** y **Búsqueda Binaria**.
   * Tabla Comparativa Integral de Complejidades Temporales y Espaciales.
2. **Implementaciones e Instrumentación de Métricas:**
   * Algoritmos instrumentados para contabilizar comparaciones, intercambios y tiempos de CPU.
   * Modelos de Dominio (`Paciente`) y Estructuras Desarrolladas (`ListaEnlazada`, `Pila`, `Cola`, `ColaPrioridad`).
3. **Benchmarks Empíricos vs Teóricos:**
   * Pruebas de escalabilidad con $N = 100, 500, 1000$ y $5000$ elementos.

---

## 🧠 1. Fundamentos Teóricos

### 1.1 Notación Asintótica y Notación Big-O ($\mathcal{O}$)
La **Notación Big-O** representa el límite superior asintótico del consumo de tiempo o memoria de un algoritmo a medida que el tamaño de entrada $n$ crece hacia el infinito ($n \to \infty$):
* **$\mathcal{O}(g(n))$ (Peor caso):** Cota superior. Garantiza que el algoritmo nunca tardará más de un factor proporcional a $g(n)$.
* **$\Omega(g(n))$ (Mejor caso):** Cota inferior.
* **$\Theta(g(n))$ (Caso ajustado):** Crecimiento exacto del algoritmo.

#### Jerarquía de Complejidades:
$$\mathcal{O}(1) < \mathcal{O}(\log n) < \mathcal{O}(n) < \mathcal{O}(n \log n) < \mathcal{O}(n^2) < \mathcal{O}(2^n) < \mathcal{O}(n!)$$

---

### 1.2 Algoritmos de Ordenamiento

#### 1. Ordenamiento Burbuja (Bubble Sort)
* **Mecanismo:** Recorre el arreglo repetidamente comparando elementos contiguos e intercambiándolos si están desordenados, haciendo que el valor mayor "flote" al final en cada iteración.
* **Optimización:** Bandera de corte temprano (`hubo_intercambio`). Si no se realizan intercambios en una pasada, termina en $\mathcal{O}(n)$.
* **Complejidad:** Mejor: $\mathcal{O}(n)$ | Promedio: $\mathcal{O}(n^2)$ | Peor: $\mathcal{O}(n^2)$.
* **Memoria:** $\mathcal{O}(1)$ (*in-place*). **Estable:** Sí.

#### 2. Ordenamiento por Inserción (Insertion Sort)
* **Mecanismo:** Divide la lista en una sección ordenada y otra por ordenar. En cada paso toma un elemento clave y desplaza los elementos mayores a la derecha para colocarlo en su posición exacta.
* **Ventaja:** Muy veloz en colecciones pequeñas o casi ordenadas.
* **Complejidad:** Mejor: $\mathcal{O}(n)$ | Promedio: $\mathcal{O}(n^2)$ | Peor: $\mathcal{O}(n^2)$.
* **Memoria:** $\mathcal{O}(1)$ (*in-place*). **Estable:** Sí.

#### 3. QuickSort (Ordenamiento Rápido)
* **Mecanismo:** Basado en **Divide y Vencerás**:
  1. Se selecciona un elemento pivote.
  2. Se particiona el arreglo (menores a la izquierda, mayores a la derecha).
  3. Se ordenan recursivamente los subarreglos resultantes.
* **Técnica de Mitigación:** Para evitar que degenere a $\mathcal{O}(n^2)$ en datos previamente ordenados o invertidos, se emplea selección de **pivote central** (`(bajo + alto) // 2`).
* **Complejidad:** Mejor: $\mathcal{O}(n \log n)$ | Promedio: $\mathcal{O}(n \log n)$ | Peor: $\mathcal{O}(n^2)$.
* **Memoria:** $\mathcal{O}(\log n)$ (pila de recursión). **Estable:** No.

---

### 1.3 Algoritmos de Búsqueda

#### 1. Búsqueda Lineal
* Inspecciona cada nodo/índice de forma consecutiva.
* **Aplicabilidad:** Estructuras no ordenadas y listas enlazadas dinámicas.
* **Complejidad:** $\mathcal{O}(n)$ en peor caso, $\mathcal{O}(1)$ en mejor caso.

#### 2. Búsqueda Binaria
* Aplica Divide y Vencerás sobre una colección previamente **ordenada** con acceso indexado $\mathcal{O}(1)$.
* Descarta la mitad del rango en cada comparación.
* **Complejidad:** $\mathcal{O}(\log n)$ en peor caso, $\mathcal{O}(1)$ en mejor caso.

---

### 1.4 Cuadro Sinóptico de Complejidades

| Algoritmo | Tiempo (Mejor) | Tiempo (Promedio) | Tiempo (Peor) | Espacio Auxiliar | Enfoque | ¿Estable? | ¿In-Place? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Burbuja** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Intercambio adyacente | Sí | Sí |
| **Inserción** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Inserción por desplazamiento | Sí | Sí |
| **QuickSort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(\log n)$ | Divide y Vencerás | No | Sí |
| **Búsqueda Lineal** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Secuencial | N/A | Sí |
| **Búsqueda Binaria** | $\mathcal{O}(1)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | Divide y Vencerás | N/A | Sí |

---

## 💻 2. Estructura del Repositorio

```text
Trabajos-de-monse/
│
├── algorithms.py           # Burbuja, Inserción, QuickSort, Selección, Búsqueda Lineal y Binaria
├── data_structures.py      # ListaEnlazada, Pila, Cola, ColaPrioridad
├── models.py               # Modelo de datos Paciente (Triage Hospitalario)
├── benchmark_algoritmos.py # Benchmark cuantitativo con recuento de operaciones
├── test_suite.py           # Suite de pruebas unitarias y validaciones
├── main.py                 # Simulación del caso de uso hospitalario
└── README.md               # Documentación e investigación teórica completa
```

---

## 📊 3. Resultados Experimentales del Benchmark

Resultados obtenidos al procesar registros del modelo `Paciente`:

### Ordenamiento
| Tamaño ($N$) | Algoritmo | Tiempo (ms) | Comparaciones | Intercambios / Desplazamientos |
| :---: | :---: | :---: | :---: | :---: |
| **$N = 100$** | Burbuja | $0.934\text{ ms}$ | $4{,}935$ | $2{,}195$ |
| | Inserción | $0.403\text{ ms}$ | $2{,}290$ | $2{,}195$ |
| | **QuickSort** | **$0.182\text{ ms}$** | **$670$** | **$367$** |
| **$N = 500$** | Burbuja | $28.347\text{ ms}$ | $124{,}597$ | $60{,}539$ |
| | Inserción | $10.200\text{ ms}$ | $61{,}035$ | $60{,}539$ |
| | **QuickSort** | **$1.426\text{ ms}$** | **$4{,}592$** | **$2{,}417$** |
| **$N = 1000$** | Burbuja | $116.479\text{ ms}$ | $499{,}094$ | $250{,}000$ |
| | Inserción | $46.238\text{ ms}$ | $250{,}994$ | $250{,}000$ |
| | **QuickSort** | **$2.896\text{ ms}$** | **$11{,}762$** | **$6{,}583$** |

### Búsqueda ($N = 5{,}000$ elementos)
* **Búsqueda Lineal:** $5{,}000$ comparaciones | $0.5099\text{ ms}$
* **Búsqueda Binaria:** **$13$ comparaciones** | **$0.0087\text{ ms}$** ($\approx 58\times$ más rápida)

---

## 🚀 4. Instrucciones de Ejecución

### Pruebas Unitarias
```bash
python test_suite.py
```

### Ejecutar Benchmarks Cuantitativos
```bash
python benchmark_algoritmos.py
```

### Ejecutar Simulación del Sistema Hospitalario
```bash
python main.py
```
