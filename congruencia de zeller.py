import os

class congruenciaZeller():

	def __init__(self,dia,mes,ano):
		
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def calculoDia(self):
		#Metodo 1
		if(self.mes<=2):
			self.mes+=10
			self.ano-=1
		else:
			self.mes-=2

		#h=((700+((26*mes -2)/10) +dia + k + (k/4) +((j/4) + 5*J))%7)

		K= self.ano%100
		J=self.ano//100
		h=((700 + ((26*self.mes -2)//10) + self.dia + K + (K//4) + ((J//4) +5*J)) %7)

		"""
		#metodo 2
		a = (14-self.mes) // 12
		y = self.ano - a
		m = self.mes + (12*a) - 2
		d = (self.dia + y + (y//4) - (y//100) + (y//400) + (31*m) // 12) % 7
		return d"""
		return h

	def impresion(self):
		dias=["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
		print("\nEl dia correspindiente a la fecha {}-{}-{} es: {}".format((self.dia),(self.mes),(self.ano),(dias[self.calculoDia()]),))

respuesta=1

while(respuesta==1):
	os.system("cls")
	os.system("color 0a")
	print("*********     Bienvenido a la Congruencia de Zeller      **************\n")
	try:
		diaC=int(input("Ingresa el dia de la fecha a calcular[1-31]: "))
		mesC=int(input("Ingresa el mes de la fecha a calular[1-12]: "))
		anoC=int(input("Ingresa el ano de la fecha a calcular[yyyy]: "))

		calculoDia = congruenciaZeller(diaC,mesC,anoC)
		calculoDia.impresion()

	except ValueError:
		print("Error: Asegurate de ingresar solo numeros...")

	respuesta = input("\nDeseas hacerlo otra vez? SI(1) NO(0) ")
	try:
		respuesta=int(respuesta)
		if(respuesta!=1):
			print("Gracias por utilizar este pequeno programa, hasta pronto...!")
			respuesta=0

	except ValueError:
		print("\nAl parecer, haz ingresado una respuesta incorrecta,\nasumiremos que no quires hacerlo nuevamente....")
		respuesta = 0

