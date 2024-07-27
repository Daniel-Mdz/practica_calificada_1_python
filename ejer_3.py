# Escribir un programa para una empresa que tiene salas de juegos para 
# todas las edades y quiere calcular de forma automática el precio que debe 
# cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad 
# del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años 
# puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 
# 18 años, 10€. 
print("-----------------------------------------------------------")
print("-------------------- Price to pay -------------------------")
print("-----------------------------------------------------------")

age = int(input("Please enter the client's age: "))
while age < 0:
    age = int(input("\t [ERROR] - Please enter the client's age again: "))

if age < 4:
    print("\t Result => The client is free to enter.")
elif age < 18:
    print("\t Result =>The client will pay 5€ for entry.")
else:
    print("\t Result =>The client will pay 10€ for entry.")