

cantidad =int(input('Cantidad de números que va a digitar --> '))

contador = 0
while (contador < cantidad):   
    numero = int(input('Digite un número --> '))
    if (numero >= 10) and (numero <= 20):
        print('Está dentro del rango')
    else:
        print('No está dentro del rango')
    contador += 1

