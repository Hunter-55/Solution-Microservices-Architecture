import pymongo
from faker import Faker
import random


# Estructura del JSON
class EstructuraJSON:
	def __init__(self,fake):
		self.fake = fake
    
	# Estructura del Json
	def Estructura_Json(self):
		# creamos lista de las categorías y tipos
		correo           = ["riverawillie@livingston.biz",
							"carolyndillon@kim-mcdaniel.info",
							"morgan81@gmail.com",
							"fitzgeraldroberta@brown.info",
							"pburnett@charles.com",
							"kristy05@yahoo.com",
							"mmurillo@sanchez.org",
							"mbrown@williams.com",
							"whitecarl@gmail.com",
							"leejessica@hotmail.com"
							]
		tipo             = ["inflow","outflow"]
		categoria        = ["groceries","salary","transfer","rent","other","savings"]
		identificar_tipo = tipo[random.randint(0,1)] # se escoge el tipo de transacción
		monto            = 0.0

		# se identifica el tipo de transacción para asignar el monto negativo o positivo
		if identificar_tipo == "inflow":
			monto = round(random.uniform(1,5000),2)
		else:
			monto = round(random.uniform(-5000,-1),2)

		# y agregamos datos random al cuerpo del json
		json = {
			"reference":  random.randint(0,5000),
			"date":       str(self.fake.date_of_birth()),
			"amount":     monto,
			"type":       identificar_tipo,
			"category":   categoria[random.randint(0,5)],
			"user_email": correo[random.randint(0,4)]
			}
		return json


# conexión a la base de datos
class Conexion:
	def __init__(self,client,fake,cantidad):
		self.client      = client
		self.fake        = fake
		self.cantidad    = cantidad
        
	# insertar a las coleción de mongo
	def Insertar_Datos(self):
		try:
			# se crea la basede datos y la colección si no existe
			db            = self.client["Ordinario"]
			coleccion     = db['registro']
			json          = {}
	
			print("Nombre de la DB: ",db.name)
			# se agrega la cantida de usuarios a la coleción 
			for i in range(self.cantidad):
				# instanciamos la estructura del json
				faker = EstructuraJSON(self.fake)
				json  = faker.Estructura_Json()

				# se agrega el primer registro a la colección
				if i == 0:
					db.registro.insert_many([json])
	
				else:
					contador    = 0
					verificador = 0
					col 	    = coleccion.find()
					lists       = []
					flag        = True
	
					# verificamos que la referencia no se duplique en la base de datos
					for cole in coleccion.find():
						lists.append(cole)
						#print(cole)
	
					while flag == True:

						if json['reference'] != col[contador]['reference']:
							verificador += 1
	
						if verificador == len(lists):
							db.registro.insert_many([json])
							flag = False
	
						if contador == (len(lists)-1) and verificador != len(lists):
							json['reference'] = random.randint(0,5000)
							contador    = 0
							verificador = 0
	
						contador += 1
			return True
		except:
			return False
  

# funcion main
def main():
	# conexión a la base de datos mongo
	client = pymongo.MongoClient("mongodb://root:root123@mongo_DB:27017/")
	fake = Faker() # utilización d faker
    
	# instancia de la clase conexión
	con = Conexion(client,fake,50)
	con.Insertar_Datos()

if __name__ == "__main__":
	main()
    
    
    
    
    
    
    
    
