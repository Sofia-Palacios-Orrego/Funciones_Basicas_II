#1- crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno en cuenta regresiva. 
def countdown (num):
    lista = [ ]
    for i in range(num, -1, -1):
        lista.append(i)
    return lista 

resultado = countdown(8)
print(resultado)


#2- crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
def imp_y_dev(list):
    print(list[0])
    return list[1]
    
result = imp_y_dev([8,10])
print(result)


#3- crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.

def suma_p_mas_l(lis):
    sum = lis[0] + len(lis)
    return sum

output = suma_p_mas_l([5,10,20,20])
print(output)


#4- escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean
#     mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 
#     2 elementos, has que la función devuelva False

def valores_mayores(lsta):
    if len(lsta) < 2:
        return False

    segundo_valor = lsta[1]
    nueva_lsta = [valor for valor in lsta if valor > segundo_valor]

    print("Cantidad de valores mayores:", len(nueva_lsta))
    return nueva_lsta

answer = valores_mayores([5, 2, 8, 3, 10, 1])
print(answer)


#5- escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una 
# lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.

def tam_y_val (size, value):
    nueva_lis= [value] * size
    return nueva_lis

resp = tam_y_val (4, 8)
print(resp)