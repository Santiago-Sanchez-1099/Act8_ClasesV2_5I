print("Clases version 2 el constructor")

class Perro:
    # Funcion constructor
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad
        
    #Funciones creadas por el usuario
    def muerde(self):
        print("Chale el perro me mordió")
    def chatperro(self,mensaje):
        print(f"Chat Perro: {mensaje}")
    def chatperra(self,mensajep):
        print(f"Chat Perra: {mensajep}")
    def datos(self):
        print(f"Color: {self.color} Edad: {self.edad}")
        
# Crear el objeto
Chihuas = Perro("Negro", 2)
# Llamadas a funciones
Chihuas.datos()
Chihuas.muerde()
Chihuas.chatperro("Hola canina")
Chihuas.chatperra("Hola bobby")
Chihuas.chatperro("Quieres ser mi guaoguao?")
Chihuas.chatperra("grrrrru......")
