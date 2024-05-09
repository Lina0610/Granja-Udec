#importar para interfaz grafica 
import tkinter as tk
from tkinter import LabelFrame, Entry, Button, ttk, messagebox
#importar las funciones para las tablas
from datos import *
#todos los complementos de la clase 
from tkinter import*
#importar la conexion a las dos tablas
from Conexion import *
from PIL import Image,ImageTk

#definir la clase principal de la interfaz
class VentanaPrincipal:
        
    #se define el constructor de nuestra clase, con el parametro base 
    def __init__(self, base):
        
        #se usa el self para definir los metodos de nuestra clase ventana 
        #ademas definimos los atributos 
        self.textBoxNameCultivo = tk.Entry()
        self.textBoxId = None
        self.textBoxTipoCultivo = None
        self.textBoxAreaCultivo = None
        self.textBoxRendimiento = None
        
        self.textBoxEspecie = None
        self.textBoxIdGanado = None
        self.textBoxRaza = None
        self.textBoxEdad = None
        self.textBoxPeso = None
        self.textBoxProduccion = None
        
        self.groupBox = None
        self.tree = None
        
        # se usa el base para definir la ventana de la interfaz
        self.base = base
        self.base.title("Bienvenido al Sistema")
        self.base.geometry("500x500")
        
        labelInicio = tk.Label(base, text="Sistema de gestión", font=("Arial", 20, "bold"))
        labelInicio.pack(pady=50)

        labelInicio = tk.Label(base, text="Granja Ucundinamarca", font=("Arial", 18)) 
        labelInicio.pack(pady=10)
        
        #creamos los botones, usamos el command para las ventanas
        buttonCultivos = tk.Button(base, text="Agregar Datos de Cultivos", command=self.abrir_ventana_cultivos)
        buttonCultivos.pack(pady=20)

        buttonGanaderos = tk.Button(base, text="Agregar Datos de Ganaderos", command=self.abrir_ventana_ganaderos)
        buttonGanaderos.pack(pady=20)
        
        buttonInforme = tk.Button(self.base, text="Reporte de Producción", command=self.abrir_ventana_informe)
        buttonInforme.pack(pady=20)
        


#Ventana de cultivos 
    def abrir_ventana_cultivos(self):
        
        
        ventana_cultivos = tk.Toplevel(self.base)
        ventana_cultivos.title("Agregar Datos de Cultivos")
        ventana_cultivos.geometry("1200x300")
        
        groupBox = LabelFrame(ventana_cultivos, text="Datos del Cultivo", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        self.textBoxId = tk.Entry(groupBox)
        self.textBoxNameCultivo = tk.Entry(groupBox)
        self.textBoxTipoCultivo = tk.Entry(groupBox)
        self.textBoxAreaCultivo = tk.Entry(groupBox)
        self.textBoxRendimiento = tk.Entry(groupBox)

        labelIdCultivo = tk.Label(groupBox,text="Id",width=12,font=("arial",12)).grid(row=0,column=0)
        self.textBoxId.grid(row=0,column=1)

        labelNameCultivo = tk.Label(groupBox,text="Nombre del \n cultivo: ",width=12,font=("arial",12)).grid(row=1,column=0)
        self.textBoxNameCultivo.grid(row=1,column=1)

        labelTipoCultivo = tk.Label(groupBox,text="Tipo Cultivo: ",width=12,font=("arial",12)).grid(row=2,column=0)
        self.textBoxTipoCultivo.grid(row=2,column=1)

        labelAreaCultivo = tk.Label(groupBox,text="Area Cultivo",width=12,font=("arial",12)).grid(row=3,column=0)
        self.textBoxAreaCultivo.grid(row=3,column=1)

        labelRendimiento = tk.Label(groupBox,text="Rendimiento",width=12,font=("arial",12)).grid(row=4,column=0)
        self.textBoxRendimiento.grid(row=4,column=1)

        tk.Button(groupBox,text="Guardar",width=10,command=self.guardarCultivos).grid(row=7,column=0)
        tk.Button(groupBox,text="Modificar",width=10,command=self.modificarCultivos).grid(row=7,column=1)
        tk.Button(groupBox,text="Eliminar",width=10,command=self.eliminarCultivos).grid(row=7,column=2)

        groupBox = LabelFrame(ventana_cultivos,text= "Lista de Cultivos", padx=5, pady=5,)
        groupBox.grid(row=0,column=1,padx=10,pady=10)

        self.tree = ttk.Treeview(groupBox,columns=("Id","Nombre Cultivo","Tipo Cultivo","Area de Cultivo","Rendimiento"),show='headings',height=5)
        self.tree.column("# 1", anchor=tk.CENTER,width=50)
        self.tree.heading("# 1", text="Id")
        self.tree.column("# 2", anchor=tk.CENTER,width=200)
        self.tree.heading("# 2", text="Nombre del Cultivo")
        self.tree.column("# 3", anchor=tk.CENTER,width=150)
        self.tree.heading("# 3", text="Tipo de Cultivo")
        self.tree.column("# 4", anchor=tk.CENTER,width=150)
        self.tree.heading("# 4", text="Area de Cultivo")
        self.tree.column("# 5", anchor=tk.CENTER,width=150)
        self.tree.heading("# 5", text="Rendimiento")
        
        #mostar la tabla

        for row in CDatosCultivos.mostrarCultivos():
            self.tree.insert("", "end", values=row)

        #funcion de hacer clic para mostrar los entry

        self.tree.bind("<<TreeviewSelect>>", self.seleccionarCultivo)
        self.tree.pack()
        

    def guardarCultivos(self):
        
        nombreCultivo = self.textBoxNameCultivo.get()
        tipoCultivo = self.textBoxTipoCultivo.get()
        areaCultivo = self.textBoxAreaCultivo.get()
        rendimientoCultivo = self.textBoxRendimiento.get()
        CDatosCultivos.ingresarCultivos(nombreCultivo, tipoCultivo, areaCultivo, rendimientoCultivo)
        messagebox.showinfo("Informacion","Los datos fueron guardados ")
        self.actualizarCultivos()
        self.limpiarCamposCultivo()

    def actualizarCultivos(self):
        if self.tree is not None:
            self.tree.delete(*self.tree.get_children())
            for row in CDatosCultivos.mostrarCultivos():
                self.tree.insert("", "end", values=row)
        else: 
            print("No inicializado el tree")

    def seleccionarCultivo(self, event):
        
        itemSeleccionado = self.tree.focus()
        if itemSeleccionado: 
            values = self.tree.item(itemSeleccionado)['values']
            self.textBoxId.delete(0, tk.END)
            self.textBoxId.insert(0, values[0])
            self.textBoxNameCultivo.delete(0, tk.END)
            self.textBoxNameCultivo.insert(0, values[1])
            self.textBoxTipoCultivo.delete(0, tk.END)
            self.textBoxTipoCultivo.insert(0, values[2])
            self.textBoxAreaCultivo.delete(0, tk.END)
            self.textBoxAreaCultivo.insert(0, values[3])
            self.textBoxRendimiento.delete(0, tk.END)
            self.textBoxRendimiento.insert(0, values[4])

    def modificarCultivos(self):
        idCultivo = self.textBoxId.get()
        nombreCultivo = self.textBoxNameCultivo.get()
        tipoCultivo = self.textBoxTipoCultivo.get()
        areaCultivo = self.textBoxAreaCultivo.get()
        rendimientoCultivo = self.textBoxRendimiento.get()
        CDatosCultivos.modificarCultivos(idCultivo, nombreCultivo, tipoCultivo, areaCultivo, rendimientoCultivo)
        messagebox.showinfo("Informacion","Los datos fueron modificados ")
        self.actualizarCultivos()
        self.limpiarCamposCultivo()

    def eliminarCultivos(self):
        idCultivo = self.textBoxId.get()
        nombreCultivo = self.textBoxNameCultivo.get()
        tipoCultivo = self.textBoxTipoCultivo.get()
        areaCultivo = self.textBoxAreaCultivo.get()
        rendimientoCultivo = self.textBoxRendimiento.get()

        CDatosCultivos.eliminarCultivos(idCultivo, nombreCultivo, tipoCultivo, areaCultivo, rendimientoCultivo)
        messagebox.showinfo("Informacion","Los datos fueron eliminados ")
        self.actualizarCultivos()
        self.limpiarCamposCultivo()


    def limpiarCamposCultivo(self):
        self.textBoxId.delete(0, tk.END)
        self.textBoxNameCultivo.delete(0, tk.END)
        self.textBoxTipoCultivo.delete(0, tk.END)
        self.textBoxAreaCultivo.delete(0, tk.END)
        self.textBoxRendimiento.delete(0, tk.END)

#ventana ganaderos 
    def abrir_ventana_ganaderos(self):
        ventana_ganaderos = tk.Toplevel(self.base)
        ventana_ganaderos.title("Agregar Datos de Ganaderos")
        ventana_ganaderos.geometry("1200x300")
        
        groupBox = LabelFrame(ventana_ganaderos, text="Datos de los Bovinos", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        self.textBoxIdGanado= tk.Entry(groupBox)
        self.textBoxEspecie = tk.Entry(groupBox)
        self.textBoxRaza = tk.Entry(groupBox)
        self.textBoxEdad = tk.Entry(groupBox)
        self.textBoxPeso = tk.Entry(groupBox)
        self.textBoxProduccion = tk.Entry(groupBox)
        
        labelIdGanado = tk.Label(groupBox,text="Id",width=12,font=("arial",12)).grid(row=0,column=0)
        self.textBoxIdGanado.grid(row=0,column=1)

        labelEspecie = tk.Label(groupBox,text="Especie: ",width=12,font=("arial",12)).grid(row=1,column=0)
        self.textBoxEspecie.grid(row=1,column=1)

        labelRaza = tk.Label(groupBox, text="Raza: ", width=12, font=("arial", 12)).grid(row=2,column=0)
        self.textBoxRaza.grid(row=2,column=1)

        labelEdad = tk.Label(groupBox,text="Edad",width=12,font=("arial",12)).grid(row=3,column=0)
        self.textBoxEdad.grid(row=3,column=1)

        labelPeso = tk.Label(groupBox,text="Peso",width=12,font=("arial",12)).grid(row=4,column=0)
        self.textBoxPeso.grid(row=4,column=1)
        
        labelProduccion = tk.Label(groupBox,text="Produccion",width=12,font=("arial",12)).grid(row=5,column=0)
        self.textBoxProduccion.grid(row=5,column=1)
        
        tk.Button(groupBox,text="Guardar",width=10,command=self.guardarGanado).grid(row=7,column=0)
        tk.Button(groupBox,text="Modificar",width=10,command=self.modificarGanado).grid(row=7,column=1)
        tk.Button(groupBox,text="Eliminar",width=10,command=self.eliminarGanado).grid(row=7,column=2)

        groupBox = LabelFrame(ventana_ganaderos,text= "Lista de Bovinos", padx=6, pady=6,)
        groupBox.grid(row=0,column=1,padx=10,pady=10)

        self.tree = ttk.Treeview(groupBox,columns=("Id","Especie","Raza","Edad","Peso","Produccion"),show='headings',height=6)
        self.tree.column("# 1", anchor=tk.CENTER, width=50)
        self.tree.heading("# 1", text="Id")
        self.tree.column("# 2", anchor=tk.CENTER,width=150)
        self.tree.heading("# 2", text="Especie")
        self.tree.column("# 3", anchor=tk.CENTER,width=150)
        self.tree.heading("# 3", text="Raza")
        self.tree.column("# 4", anchor=tk.CENTER,width=150)
        self.tree.heading("# 4", text="Edad")
        self.tree.column("# 5", anchor=tk.CENTER,width=150)
        self.tree.heading("# 5", text="Peso")
        self.tree.column("# 6", anchor=tk.CENTER,width=150)
        self.tree.heading("# 6", text="Producción")
        
        #mostar la tabla

        for row in CDatosGanado.mostrarGanado():
            self.tree.insert("", "end", values=row)

        #funcion de hacer clic para mostrar los entry

        self.tree.bind("<<TreeviewSelect>>", self.seleccionarGanado)
        self.tree.pack()
        
    def guardarGanado(self):

        nombreEspecie = self.textBoxEspecie.get()
        nombreRaza = self.textBoxRaza.get()
        edadGanado = self.textBoxEdad.get()
        pesoGanado = self.textBoxPeso.get()
        produccionGanado = self.textBoxProduccion.get()
        CDatosGanado.ingresarGanado(nombreEspecie,nombreRaza,edadGanado,pesoGanado,produccionGanado)
        messagebox.showinfo("Informacion","Los datos fueron guardados ")
        self.actualizarGanado()
        self.limpiarCamposGanado()

    def actualizarGanado(self):
        if self.tree is not None:
            self.tree.delete(*self.tree.get_children())
            for row in CDatosGanado.mostrarGanado():
                self.tree.insert("", "end", values=row)
        else: 
            print("No inicializado el tree")

    def seleccionarGanado(self, event):
        
        itemSeleccionado = self.tree.focus()
        if itemSeleccionado: 
            values = self.tree.item(itemSeleccionado)['values']
            self.textBoxIdGanado.delete(0, tk.END)
            self.textBoxIdGanado.insert(0, values[0])
            self.textBoxEspecie.delete(0, tk.END)
            self.textBoxEspecie.insert(0, values[1])
            self.textBoxRaza.delete(0, tk.END)
            self.textBoxRaza.insert(0, values[2])
            self.textBoxEdad.delete(0, tk.END)
            self.textBoxEdad.insert(0, values[3])
            self.textBoxPeso.delete(0, tk.END)
            self.textBoxPeso.insert(0, values[4])
            self.textBoxProduccion.delete(0, tk.END)
            self.textBoxProduccion.insert(0, values[5])
            
    def modificarGanado(self):
        
        idGanado = self.textBoxIdGanado.get()
        nombreEspecie = self.textBoxEspecie.get()
        nombreRaza = self.textBoxRaza.get()
        edadGanado = self.textBoxEdad.get()
        pesoGanado = self.textBoxPeso.get()
        produccionGanado = self.textBoxProduccion.get()
        CDatosGanado.modificarGanado(idGanado, nombreEspecie,nombreRaza,edadGanado,pesoGanado,produccionGanado)
        messagebox.showinfo("Informacion","Los datos fueron actualizados ")
        self.actualizarGanado()
        self.limpiarCamposGanado()
        
    def eliminarGanado(self):
        
        idGanado = self.textBoxIdGanado.get()
        nombreEspecie = self.textBoxEspecie.get()
        nombreRaza = self.textBoxRaza.get()
        edadGanado = self.textBoxEdad.get()
        pesoGanado = self.textBoxPeso.get()
        produccionGanado = self.textBoxProduccion.get()

        CDatosGanado.eliminarGanado(idGanado, nombreEspecie,nombreRaza,edadGanado,pesoGanado,produccionGanado)
        messagebox.showinfo("Informacion","Los datos fueron eliminados ")
        self.actualizarGanado()
        self.limpiarCamposGanado()

    def limpiarCamposGanado(self):
        
        self.textBoxIdGanado.delete(0, tk.END)
        self.textBoxEspecie.delete(0, tk.END)
        self.textBoxRaza.delete(0, tk.END)
        self.textBoxEdad.delete(0, tk.END)
        self.textBoxPeso.delete(0, tk.END)
        self.textBoxProduccion.delete(0, tk.END)

    def abrir_ventana_informe(self):
        ventana_informe = tk.Toplevel(self.base)
        ventana_informe.title("Reporte de Producción")
        ventana_informe.geometry("500x300")
        
        groupBox = LabelFrame(ventana_informe, text="Datos de la Granja", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)
        
        label_informe1 = tk.Label(groupBox, text="Producción total de los cultivos", font=("Arial", 10))
        label_informe1.grid(row=0, column=0, pady=5, padx=10)

        label_informe2 = tk.Label(groupBox, text="Producción total de ganado", font=("Arial", 10))
        label_informe2.grid(row=1, column=0, pady=5, padx=10)
        
        label_informe3 = tk.Label(groupBox, text="Producción total de la granja", font=("Arial", 10))
        label_informe3.grid(row=2, column=0, pady=5, padx=10)

        # Calcular producción total de los cultivos
        produccion_total_cultivos = sum(float(row[3]) * float(row[4]) for row in CDatosCultivos.mostrarCultivos())

        # Calcular producción total de ganado
        produccion_total_ganado = sum(float(row[5]) for row in CDatosGanado.mostrarGanado())

        # Calcular producción total de la granja
        produccion_total_granja = produccion_total_cultivos + produccion_total_ganado
        
        entry_cultivos = tk.Entry(groupBox)
        entry_cultivos.insert(tk.END, produccion_total_cultivos) 
        entry_cultivos.grid(row=0, column=1, pady=5, padx=10)

        entry_ganado = tk.Entry(groupBox)
        entry_ganado.insert(tk.END, produccion_total_ganado)
        entry_ganado.grid(row=1, column=1, pady=5, padx=10)
        
        entry_granja = tk.Entry(groupBox)
        entry_granja.insert(tk.END, produccion_total_granja)
        entry_granja.grid(row=2, column=1, pady=5, padx=10)



def main():
    try:
        base = tk.Tk()
        app = VentanaPrincipal(base)
        base.mainloop()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()