import sqlite3
from sqlite3.dbapi2 import OperationalError
from tkinter import messagebox as viewMessage


class Querys():

    _conexionDB = sqlite3.connect('server/database/alumnosDB.db3')
    _cursor = _conexionDB.cursor()

    def crearBaseDatos(self):

        try:
            self._cursor.execute('''CREATE TABLE alumnos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            clave VARCHAR(4) UNIQUE,
            nombre_escuela  VARCHAR(100),
            nivel_educativo VARCHAR(50),
            genero VARCHAR(10),
            edad VARCHAR(5),
            estado VARCHAR(10),
            motivo VARCHAR(100),
            ciclo VARCHAR(50))''')
            print('tabla creada')

        except sqlite3.OperationalError as mensaje:
            viewMessage.showerror("Base de datos", mensaje.args)
            self._conexion.close()

    def nuevoRegistro(self, parametros):
        try:
            if self.validarClave(parametros[0]) == 0:

                # self._conexionDB = sqlite3.connect('server/database/alumnosDB.db3')
                
                self._cursor.execute(f""" INSERT INTO alumnos VALUES (NULL, '{parametros[0]}', '{parametros[1]}',
                '{parametros[2]}', '{parametros[3]}', '{parametros[4]}', '{parametros[5]}', '{parametros[6]}', '{parametros[7]}'); """)

                
                self._conexionDB.commit()
                # self._conexionDB.close()

                viewMessage.showinfo("Nuevo registro", "Registro agregado correctamente")
                return 1

            else:
                viewMessage.showerror("Base de datos", f"La clave {parametros[0]} ya se encuentra registrada")
                return 0

        except sqlite3.DatabaseError as mensajeError:
            viewMessage.showerror("Base de datos", mensajeError.args)
            # self._conexion.close()
            return 0

    def modificarRegistro(self, params):
        try:
            # print(f"clave m : {params[0]}")

            if self.validarClave(params[0]) == 1:

                # self._conexionDB = sqlite3.connect('server/database/alumnosDB.db3')

                self._cursor.execute(f""" UPDATE alumnos SET nombre_escuela = '{params[1]}', nivel_educativo = '{params[2]}', 
                        genero = '{params[3]}', edad = '{params[4]}', estado = '{params[5]}', motivo = '{params[6]}', ciclo = '{params[7]}'
                        WHERE clave = '{params[0]}' """)

                self._conexionDB.commit()
                # self._conexionDB.close()
                viewMessage.showinfo("Nuevo registro", "Datos agregados exitosamente")
            else:
                viewMessage.showwarning("Modificar registro", f"No se ha encontrado la clave {params[0]}")

        except sqlite3.OperationalError as mensaje:
            viewMessage.showerror("Nuevo registro", mensaje.args)
            # self._conexionDB.close()

    def eliminarRegistro(self, clave):
        try:
            # self._conexionDB = sqlite3.connect('server/database/alumnosDB.db3')

            if self.validarClave(clave) == 1:
                self._cursor.execute(f""" DELETE FROM alumnos WHERE clave = '{clave}'""")
                self._conexionDB.commit()
                return 0
            else:
                return 1
        except sqlite3.DatabaseError as mensaje:
            viewMessage.showerror("Eliminar registro", mensaje.args)
            # self._conexionDB.close()
            return 1

    def buscarRegistro(self, clave):

        try:
            self.listaTemporal = {}
            # self._conexionDB = sqlite3.connect('server/database/alumnosDB.db3')
            print('entro a buscar')
            self._cursor.execute(f"""SELECT * FROM alumnos WHERE clave = '{clave}'""")

            if self._cursor.rowcount == 0:

                self.listaTemporal = {"error": 1 , "message": "sin registros"}
                return self.listaTemporal
            
            else:

                self.alumno = self._cursor.fetchall()

                for self.item in self.alumno:
                    
                    self.dato = {
                        "error": 0,
                        "id": self.item[0],
                        "clave": self.item[1],
                        "nombre_escuela": self.item[2],
                        "nivel_educativo": self.item[3],
                        "genero": self.item[4],
                        "edad": self.item[5],
                        "estado": self.item[6],
                        "motivo": self.item[7],
                        "ciclo": self.item[8]
                        
                    }

                    return self.dato

        except sqlite3.OperationalError as mensaje:
            viewMessage.showerror("validar clave", mensaje.args)
            # self._conexionDB.close()
    
    def validarClave(self, clave):
        try:
            self._cursor.execute(f""" SELECT * FROM alumnos WHERE clave = '{clave}' """)
            respueta = self._cursor.fetchall()
            print(f"numero de resultados {respueta}")
            if len(respueta) == 0:
                return 0
            else:
                return 1
            # print(len(respueta))
            # if len(respueta) > 0:
            #     return 0
            # else:
            #     return 1

        except sqlite3.OperationalError as mensaje:
            viewMessage.showerror("validar clave", mensaje.args)
            # self._conexionDB.close()
            return 1

    def todosLosRegistros(self):

        try:
            # self._conexionDB = sqlite3.connect('server/database/alumnosDB.db3')
            self._cursor.execute(f"""SELECT * FROM alumnos""")

            if self._cursor.rowcount == 0:
                return None
            else:
                self.respuesta = self._cursor.fetchall()
                self.listaRespuesta = []

                for self.registro in self.respuesta:
                    datos = {

                        "id": self.registro[0],
                        "clave": self.registro[1],
                        "nombre_escuela": self.registro[2],
                        "nivel_educativo": self.registro[3],
                        "genero": self.registro[4],
                        "edad": self.registro[5],
                        "estado": self.registro[6],
                        "motivo": self.registro[7],
                        "ciclo": self.registro[8]
                    }
                    self.listaRespuesta.append(datos)
                
                return self.listaRespuesta
        except sqlite3.OperationalError as mensaje:
            viewMessage.showerror("Base Datos", mensaje.args)
            # self._conexionDB.close()
            return 1

    
