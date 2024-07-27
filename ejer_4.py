# Escribir un programa que almacene la cadena de caracteres contraseña en 
# una variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
# contraseña introducida por el usuario coincide con la guardada en la variable 
# sin tener en cuenta mayúsculas y minúsculas. 

print("----------------------------------------------------------------")
print("-------------------- Compare passwords -------------------------")
print("---------------- password = contraseña_123 ---------------------")
print("----------------------------------------------------------------")

authentic_password = "contraseña_123";
input_password = input("Please enter your password: ");
input_password.lower(); # convert to lowercase
while input_password != authentic_password:
    print("\t[ERROR] - Please enter the correct password")
    input_password = input("Please enter your password: ");
    input_password.lower(); # convert to lowercase
    
print("\t [SUCCES] - Your password is correct!")