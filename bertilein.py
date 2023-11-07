"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""
import random
import string


def input_validate(_string):
    option = input(_string)
    option = option.upper()
    
    print(option)
    while not(option == 'S' or option == 'N'):
        print("'Opción incorrecta!!!'")
        option = input(_string)
        option = option.upper()
        
    return option


def length_validate(_string)->int:
    pwd_length = input(_string)

    is_numeric = pwd_length.isnumeric()
    in_range = False
    
    while not(is_numeric) or not(in_range):
         
        print("Longitud incorrecta!!!")
        pwd_length = input(_string)
        is_numeric = pwd_length.isnumeric()
        print(is_numeric)
        if is_numeric:
            in_range = int(pwd_length) <8 or int(pwd_length) >16
        else :
            in_range = False
            
        #in_range = (False, (int(pwd_length) <8 or int(pwd_length) >16) )[is_numeric]
    
    return int(pwd_length)


def pwd_generate(pwd_length, _with_uppercase,_with_digits, _with_symbols):
    
    letters = (string.ascii_lowercase,string.ascii_letters)[_with_uppercase]
    digits  = ("",string.digits)[_with_digits]
    punctuation = ("", string.punctuation)[_with_symbols]
    #characters = string.printable 
    characters = letters+digits+punctuation 
    
    pwd = ""
    
    for i in range(pwd_length):
        pwd += characters[random.randint(0, len(characters)-1)]


    return pwd


pwd_length = length_validate('Introduzca longitud de contraseña (8-16): ')
uppercase  = input_validate('¿Desea que la contraseña incluya mayúsculas (S/N): ')
digit      = input_validate('¿Desea que la contraseña incluya dígitos (S/N): ')
simb       = input_validate('¿Desea que la contraseña incluya símbolos (S/N): ')
  
print("Contraseña generada: "+pwd_generate(pwd_length, uppercase =='S', digit =='S', simb =='S'))  