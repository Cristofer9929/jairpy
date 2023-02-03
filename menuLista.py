salir=False
while not salir:
    print("\n\n***Sistema de Listas****")
    print("\n\n1)Crear lista")
    print("2)Agregar elemento")
    print("3)Eliminar elemento")
    print("4)Modificar elemento")
    print("5)Mostrar datos")
    print("6)Mostar datos de forma inversa")
    print("7)Limpiar lista")
    print("8)Borrar lista")
    print("9)Salir")
    opc=input("\n\nIngrese una opcion valida (1-9): ")
    print("\n\n")
    
    if(opc=='1'):
        print("--->Crear lista<---")
        if 'lista' in locals():
            print("\nLa lista ya existe")
        else:
            lista=[]
            print("\nLista creada")

    elif(opc=='2'):
        print("-->Agregar elemento<--")
        if 'lista' in locals():
            ll=input("\nIngrese un elemento: ")
            lista.append(ll)
            print("\nElemento ingresado correctamente")
        else:
            print("\nLa lista no existe")
            

    elif(opc=='3'):
        print("-->Eliminar elemento<--")
        if 'lista' in locals():
            lista[0]=''
            print("\nElemento eliminado")
        else:
            print("\La lista no existe")

    elif(opc=='4'):
        print("-->Modificar elemento<--")
        if 'lista' in locals():
            lista[0]=input('\nSustitucion:')
            print("Elemento modificado")
        else:
            print("\La lista no existe")

    elif(opc=='5'):
        print("-->Mostrar datos<--")
        if 'lista' in locals():
            print(lista)
        else:
            print("\nLa lista no contiene ningun dato")

    elif(opc=='6'):
        print("-->Mostar datos de forma inversa<--")
        if 'lista' in locals():
            for x in reversed(lista):
                print(x)
        else:
            print("\nLa lista no contiene ningun dato")

    elif(opc=='7'):
        print("-->Limpiar lista<--")
        if 'lista' in locals():
            del(lista)
            lista=[]
            print("\Elementos de la lista eliminados")
        else:
            print("\nLa lista no existe")

    elif(opc=='8'):
        print("-->Borrar lista<--")
        if 'lista' in locals():
            del(lista)
            print("\nLista eliminada con exitosamente")
        else:
            print("\nLa lista no existe")

    elif(opc=='9'):
        print("\nHasta la proxima :) ")
        salir=True
        
    else:
        print("Opcion o valor invalido")
