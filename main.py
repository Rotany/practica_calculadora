from code.division import division
from code.suma import suma
from code.resta import resta
from code.multiplicacion import multiplicacion
valor_input = input("Que funcion desea realizar: \n1-suma 2-resta 3-multiplicacion 4-division : " ) 
primer_valor = float( input ('ingrese el primer valor: '))
segundo_valor = float( input( 'ingrese el segundo valor: '))
if valor_input == '1' :
    print(suma(primer_valor,segundo_valor))
if valor_input == '2' :
    print(resta(primer_valor,segundo_valor))
if valor_input =='3' :
    print(multiplicacion(primer_valor,segundo_valor))
if valor_input == '4':
    print(division(primer_valor,segundo_valor))
    
    
    





