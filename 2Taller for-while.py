'''
Elaborar un programa en Python el cual tiene los siguientes productos: 1. 
Computador de escritorio 2. Computador de escritorio 3. Tabletas 4. Videobeam 5. 
Televisores y determinar cuantos de cada uno se han comprado, tener en cuenta 
que el precio de los artículos debe estar establecidos de manera constante, el 
sistema debe recibir todos los productos de manera infinita y al momento de 
seleccionar la opción de “FACTURAR” debe mostrar el total de la suma de los 
artículos, cuantos de cada uno se agregaron, el total a pagar.
'''

#ESTABLECER PRECIO DE LOS PRODUCTOS EN CONS
computadorEscritorio = 2400000
computadorPortatil = 2000000
tableta = 1800000
videobeam = 540000
televisor = 2800000

import os
#INICIALIZAR VALORES
control = True 
total = 0
cComputador =0
cPortatil =0 
cTableta = 0
cVideobeam = 0 
cTelevisor =0

#ENTRADA-proceso
while (control == True):
    os.system('cls')  #borrar consola
    #MOSTRAR MENÚ
    print('\t.:Tienda electronica menesex:.\n\n[0] Facturación\n[1]Computador escritorio (2.4M)\n[2]Computador portatil (2M) [3]Tableta(1.8M)\n[4]Videobeam(540K)\n[5]Televisor(2.8M)')
    opcion = int(input('[]--> '))
    if opcion == 0:
        control = False
        
    elif opcion == 1:
        total = total + computadorEscritorio
        cComputador += 1
        
    elif opcion == 2:
        total += computadorPortatil
        cPortatil += 1
        
    elif opcion == 3:
        total += tableta
        cTableta += 1
        
    elif opcion == 4:
        total += videobeam
        cVideobeam += 1
        
    elif opcion == 5:    
          total += televisor
          cTelevisor = 1
          
    if opcion != 0:
        input('Compra realizada con exito (enter para continuar)')
    
#SALIDA (facturación)
if total != 0: #Si se realizo una compra entonces..
    print(f'\t<<Menú de facturación>>\n\nUsted compró:\nComputador de escritorio ({cComputador})\nComputador portatil({cPortatil})\nTableta ({cTableta})\nVideobeam ({cVideobeam})\nTelevisor ({cTelevisor})')
    print(f'\nTotal: {total}$')
