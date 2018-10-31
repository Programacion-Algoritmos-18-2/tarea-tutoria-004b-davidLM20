#clase padre 
class Persona():
	"""docstring for Persona"""
	
	#metodo para definir los atributos de la clase
	def __init__(self):
		self.nombres = " "
		self.edad = 0
	
	#metodos para agregar los valores a edad y nombres	
	def agregar_nombres(self,n):
			self.nombres = n

	def agregar_edad(self,n):
			self.edad = n
	
	#metodos para el retorno de valores los valores a edad y nombres
	def obtener_edad(self):
			return self.edad

	def obtener_nombre(self):
			return self.nombres
	
	#metodos para presentar datos de la clase padre 
	def presentar_datos(self):
		c = "%s - %s" % (self.obtener_edad(), self.nombres)
		return c

# clase a la cual se le hereda los atributos de la clase persona
class Estudiante(Persona):#en esta linea se expecifica de que clse se hereda los atributos
	"""docstring for Estudiante"""
	# metodo para definir los atributos 
	def __init__(self):
		super(Estudiante, self).__init__()
		self.nota = 0 

	#metodo para poder agragar un valor al atributo nota
	def agregar_nota(self,n):
			self.nota = n

	#este metodo permite presentar los valores 
	def presentar_datos(self):
		#c = "%s - %s - %s" % (self.nombres, self.edad, self.nota)// esta forma de presentar tambien es valido 
		c = "%s -%s" % (super(Estudiante,self).presentar_datos(),self.nota)
		return c
		
		