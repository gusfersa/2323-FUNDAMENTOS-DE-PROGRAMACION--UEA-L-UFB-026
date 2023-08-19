nombre = input('Ingrese su nombre: ')
sueldo_basico = float(input('Ingrese el sueldo basico: '))
horas = int(input('Ingrese las horas laboradas en el mes: '))
print('-------------------')
if (horas > 160) :
    horas_extras = horas - 160
    valor_extra = ((sueldo_basico / 160) * 1.5)
    sueldo_extra = horas_extras * valor_extra
    sueldo_total = sueldo_basico + sueldo_extra
    print('Horas Extras: ', horas_extras)
    print('Valor de la hora extra: ', round(valor_extra, 2))
    print('Sueldo Extra: ', round(sueldo_extra, 2))
else :
    horas_descuento = 160 - horas
    valor_hora = sueldo_basico / 160
    valor_descuento = horas_descuento * valor_hora
    sueldo_total = sueldo_basico - valor_descuento
    print('Horas descontadas: ', horas_descuento)
    print('Valor de la hora: ', round(valor_hora, 2))
    print('Valor de descuento: ', round(valor_descuento, 2))
print(f'El sueldo total a recibir para {nombre} es de {round(sueldo_total,2)}')