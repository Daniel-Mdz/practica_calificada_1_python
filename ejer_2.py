# Para tributar un determinado impuesto se debe ser mayor de 16 años y 
# tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un 
# programa que pregunte al usuario su edad y sus ingresos mensuales y muestre 
# por pantalla si el usuario tiene que tributar o no.
    
age = int(input("Please enter your age: "));
while age.isanumber() == 0:
    print("\t [ERROR] - Please enter correct age: ");
    age = int(input("Please enter your age: "));
    
income = float(input("Please enter your monthly income: ")); 
while income.isanumber() == 0:
    print("\t [ERROR] - Please enter correct income: ");
    income = float(input("Please enter your monthly income: "));

if age >= 16 and income >= 1000:
    print(f"You're {age} and monthly income is {income} - You can pay taxes");
else:
    print(f"You're {age} and monthly income is {income} - You can't pay taxes");

    