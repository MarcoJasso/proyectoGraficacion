from server.querys.Querys import Querys
from tkinter import *
# from PIL import ImageTk, Image

from tkinter import ttk

class VAagregar():


    def mostrarVentanaA(self):

        self.varClave = StringVar()
        self.varNombreEsc = StringVar()

        self.rootVA = Toplevel()

        self.w_ventanaA = 700
        self.h_ventanaA = 400

        self.x_ventanaA = self.rootVA.winfo_screenwidth() // 2 - self.w_ventanaA // 2
        self.y_ventanaA = self.rootVA.winfo_screenheight() // 2 - self.h_ventanaA // 2

        self.posicion = str(self.w_ventanaA) + "x" + str(self.h_ventanaA) + "+" + str(self.x_ventanaA) + "+" + str(self.y_ventanaA)
        self.rootVA.geometry(self.posicion)
        self.rootVA.title("Nuevo registro")
        self.rootVA.iconbitmap("assets/editar_ico.ico")

        self.componentes()

        self.rootVA.mainloop()

    def componentes(self):
        self.font_text = "Arial 18 normal"

        self.contenedor = Frame(self.rootVA, width=self.w_ventanaA, height=self.h_ventanaA)
        
        # ========== Marco de ventana ==============
        self.img_lbl_marco = PhotoImage(file="assets/masA.png")
        self.img_lbl_marco = self.img_lbl_marco.subsample(10, 10)

        self.lbl_leyenda_marco = Label(self.contenedor, text="Agregar dato", font=self.font_text, justify=LEFT, anchor="w")
        self.lbl_leyenda_marco.place(x=320, y=15, width=150, height=50)

        self.lbl_logo_marco = Label(self.contenedor, image=self.img_lbl_marco)
        self.lbl_logo_marco.place(x=250, y=10, width=60, height=60)

        # ============ cajas de texto ===========

        self.lbl_clave = Label(self.contenedor, text="Clave : ", font=(self.font_text, 10), anchor="e")
        self.lbl_clave.place(x=20, y=100, width=110, height=20)
        self.lbl_clave.config(fg='black')

        self.tf_clave = Entry(self.contenedor, textvariable=self.varClave)
        self.tf_clave.place(x=130, y=100, width=100, height=20)

        # command=lambda: elementoSeleccionado(str(varClave.get()), str(varNombreEsc.get()), cbx_secciones.get(), cbx_genero.get(), cbx_Edad.get(), cbx_Estado.get(), cbx_Motivo.get(), cbx_Ciclo.get()))

        self.lbl_nombre_escuela = Label(self.contenedor, text="Nombre escuela : ", font=(self.font_text, 10), anchor="w")
        self.lbl_nombre_escuela.place(x=20, y=150, width=110, height=20)
        self.lbl_nombre_escuela.config(fg='black')

        self.tf_nombre_escuela = Entry(self.contenedor, textvariable=self.varNombreEsc)
        self.tf_nombre_escuela.place(x=130, y=150, width=140, height=20)

        self.btn_guardar = Button(self.contenedor, text="Guardar", command=lambda: self.registrarDatos(str(self.varClave.get()), str(self.varNombreEsc.get()), self.cbx_secciones.get(), self.cbx_genero.get(), self.cbx_Edad.get(), self.cbx_Estado.get(), self.cbx_Motivo.get(), self.cbx_Ciclo.get()))
        self.btn_guardar.place(width=100, height=30, x=370, y=350, )
        self.btn_guardar.config(bd=0, bg="#79B705", fg="white", font=(self.font_text, 10, "bold"))

        self.btn_cancelar = Button(self.contenedor, text="Cancelar")
        self.btn_cancelar.place(width=100, height=30, x=220, y=350, )
        self.btn_cancelar.config(bd=0, bg="#BF4702", fg="white", font=(self.font_text, 10, "bold"))

        # Combobox para nivel educativo
        self.lbl_nivelEducatico = Label(self.contenedor, text="Nivel educativo :", font=(self.font_text, 10), anchor="e")
        self.lbl_nivelEducatico.place(x=20, y=190, width=110, height=20)
        self.lbl_nombre_escuela.config(fg='black')

        self.opcionesNivelEdu = ["Selecciona","Primaria", "Secundaria Matutina", "Secundaria Vespertina", "Bachillerato", "Universidad",
                            "Posgrado", "Maestria"]
        self.cbx_secciones = ttk.Combobox(self.contenedor, values=self.opcionesNivelEdu, state="readonly")
        self.cbx_secciones.place(x=130, y=190)
        self.cbx_secciones.current(0)

        # Combobox para genero
        self.lbl_genero = Label(self.contenedor, text="Genero :", font=(self.font_text, 10), anchor="e")
        self.lbl_genero.place(x=20, y=230, width=110, height=20)
        self.lbl_genero.config(fg='black')

        self.opcionesGneero = ["Selecciona","Femenino", "Masculino"]
        self.cbx_genero = ttk.Combobox(self.contenedor, values=self.opcionesGneero, state="readonly")
        self.cbx_genero.place(x=130, y=230)
        self.cbx_genero.current(0)

        # Combobox para Edad
        self.lbl_Edad = Label(self.contenedor, text="Edad :", font=(self.font_text, 10), anchor="w")
        self.lbl_Edad.place(x=300, y=100, width=50, height=20)
        self.lbl_Edad.config(fg='black')

        self.opcionesEdad = ["Selecciona"]
        for i in range(6, 31, 1):
            self.opcionesEdad.append(str(i))

        self.cbx_Edad = ttk.Combobox(self.contenedor, values=self.opcionesEdad, state="readonly")
        self.cbx_Edad.place(x=350, y=100)
        self.cbx_Edad.current(0)

        # Combobox para Estado
        self.lbl_Estado = Label(self.contenedor, text="Estado :", font=(self.font_text, 10), anchor="w")
        self.lbl_Estado.place(x=290, y=150, width=50, height=20)
        self.lbl_Estado.config(fg='black')

        self.opcionesEstado = ["Selecciona","Activo", "Baja"]
        self.cbx_Estado = ttk.Combobox(self.contenedor, values=self.opcionesEstado, state="readonly")
        self.cbx_Estado.place(x=350, y=150)
        self.cbx_Estado.current(0)

        # Combobox para motivo
        self.lbl_Motivo = Label(self.contenedor, text="Motivo :", font=(self.font_text, 10), anchor="w")
        self.lbl_Motivo.place(x=290, y=190, width=50, height=20)
        self.lbl_Motivo.config(fg='black')

        self.opcionesMotivo = ["Selecciona","Efectivo", "Pandemia", "Familiares", "Horarios", "Forma de impartir clases", "Otro"]
        self.cbx_Motivo = ttk.Combobox(self.contenedor, values=self.opcionesMotivo, state="readonly")
        self.cbx_Motivo.place(x=350, y=190)
        self.cbx_Motivo.current(0)

        # ==== ciclo que curso ====
        self.lbl_ciclo = Label(self.contenedor, text="Ciclo :", font=(self.font_text, 10), anchor="w")
        self.lbl_ciclo.place(x=290, y=230, width=50, height=20)
        self.lbl_ciclo.config(fg='black')

        self.opcionesCiclo = ["Selecciona","2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2019", "2020"]
        self.cbx_Ciclo = ttk.Combobox(self.contenedor, values=self.opcionesCiclo, state="readonly")
        self.cbx_Ciclo.place(x=350, y=230)
        self.cbx_Ciclo.current(0)

        self.contenedor.pack()

    def registrarDatos(self, clave, NombreEsc, Seccion, Genero, Edad, Estado, Motivo, Ciclo):
        # print(f"Clave : {clave}\nNombre Escuela: {NombreEsc}\nSeccion: {Seccion}\nGenero: {Genero}\nEdad: {Edad}\nEstado: {Estado}\nMotivo: {Motivo}\nCiclo: {Ciclo}")
        nuevosDatos = [clave, NombreEsc, Seccion, Genero, Edad, Estado, Motivo, Ciclo]
        sentencia = Querys()
        
        if sentencia.nuevoRegistro(nuevosDatos) == 1:

            self.varClave.set("")
            self.varNombreEsc.set("")
            self.cbx_Ciclo.current(0)
            self.cbx_Edad.current(0)
            self.cbx_Estado.current(0)
            self.cbx_genero.current(0)
            self.cbx_Motivo.current(0)
            self.cbx_secciones.current(0)
