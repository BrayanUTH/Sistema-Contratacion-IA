import json
from os import system
from datetime import datetime
from dateutil import relativedelta

def getData():
    try:
        file = open('database.json')
        data = json.load(file)
        return data
    except:
        print("Se produjo un error al obtener los datos")
    finally:
        file.close()

def menuPrincipal():
    print("================================")
    print("  SISTEMA DE RECLUTAMIENTO IA")
    print("================================")
    print("1. Administracion")
    print("2. Almacenamiento")
    print("3. Apoyo De Oficina")
    print("4. Banca | Servicios Financieros")
    print("5. Call Center")
    print("6. Finanzas | Contabilidad | Auditoria")
    print("7. Informatica | Internet")
    print("8. Mantenimiento")
    print("9. Marketing")
    print("10. Operaciones | Logistica")
    print("11. Produccion | Ingenieria | Calidad")
    print("12. Publicidad | Comunicaciones | Servicios")
    print("13. Recursos Humanos")
    print("14. Restaurantes")
    print("15. Salud")
    print("16. Telecomunicaciones")
    print("17. Automotriz")
    print("18. Otros")
    print("19. Salir")
    opcion = int(input("Ingrese una opcion -> "))

    return opcion

def evaluarVacantes(arregloFiltros):
    arrayIdVacantes = []
    existenVacantes = False
    dataDB = getData()  

    for item in dataDB:
        
        if (item["categoria"] == arregloFiltros[4]):
            if len(arregloFiltros[0]) != 0 and existenVacantes == False:
                categoriasPorSkills = obtenerCategoriasConSkills(dataDB, item["categoria"])
                arrayIdVacantes = filtrarSkills(categoriasPorSkills[0], categoriasPorSkills[1], arregloFiltros[0])
                existenVacantes = True

            if arregloFiltros[1] != 0:
                endDate = formattedCurrentDate()
                startDate = datetime.strptime(item["fecha_inicio_experiencia"], "%d/%m/%Y");
                yearsExperience = relativedelta.relativedelta(endDate, startDate)

                if arregloFiltros[1] <= yearsExperience.years:
                    arrayIdVacantes.append(item["id"])

            if arregloFiltros[2] != "" and arregloFiltros[3] != "Remoto" and arregloFiltros[3] != "":
                if arregloFiltros[2].upper() == item["ciudad"].upper():
                    arrayIdVacantes.append(item["id"])

            if arregloFiltros[3] != "":
                if arregloFiltros[3].upper() == item["modalidad_trabajo"].upper():
                    arrayIdVacantes.append(item["id"])

    arrayIdVacantes = list(dict.fromkeys(arrayIdVacantes))
    mostrarResultados(arrayIdVacantes, dataDB)


def filtrarSkills(arrSkillsJSON, indexSkillsJSON, arrSkillsUser):
    arrayIdVacantes = []

    for i in range(0, indexSkillsJSON, 1):
        if bool(set(arrSkillsJSON[i]["skills"]).intersection(arrSkillsUser)):
            arrayIdVacantes.append(arrSkillsJSON[i]["id"])
    
    return arrayIdVacantes


def obtenerCategoriasConSkills(item, idCategoria):
    categorias = []
    result = []
    index = 0

    for param in item:
        if param["categoria"] == idCategoria:
            index = index + 1
            param["skills"] = param["skills"].split(',')
            categorias.append(param)

    result.append(categorias)
    result.append(index)

    return result

def mostrarResultados(arreglo, dataBD):
    index = 1
    limpiarConsola()
    endDate = formattedCurrentDate()

    if len(arreglo) == 0:
        print("No tenemos vacantes para el area")
    else:
        print("====================================")
        print(len(arreglo), "VACANTES DISPONIBLES")
        print("====================================")
        
        for item in dataBD:
            for j in range(0, len(arreglo), 1):
                if item["id"] == arreglo[j]:
                    startDate = datetime.strptime(item["fecha_inicio_experiencia"], "%d/%m/%Y")
                    delta = relativedelta.relativedelta(endDate, startDate)

                    print(index, ".-", item["puesto_trabajo"])
                    print("<Nombre>", item["nombre"], item["apellido"])
                    print("<Habilidades>", item["skills"])
                    print("<Experiencia>", delta.years, "Años")
                    print("<Ciudad>", item["ciudad"])
                    print("<Modalidad>", item["modalidad_trabajo"])
                    print("<Email>", item["correo"], "\n")

                    index = index + 1

def formattedCurrentDate():
    dateCurrent = datetime.now().strftime("%d/%m/%Y")
    return datetime.strptime(dateCurrent, "%d/%m/%Y")

def getNameCategory(opcion):
    if opcion == 1:
        return "Administracion"
    elif opcion == 2:
        return "Almacenamiento"
    elif opcion == 3:
        return "APOYO DE OFICINA"
    elif opcion == 4:
        return "Banca | Servicios Financieros"
    elif opcion == 5:
        return "Call Center"
    elif opcion == 6:
        return "Finanzas | Contabilidad | Auditoria"
    elif opcion == 7:
        return "Informatica | Internet"
    elif opcion == 8:
        return "Mantenimiento"
    elif opcion == 9:
        return "Marketing"
    elif opcion == 10:
        return "Operaciones | Logistica"
    elif opcion == 11:
        return "Produccion | Ingenieria | Calidad"
    elif opcion == 12:
        return "Publicidad | Comunicaciones | Servicios"
    elif opcion == 13:
        return "Recursos Humanos"
    elif opcion == 14:
        return "Restaurantes"
    elif opcion == 15:
        return "Salud"
    elif opcion == 16:
        return "Telecomunicaciones"
    elif opcion == 17:
        return "Automotriz"
    elif opcion == 18:
        return "Otros"
    else:
        return "Ninguna Opcion"

def limpiarConsola():
    system("cls")

def validarIngresoCorrecto(texto, cantidadSkills, parametro):
    while cantidadSkills <= parametro:
        cantidadSkills = int(input(texto))

    return cantidadSkills

def preguntarPorFiltros(idCategoria):
    arregloFiltros = []
    arregloSkills = []
    cantidadSkills = 0
    yearsExperiencia = 0
    ciudadVacante = ""
    modalidadVacante = ""

    busquedaSkills = input("¿Quiere filtrar por Skills? S/N -> ").upper()

    if busquedaSkills == "S":
        cantidadSkills = int(input("Ingrese la cantidad de skills para la busqueda -> "))

        if cantidadSkills == 0 or cantidadSkills < 0:
            print("")
            print("Debes ingresar una cantidad de skills valida")
            cantidadSkills = validarIngresoCorrecto("Ingrese la cantidad para la busqueda -> ", cantidadSkills, 0)

    for i in range(0, cantidadSkills, 1):
        print((i + 1), ".- Nombre Skill: ")
        skill = input().lower()
        arregloSkills.append(skill)

    busquedaExperiencia = input("¿Quiere filtrar por años de experiencia? S/N -> ").upper()

    if (busquedaExperiencia == "S"):
        yearsExperiencia = int(input("Ingrese la cantidad de años de experiencia -> "))

    busquedaModalidad = input("¿Quiere filtrar por modalidad? S/N -> ").upper()

    if (busquedaModalidad == "S"):
        modalidadVacante = input("Ingrese la modalidad deseada -> ")

    busquedaCiudad = input("¿Quiere filtrar por ciudad? S/N -> ").upper()

    if (busquedaCiudad == "S"):
        ciudadVacante = input("Ingrese la ciudad que desea -> ")


    arregloFiltros.append(arregloSkills)
    arregloFiltros.append(yearsExperiencia)
    arregloFiltros.append(ciudadVacante)
    arregloFiltros.append(modalidadVacante)
    arregloFiltros.append(idCategoria)

    evaluarVacantes(arregloFiltros)
