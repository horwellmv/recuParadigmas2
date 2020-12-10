import csv



def decodificar(archivoCodigo):

    print("\tDECODIFICANDO ARCHIVO .CSV\n")


    try:
        with open(archivoCodigo) as fCodificado:
            codificadoCsv = csv.reader(fCodificado, delimiter = ",")

            for i in codificadoCsv:

                eliminar = {
                    ord ('?'): None,
                    ord ('%'): None,
                    ord ('2'): None,
                    ord ('0'): " "
                }
                index0 = i[0].translate(eliminar)
                index1 = i[1].translate(eliminar)
                index2 = i[2]

                print (f"\t{index0},  {index1},  {index2}")

        return

    except FileNotFoundError:
        print("No se pudo abrir el archivo, o no existe.")
        return




# -------------------- Funcion crea lista de diccionarios con datos limpios -----



def analizar(archivoCodigo):

    print("\tANALIZANDO ARCHIVO .CSV\n")
    try:
        listaDicionarios =[]
        cabeceras = ["beneficiario", "prestacion", "monto"]

        with open(archivoCodigo) as fCodificado:
            codificadoCsv = csv.reader(fCodificado, delimiter = ",")

            for i in codificadoCsv:
                diccionario = {}
                mapeo = {
                    ord ('?'): None,
                    ord ('%'): None,
                    ord ('2'): None,
                    ord ('0'): " "
                }
                index0 = i[0].translate(mapeo)
                index1 = i[1].translate(mapeo)
                index2 = i[2]

                diccionario["beneficiario"] = index0
                diccionario["prestacion"] = index1
                diccionario["monto"] = index2

                listaDicionarios.append(diccionario)


        print(listaDicionarios)
        return #nuevoArchivo(listaDicionarios)



    except FileNotFoundError:
        print("No se pudo abrir el archivo, o no existe.")
        return
# --------------------- Funcion Nuevo Archivo -------------------3.3

def nuevoArchivo(listaDeDatos):
    nuevaLista = []
    cabecera = ["beneficiario","total","auditoria"]
    with open("verificado.csv", "w") as newF
        nuevoCsv = csv.DictWriter(newF, fieldnames= cabecera)

        for i in listaDeDatos:
            






# ----------------------- Funcion imprimir -------------------------- 4 ------
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
                decodificar("prestaciones.csv")


            if menu == 2:
                analizar("prestaciones.csv")

            if menu == 3:
                imprimir()


            if menu == 4:
                salir = "s"

        except ValueError:
            print("\n\t\tNo es una entrada valida de menu.")
            return principal()

principal()


# print(x[2])
