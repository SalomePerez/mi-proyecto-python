"""
Sistema de Gestión de Notas de Estudiantes
===========================================

Este programa permite registrar las notas de un estudiante,
validarlas, calcular su promedio final y clasificar su rendimiento
según las reglas académicas establecidas.

Salome Perez Franco
Fecha: 24 de Noviembre 2025
Curso: Programación en Python - DevSenior
"""

# CONSTANTES GLOBALES

# Clasificación según promedio (0 - 5)
CLASIFICACIONES = {
    "Excelente": 4.5,
    "Sobresaliente": 4.0,
    "Aceptable": 3.0,
    "Insuficiente": 0.0
}

NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0


# FUNCIONES DE VALIDACIÓN

def validar_float(mensaje: str) -> float:
    while True:
        try:
            entrada = float(input(mensaje))

            if entrada < NOTA_MINIMA or entrada > NOTA_MAXIMA:
                print(f"ERROR: La nota debe estar entre {NOTA_MINIMA} y {NOTA_MAXIMA}.\n")
                continue

            return entrada

        except ValueError:
            print("ERROR: Debe ingresar un número válido.\n")


def validar_cantidad(mensaje: str) -> int:
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad <= 0:
                print("ERROR: La cantidad debe ser un número positivo.\n")
                continue
            return cantidad

        except ValueError:
            print("ERROR: Debe ingresar un número entero válido.\n")


# FUNCIONES DE LÓGICA

def calcular_promedio(notas: list[float]) -> float:
    return sum(notas) / len(notas)


def clasificar_promedio(promedio: float) -> str:
    """
    Determina la clasificación del estudiante según su promedio.
    """
    for categoria, minimo in CLASIFICACIONES.items():
        if promedio >= minimo:
            return categoria
    return "Sin clasificación"


# FUNCIONES DE PRESENTACIÓN

def mostrar_encabezado() -> None:
    """Muestra el encabezado principal del programa."""
    print("\n" + "="*60)
    print("       SISTEMA DE GESTIÓN DE NOTAS")
    print("="*60 + "\n")


def mostrar_resultado(notas: list[float], prom: float, clasif: str) -> None:
    """
    Presenta en pantalla los resultados finales del estudiante.
    """
    print("\n" + "-"*60)
    print("Resumen del estudiante")
    print("-"*60)

    print("\nNotas registradas:")
    for i, nota in enumerate(notas, start=1):
        print(f"  Nota {i}: {nota:.2f}")

    print("\n" + "-"*60)
    print(f"Promedio final: {prom:.2f}")
    print(f"Clasificación: {clasif}")
    print("-"*60 + "\n")


def preguntar_continuar() -> bool:
    """
    Pregunta si se desea evaluar otro estudiante.
    """
    while True:
        r = input("¿Desea evaluar otro estudiante? (s/n): ").strip().lower()

        if r in ["s", "si", "y", "yes"]:
            return True
        if r in ["n", "no"]:
            return False

        print("Por favor responda con 's' o 'n'.\n")


# FUNCIÓN PRINCIPAL

def main() -> None:
    """Controla el flujo principal del programa."""
    mostrar_encabezado()

    continuar = True

    while continuar:
        # Número de notas
        cantidad = validar_cantidad("¿Cuántas notas desea registrar?: ")

        # Registro de notas
        notas = []
        for i in range(1, cantidad + 1):
            nota = validar_float(f"Ingrese la nota {i}: ")
            notas.append(nota)

        # Cálculo
        prom = calcular_promedio(notas)
        clasif = clasificar_promedio(prom)

        # Mostrar resultados
        mostrar_resultado(notas, prom, clasif)

        # Continuar o salir
        continuar = preguntar_continuar()

    print("\nGracias por usar el sistema. ¡Hasta pronto!\n")


# PUNTO DE ENTRADA

if __name__ == "__main__":
    main()
