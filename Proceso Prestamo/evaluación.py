import pickle
from aprobados import aprobados
from rechazados import rechazados

clientes = []

def calcular_25_por_ciento(sueldo):
    return sueldo * 0.25

def calcular_cuota_mensual(monto, años):
    meses = años * 12
    return monto / meses

def guardar_datos():
    with open('aprobados.pkl', 'wb') as f:
        pickle.dump(aprobados, f)
    with open('rechazados.pkl', 'wb') as f:
        pickle.dump(rechazados, f)

def evaluar_clientes():
    for cliente in clientes:
        sueldo = cliente['sueldo']
        credito_solicitado = cliente['credito_solicitado']
        años_pagar = cliente['años_pagar']
        
        porcentaje_25 = calcular_25_por_ciento(sueldo)
        cuota_mensual = calcular_cuota_mensual(credito_solicitado, años_pagar)
        
        if cuota_mensual > porcentaje_25:
            rechazados.append(cliente)
            print(f"Préstamo rechazado para {cliente['nombres']} {cliente['apellidos']}. Cuota mensual: {cuota_mensual:.2f}, 25% del sueldo: {porcentaje_25:.2f}")
        else:
            aprobados.append(cliente)
            print(f"Préstamo aprobado para {cliente['nombres']} {cliente['apellidos']}. Cuota mensual: {cuota_mensual:.2f}, 25% del sueldo: {porcentaje_25:.2f}")

    guardar_datos()

if __name__ == "__main__":
    evaluar_clientes()
