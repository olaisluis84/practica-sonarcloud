def calcular_promedio(valores: list[float]) -> float:
    """Calcula el promedio de una lista de números.
    Retorna 0.0 si la lista está vacía.
    """
    if not valores:
        return 0.0
    return sum(valores) / len(valores)