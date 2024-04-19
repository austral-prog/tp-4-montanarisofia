import math
def line():
#input the num
	A=float(input("Ingrese el coeficiente A: "))
	B=float(input("Ingrese el coeficiente B: "))
	X1=float(input("Ingrese el coeficiente X1: "))
	X2=float(input("Ingrese el coeficiente X2: "))

#convert to float
	if isinstance(A, int):
		A=float(A)
	if isinstance(B, int):
		B=float(B)
	if isinstance(X1, int):
		X1=float(X1)
	if isinstance(X2, int):
		X2=float(X2)

#now i jst print em
	print(f"El coeficiente A de su ecuacion de la recta es: {A}")
	print(f"El coeficiente B de su ecuacion de la recta es: {B}")
	print(f"El coeficiente X1 de su ecuacion de la recta es: {X1}")
	print(f"El coeficiente X2 de su ecuacion de la recta es: {X2}")
	print(f"\nPara la siguiente ecuacion: ")
	print(f"\tY= {A}X + {B}")

#gotta do the math
	Y=A*X1+B
	Y2=A*X2+B
	print(f"\nDados los siguientes puntos")
	print(f"\tP1 ({X1}, {Y})")
	print(f"\tP2 ({X2}, {Y2})")
	P=[X1, Y]
	Q=[X2, Y2]
	Distancia=math.dist(P, Q)
	print(f"\nLa distancia entre ellos es: {Distancia}")
    
#crossing ma fingers
line()
