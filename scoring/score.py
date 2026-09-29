#!/usr/bin/env python3
"""Puntuación ponderada y análisis de sensibilidad para una matriz de decisión.

Formato del CSV:
  - Primera columna: nombre de la opción.
  - Resto de columnas: criterios puntuados de 0 a 10 (10 = mejor para nosotros,
    también en criterios "inversos" como capital o dependencia de tiempo).
  - Una fila cuyo nombre es PESO define el peso de cada criterio.

Uso:
  python3 scoring/score.py scoring/modelos.csv
  python3 scoring/score.py scoring/nichos.csv --sin-sensibilidad
"""

import argparse
import csv
import random
import sys


def cargar(ruta):
    with open(ruta, newline="", encoding="utf-8") as f:
        filas = list(csv.reader(f))
    encabezado = filas[0]
    criterios = encabezado[1:]
    pesos = None
    opciones = []
    for fila in filas[1:]:
        if not fila or not fila[0].strip():
            continue
        valores = [float(v) for v in fila[1:]]
        if len(valores) != len(criterios):
            sys.exit(f"Fila con {len(valores)} valores, se esperaban {len(criterios)}: {fila[0]}")
        if fila[0].strip().upper() == "PESO":
            pesos = valores
        else:
            if any(v < 0 or v > 10 for v in valores):
                sys.exit(f"Puntajes fuera de rango 0-10 en: {fila[0]}")
            opciones.append((fila[0].strip(), valores))
    if pesos is None:
        sys.exit("Falta la fila PESO")
    return criterios, pesos, opciones


def puntuar(opciones, pesos):
    total = sum(pesos)
    return sorted(
        ((nombre, sum(p * v for p, v in zip(pesos, valores)) / total) for nombre, valores in opciones),
        key=lambda x: x[1],
        reverse=True,
    )


def tabla(resultados):
    lineas = ["| # | Opción | Puntaje ponderado (0-10) |", "|---|---|---|"]
    for i, (nombre, puntaje) in enumerate(resultados, 1):
        lineas.append(f"| {i} | {nombre} | {puntaje:.2f} |")
    return "\n".join(lineas)


def escenario(criterios, pesos_base, cambios):
    pesos = list(pesos_base)
    for criterio, peso in cambios.items():
        pesos[criterios.index(criterio)] = peso
    return pesos


def robustez(opciones, pesos, iteraciones=10000, ruido=1.0, semilla=42):
    """Perturba cada puntaje con ruido uniforme de ±ruido y cuenta cuántas veces gana cada opción."""
    rng = random.Random(semilla)
    victorias = {nombre: 0 for nombre, _ in opciones}
    for _ in range(iteraciones):
        perturbadas = [
            (nombre, [min(10, max(0, v + rng.uniform(-ruido, ruido))) for v in valores])
            for nombre, valores in opciones
        ]
        ganador = puntuar(perturbadas, pesos)[0][0]
        victorias[ganador] += 1
    return sorted(((n, c / iteraciones) for n, c in victorias.items() if c), key=lambda x: x[1], reverse=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    parser.add_argument("--sin-sensibilidad", action="store_true")
    args = parser.parse_args()

    criterios, pesos, opciones = cargar(args.csv)
    print("## Ranking con pesos base\n")
    print("Pesos: " + ", ".join(f"{c}={p:g}" for c, p in zip(criterios, pesos)) + "\n")
    print(tabla(puntuar(opciones, pesos)))
    if args.sin_sensibilidad:
        return

    # Cada escenario: (criterios que necesita, pesos a aplicar). Si el CSV no tiene
    # esos criterios, el escenario se omite en lugar de degradar a pesos iguales.
    def enfatizar(claves, peso=3):
        return claves, {c: (peso if c in claves else 1) for c in criterios}

    escenarios = {
        "Pesos iguales": ((), {c: 1 for c in criterios}),
        "Prudente (castiga capital, dificultad y captación difícil)": (
            ("capital", "dificultad", "primeros_clientes"),
            {"capital": 2.5, "dificultad": 2, "primeros_clientes": 3},
        ),
        "Solo automatización + baja dependencia de tiempo": enfatizar(("automatizacion", "tiempo")),
        "Solo dinero (rentabilidad + escalabilidad + recurrencia)": enfatizar(
            ("rentabilidad", "escalabilidad", "recurrencia")
        ),
        "Prioriza competencia débil y bajo riesgo de plataforma": enfatizar(
            ("debilidad_competencia", "riesgo_plataforma")
        ),
        "Prioriza demanda probada y facilidad para llegar a clientes": enfatizar(
            ("demanda_probada", "alcance_clientes")
        ),
    }
    print("\n## Sensibilidad: ¿cambia el ganador si cambian los pesos?\n")
    print("| Escenario | 1.º | 2.º | 3.º |")
    print("|---|---|---|---|")
    for nombre, (requeridos, cambios) in escenarios.items():
        if not all(c in criterios for c in requeridos):
            continue
        top = puntuar(opciones, escenario(criterios, pesos, cambios))[:3]
        print(f"| {nombre} | " + " | ".join(f"{n} ({p:.2f})" for n, p in top) + " |")

    print("\n## Robustez: ruido de ±1 punto en cada puntaje (10.000 simulaciones)\n")
    print("| Opción | % de simulaciones en que queda 1.ª |")
    print("|---|---|")
    for nombre, frac in robustez(opciones, pesos):
        print(f"| {nombre} | {frac:.1%} |")


if __name__ == "__main__":
    main()
