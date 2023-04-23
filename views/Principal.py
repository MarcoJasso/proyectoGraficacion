from tkinter import *
# from PIL import ImageTk, Image
from views.VAgregar import VAagregar
from views.VModificar import VModificar
from views.VEliminar import VEliminar
from rutas.GraficaMotivos import GraficaMotivos
from server.querys.Querys import Querys

class Principal():   

    def inicicarVentana(self):

        self.rootPrincipal = Tk()

        self.w_ventanaP = 800
        self.h_ventanaP = 500

        self.x_ventanaP = self.rootPrincipal.winfo_screenwidth() // 2 - self.w_ventanaP // 2
        self.y_ventanaP = self.rootPrincipal.winfo_screenheight() // 2 - self.h_ventanaP // 2

        self.posicion = str(self.w_ventanaP) + "x" + str(self.h_ventanaP) + "+" + str(self.x_ventanaP) + "+" + str(self.y_ventanaP)
        self.rootPrincipal.geometry(self.posicion)
        self.rootPrincipal.title("Proyecto final")
        self.rootPrincipal.iconbitmap("assets/iconoGrf.ico")

        self.menuOpciones()

        self.rootPrincipal.mainloop()


    def menuOpciones(self):

        self.ventanaAgreagr = VAagregar()
        self.ventanaModificar = VModificar()
        self.ventanaEliminar = VEliminar()
        self.graficas = GraficaMotivos()
        self.crear = Querys()
        
        # ============== Menu Raiz =========================

        self.barraMenu = Menu(self.rootPrincipal)

        # =============== Imagenes de la barra de menu ====================

        self.img_connect = PhotoImage(file="assets/conectado.png")
        self.img_connect = self.img_connect.subsample(20, 20)
        self.img_add = PhotoImage(file="assets/mas.png")
        self.img_add = self.img_add.subsample(20, 20)
        self.img_delete = PhotoImage(file="assets/boton-x.png")
        self.img_delete = self.img_delete.subsample(20, 20)
        self.img_search = PhotoImage(file="assets/lupa.png")

        self.img_search = self.img_search.subsample(20, 20)
        self.img_edit = PhotoImage(file="assets/editar.png")
        self.img_edit = self.img_edit.subsample(20, 20)

        # ================= Conexion base de datos ========================
        self.columna_db = Menu(self.barraMenu, tearoff=0)
        self.columna_db.add_command(label='   Crear database', image=self.img_connect, underline=0, compound=LEFT)

        # ========================== CRUD =============================

        self.columna_consultas = Menu(self.barraMenu, tearoff=0)
        self.columna_consultas.add_command(label="Agregar", image=self.img_add, underline=0, compound=LEFT, command= lambda: self.ventanaAgreagr.mostrarVentanaA())
        self.columna_consultas.add_command(label="Consultar", image=self.img_search, underline=0, compound=LEFT)
        self.columna_consultas.add_command(label="Modificar", image=self.img_edit, underline=0, compound=LEFT, command= lambda: self.ventanaModificar.mostrarVentanaM())
        self.columna_consultas.add_command(label="Borrar", image=self.img_delete, underline=0, compound=LEFT, command= lambda: self.ventanaEliminar.inicicarVentana())
        

        # ============= Menu graficas =====================

        self.columna_graficas = Menu(self.barraMenu, tearoff=0)
        self.columna_graficas.add_command(label='Grafica motivos')
        self.columna_graficas.add_command(label='Grafica niveles educativos afectados', command=lambda : self.graficas.mostarGraficaBarrar())
        self.columna_graficas.add_command(label='Grafica genero predominante', command=lambda : self.graficas.mostrarGraficaPastel())
        self.columna_graficas.add_command(label='Grafica edades afectadas')
        self.columna_graficas.add_command(label='Grafica probabilistica')

        
        # ============== Agregar los submenus ================
        self.barraMenu.add_cascade(label="Base de datos", menu=self.columna_db)
        self.barraMenu.add_cascade(label="Consultas", menu=self.columna_consultas)
        self.barraMenu.add_cascade(label="Graficas" ,menu=self.columna_graficas)

        self.rootPrincipal.config(menu=self.barraMenu)
    
    def mostarVentanaAdd(self):
        self.rootPrincipal.destroy()