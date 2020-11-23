import csv



def decodificar():
    print("decodificamos")
    return


def analizar():
    print("analizamos")
    return


def imprimir():
    print("Imprimimos")
    return





def principal():
    salir = ""
    while salir != "s":

        try:
            print (f"\nMENU PRINCIPAL: 1: Decodificar.\n\t\t2: Ananlizar.\n\t\t3: Imprimir.\n\t\t4: salir.")
            menu = int(input("\t\t : "))

            if menu == 1:
                decodificar()

            if menu == 2:
                analizar()

            if menu == 3:
                imprimir()


            if menu == 4:
                salir = "s"

        except ValueError:
            print("\n\t\tNo es una entrada valida de menu.")
            return principal()

principal()
