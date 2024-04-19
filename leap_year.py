def leap_year():
#input and allat
    year=int(input("Ingrese un año: "))
    if (year%4==0 and year%100!=0 or year%400==0):
        print(f"El año {year} es bisiesto")
    else: 
        print(f"El año {year} no es bisiesto")
#crossing fingers :)
leap_year()
