import entrevista
import evaluación
import desembolso
from rechazados import rechazados
from aprobados import aprobados
import pickle

def mostrar_clientes_rechazados():
    if not rechazados:
        print("No hay clientes rechazados.")
        return

    print("\nListado de clientes rechazados:")
    for cliente in rechazados:
        print(f"{cliente['nombres']} {cliente['apellidos']} - Crédito: ${cliente['credito_solicitado']} - Años: {cliente['años_pagar']}")

def mostrar_clientes_aprobados():
    if not aprobados:
        print("No hay clientes aprobados.")
        return

    print("\nListado de clientes aprobados:")
    for cliente in aprobados:
        print(f"{cliente['nombres']} {cliente['apellidos']} - Crédito: ${cliente['credito_solicitado']} - Años: {cliente['años_pagar']}")


def mostrar_clientes_desembolsados():
    try:
        with open('clientes_desembolsados.pkl', 'rb') as f:
            clientes_desembolsados = pickle.load(f)
    except FileNotFoundError:
        clientes_desembolsados = []

    if not clientes_desembolsados:
        print("No hay clientes desembolsados.")
        return

    print("\nListado de clientes desembolsados:")
    for cliente in clientes_desembolsados:
        print(f"{cliente['nombres']} {cliente['apellidos']} - Crédito: ${cliente['credito_solicitado']} - Años: {cliente['años_pagar']}")

def menu():
    while True:
        print("\nOpciones:")
        print("1. Nuevo cliente")
        print("2. Mostrar los clientes rechazados")
        print("3. Mostrar los clientes aprobados")
        print("4. Desembolsar")
        print("5. Mostrar los clientes desembolsados")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            entrevista.realizar_entrevista()
            evaluación.evaluar_clientes()
        elif opcion == '2':
            mostrar_clientes_rechazados()
        elif opcion == '3':
            mostrar_clientes_aprobados()
        elif opcion == '4':
            desembolso.main()
        elif opcion == '5':
            mostrar_clientes_desembolsados() 
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()