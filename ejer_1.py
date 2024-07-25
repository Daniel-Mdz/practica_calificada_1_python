# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al 
# sexo y el nombre. El grupo A esta formado por las mujeres con un nombre 
# anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el 
# resto. Escribir un programa que pregunte al usuario su nombre y sexo, y 
# muestre por pantalla el grupo que le corresponde.


name = input("Please enter your name: "); # exclui str(input) porque el texto ingresado esta en cadena
while name.isalpha() == 0:
    print("\t [ERROR] - Please enter correct name: ");
    name = input("Please enter your name: ");

gender = input("Please enter your gender: "); # exclui str(input) porque el texto ingresado esta en cadena
while gender.lower() != "male" and gender.lower() != "m" and gender.lower() != "female" and gender.lower() != "f":
    print("\t [ERROR] - Please enter correct gender");
    gender = input("Please enter your gender: ");
    
if gender.lower() == "female" or gender.lower() == "f":
    if name[0].lower() < "m":
        print(f"\t{name} your name starts in {name[0]} - Your group is: Group A");
    else:
        print(f"\t{name} your name starts in {name[0]} - Your group is: Group B");

if gender.lower() == "male" or gender.lower() == "m":
    if name[0].lower() > "n":
        print(f"\t{name} your name starts in {name[0]} - Your group is: Group A");
    else:
        print(f"\t{name} your name starts in {name[0]} - Your group is: Group B");