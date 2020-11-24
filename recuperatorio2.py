import csv



def decodificar(archivoCodigo):

    print("\tDECODIFICANDO ARCHIVO .CSV\n")


    try:
        with open(archivoCodigo) as fCodificado:
            codificadoCsv = csv.reader(fCodificado, delimiter = ",")

            for i in codificadoCsv:

                mapeo = {
                    ord ('?'): None,
                    ord ('%'): None,
                    ord ('2'): None,
                    ord ('0'): " "
                }
                index0 = i[0].translate(mapeo)
                index1 = i[1].translate(mapeo)
                index2 = i[2]

                print (f"\t{index0}, {index1}, {index2}")

        return

    except FileNotFoundError:
        print("No se pudo abrir el archivo, o no existe.")
        return








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


        with open("analisis.csv", "w") as f:
            nuevoAnalisis = csv.DictWriter(f,fieldnames=cabeceras)

            nuevoAnalisis.writeheader()
            nuevoAnalisis.writerows(listaDicionarios)


        print(f"\t.csv ha sido creado con exito. ")
        print(listaDicionarios)



    except FileNotFoundError:
        print("No se pudo abrir el archivo, o no existe.")
        return


def nuevoArchivo(archivoAnalisis):
    cabecera2 = ["beneficiario","total","auditoria"]
    with open("verificado.csv", "w") as nuevoF, open(archivoAnalisis) as origen:
        nuevoCsv = csv.DictWriter(nuevoF, fieldnames= cabecera2)
        origenCsv = csv.DictReader(origen)

        lineaO = next(origenCsv, None)
        lineaN = next(nuevoCsv, None)

        monto = 0 
        while lineaO:

                        while alumno:
                            print(f"{alumno[0]}")
                            if not nota or nota[0] != alumno[0]:
                                print("\tNo se registran notas")

                            while nota and nota[0] == alumno[0]:
                                print(f"\t{alumno[0]} en {nota[1]}: {nota[2]}")
                                nota = next(notas_csv, None)
                            alumno = next(alumnos_csv, None)





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
