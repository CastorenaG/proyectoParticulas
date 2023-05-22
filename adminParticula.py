from particula  import Particula
import json
from algoritmos import *

class AdminParticulas:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula: Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def ordenar_id(self):
       self.__particulas.sort(key=lambda particula: particula.id)

    def ordenar_distancia(self):
        self.__particulas.sort(key=lambda particula: particula.distancia, reverse=True)

    def ordenar_velocidad(self):
        self.__particulas.sort(key=lambda particula: particula.velocidad)
        
    def __str__(self):   
        return '\n'.join(str(particula) for particula in self.__particulas)

    def particulas_cercanas(self):
        particulas = []
        for p in self.__particulas:
        #Pasar a lista de tuplas para el algoritmo y agregar los colores
            p1 = (p.origen_x,p.origen_y,p.red,p.green,p.blue)
            p2 = (p.destino_x,p.destino_y,p.red,p.green,p.blue)
            particulas.append(p1)
            particulas.append(p2)
        res = particulas_mas_cercanas(particulas)
        return res
    
    """def particulas_cercanas(self):
        particulas = self.get_particulas()
        grafo = Grafo()
        for particula in particulas:
            origen = (particula[0], particula[1])
            destino = (particula[5], particula[6])
            distancia = particula[9]
            grafo.agregar_arista(origen, destino, distancia)

        res = particulas_mas_cercanas(particulas)
        return res"""
    
    def get_particulas(self):
        particulas = []
        for p in self.__particulas:
            p1 = (p.origen_x,p.origen_y,p.red,p.green,p.blue)
            p2 = (p.destino_x,p.destino_y,p.red,p.green,p.blue)
            particulas.append(p1)
            particulas.append(p2)

        return particulas

    def __len__(self):
        return(
            len(self.__particulas)
        )
    
    def __iter__(self):
        self.count=0
        return self
    
    def __next__ (self):
        if self.count < len(self.__particulas):
            conjunto=self.__particulas[self.count]
            self.count += 1
            return conjunto
        else:
            raise StopIteration
        
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
                return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
                return 1
            
        except:
            return 0
        
