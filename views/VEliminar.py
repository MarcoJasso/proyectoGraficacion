from tkinter import *
# from PIL import ImageTk, Image
from tkinter import ttk
from server.querys.Querys import Querys
from tkinter import messagebox as viewMessage

class VEliminar():

    def inicicarVentana(self):

        self.varClave = StringVar()
        
        self.rootVE = Toplevel()

        self.w_ventanaE = 300
        self.h_ventanaE = 300

        self.x_ventanaA = self.rootVE.winfo_screenwidth() // 2 - self.w_ventanaE // 2
        self.y_ventanaA = self.rootVE.winfo_screenheight() // 2 - self.h_ventanaE // 2

        self.posicion = str(self.w_ventanaE) + "x" + str(self.h_ventanaE) + "+" + str(self.x_ventanaA) + "+" + str(self.y_ventanaA)
        self.rootVE.geometry(self.posicion)
        self.rootVE.title("Eliminar registro")
        self.rootVE.iconbitmap("assets/editar_ico.ico")

        self.componentes()

        self.rootVE.mainloop()

    def componentes(self):

        self.font_text = "Arial 18 normal"

        self.contenedor = Frame(self.rootVE, width=self.w_ventanaE, height=self.h_ventanaE)
        
        # ========== Marco de ventana ==============
        self.img_lbl_marco = PhotoImage(file="assets/boton-x.png")
        self.img_lbl_marco = self.img_lbl_marco.subsample(10, 10)

        self.lbl_leyenda_marco = Label(self.contenedor, text="Agregar dato", font=self.font_text, justify=LEFT, anchor="w")
        self.lbl_leyenda_marco.place(x=100, y=15, width=150, height=50)

        self.lbl_logo_marco = Label(self.contenedor, image=self.img_lbl_marco)
        self.lbl_logo_marco.place(x=30, y=10, width=60, height=60)

        self.btn_Actualizar = Button(self.contenedor, text="Borrar", command= lambda: self.eliminarClave(str(self.cbx_claveE.get())))
        self.btn_Actualizar.place(width=100, height=30, x=110, y=250)
        self.btn_Actualizar.config(bd=0, bg="#BF360C", fg="white", font=(self.font_text, 10, "bold"))

        # Combobox para nivel educativo
        self.lbl_clave = Label(self.contenedor, text="Clave:", font=(self.font_text, 10, "bold"), anchor="e")
        self.lbl_clave.place(x=20, y=100, width=50, height=20)
        self.lbl_clave.config(fg='black')

        # ========== ComboBox con las claves registradas en la DB ====================
        self.clavesR = ["Selecciona"]
        self.consulta = Querys()
        self.respuesta = self.consulta.todosLosRegistros()

        if self.respuesta != None:

            for self.item in self.respuesta:
                self.clavesR.append(self.item['clave'])

        self.cbx_claveE = ttk.Combobox(self.contenedor, values=self.clavesR, state="readonly")
        self.cbx_claveE.place(x=100, y=100, width=150)
        self.cbx_claveE.current(0)

        self.contenedor.pack()

    def eliminarClave(self, clave):
        print(f"clave eliminar :{clave}.")
        if self.consulta.eliminarRegistro(clave) == 0:
            viewMessage.showinfo("Eliminar registro", f"El registro con la clave {clave} ha sido eliminado")
            self.actualizarCombo()
        else:
            viewMessage.showerror("Eliminar registro", f"El registro con la clave {clave} No se elimino\n puede que no se encuentre registrado")

    def actualizarCombo(self):
        # print(f"tamaño combobox : {str(self.cbx_claveE.size())}")
        self.cbx_claveE.delete(0)
        
        self.clavesR = ["Selecciona"]

        self.respuesta = self.consulta.todosLosRegistros()

        if self.respuesta != None:
            for self.item in self.respuesta:
                self.clavesR.append(self.item['clave'])
        
        self.cbx_claveE.config(values=self.clavesR)

        self.cbx_claveE.current(0)
        
