# Para tributar un determinado impuesto se debe ser mayor de 16 años y 
# tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un 
# programa que pregunte al usuario su edad y sus ingresos mensuales y muestre 
# por pantalla si el usuario tiene que tributar o no.

print("----------------------------------------------------------------");
print("-------------------------- Pay Taxes ---------------------------");
print("--------------------- over 16 years old ------------------------");
print("--------- income equal or greater to €1000 monthly -------------");
print("----------------------------------------------------------------");
    
age = input("Please enter your age: "); # Esta sin int() porque age.isnumeric() no funcion con enteros 
while age.isnumeric() == 0:
    print("\t [ERROR] - Please enter correct age: ");
    age = input("Please enter your age: "); # Esta sin int() porque age.isnumeric() no funcion con enteros 
    
income = input("Please enter your monthly income: "); # Esta sin float() porque age.isnumeric() no funcion con enteros 
while income.isnumeric() == 0:
    print("\t [ERROR] - Please enter correct income: ");
    income = input("Please enter your monthly income: "); # Esta sin float() porque age.isnumeric() no funcion con enteros 

if int(age) >= 16 and float(income) >= 1000: # Acá se convierte a age y income en entero y floar respectivamente para compararlos
    print(f"You're {age} and monthly income is {income} - You can pay taxes");
else:
    print(f"You're {age} and monthly income is {income} - You can't pay taxes");

    