from tkinter.constants import W
import matplotlib.pyplot as plt
from server.querys.Querys import Querys
from tkinter import messagebox as viewMessage


class GraficaMotivos():

    
    def mostrarGraficaPastel(self):

        self.sentencia = Querys()
        self.respuesta = self.sentencia.todosLosRegistros()

        self.cuentaHombres = 0
        self.cuentaMujeres = 0
        self.mujeresBaja = 0
        self.hombresBaja = 0

        if self.respuesta != None:
            
            for item in self.respuesta:
                
                if item['genero'] == 'Femenino' and item['estado'] == 'Activo':

                    self.cuentaMujeres += 1

                elif item['genero'] == 'Femenino' and item['estado'] == 'Baja':

                    self.mujeresBaja += 1
                
                elif item['genero'] == 'Masculino' and item['estado'] == 'Activo':

                    self.cuentaHombres += 1

                elif item['genero'] == 'Masculino' and item['estado'] == 'Baja':

                    self.hombresBaja += 1

            print(f"mujeres Activos : {self.cuentaMujeres} hombres Activos : {self.cuentaHombres} mujeres Baja : {self.cuentaMujeres} hombres Baja : {self.cuentaHombres}")

            self.diviciones = [self.cuentaMujeres, self.cuentaHombres, self.mujeresBaja, self.hombresBaja]

            self.colores = ['#E91E63', '#01579B', '#FF6F00','#DCE775']
            self.actividades = ['Mujeres Estudiando', 'Hombres Estudiando', 'Mujeres no estudiando', 'Mombres no estudiando']

            plt.pie(self.diviciones, colors=self.colores, labels=self.actividades, startangle=90, shadow=True, explode=(0.1, 0, 0, 0), autopct='%1.1f%%')

            plt.title('Genero predominante')

            plt.show()
        
        else:
            viewMessage.showinfo("Grafiaca pastel", "No se encontraron registros")



    def mostarGraficaBarrar(self):
        
        self.sentencia = Querys()
        self.respuesta = self.sentencia.todosLosRegistros()
        self.listaSecciones = []
        self.auxiliarLista = []
        self.listaSeccionesAux = ["Primaria", "Secundaria Matutina", "Secundaria Vespertina", "Bachillerato", "Universidad","Posgrado", "Maestria"]
        self.diccionarioNivel = {"Primaria": 0, "Secundaria Matutina": 0, "Secundaria Vespertina": 0, "Bachillerato": 0, "Universidad": 0,"Posgrado": 0, "Maestria": 0}
        self.diccionarioNivelB = {"Primaria": 0, "Secundaria Matutina": 0, "Secundaria Vespertina": 0, "Bachillerato": 0, "Universidad": 0,"Posgrado": 0, "Maestria": 0}
        self.cuentaSecciones = 0
        
        if self.respuesta != None:

            for self.item in self.respuesta:

                if self.item['nivel_educativo'] not in self.listaSecciones:

                    self.listaSecciones.append(self.item['nivel_educativo'])
                    print(self.item['nivel_educativo'])
                    print(f"lista {self.listaSecciones}")

            # self.diccionarioNivel['Primaria'] = 5

            # print(self.diccionarioNivel['Primaria'] + 1)

            for self.item2 in self.respuesta:

                if self.item2['nivel_educativo'] in self.listaSeccionesAux:

                    # self.diccionarioNivel[self.item2['nivel_educativo']] += 1

                    if self.item2['estado'] == 'Baja': # Baja

                        self.diccionarioNivelB[self.item2['nivel_educativo']] += 1

                    else:

                        self.diccionarioNivel[self.item2['nivel_educativo']] += 1

            print(f" activos : {self.diccionarioNivel}")
            print(f" baja : {self.diccionarioNivelB}")

            self.claves = self.diccionarioNivel.keys()
            self.valores = self.diccionarioNivel.values()

            print(f"valores : {self.valores}")
            self.clavesAux = []
            for self.aux in self.claves:
                self.clavesAux.append(self.aux)
            
            # para activos
            
            plt.bar(self.clavesAux[0], self.diccionarioNivel['Primaria'], width=0.2, color='#AD1457', label='Alumnos activos')
            plt.bar(self.clavesAux[0], self.diccionarioNivelB['Primaria'], bottom= self.diccionarioNivel['Primaria'], width=0.2, color='#EC407A', label='Alumnos inactivos')
            plt.bar(self.clavesAux[1], self.diccionarioNivel['Secundaria Matutina'], width=0.2, color='#AD1457')
            plt.bar(self.clavesAux[1], self.diccionarioNivelB['Secundaria Matutina'], bottom= self.diccionarioNivel['Secundaria Matutina'], width=0.2, color='#EC407A')
            plt.bar(self.clavesAux[2], self.diccionarioNivel['Secundaria Vespertina'], width=0.2 , color='#AD1457')
            plt.bar(self.clavesAux[2], self.diccionarioNivelB['Secundaria Vespertina'], bottom= self.diccionarioNivel['Secundaria Vespertina'], width=0.2, color='#EC407A')
            plt.bar(self.clavesAux[3], self.diccionarioNivel['Bachillerato'], width=0.2, color='#AD1457')
            plt.bar(self.clavesAux[3], self.diccionarioNivelB['Bachillerato'], bottom= self.diccionarioNivel['Bachillerato'], width=0.2, color='#EC407A')
            plt.bar(self.clavesAux[4], self.diccionarioNivel['Universidad'], width=0.2, color='#AD1457')
            plt.bar(self.clavesAux[4], self.diccionarioNivelB['Universidad'], bottom= self.diccionarioNivel['Universidad'], width=0.5, color='#EC407A')
            plt.bar(self.clavesAux[5], self.diccionarioNivel['Posgrado'], width=0.2, color='#AD1457')
            plt.bar(self.clavesAux[5], self.diccionarioNivelB['Posgrado'], bottom= self.diccionarioNivel['Posgrado'], width=0.2, color='#EC407A')
            plt.bar(self.clavesAux[6], self.diccionarioNivel['Maestria'], width=0.2, color='#AD1457')
            plt.bar(self.clavesAux[6], self.diccionarioNivelB['Maestria'], bottom= self.diccionarioNivel['Maestria'], width=0.2, color='#EC407A')
            
            plt.title('Niveles educativos afectados')
            plt.ylabel('Personas Entrvistadas')
            plt.xlabel('Niveles educativos')

            plt.legend()
            # plt.grid()
            plt.show()

        else:
            viewMessage.showinfo("Grafiaca de barras", "No se encontraron registros")


