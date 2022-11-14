class Usuario():
    def __init__(self,nombre_de_usuario,clave):
        self.nombre_de_usuario = nombre_de_usuario
        self.clave = clave
        self.plata = 0
    
    def imprimir_usuario(self):
        print(self.nombre_de_usuario+" "+str(self.clave))
        
    def extrae(self,monto):
       self.plata = self.plata - monto

    def depositar(self,monto):
        self.plata = self.plata + monto
     
    def verificar_extraccion(self,monto):
        if  self.plata >= monto :
            return True
        return False    
        

class ContenedorDeUsuarios():
    def __init__(self):
        self.lista_de_usuarios=[]
        
    def registrar_usuario(self,usuario):
        if not (self.existe_usuario(usuario.nombre_de_usuario)):
            self.lista_de_usuarios.append(usuario)
        else:
            print("El usuario ya existe.")

    def existe_usuario(self,nombre):
        for user in self.lista_de_usuarios:
            if user.nombre_de_usuario == nombre:
                return True
        return False
    
    def validar_usuario(self,nombre,contraseña):
        for user in self.lista_de_usuarios:
            if user.nombre_de_usuario == nombre and user.clave == contraseña:
                return user
        return False

    def get_user(self,nombre):
        for user in self.lista_de_usuarios:
            if user.nombre_de_usuario == nombre:
                return user
            


