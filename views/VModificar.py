from server.querys.Querys import Querys
from tkinter import *
# from PIL import ImageTk, Image
from tkinter import messagebox as viewMessage
from tkinter import ttk

class VModificar():

    def mostrarVentanaM(self):

        self.varClaveM = StringVar()
        self.varNombreEscM = StringVar()

        self.rootVM = Toplevel()

        self.w_ventanaM = 700
        self.h_ventanaM = 400

        self.x_ventanaM = self.rootVM.winfo_screenwidth() // 2 - self.w_ventanaM // 2
        self.y_ventanaM = self.rootVM.winfo_screenheight() // 2 - self.h_ventanaM // 2

        self.posicion = str(self.w_ventanaM) + "x" + str(self.h_ventanaM) + "+" + str(self.x_ventanaM) + "+" + str(self.y_ventanaM)
        self.rootVM.geometry(self.posicion)
        self.rootVM.title("Modifiar registro")
        self.rootVM.iconbitmap("assets/editar_ico.ico")

        self.componentesM()

        self.rootVM.mainloop()
    
    def componentesM(self):

        self.alumnoEncontrado = {}

        self.font_text = "Arial 18 normal"
        self.contenedor = Frame(self.rootVM, width=self.w_ventanaM, height=self.h_ventanaM)

        self.img_lbl_marco = PhotoImage(file="assets/editar.png")
        self.img_lbl_marco = self.img_lbl_marco.subsample(10, 10)

        self.lbl_leyenda_marco = Label(self.contenedor, text="Modiciar datos", font=self.font_text, justify=LEFT, anchor="w")
        self.lbl_leyenda_marco.place(x=320, y=15, width=170, height=50)

        self.lbl_logo_marco = Label(self.contenedor, image=self.img_lbl_marco)
        self.lbl_logo_marco.place(x=250, y=10, width=60, height=60)

        # =================== Contenedores  datos ==============
        self.lbl_clave = Label(self.contenedor, text="Clave : ", font=(self.font_text, 10), anchor="e")
        self.lbl_clave.place(x=20, y=100, width=110, height=20)
        self.lbl_clave.config(fg='black')

        self.tf_clave = Entry(self.contenedor, textvariable=self.varClaveM)
        self.tf_clave.place(x=130, y=100, width=100, height=20)

        self.lbl_nombre_escuela = Label(self.contenedor, text="Nombre escuela : ", font=(self.font_text, 10), anchor="w")
        self.lbl_nombre_escuela.place(x=20, y=150, width=110, height=20)
        self.lbl_nombre_escuela.config(fg='black')

        self.tf_nombre_escuela = Entry(self.contenedor, textvariable=self.varNombreEscM)
        self.tf_nombre_escuela.place(x=130, y=150, width=140, height=20)

        self.btn_Actualizar = Button(self.contenedor, text="Actualizar",
                            command=lambda: self.modificarDatosAlumno(str(self.varClaveM.get()),
                                                                str(self.varNombreEscM.get()),
                                                                 self.cbx_secciones.get(),
                                                                 self.cbx_genero.get(),
                                                                 self.cbx_Edad.get(),
                                                                 self.cbx_Estado.get(), 
                                                                 self.cbx_Motivo.get(),
                                                                 self.cbx_CicloM.get()))

        self.btn_Actualizar.place(width=100, height=30, x=370, y=350)
        self.btn_Actualizar.config(bd=0, bg="#79B705", fg="white", font=(self.font_text, 10, "bold"))

        self.btn_cancelar = Button(self.contenedor, text="Cancelar")
        self.btn_cancelar.place(width=100, height=30, x=220, y=350, )
        self.btn_cancelar.config(bd=0, bg="#BF4702", fg="white", font=(self.font_text, 10, "bold"))

        self.btn_buscar = Button(self.contenedor, text="Buscar", command=lambda: self.buscarClaveRegistro(clave=str(self.varClaveM.get())))
        self.btn_buscar.place(width=100, height=30, x=370, y=90)
        self.btn_buscar.config(bd=0, bg="#E5BC03", fg="white", font=(self.font_text, 10, "bold"))

        # Combobox para nivel educativo
        self.lbl_nivelEducatico = Label(self.contenedor, text="Nivel educativo :", font=(self.font_text, 10), anchor="e")
        self.lbl_nivelEducatico.place(x=20, y=190, width=110, height=20)
        self.lbl_nombre_escuela.config(fg='black')

        self.opcionesNivelEdu = ["Selecciona", "Primaria", "Secundaria Matutina", "Secundaria Vespertina", "Bachillerato", "Universidad",
                        "Posgrado", "Maestria"]
        self.cbx_secciones = ttk.Combobox(self.contenedor, values=self.opcionesNivelEdu, state="readonly")
        self.cbx_secciones.place(x=130, y=190)
        self.cbx_secciones.current(0)

        # Combobox para genero
        self.lbl_genero = Label(self.contenedor, text="Genero :", font=(self.font_text, 10), anchor="e")
        self.lbl_genero.place(x=20, y=230, width=110, height=20)
        self.lbl_genero.config(fg='black')

        self.opcionesGneero = ["Selecciona", "Femenino", "Masculino"]
        self.cbx_genero = ttk.Combobox(self.contenedor, values=self.opcionesGneero, state="readonly")
        self.cbx_genero.place(x=130, y=230)
        self.cbx_genero.current(0)

        # Combobox para Edad
        self.lbl_Edad = Label(self.contenedor, text="Edad :", font=(self.font_text, 10), anchor="w")
        self.lbl_Edad.place(x=300, y=150, width=50, height=20)
        self.lbl_Edad.config(fg='black')

        self.opcionesEdad = ["Selecciona"]
        for i in range(6, 31, 1):
            self.opcionesEdad.append(str(i))

        self.cbx_Edad = ttk.Combobox(self.contenedor, values=self.opcionesEdad, state="readonly")
        self.cbx_Edad.place(x=350, y=150)
        self.cbx_Edad.current(0)

        # Combobox para Estado
        self.lbl_Estado = Label(self.contenedor, text="Estado :", font=(self.font_text, 10), anchor="w")
        self.lbl_Estado.place(x=290, y=190, width=50, height=20)
        self.lbl_Estado.config(fg='black')

        self.opcionesEstado = ["Selecciona", "Activo", "Baja"]
        self.cbx_Estado = ttk.Combobox(self.contenedor, values=self.opcionesEstado, state="readonly")
        self.cbx_Estado.place(x=350, y=190)
        self.cbx_Estado.current(0)

        # Combobox para motivo
        self.lbl_Motivo = Label(self.contenedor, text="Motivo :", font=(self.font_text, 10), anchor="w")
        self.lbl_Motivo.place(x=290, y=230, width=50, height=20)
        self.lbl_Motivo.config(fg='black')

        self.opcionesMotivo = ["Selecciona", "Efectivo", "Pandemia", "Familiares", "Horarios", "Forma de impartir clases", "Otro"]
        self.cbx_Motivo = ttk.Combobox(self.contenedor, values=self.opcionesMotivo, state="readonly")
        self.cbx_Motivo.place(x=350, y=230)
        self.cbx_Motivo.current(0)

        # ==== ciclo que curso ====
        self.lbl_cicloM = Label(self.contenedor, text="Ciclo :", font=(self.font_text, 10), anchor="w")
        self.lbl_cicloM.place(x=85, y=270, width=50, height=20)
        self.lbl_cicloM.config(fg='black')

        self.opcionesCicloM = ["Selecciona", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2019", "2020"]
        self.cbx_CicloM = ttk.Combobox(self.contenedor, values=self.opcionesCicloM, state="readonly")
        self.cbx_CicloM.place(x=130, y=270)
        self.cbx_CicloM.current(0)

        self.contenedor.pack()

    def buscarClaveRegistro(self, clave):
        sentencia = Querys()
        self.alumnoEncontrado = sentencia.buscarRegistro(clave=clave)

        if self.alumnoEncontrado != None:
            self.varNombreEscM.set(self.alumnoEncontrado['nombre_escuela'])
            
            self.cbx_Edad.set(self.alumnoEncontrado['edad'])
            self.cbx_CicloM.set(self.alumnoEncontrado['ciclo'])
            self.cbx_Estado.set(self.alumnoEncontrado['estado'])
            self.cbx_genero.set(self.alumnoEncontrado['genero'])
            self.cbx_Motivo.set(self.alumnoEncontrado['motivo'])
            self.cbx_secciones.set(self.alumnoEncontrado['nivel_educativo'])
            print(self.alumnoEncontrado)
        

    def modificarDatosAlumno(self, clave, NombreEsc, seccion, Genero, Edad, Estado, Motivo, Ciclo):
        sentencia = Querys()
        datosModificados = [clave, NombreEsc, seccion, Genero, Edad, Estado, Motivo, Ciclo]
        sentencia.modificarRegistro(datosModificados)