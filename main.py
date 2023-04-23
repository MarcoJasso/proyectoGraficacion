from views.Principal import Principal
# from server.querys.Querys import Querys
# from rutas.GraficaMotivos import GraficaMotivos

def iniciarApp():
    # consulta = Querys()
    # consulta.crearBaseDatos()
    # nuevosDatos = ['AL01', 'MODIFICADO 2', 'PRIMARIA', 'Femenino', '17', 'Baja', 'Efectivo', '2010']
    # consulta.nuevoRegistro(nuevosDatos)
    # consulta.modificarRegistro(nuevosDatos)
    # consulta.eliminarRegistro(nuevosDatos[0])

    ventanaP = Principal()
    ventanaP.inicicarVentana()

    # grafica = GraficaMotivos()
    # grafica.mostrarGrafica()

    # sentencia = Querys()
    # respuesta = sentencia.todosLosRegistros()

    # for item in respuesta:
    #     print(item['clave'] + " " + item['edad'])

    
    

if __name__ == '__main__':
    iniciarApp()