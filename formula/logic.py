def calcular_propina(total, porcentaje):
    decimal = porcentaje / 100
    propina = decimal * total
    return propina

def calcular_total(total, propina):
    return total + propina

def dividir_total(total, personas):
    return total / personas