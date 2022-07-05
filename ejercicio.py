from funciones import *

opcion = 20

while opcion != 19:
    opcion = menuPrincipal()
    if opcion == 19:
        break

    nombreCategoria = getNameCategory(opcion)
    limpiarConsola()
    
    print("=========================================")
    print("VACANTES PARA",nombreCategoria.upper())
    print("=========================================")

    preguntarPorFiltros(opcion)

limpiarConsola()
print("================================================================")
print("     GRACIAS POR UTILIZAR EL SISTEMA DE RECLUTAMIENTO IA")
print("================================================================")