import pickle
from aprobados import aprobados
from clientesAprobados import clientes_aprobados

try:
    with open('clientes_desembolsados.pkl', 'rb') as f:
        clientes_aprobados = pickle.load(f)
except FileNotFoundError:
    clientes_aprobados = []

def guardar_clientes_desembolsados():
    with open('clientes_desembolsados.pkl', 'wb') as f:
        pickle.dump(clientes_aprobados, f)

def guardar_aprobados():
    with open('aprobados.pkl', 'wb') as f:
        pickle.dump(aprobados, f)

def mostrar_listado_aprobados():
    if not aprobados:
        print("No hay clientes aprobados.")
        return

    print("\nListado de clientes aprobados:")
    for idx, cliente in enumerate(aprobados, 1):
        print(f"{idx}. {cliente['nombres']} {cliente['apellidos']} - Crédito: ${cliente['credito_solicitado']} - Años: {cliente['años_pagar']}")

def seleccionar_cliente():
    while True:
        try:
            seleccion = int(input("\nSeleccione el número del cliente al que se le va a desembolsar el préstamo: "))
            if 1 <= seleccion <= len(aprobados):
                cliente_seleccionado = aprobados[seleccion - 1]
                return cliente_seleccionado, seleccion - 1 
            else:
                print("Número de cliente inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")

def realizar_desembolso(cliente, indice):

    clientes_aprobados.append(cliente)
    guardar_clientes_desembolsados()


    del aprobados[indice]
    guardar_aprobados()

    print(f"\nSe ha aprobado el préstamo para {cliente['nombres']} {cliente['apellidos']} por ${cliente['credito_solicitado']} durante {cliente['años_pagar']} años.")

def main():
    mostrar_listado_aprobados()
    if aprobados:
        cliente_seleccionado, indice = seleccionar_cliente()
        realizar_desembolso(cliente_seleccionado, indice)

if __name__ == "__main__":
    main()