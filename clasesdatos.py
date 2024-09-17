class Informacion:
    def mi_lista(self):
        lista_Nomperros=["Bobby","Dollar","Fanny"]
        for x in lista_Nomperros:
            print(x)

    def mi_tupla(self):
        tupla_Nomperros=("Rob","Firulais","Cent")
        for x in tupla_Nomperros:
            print(x)

    def mi_conjunto(self):
        conjunto_Nomperros={"Max","Pablo","Pelusa"}
        for x in conjunto_Nomperros:
            print(x)

    def mi_diccionario(self):
        diccionario_perros={
            "Nombre": ["Joseph","Princesa","Juan"],
            "Edad": [2,4,1],
            "Color": ["Negro", "Naranja", "Blanco"]
            }
        for x, y in diccionario_perros.items():
            print(x, y)
# Creando el objeto
datos=Informacion()
print("------------------------------")
print("Listado de nombres de perros")
datos.mi_lista()
print("------------------------------")
print("Tupla de nombres de perros")
datos.mi_tupla()
print("------------------------------")
print("Conjunto de nombres de perros")
datos.mi_conjunto()
print("------------------------------")
print("Listado de nombres de perros")
datos.mi_diccionario()
print("------------------------------")