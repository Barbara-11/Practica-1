print('ingresa la edad: ')
edad = float(input())
year = 2020 - edad
if(edad<0):
    print('Dato no valido')
elif(edad>=18):
    print('Eres mayor de edad')
    print('Naciste en el anio ' + str(year))
else:
    print('No eres mayor de edad')
    print('Naciste en el anio ' + str(year))
