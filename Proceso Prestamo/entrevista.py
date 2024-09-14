import evaluación

def realizar_entrevista():
    nombre = input("Nombres: ")
    apellidos = input("Apellidos: ")
    dpi = input("DPI (números únicamente): ")
    trabajo = input("Trabajo: ")
    sueldo = float(input("Sueldo mensual: "))
    credito_solicitado = float(input("Crédito solicitado: "))
    años_pagar = int(input("Años en los que desea pagar: "))

    cliente = {
        'nombres': nombre,
        'apellidos': apellidos,
        'dpi': dpi,
        'trabajo': trabajo,
        'sueldo': sueldo,
        'credito_solicitado': credito_solicitado,
        'años_pagar': años_pagar
    }

    evaluación.clientes.append(cliente)
    print("Cliente registrado con éxito.")
