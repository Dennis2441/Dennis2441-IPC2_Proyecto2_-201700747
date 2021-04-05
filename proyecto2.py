import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import xml.dom.minidom
import numpy as np
import os
from xml.dom import minidom
from xml.dom.minidom import Node
import os
from datetime import datetime


now = datetime.now()
original=""
segunda=""
resultado=""
tipo=""
valor=""
valor2=""
fll=""
coll=""
fll2=""
coll2=""
fll3=""
coll3=""
ima=""
ima2=""
ima3=""
listaextra=[]
listareporte=[]
class report():
    def __init__(self, id,descripcion):
        self.id = id
        self.descripcion = descripcion
        
class matriz():
    def __init__(self, nombre, fila, columna,imagen):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.imagen=imagen
lista_matriz=[]
#______________________________________________________
class Nodo():
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class lista_circular():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def Agregarinicio(self, Nodo):
        if self.primero == None:
            self.primero = Nodo
            self.primero.siguiente = self.primero
        else:
            aux = self.primero
            while aux.siguiente is not self.primero:
                aux = aux.siguiente
            aux.siguiente = Nodo
            Nodo.siguiente = self.primero

    def buscar(self, data):
        aux = self.primero
        encontrado = False
        if self.primero == None:
            print("Vacio")
        while (True):
            if (aux.nombre == data):
                encontrado = True
                break
            aux = aux.siguiente
            if (aux == self.primero):
                break
        if (encontrado == True):
            print("Ya esta en la lista")
        else:
            print("No esta en la lista")
        return encontrado

    def display(self):
        curr = self.primero
        n = 1
        if self.primero is None:
            print("List is empty")
            return
        else:
            # Prints each node by incrementing pointer.
            print(n + "- " + curr.nombre)
            n = n + 1
            while (curr.siguiente != self.primero):
                curr = curr.siguiente
                print(n + "- " + curr.nombre)
                n = n + 1

    
#________________________________________________________________________________________________________________
class Nodo1():
    def __init__(self,fila,columna,valor,nombre):
        self.nombre=nombre
        self.valor=valor
        self.fila=fila
        self.columna=columna
        self.derecha=None
        self.izquierda=None
        self.abajo=None
        self.arriba=None
class nodoencabezado:
    def __init__(self,id):
        self.id=id
        self.siguiente=None
        self.anterior=None
        self.acceso=None
    
class listaencabezado:
    def __init__(self,primero=None):
        self.primero=primero
    def eliminarp(self):
        if(self.primero==None):
            print("vacio")
        
        if self.primero.siguiente==None:
                self.primero=None
                return
        
        self.primero=self.primero.siguiente
        self.primero.anterior=None
    def eliminar(self,id):
        if(self.primero==None):
            print("vacio")
        else:
            if(self.primero==id):
                print(self.primero.id)
                self.eliminarp()
                return
                
    def setencabezadp(self,nuevo):
        if (self.primero==None):
            self.primero=nuevo
        elif(nuevo.id<self.primero.id):
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
        else:
            actual=self.primero
            while actual.siguiente !=None:
                if(nuevo.id<self.primero.id):
                    nuevo.siguiente=actual.siguiente
                    actual.siguiente.anterior=nuevo
                    nuevo.anterior=actual
                    actual.siguiente=nuevo
                    break
                actual=actual.siguiente
            if(actual.siguiente==None):
                actual.siguiente=nuevo
                nuevo.anterior=actual
    def getencabezado(self,id):
        actual=self.primero
        while actual !=None:
            if(actual.id==id):
                return actual
            actual=actual.siguiente
        return None
class matrizx:
    def __init__(self):
        self.efilas=listaencabezado()
        self.ecolumnas=listaencabezado()

    
    def insertar(self,fila,columna,valor,nombre):

        nuevo=Nodo1(fila,columna,valor,nombre)
        ecolumna=self.ecolumnas.getencabezado(columna)
        print(ecolumna)
        if ecolumna==None:
            ecolumna=nodoencabezado(columna)
            ecolumna.acceso=nuevo
            self.ecolumnas.setencabezadp(ecolumna)
        else:
            if (nuevo.fila < ecolumna.acceso.fila):
                nuevo.abajo=ecolumna.acceso
                ecolumna.acceso.arriba=nuevo
                ecolumna.acceso=nuevo
            else:
                actual=ecolumna.acceso
                while actual.abajo !=None:
                    if nuevo.fila< actual.abajo.fila:
                        nuevo.abajo=actual.abajo
                        actual.abajo.arriba=nuevo
                        nuevo.arriba=actual
                        actual.abajo=nuevo
                        break
                    actual=actual.abajo
                if(actual.abajo==None):
                    actual.abajo=nuevo
                    nuevo.arriba=actual
        #insercion encabezado por filas
        efila= self.efilas.getencabezado(fila)
        if efila==None:
            efila=nodoencabezado(fila)
            efila.acceso=nuevo
            self.efilas.setencabezadp(efila)
        else:
            if (nuevo.columna < efila.acceso.columna):
                nuevo.derecha=efila.acceso
                efila.acceso.izquierda=nuevo
                efila.acceso=nuevo
            else:
                actual=efila.acceso
                while actual.derecha !=None:
                    if nuevo.columna< actual.derecha.columna:
                        nuevo.derecha=actual.derecha
                        actual.derecha.izquierda=nuevo
                        nuevo.izquierda=actual
                        actual.derecha=nuevo
                        break
                    actual=actual.derecha
                if(actual.derecha==None):
                    actual.derecha=nuevo
                    nuevo.izquierda=actual
    def buscar1(self,fila,columna):
        ecolumna=self.ecolumnas.primero
        while ecolumna !=None:
            actual=ecolumna.acceso
            while actual !=None:
                if actual.fila==fila and actual.columna==columna:
                    return actual.valor
                actual=actual.abajo
            ecolumna=ecolumna.siguiente
            
    def lineavertical(self,fila,columna,f11,c11,ele):
        global fll3
        global coll3
        li3.eliminar()
        fll3=fila
        coll3=columna
        linea=''
        jump=''
        final=''
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        f1=int(f11)
        c1=int(c11)
        f2=int(ele)
        f2=f2+1
        for i in range(1,jk):
            for j in range(1, kj):
                val=self.buscar1(i,j)
                if val==None:
                    pass
                elif(i==f1 and j==c1):
                    if(f1<=f2):
                        val='*'
                        li3.insertar(i,j,val,"nuevo")
                        linea=linea+val
                        f1=f1+1
                    else:
                        li3.insertar(i,j,val,"nuevo")
                        linea=linea+val
                        f1=0
                else:
                    li3.insertar(i,j,val,"nuevo")
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
        return(final)
    def lineahorizontal(self,fila,columna,f11,c11,ele):
        li3.eliminar()
        linea=''
        jump=''
        final=''
        global fll3
        global coll3
        fll3=fila
        coll3=columna
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        f1=int(f11)
        c1=int(c11)
        c2=int(ele)
        c2=c2+1
        for i in range(1,jk):
            for j in range(1, kj):
                val=self.buscar1(i,j)
                if val==None:
                    pass
                elif(i==f1 and j==c1):
                    if(c1<=c2):
                        val='*'
                        li3.insertar(i,j,val,"nuevo")
                        linea=linea+val
                        c1=c1+1
                    else:
                        li3.insertar(i,j,val,"nuevo")
                        linea=linea+val
                        c1=0
                else:
                    li3.insertar(i,j,val,"nuevo")
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
        return(final)
    def Limpiar(self,fila,columna,f11,c11,f22,c22):
        li3.eliminar()
        linea=''
        jump=''
        final=''
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        f1=int(f11)
        f2=int(f22)
        c1=int(c11)
        aux=int(c11)
        c2=int(c22)
        c2=c2+1
        global fll3
        global coll3
        fll3=fila
        coll3=columna
        for i in range(1,jk):
            for j in range(1, kj):
                val=self.buscar1(i,j)

                if val==None:
                    pass
                elif(i==f1 and j==c1):
                    if(c1<c2):
                        val="-"
                        li3.insertar(i,j,val,"nuevo")
                        linea=linea+val
                        c1=c1+1
                        if(c1==c2):
                            c1=aux
                            f1=f1+1
                            if(f1>f2):
                                f1=0
                            


                else:
                    li3.insertar(i,j,val,"nuevo")
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
        return(final)
    def rectangulo(self,fila,columna,f11,c11,f22,c22):
        li3.eliminar()
        linea=''
        jump=''
        final=''
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        f1=int(f11)
        f2=int(f22)
        c1=int(c11)
        aux=int(c11)
        c2=int(c22)
        c3=int(c22)
        c2=c2+1
        flag=False
        estado=0
        global fll3
        global coll3
        fll3=fila
        coll3=columna
        for i in range(1,jk):
            for j in range(1, kj):
                val=self.buscar1(i,j)
                print("linea:"+linea)
                if val==None:
                    pass
                elif(i==f1 and j==c1):
                    if(estado==0):
                        if(c1<c2):
                            val="*"
                            li3.insertar(i,j,val,"nuevo")
                            linea=linea+val
                            c1=c1+1
                            if(c1==c2):
                                f1=f1+1
                                if(f1==f2):
                                    estado=2
                                    c1=aux
                                else:
                                    c1=aux
                                    estado=1
                    elif(estado==1):
                        if(c1==aux):
                            val="*"
                            li3.insertar(i,j,val,"nuevo")
                            linea=linea+val
                            c1=c3
                        elif(c1==c3):
                            val="*"
                            li3.insertar(i,j,val,"nuevo")
                            linea=linea+val
                            c1=aux
                            f1=f1+1
                            if(f1==f2):
                                c1=aux
                                estado=2
                        else:
                            linea=linea+val
                    elif(estado==2):
                        if(c1<c2):
                            val="*"
                            li3.insertar(i,j,val,"nuevo")
                            linea=linea+val
                            c1=c1+1
                            if(c1==c2):
                                c1=0
                                estado=0

                    
                else:
                    li3.insertar(i,j,val,"nuevo")
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
            print("final:\n"+final)
        return(final)
    def matrizp(self,fila,columna):
        linea=''
        jump=''
        final=''
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        for i in range(1,jk):
            for j in range(1, kj):
                val=self.buscar1(i,j)
                if val==None:
                    pass
                else:
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
        return(final)
    def triangul(self,fila,columna,f11,c11,ele):
        li3.eliminar()
        global fll3
        global coll3
        fll3=fila
        coll3=columna
        linea=''
        jump=''
        final=''
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        f1=int(f11)
        c1=int(c11)
        c3=int(c11)
        c4=int(ele)
        aux=int(c11)
        f2=int(ele)

        c2=int(ele)
        flag=False
        flag2=False
        if(f1==1):
            flag2=False
        else:
            f2=f2+1
        if(c1==1):
            flag=False
        else:
            c2=c2+1
            flag=True
        
        
        n=1
        estado=0
        for i in range(1,jk):
            for j in range(1, kj):
                val=self.buscar1(i,j)
                print("linea:"+linea)
                if val==None:
                    pass
                elif(i==f1 and j==c1):
                    if(estado==0):
                        val="*"
                        li3.insertar(i,j,val,"nuevo")
                        linea=linea+val
                        f1=f1+1
                        estado=1
                        c1=aux
                        c3=c3+1
                        n=n+1
                    elif(estado==1):
                        if (c1<=c3):
                            val="*"
                            li3.insertar(i,j,val,"nuevo")
                            linea=linea+val
                            if(c1==c3):
                                c1=aux
                                f1=f1+1
                                if(f1==f2):
                                    estado=3

                                else:
                                    estado=2
                            else:
                                c1=c1+1
                    elif(estado==2):
                        if(c1==aux):
                            val="*"
                            li3.insertar(i,j,val,"nuevo")
                            linea=linea+val
                            c1=c1+n
                            n=n+1
                        else:
                            val="*"
                            li3.insertar(i,j,val,"nuevo")
                            linea=linea+val
                            c1=aux
                            f1=f1+1
                            if(f1==f2):
                                estado=3
                    elif(estado==3):
                        if(flag==False):
                            if(c1<=c2):
                                val="*"
                                li3.insertar(i,j,val,"nuevo")
                                linea=linea+val
                                c1=c1+1
                                if(c1>c2):
                                    c1=0
                                    f1=0
                        else:
                            if(c1<=c2):
                                val="*"
                                li3.insertar(i,j,val,"nuevo")
                                linea=linea+val
                                c1=c1+1
                                if(c1>c2):
                                    c1=0
                                    f1=0
                else:
                    li3.insertar(i,j,val,"nuevo")
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
            print("final: \n"+final)
        return(final)
    def horiz(self,fila,columna):
        li3.eliminar()
        global fll3
        global coll3
        fll3=fila
        coll3=columna
        linea=''
        jump=''
        final=''
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        f1=int(fila)
        c1=int(columna)
        flag=False
        cab=self.ecolumnas.primero
        for i in reversed(range(jk)):
            for j in range(1, kj):
                val=self.buscar1(i,j)
                if val==None:
                    pass
                else:
                    li3.insertar(i,j,val,"nuevo")
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
        return(final)
    def verti(self,fila,columna):
        li3.eliminar()
        linea=''
        jump=''
        final=''
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        f1=int(fila)
        c1=int(columna)
        flag=False
        cab=self.ecolumnas.primero
        for i in  range(1, jk):
            for j in reversed(range(kj)):
                val=self.buscar1(i,j)
                if val==None:
                    pass
                else:
                    li3.insertar(i,j,val,"nuevo")
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
        return(final)
    def tra(self,fila,columna):
        li3.eliminar()
        global fll3
        global coll3
        fll3=fila
        coll3=columna
        linea=''
        jump=''
        final=''
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        f1=int(fila)
        c1=int(columna)
        flag=False
        cab=self.ecolumnas.primero
        for i in  range(1, jk):
            for j in range(1,kj):
                val=self.buscar1(i,j)
                if val==None:
                    pass
                else:
                    li3.insertar(i,j,val,"nuevo")
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
        return(final)
    def dell(self):
        self.ecolumnas.primero=None
    def eliminar(self):
        columna=1
        flag=True
        
        while flag==True:
            ecolumna=self.ecolumnas.getencabezado(columna)
            if(ecolumna==None):
                flag=False
            else:
                self.ecolumnas.eliminar(ecolumna)
                columna=columna+1

                


                
            

        

#________________________________________________________________________________________________________________
lista=lista_circular()
def leerarchivo(cadena):
    global lista_matriz
    ver=False
    doc = xml.dom.minidom.parseString(cadena)
    
    nombre = doc.getElementsByTagName("matrices")

    matris = doc.getElementsByTagName("matriz")
    for ma in matris:
        if lista.vacia():
                
            nombre = ma.getElementsByTagName("nombre")
            name = Nodo(nombre[0].firstChild.nodeValue)
            lista.Agregarinicio(name)
            fila = ma.getElementsByTagName("filas")
            columna = ma.getElementsByTagName("columnas")
            im = ma.getElementsByTagName("imagen")
            print(nombre[0].firstChild.nodeValue,fila[0].firstChild.nodeValue,columna[0].firstChild.nodeValue)
            lista_matriz.append(matriz(nombre[0].firstChild.nodeValue,fila[0].firstChild.nodeValue,columna[0].firstChild.nodeValue,im[0].firstChild.nodeValue))
            
            ver=True
        else:
            nombre = ma.getElementsByTagName("nombre")
            name=Nodo(nombre[0].firstChild.nodeValue)
            if(lista.buscar(nombre[0].firstChild.nodeValue)==True):
                    print("ya esta: "+nombre[0].firstChild.nodeValue)
            else:
                lista.Agregarinicio(name)
                fila = ma.getElementsByTagName("filas")
                columna = ma.getElementsByTagName("columnas")
                im = ma.getElementsByTagName("imagen")
                print(nombre[0].firstChild.nodeValue,fila[0].firstChild.nodeValue,columna[0].firstChild.nodeValue)
                lista_matriz.append(matriz(nombre[0].firstChild.nodeValue,fila[0].firstChild.nodeValue,columna[0].firstChild.nodeValue,im[0].firstChild.nodeValue))

    if lista_matriz==None:
        print()
    else:
        for i in lista_matriz:
            print(i.nombre,i.imagen)

    
    if(ver==True):
        messagebox.showinfo(message="CARGA COMPLETA")
    else:
        messagebox.showinfo(message="ESTRUCTURA DE ARCHIVO XML INCORRECTO")
    

def buscar():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select un archivo xml",
                                          filetypes = (("xml files",
                                                        "*.xml*"),
                                                       ("all files",
                                                        "*.*")))
    print(filename)
    archivo = open(filename, "r", encoding='utf-8')
    mm = archivo.read()
    print(mm)
    leerarchivo(mm)
li=matrizx()
li2=matrizx()
li3=matrizx()
def main():
    raiz=Tk()
    global original
    global segunda
    global resultado
    if(original !=""):
        
        raiz.title("Proyecto2")
        menubar=Menu(raiz)
        panel_1=PanedWindow(bd=4, relief='raised', bg='white')
        panel_1.pack(fill=BOTH, expand=1)
        
        
        ayuda=Menu(menubar,tearoff=0)
        menubar.add_command(label='Cargar Archivo', command=buscar)
        menubar.add_command(label='Operaciones',command=Operaciones)
        menubar.add_command(label='Reportes')
        
        #_________________________________
        ayuda.add_command(label='Informacion Estudiante')
        ayuda.add_command(label='Documentacion del programa')
        ayuda.add_separator()
        menubar.add_cascade(label='Ayuda', menu=ayuda)
        raiz.config(menu=menubar)
        raiz.geometry("520x480")
    else:
        
        raiz.title("Proyecto2")
        menubar=Menu(raiz)
        
        
        
        ayuda=Menu(menubar,tearoff=0)
        menubar.add_command(label='Cargar Archivo', command=buscar)
        menubar.add_command(label='Operaciones',command=Operaciones)
        menubar.add_command(label='Reportes',command=html)
        
        #_________________________________
        ayuda.add_command(label='Informacion Estudiante')
        ayuda.add_command(label='Documentacion del programa')
        ayuda.add_separator()
        menubar.add_cascade(label='Ayuda', menu=ayuda)
        raiz.config(menu=menubar)
        raiz.geometry("520x480")

    raiz.mainloop()
idk=False
def Operaciones():
    global lista_matriz
    global original
    global segunda
    global resultado
    global tipo
    global valor
    global valor2
    global idk
    listaux=[]
    raiz=tk.Toplevel()
    raiz.title("Proyecto2")
    menubar=Menu(raiz)
    ayuda=Menu(menubar,tearoff=0)
    
    
    #_________________________________
    ayuda.add_command(label='Informacion Estudiante')
    ayuda.add_command(label='Documentacion del programa')
    menubar.add_command(label='Regresar a Ventana principal', command=main)
    ayuda.add_separator()
    menubar.add_cascade(label='Ayuda', menu=ayuda)
    raiz.config(menu=menubar)
    3
    raiz.geometry("1000x1000")
    if len(lista_matriz)==0:
        messagebox.showinfo("Hacer Carga Para Poder Mostrar Datos")
    else:
        combo= ttk.Combobox(raiz,width = 27)
        combo2= ttk.Combobox(raiz,width = 27)
        limpiar = ttk.Entry(raiz)
        rectangulo = ttk.Entry(raiz)
        vertical = ttk.Entry(raiz)
        horizontal = ttk.Entry(raiz)
        triangulo = ttk.Entry(raiz)
        data = ("Unión", "Intersección", "Diferencia", "Diferenciasimétrica")
        data1=("horizontal","vertical","Transpuesta")
        cb = ttk.Combobox(raiz, values=data)
        cb2 = ttk.Combobox(raiz, values=data1)
        ttk.Label(raiz, text = "Selecione Matrix Original :", 
        font = ("Times New Roman", 10)).grid(column = 0, 
        row = 15, padx = 10, pady = 25)
        ttk.Label(raiz, text = "Limpiar :", 
        font = ("Times New Roman", 10)).grid(column = 7, 
        row = 15, padx = 10, pady = 25)
        ttk.Label(raiz, text = "Selecione Matrix a operar :", 
        font = ("Times New Roman", 10)).grid(column = 0, 
        row = 20, padx = 10, pady = 25)
        ttk.Label(raiz, text = "Linea Horizontal :", 
        font = ("Times New Roman", 10)).grid(column = 7, 
        row =20 , padx = 10, pady = 25)
        ttk.Label(raiz, text = "Tipo de Operacion :", 
        font = ("Times New Roman", 10)).grid(column = 0, 
        row = 25, padx = 10, pady = 25)
        ttk.Label(raiz, text = "Linea Vertical :", 
        font = ("Times New Roman", 10)).grid(column = 7, 
        row =25 , padx = 10, pady = 25)
        ttk.Label(raiz, text = "Rotacion :", 
        font = ("Times New Roman", 10)).grid(column = 0, 
        row = 30, padx = 10, pady = 25)
        ttk.Label(raiz, text = "Rectangulo :", 
        font = ("Times New Roman", 10)).grid(column = 7, 
        row =30 , padx = 10, pady = 25)
        ttk.Label(raiz, text = "Triángulo rectángulo :", 
        font = ("Times New Roman", 10)).grid(column = 7, 
        row =35 , padx = 10, pady = 25)
        
        for i in lista_matriz:
            nombre=i.nombre
            listaux.append(nombre)
        for j in listaux:
            no=j
            combo['values'] = (*combo['values'], no)
            combo2['values'] = (*combo2['values'], no)
        combo.grid(column = 1, row = 15)

        combo2.grid(column = 1, row = 20)
        cb.grid(column = 1, row = 25)
        cb2.grid(column = 1, row = 30)
        def verlo():
            global lista_matriz
            global original
            global segunda
            global valor
            global ima
            global fll
            global coll
            
            valor=combo.get()
            valor2=combo2.get()
            
            if valor=="":
                if valor=="":
                    messagebox.showinfo("matriz","Escoger matriz orginal antes de operar")
            else:
                leerimagen1()
                ima= li.matrizp(fll,coll)
                iconPath = r"C:\Users\denni\OneDrive\Desktop\ima.jpg"
                icon = ImageTk.PhotoImage(Image.open(iconPath))
                icon_size = Label(raiz)
                icon_size.image = icon  # <== this is were we anchor the img object
                icon_size.configure(image=icon)
                icon_size.grid(column=0,row=50)
                raiz.update()
                

                
                

        def verlo2():
            global lista_matriz
            global original
            global segunda
            global valor2
            
            
            valor=combo.get()
            valor2=combo2.get()
            
            if valor2=="":
                if valor2=="":
                    messagebox.showinfo("matriz","Escoger segunda matriz antes de operar")
            else:
                leerimagen2()
                global ima2
                global fll2
                global coll2
                ima2=""
                ima2= li2.matrizp(fll2,coll2)
                iconPath = r"C:\Users\denni\OneDrive\Desktop\ima2.jpg"
                icon = ImageTk.PhotoImage(Image.open(iconPath))
                icon_size = Label(raiz)
                icon_size.image = icon  # <== this is were we anchor the img object
                icon_size.configure(image=icon)
                icon_size.grid(column=1,row=50)
                raiz.update()
        
        
        def rotacion():
            global lista_matriz
            
            global original
            global segunda
            global valor
            global ima3
            global fll
            global coll
            global listareporte
            today = now.strftime("%d/%m/%Y %H:%M:%S")
            reporte=""
            reporte=today + " Nombre Matriz: "+valor
            au=cb2.get()
            if valor=="":
                if valor=="":
                    messagebox.showinfo("matriz","Escoger matriz orginal antes de operar")
            elif(au==""):
                messagebox.showinfo("matriz","Escoger Rotacion")
            elif(au=="horizontal"):
                
                ima3= li.horiz(fll,coll)
                valor=valor+'\n'
                reporte=reporte+" Rotacion:  Horizontal"
                listareporte.append(report("operacion",reporte))
                mo3()
                iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                icon = ImageTk.PhotoImage(Image.open(iconPath))
                icon_size = Label(raiz)
                icon_size.image = icon  # <== this is were we anchor the img object
                icon_size.configure(image=icon)
                icon_size.grid(column=2,row=50)
                raiz.update()
            elif(au=="vertical"):
                
                ima3= li.verti(fll,coll)
                valor=valor+'\n'
                reporte=reporte+" Rotacion:  Vertical"
                listareporte.append(report("operacion",reporte))
                mo3()
                iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                icon = ImageTk.PhotoImage(Image.open(iconPath))
                icon_size = Label(raiz)
                icon_size.image = icon  # <== this is were we anchor the img object
                icon_size.configure(image=icon)
                icon_size.grid(column=2,row=50)
                raiz.update()
            elif(au=="Transpuesta"):
                ima3= traa(fll,coll)
                valor=valor+'\n'
                reporte=reporte+" Rotacion:  Transpuesta"
                listareporte.append(report("operacion",reporte))
                mo3()
                iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                icon = ImageTk.PhotoImage(Image.open(iconPath))
                icon_size = Label(raiz)
                icon_size.image = icon  # <== this is were we anchor the img object
                icon_size.configure(image=icon)
                icon_size.grid(column=2,row=50)
                raiz.update()
        def operar():
            global original
            global segunda
            global valor
            global valor2
            global ima3
            global fll
            global coll
            global fll2
            global coll2
            global fll3
            global coll3
            global listareporte
            today = now.strftime("%d/%m/%Y %H:%M:%S")
            reporte=""
            f1=int(fll)
            c1=int(coll)
            f2=int(fll2)
            c2=int(coll2)
            aux1=int(coll)
            aux2=int(coll2)
            au=cb.get()
            linea=''
            jump=''
            final=''
            x=1
            y=1
            x2=1
            y2=1
            flag=False
            estado=0
            ver=True
            kj=f1+f2
            vv=False
            vv2=False
            vv3=False
            if(valor==""):
                if(valor2==""):
                    reporte=today + "Matriz Original:   Matriz Secundaria: "
                    messagebox.showinfo("matriz","Escoger las dos Matrices")
                    reporte=reporte+" Tipo Operacion: "+ au+" No se Escogio Matriz Original ni la Secundaria"
                    listareporte.append(report("error",reporte))
                    reporte=""
                else:
                    reporte=today + "Matriz Original:  Matriz Secundaria: "+valor2
                    messagebox.showinfo("matriz","Escoger matriz orginal antes de operar")
                    reporte=reporte+" Tipo Operacion: "+ au+" No se Escogio Matriz Original"
                    listareporte.append(report("error",reporte))
                    reporte=""
            elif(valor2==""):
                reporte=today + "Matriz Original: "+valor +" Matriz Secundaria: "
                messagebox.showinfo("matriz","Escoger las dos Matrices")
                reporte=reporte+" Tipo Operacion: "+ au+" No se Escogio Matriz Secundaria"
                listareporte.append(report("error",reporte))
            elif(au=="Unión"):
                reporte=today + "Matriz Original: "+valor +", Matriz Secundaria: "+valor2+", Tipo Operacion: "+au
                listareporte.append(report("operacion",reporte))
                fila=1
                columna=1
                cc=1
                li3.eliminar()
                if(c1>c2):
                    cl=c1
                    coll3=c1
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1
                    else:
                    
                        fll3=f2
                elif(c1==c2):
                    coll3=c1
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1
                    else:
                    
                        fll3=f2
                else:
                    coll3=c2
                    cl=c2
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1 
                    else:
                        fll3=f2

                while ver==True:
                    print("Linea:" + linea)
                    if(flag==False):
                        print
                    else:
                        salto=linea+'\n'
                        final=final+salto
                        linea=''
                        print("final: \n"+final)
                        flag=False
                        vv2=False
                        vv=False
                    if(estado==0):
                        if(x<=c1 and y<=f1):
                            v1=li.buscar1(y,x)
                            if(x2<=c2 and y2<=f2):
                                v2=li2.buscar1(y2,x2)
                                if(x==c1):
                                    y=y+1
                                    x=1

                                    vv=True
                                    if(x2==c2):
                                        vv3=True

                                        
                                    
                                        y2=y2+1
                                        x2=1
                                        flag=True
                                        vv2=True
                                    else:

                                        estado=1
                                if(x2==c2):
                                    y2=y2+1
                                    x2=1
                                    vv2=True
                                    if(x==c1):
                                        vv3=True
                                        
                                        
                                        y=y+1
                                        x=1
                                        flag=True
                                        vv=False
                                    else:
                                        estado=2
                                #______________________
                                if(vv==False):
                                    if(vv2==False):
                                        x=x+1
                                        x2=x2+1
                                          
                                    else:      
                                        x=x+1
                                elif(vv2==False):
                                    if(vv==False):
                                        x=x+1
                                        
                                        x2=x2+1
                                    else:
                                        x2=x2+1  
                                #_________________________
                                if(v1=="-"):
                                    
                                    linea=linea+v2
                                    li3.insertar(fila,columna,v2,"nuevo")
                                    columna=columna+1
                                    if(vv3==True):
                                        columna=1
                                        vv3=False
                                        fila=fila+1
                                elif(v2=="-"):
                                    li3.insertar(fila,columna,v1,"nuevo")
                                    linea=linea+v1
                                    columna=columna+1
                                    if(vv3==True):
                                        columna=1
                                        vv3=False
                                        fila=fila+1
                                else:
                                    li3.insertar(fila,columna,v1,"nuevo")
                                    linea=linea+v1
                                    columna=columna+1
                                    if(vv3==True):
                                        columna=1
                                        vv3=False
                                        fila=fila+1
                                    if(x==c1):
                                        fila=fila+1
                                        columna=1
                                        y=y+1
                                        x=1
                                        flag=True
                            else:
                                v1=li.buscar1(y,x)
                                li3.insertar(fila,columna,v1,"nuevo")
                                linea=linea+v1
                                if(x==c1):
                                    if(c2>c1):
                                        fin=c2-c1
                                        for i in range(0,fin):
                                            v1="-"
                                            columna=columna+1 
                                            li3.insertar(fila,columna,v1,"nuevo")
                                            linea=linea+v1
                                            
                                    y=y+1
                                    fila=fila+1
                                    columna=1 
                                    x=1
                                    flag=True
                                else:
                                    columna=columna+1 
                                    x=x+1
                        elif(x2<=c2 and y2<=f2):
                            v2=li2.buscar1(y2,x2)
                            li3.insertar(fila,columna,v2,"nuevo")
                            linea=linea+v2
                            if(x2==c2):
                                if(c1>c2):
                                    fin=c1-c2
                                    for i in range(0,fin):
                                        v1="-"
                                        columna=columna+1 
                                        li3.insertar(fila,columna,v1,"nuevo")
                                        linea=linea+v1
                                        
                                y2=y2+1
                                x2=1
                                fila=fila+1
                                columna=1
                                flag=True
                            else:
                                columna=columna+1 
                                x2=x2+1
                            
                        else:
                            ver=False
                    elif(estado==1):
                        if(x2<=c2 and y2<=f2):
                            v2=li2.buscar1(y2,x2)
                            li3.insertar(fila,columna,v2,"nuevo")
                            linea=linea+v2
                            if(x2==c2):
                                
                                y2=y2+1
                                fila=fila+1
                                columna=1
                                x2=1
                                flag=True
                                estado=0
                            else:
                                columna=columna+1
                                x2=x2+1
                        else:
                            flag=True
                            estado=0
                    elif(estado==2):
                        if(x<=c1 and y<=f1):
                            v1=li.buscar1(y,x)
                            li3.insertar(fila,columna,v1,"nuevo")
                            linea=linea+v1
                            if(x==c1):
                                fila=fila+1 
                                columna=1 
                                y=y+1
                                x=1
                                flag=True
                                estado=0
                            else:
                                columna=columna+1 
                                x=x+1
                        else:
                            flag=True
                            estado=0
                ima3=final            
                
                mo3()
                iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                icon = ImageTk.PhotoImage(Image.open(iconPath))
                icon_size = Label(raiz)
                icon_size.image = icon  # <== this is were we anchor the img object
                icon_size.configure(image=icon)
                icon_size.grid(column=2,row=50)
                raiz.update()
            elif(au=="Intersección"):
                reporte=today + "Matriz Original: "+valor +", Matriz Secundaria: "+valor2+", Tipo Operacion: "+au
                listareporte.append(report("operacion",reporte))
                fila=1
                columna=1
                cc=1
                li3.eliminar()
                if(c1>c2):
                    cl=c1
                    coll3=c1
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1
                    else:
                    
                        fll3=f2
                elif(c1==c2):
                    coll3=c1
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1
                    else:
                    
                        fll3=f2
                else:
                    coll3=c2
                    cl=c2
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1 
                    else:
                        fll3=f2
                while ver==True:
                    print("Linea:" + linea)
                    if(flag==False):
                        print
                    else:
                        salto=linea+'\n'
                        final=final+salto
                        linea=''
                        print("final: \n"+final)
                        flag=False
                        vv2=False
                        vv=False
                    if(estado==0):
                        if(x<=c1 and y<=f1):
                            v1=li.buscar1(y,x)
                            if(x2<=c2 and y2<=f2):
                                v2=li2.buscar1(y2,x2)
                                if(x==c1):
                                    y=y+1
                                    x=1
                                    vv=True
                                    if(x2==c2):
                                        vv3=True
                                        y2=y2+1
                                        x2=1
                                        flag=True
                                        vv2=True
                                    else:
                                        estado=1
                                if(x2==c2):
                                    y2=y2+1
                                    x2=1
                                    vv2=True
                                    if(x==c1):
                                        vv3=True
                                        y=y+1
                                        x=1
                                        flag=True
                                        vv=False
                                    else:
                                            estado=2
                                #______________________
                                if(vv==False):        
                                    x=x+1
                                if(vv2==False):
                                    x2=x2+1  
                                #_________________________
                                if(v1==v2):
                                    if(v1=="*"):
                                        li3.insertar(fila,columna,v1,"nuevo")
                                        linea=linea+v1
                                        columna=columna+1
                                        if(vv3==True):
                                            columna=1
                                            vv3=False
                                            fila=fila+1
                                    else:
                                        v1="-"
                                        li3.insertar(fila,columna,v1,"nuevo")
                                        linea=linea+v1
                                        columna=columna+1
                                        if(vv3==True):
                                            columna=1
                                            vv3=False
                                            fila=fila+1
                                else:
                                    v1="-"
                                    li3.insertar(fila,columna,v1,"nuevo")
                                    linea=linea+v1
                                    columna=columna+1
                                    if(vv3==True):
                                            columna=1
                                            vv3=False
                                            fila=fila+1
                            else:
                                v1="-"
                                li3.insertar(fila,columna,v1,"nuevo")
                                linea=linea+v1
                                if(x==c1):
                                    if(c2>c1):
                                        fin=c2-c1
                                        for i in range(0,fin):
                                            v1="-"
                                            columna=columna+1
                                            li3.insertar(fila,columna,v1,"nuevo")
                                            linea=linea+v1
                                    fila=fila+1
                                    columna=1
                                    y=y+1
                                    x=1
                                    flag=True
                                else:
                                    x=x+1
                        elif(x2<=c2 and y2<=f2):
                            v2="-"
                            li3.insertar(fila,columna,v2,"nuevo")
                            linea=linea+v2
                            if(x2==c2):
                                if(c1>c2):
                                    fin=c1-c2
                                    for i in range(0,fin):
                                        v1="-"
                                        columna=columna+1
                                        li3.insertar(fila,columna,v2,"nuevo")
                                        linea=linea+v1
                                fila=fila+1
                                columna=1
                                y2=y2+1
                                x2=1
                                flag=True
                            else:
                                columna=columna+1
                                x2=x2+1
                        else:
                            ver=False
                    elif(estado==1):
                        if(x2<=c2 and y2<=f2):
                            v2="-"
                            li3.insertar(fila,columna,v2,"nuevo")
                            linea=linea+v2
                            if(x2==c2):
                                fila=fila+1
                                columna=1    
                                y2=y2+1
                                x2=1
                                flag=True
                                estado=0
                            else:
                                columna=columna+1
                                x2=x2+1
                        else:
                            flag=True
                            estado=0
                    elif(estado==2):
                        if(x<=c1 and y<=f1):
                            v1="-"
                            li3.insertar(fila,columna,v1,"nuevo")
                            linea=linea+v1
                            if(x==c1):
                                fila=fila+1 
                                columna=1
                                y=y+1
                                x=1
                                flag=True
                                estado=0
                            else:
                                columna=columna+1
                                
                                x=x+1
                        else:
                            flag=True
                            estado=0
                ima3=final            
                
                mo3()   
                iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                icon = ImageTk.PhotoImage(Image.open(iconPath))
                icon_size = Label(raiz)
                icon_size.image = icon  # <== this is were we anchor the img object
                icon_size.configure(image=icon)
                icon_size.grid(column=2,row=50)
                raiz.update()  
            elif(au=="Diferencia"):
                reporte=today + "Matriz Original: "+valor +", Matriz Secundaria: "+valor2+", Tipo Operacion: "+au
                listareporte.append(report("operacion",reporte))
                print
                fila=1
                columna=1
                cc=1
                li3.eliminar()
                if(c1>c2):
                    cl=c1
                    coll3=c1
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1
                    else:
                    
                        fll3=f2
                elif(c1==c2):
                    coll3=c1
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1
                    else:
                    
                        fll3=f2
                else:
                    coll3=c2
                    cl=c2
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1 
                    else:
                        fll3=f2
                while ver==True:
                    print("Linea:" + linea)
                    if(flag==False):
                        print
                    else:
                        salto=linea+'\n'
                        final=final+salto
                        linea=''
                        print("final: \n"+final)
                        flag=False
                        vv2=False
                        vv=False
                    if(estado==0):
                        if(x<=c1 and y<=f1):
                            v1=li.buscar1(y,x)
                            if(x2<=c2 and y2<=f2):
                                v2=li2.buscar1(y2,x2)
                                if(x==c1):
                                    y=y+1
                                    x=1
                                    vv=True
                                    if(x2==c2):
                                        vv3=True
                                        y2=y2+1
                                        x2=1
                                        flag=True
                                        vv2=True
                                    else:
                                        estado=1
                                if(x2==c2):
                                    y2=y2+1
                                    x2=1
                                    vv2=True
                                    if(x==c1):
                                        vv3=True
                                        y=y+1
                                        x=1
                                        flag=True
                                        vv=False
                                    else:
                                            estado=2
                                #______________________
                                if(vv==False):        
                                    x=x+1
                                if(vv2==False):
                                    x2=x2+1  
                                #_________________________
                                if(v1==v2):
                                    v1="-"
                                    linea=linea+v1  
                                    li3.insertar(fila,columna,v1,"nuevo")
                                    columna=columna+1
                                    if(vv3==True):
                                        columna=1
                                        vv3=False
                                        fila=fila+1         
                                else:
                                    
                                    linea=linea+v1
                                    li3.insertar(fila,columna,v1,"nuevo")
                                    columna=columna+1
                                    if(vv3==True):
                                        columna=1
                                        vv3=False
                                        fila=fila+1
                            else:
                                v1=li.buscar1(y,x)
                                li3.insertar(fila,columna,v1,"nuevo")
                                linea=linea+v1
                                if(x==c1):
                                    if(c2>c1):
                                        fin=c2-c1
                                        for i in range(0,fin):
                                            v1="-"
                                            columna=columna+1
                                            li3.insertar(fila,columna,v1,"nuevo")
                                            linea=linea+v1
                                    columna=1
                                    fila=fila+1
                                    y=y+1
                                    x=1
                                    flag=True
                                else:
                                    columna=columna+1
                                    x=x+1
                        elif(x2<=c2 and y2<=f2):
                            v2="-"
                            li3.insertar(fila,columna,v2,"nuevo")
                            linea=linea+v2
                            if(x2==c2):
                                if(c1>c2):
                                    fin=c1-c2
                                    for i in range(0,fin):
                                        v1="-"
                                        columna=columna+1
                                        li3.insertar(fila,columna,v1,"nuevo")
                                        linea=linea+v1
                                columna=1
                                fila=fila+1
                                y2=y2+1
                                x2=1
                                flag=True
                            else:
                                columna=columna+1
                                x2=x2+1
                        else:
                            ver=False
                    elif(estado==1):
                        if(x2<=c2 and y2<=f2):
                            v2="-"
                            li3.insertar(fila,columna,v2,"nuevo")
                            linea=linea+v2
                            if(x2==c2):
                                    
                                y2=y2+1
                                x2=1
                                columna=1
                                fila=fila+1
                                flag=True
                                estado=0
                            else:
                                columna=columna+1
                                x2=x2+1
                        else:
                            flag=True
                            estado=0
                    elif(estado==2):
                        if(x<=c1 and y<=f1):
                            v1=li.buscar1(y,x)
                            li3.insertar(fila,columna,v1,"nuevo")
                            linea=linea+v1
                            if(x==c1):
                                y=y+1
                                x=1
                                columna=1
                                fila=fila+1
                                flag=True
                                estado=0
                            else:
                                columna=columna+1
                                x=x+1
                        else:
                            flag=True
                            estado=0
                ima3=final  
                mo3()          
                iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                icon = ImageTk.PhotoImage(Image.open(iconPath))
                icon_size = Label(raiz)
                icon_size.image = icon  # <== this is were we anchor the img object
                icon_size.configure(image=icon)
                icon_size.grid(column=2,row=50)
                raiz.update()
            elif(au=="Diferenciasimétrica"):
                reporte=today + "Matriz Original: "+valor +", Matriz Secundaria: "+valor2+", Tipo Operacion: Diferencia simétrica"
                listareporte.append(report("operacion",reporte))
                fila=1
                columna=1
                cc=1
                li3.eliminar()
                if(c1>c2):
                    cl=c1
                    coll3=c1
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1
                    else:
                    
                        fll3=f2
                elif(c1==c2):
                    coll3=c1
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1
                    else:
                    
                        fll3=f2
                else:
                    coll3=c2
                    cl=c2
                    if(f1>f2):
                        fll3=f1
                    elif(f1==f2):
                        fll3=f1 
                    else:
                        fll3=f2
                while ver==True:
                    print("Linea:" + linea)
                    if(flag==False):
                        print
                    else:
                        salto=linea+'\n'
                        final=final+salto
                        linea=''
                        print("final: \n"+final)
                        flag=False
                        vv2=False
                        vv=False
                    if(estado==0):
                        if(x<=c1 and y<=f1):
                            v1=li.buscar1(y,x)
                            if(x2<=c2 and y2<=f2):
                                v2=li2.buscar1(y2,x2)
                                if(x==c1):
                                    y=y+1
                                    x=1
                                    vv=True
                                    if(x2==c2):
                                        vv3=True
                                        y2=y2+1
                                        x2=1
                                        flag=True
                                        vv2=True
                                    else:
                                        estado=1
                                if(x2==c2):
                                    y2=y2+1
                                    x2=1
                                    vv2=True
                                    if(x==c1):
                                        vv3=True
                                        y=y+1
                                        x=1
                                        flag=True
                                        vv=False
                                    else:
                                            estado=2
                                #______________________
                                if(vv==False):        
                                    x=x+1
                                if(vv2==False):
                                    x2=x2+1  
                                #_________________________
                                if(v1==v2):
                                    v1="-"
                                    
                                    linea=linea+v1
                                    li3.insertar(fila,columna,v1,"nuevo")
                                    columna=columna+1
                                    if(vv3==True):
                                        columna=1
                                        vv3=False
                                        fila=fila+1
                                else:
                                    if(v1=="-"):
                                        linea=linea+v2
                                        li3.insertar(fila,columna,v2,"nuevo")
                                        columna=columna+1
                                        if(vv3==True):
                                            columna=1
                                            vv3=False
                                            fila=fila+1
                                    else:
                                        linea=linea+v1
                                        li3.insertar(fila,columna,v1,"nuevo")
                                        columna=columna+1
                                        if(vv3==True):
                                            columna=1
                                            vv3=False
                                            fila=fila+1
                            else:
                                v1="-"
                                linea=linea+v1
                                
                                li3.insertar(fila,columna,v1,"nuevo")
                                if(x==c1):
                                    if(c2>c1):
                                        fin=c2-c1
                                        for i in range(0,fin):
                                            v1="-"
                                            columna=columna+1
                                            li3.insertar(fila,columna,v1,"nuevo")
                                            linea=linea+v1
                                    columna=1
                                    fila=fila+1
                                    y=y+1
                                    x=1
                                    flag=True
                                else:
                                    columna=columna+1
                                    x=x+1
                        elif(x2<=c2 and y2<=f2):
                            v2="-"
                            linea=linea+v2
                            li3.insertar(fila,columna,v2,"nuevo")
                            if(x2==c2):
                                if(c1>c2):
                                    fin=c1-c2
                                    for i in range(0,fin):
                                        v1="-"
                                        columna=columna+1
                                        li3.insertar(fila,columna,v1,"nuevo")
                                        linea=linea+v1
                                columna=1
                                fila=fila+1
                                y2=y2+1
                                x2=1
                                flag=True
                            else:
                                columna=columna+1
                                x2=x2+1
                        else:
                            ver=False
                    elif(estado==1):
                        if(x2<=c2 and y2<=f2):
                            v2="-"
                            li3.insertar(fila,columna,v2,"nuevo")
                            linea=linea+v2
                            if(x2==c2):
                                fila=fila+1
                                columna=1   
                                y2=y2+1
                                x2=1
                                flag=True
                                estado=0
                            else:
                                columna=columna+1
                                x2=x2+1
                        else:
                            flag=True
                            estado=0
                    elif(estado==2):
                        if(x<=c1 and y<=f1):
                            v1="-"
                            li3.insertar(fila,columna,v1,"nuevo")
                            linea=linea+v1
                            if(x==c1):
                                fila=fila+1
                                columna=1
                                y=y+1
                                x=1
                                flag=True
                                estado=0
                            else:
                                columna=columna+1
                                x=x+1
                        else:
                            flag=True
                            estado=0
                ima3=final 
                mo3()           
                iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                icon = ImageTk.PhotoImage(Image.open(iconPath))
                icon_size = Label(raiz)
                icon_size.image = icon  # <== this is were we anchor the img object
                icon_size.configure(image=icon)
                icon_size.grid(column=2,row=50)
                raiz.update()
            
        def extra():
            global lista_matriz
            global original
            global segunda
            global valor
            global ima3
            global fll
            global coll
            global listareporte
            today = now.strftime("%d/%m/%Y %H:%M:%S")
            reporte=""
            lim=str(limpiar.get())
            ho=str(horizontal.get())
            ve=str(vertical.get())
            re=str(rectangulo.get())
            tri=str(triangulo.get())

            if valor=="":
                if valor=="":
                    messagebox.showinfo("matriz","Escoger matriz orginal antes de operar")
            elif(lim !=''):
                reporte=today+" Nombre Matriz: "+valor+", Tipo operacion: Limpiar"
                print()
                oo=[]
                f11=""
                f22=""
                c11=""
                c22=""
                f1=0
                f2=0
                c1=0
                c2=0
                oo=lim.split(",")
                f11=oo[0]
                c11=oo[1]
                f22=oo[2]
                c22=oo[3]    
                print(f11,c11,f22,c22)
                f1=int(f11)
                f2=int(f22)
                c1=int(c11)
                c2=int(c22)
                if(f1==0 or f2==0 or c1==0 or c2==0):
                    reporte=reporte+" Las dimensiones no pueden ser igual a 0"
                    listareporte.append(report("error",reporte))
                elif(f1>int(fll)):
                    reporte=reporte+" La primera fila ingresada: "+f11+" ingresada es mayor que la dimension aceptada: "+fll
                    listareporte.append(report("error",reporte))
                elif(f2>int(fll)):
                    reporte=reporte+" La primera fila ingresada: "+f22+" ingresada es mayor que la dimension aceptada: "+fll
                    listareporte.append(report("error",reporte))
                elif(f1>f2):
                    reporte=reporte+" La segunda fila ingresada: "+f11+" ingresada es menor que la primera ingresada: "+f22
                    listareporte.append(report("error",reporte))
                elif(c1>int(coll)):
                    reporte=reporte+" La primera columna ingresada: "+c11+" ingresada es mayor que la dimension aceptada: "+coll
                    listareporte.append(report("error",reporte))
                elif(c2>int(coll)):
                    reporte=reporte+" La segunda columna ingresada: "+c22+" ingresada es mayor que la dimension aceptada: "+coll
                    listareporte.append(report("error",reporte))
                elif(c1>c2):
                    reporte=reporte+" La segunda columna ingresada: "+c11+" ingresada es menor que la primera ingresada: "+c22
                    listareporte.append(report("error",reporte))

                else:
                    ima3=li.Limpiar(fll,coll,f11,c11,f22,c22)
                    valor=valor
                    listareporte.append(report("operacion",reporte))
                    mo3()
                    iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                    icon = ImageTk.PhotoImage(Image.open(iconPath))
                    icon_size = Label(raiz)
                    icon_size.image = icon  # <== this is were we anchor the img object
                    icon_size.configure(image=icon)
                    icon_size.grid(column=2,row=50)
                    raiz.update()
                
                #ima3=li.Limpiar()
            elif(ho !=''):
                reporte=today+" Nombre Matriz: "+valor+", Tipo operacion: Linea Horizontal"
                print
                hh=[]
                f11=""
                c11=""
                ele=""
                f1=0
                c1=0
                elel=0
                hh=ho.split(",")
                f11=hh[0]
                c11=hh[1]
                ele=hh[2]
                f1=int(f11)
                c1=int(c11)
                elel=int(ele)
                if(f1>int(fll)):
                    reporte=reporte+" La primera fila ingresada: "+f11+" ingresada es mayor que la dimension aceptada: "+fll
                    listareporte.append(report("error",reporte))
                elif(c1>int(coll)):
                    reporte=reporte+" La primera columna ingresada: "+c11+" ingresada es mayor que la dimension aceptada: "+coll
                    listareporte.append(report("error",reporte))
                elif(elel>int(coll)):
                    reporte=reporte+"EL numero de elementos: "+ele+" es mas grande que una de las dimensiones columna: "+coll
                    listareporte.append(report("error",reporte))
                
                else:
                    ima3=li.lineahorizontal(fll,coll,f11,c11,ele)
                    listareporte.append(report("operacion",reporte))
                    mo3()
                    iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                    icon = ImageTk.PhotoImage(Image.open(iconPath))
                    icon_size = Label(raiz)
                    icon_size.image = icon  # <== this is were we anchor the img object
                    icon_size.configure(image=icon)
                    icon_size.grid(column=2,row=50)
                    raiz.update()
                
            elif(ve !=''):
                reporte=today+" Nombre Matriz: "+valor+", Tipo operacion: Linea Vertical"
                print
                vv=[]
                f11=""
                c11=""
                ele=""
                f1=0
                c1=0
                elel=0
                vv=ve.split(",")
                f11=vv[0]
                c11=vv[1]
                ele=vv[2]
                f1=int(f11)
                c1=int(c11)
                elel=int(ele)
                if(f1>int(fll)):
                    reporte=reporte+" La primera fila ingresada: "+f11+" ingresada es mayor que la dimension aceptada: "+fll
                    listareporte.append(report("error",reporte))
                elif(c1==0 or f1==0 or elel==0):
                    reporte=reporte+"Los elementos ingresados o dimensiones no pueden ser 0 "
                    listareporte.append(report("error",reporte))
                elif(c1>int(coll)):
                    reporte=reporte+" La primera columna ingresada: "+c11+" ingresada es mayor que la dimension aceptada: "+coll
                    listareporte.append(report("error",reporte))
                elif(elel>int(fll)):
                    reporte=reporte+"EL numero de elementos: "+ele+" es mas grande que una de las dimensiones  fila: "+fll
                    listareporte.append(report("error",reporte))
                else:
                    ima3=li.lineavertical(fll,coll,f11,c11,ele)
                    listareporte.append(report("operacion",reporte))
                    mo3()
                    iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                    icon = ImageTk.PhotoImage(Image.open(iconPath))
                    icon_size = Label(raiz)
                    icon_size.image = icon  # <== this is were we anchor the img object
                    icon_size.configure(image=icon)
                    icon_size.grid(column=2,row=50)
                    raiz.update()
            elif(re !=''):
                reporte=today+" Nombre Matriz: "+valor+", Tipo operacion: Rectangulo"
                rr=[]
                f11=""
                f22=""
                c11=""
                c22=""
                f1=0
                f2=0
                c1=0
                c2=0
                rr=re.split(",")
                f11=rr[0]
                c11=rr[1]
                f22=rr[2]
                c22=rr[3]
                f1=int(f11)
                f2=int(f22)
                c1=int(c11)
                c2=int(c22)
                print(f11,c11,f22,c22)
                if(f1==0 or f2==0 or c1==0 or c2==0):
                    reporte=reporte+" Las dimensiones no pueden ser igual a 0"
                    listareporte.append(report("error",reporte))
                elif(f1>int(fll)):
                    reporte=reporte+" La primera fila ingresada: "+f11+" ingresada es mayor que la dimension aceptada: "+fll
                    listareporte.append(report("error",reporte))
                elif(f2>int(fll)):
                    reporte=reporte+" La primera fila ingresada: "+f22+" ingresada es mayor que la dimension aceptada: "+fll
                    listareporte.append(report("error",reporte))
                elif(f1>f2):
                    reporte=reporte+" La segunda fila ingresada: "+f11+" ingresada es menor que la primera ingresada: "+f22
                    listareporte.append(report("error",reporte))
                elif(c1>int(coll)):
                    reporte=reporte+" La primera columna ingresada: "+c11+" ingresada es mayor que la dimension aceptada: "+coll
                    listareporte.append(report("error",reporte))
                elif(c2>int(coll)):
                    reporte=reporte+" La segunda columna ingresada: "+c22+" ingresada es mayor que la dimension aceptada: "+coll
                    listareporte.append(report("error",reporte))
                elif(c1>c2):
                    reporte=reporte+" La segunda columna ingresada: "+c11+" ingresada es menor que la primera ingresada: "+c22
                    listareporte.append(report("error",reporte))
                else:
                    ima3=li.rectangulo(fll,coll,f11,c11,f22,c22)
                    listareporte.append(report("operacion",reporte))
                    valor=valor
                    
                    mo3()
                    iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                    icon = ImageTk.PhotoImage(Image.open(iconPath))
                    icon_size = Label(raiz)
                    icon_size.image = icon  # <== this is were we anchor the img object
                    icon_size.configure(image=icon)
                    icon_size.grid(column=2,row=50)
                    raiz.update()
            elif(tri !=''):
                reporte=today+" Nombre Matriz: "+valor+", Tipo operacion: Triangulo"
                print
                tt=[]
                f11=""
                c11=""
                ele=""
                f1=0
                
                c1=0
                elel=0
                tt=tri.split(",")
                f11=tt[0]
                c11=tt[1]
                ele=tt[2]
                f1=int(f11)
                
                c1=int(c11)
                elel=int(ele)
                if(f1>int(fll)):
                    reporte=reporte+" La primera fila ingresada: "+f11+" ingresada es mayor que la dimension aceptada: "+fll
                    listareporte.append(report("error",reporte))
                elif(c1==0 or f1==0 or elel==0):
                    reporte=reporte+"Los elementos ingresados o dimensiones no pueden ser 0 "
                    listareporte.append(report("error",reporte))
                elif(c1>int(coll)):
                    reporte=reporte+" La primera columna ingresada: "+c11+" ingresada es mayor que la dimension aceptada: "+coll
                    listareporte.append(report("error",reporte))
                elif(elel>int(fll)):
                    reporte=reporte+"EL numero de elementos: "+ele+" es mas grande que una de las dimensiones  fila: "+fll
                    listareporte.append(report("error",reporte))
                else:
                    ima3=li.triangul(fll,coll,f11,c11,ele)
                    listareporte.append(report("operacion",reporte))
                    mo3()
                    iconPath = r"C:\Users\denni\OneDrive\Desktop\ima3.jpg"
                    icon = ImageTk.PhotoImage(Image.open(iconPath))
                    icon_size = Label(raiz)
                    icon_size.image = icon  # <== this is were we anchor the img object
                    icon_size.configure(image=icon)
                    icon_size.grid(column=2,row=50)
                    raiz.update()

            else:
                messagebox.showinfo("matriz","Llenar Datos Porfavor")
            

        B = ttk.Button(raiz, text ="Seleccionar",command=verlo)
        B2 = ttk.Button(raiz, text ="Seleccionar", command=verlo2)
        B3 = ttk.Button(raiz, text ="Seleccionar",command=operar)
        B4 = ttk.Button(raiz, text ="Seleccionar",command=rotacion)
        B5 = ttk.Button(raiz, text ="Seleccionar",command=extra)
        B.grid(column = 2, row = 15)
        B2.grid(column = 2, row = 20)
        B4.grid(column = 2, row = 30)
        B3.grid(column = 2, row = 25) 
        B5.grid(column = 7, row = 40)
        triangulo.grid(column=8,row=35)
        horizontal.grid(column=8,row=20)
        vertical.grid(column=8,row=25)
        rectangulo.grid(column=8,row=30)
        limpiar.grid(column=8,row=15)
        
    raiz.mainloop()

def html():
    global listareporte
    qu=""
    sk=""
    nombre=""
    estado=0
    error=[]
    matriz=[]
    operacion=[]
    f = open(r"C:\Users\denni\OneDrive\Desktop\reporte.html",'w')
    f.write("<html> <head> <style> </style></head> <body>"+'\n')
    for i in listareporte:
        ver=i.id
        nombre=i.descripcion
        if(ver=="operacion"):
            operacion.append(nombre)
        elif(ver=="matriz"):
            matriz.append(nombre)
        elif(ver=="error"):
            error.append(nombre)
    f.write("<h1 align="+qu+"center"+qu+">Matrices Trabajadas</h1>"+'\n')
    for j in matriz:
        nombre=j
        f.write("<h2>"+nombre+"</h2>"+'\n')
    f.write("<h1 align="+qu+"center"+qu+">Operaciones</h1>"+'\n')
    for k in operacion:
        nombre=k
        f.write("<h2>"+nombre+"</h2>"+'\n')
    f.write("<h1 align="+qu+"center"+qu+">Errores</h1>"+'\n')
    for l in error:
        nombre=l
        f.write("<h2>"+nombre+"</h2>"+'\n')

    f.write("</body> </html>")


    f.close()      
    os.startfile(r"C:\Users\denni\OneDrive\Desktop\reporte.html")
def traa(fila,columna):
        li3.eliminar()
        global valor
        global fll3
        global coll3
        linea=''
        jump=''
        final=''
        ver=True
        flag=True
        estado=0
        f1=int(fila)
        c1=int(columna)
        ff=int(columna)
        cc=int(fila)
        kf=ff+1
        kc=cc+1
        x=1
        y=1
        fila=1
        columna=1
        vv3=False       
        while ver==True:
            if(estado==0):
                if(x<=c1):
                    if(y<=f1):
                        val=li.buscar1(y,x)
                        li3.insertar(x,y,val,valor)
                        if(x==c1):
                            y=y+1
                            x=1
                            if(y>f1):
                                ver=False
                                estado=1
                        else:
                            x=x+1
                elif(y<=f1):
                    print

        
        for i in  range(1, kf):
            if(flag==False):
                    print
            else:
                salto=linea+'\n'
                final=final+salto
                linea=''
                print("final: \n"+final)
                flag=False      
            for j in range(1,kc):
                val=li3.buscar1(i,j)
                if val==None:
                    pass
                else:
                    
                    linea=linea+val
                    flag=True
        return(final)
def mo1():
    global ima
    global valor
    global fll
    global coll
    kf=int(fll)
    kc=int(coll)
    kf=kf+1
    kc=kc+1
    f=1
    c=1
    fila=int(fll)
    columna=int(coll)
    x=1
    y=1
    flag=False
    quotes='"'
    MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\ima.txt",'w')
    MapaRuta.write('digraph {' + "\n")
    MapaRuta.write('node [shape=plaintext]' + "\n")
    MapaRuta.write('some_node [' + "\n")
    MapaRuta.write('label=<' + "\n")
    MapaRuta.write('<table border="0" cellborder="1" cellspacing="0">' + "\n")
    MapaRuta.write('<tr>' + "\n")
    MapaRuta.write('<td>' + "\n")
    MapaRuta.write(valor + "\n")
    MapaRuta.write('</td>' + "\n")
    for i in range(1,kc):
        MapaRuta.write('<td>' + "\n")
        MapaRuta.write(str(i) + "\n")
        MapaRuta.write('</td>' + "\n")
    MapaRuta.write('</tr>' + "\n")
    for i in range(1,kf):
        MapaRuta.write('<tr>' + "\n")
        MapaRuta.write('<td>' + "\n")
        MapaRuta.write(str(i) + "\n")
        MapaRuta.write('</td>' + "\n")
        for j in range(1,kc):
            val=li.buscar1(i,j)
            MapaRuta.write('<td>' + "\n")
            MapaRuta.write(val + "\n")
            MapaRuta.write('</td>' + "\n")
            if(j==columna):
                MapaRuta.write('</tr>' + "\n")

    MapaRuta.write(' </table>>' + "\n")
    MapaRuta.write('  ];' + "\n")
    MapaRuta.write(' }' + "\n")
    MapaRuta.close()
    os.system("dot -Tsvg "r"C:\Users\denni\OneDrive\Desktop\ima.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima.svg")
    os.system("dot -Tjpg "r"C:\Users\denni\OneDrive\Desktop\ima.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima.jpg")
    os.system("dot -Tpng "r"C:\Users\denni\OneDrive\Desktop\ima.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima.png")
def mo3():
    global ima
    global valor
    global fll3
    global coll3
    kf=int(fll3)
    kc=int(coll3)
    kf=kf+1
    kc=kc+1
    f=1
    c=1
    fila=int(fll3)
    columna=int(coll3)
    x=1
    y=1
    flag=False
    quotes='"'
    MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\ima3.txt",'w')
    MapaRuta.write('digraph {' + "\n")
    MapaRuta.write('node [shape=plaintext]' + "\n")
    MapaRuta.write('some_node [' + "\n")
    MapaRuta.write('label=<' + "\n")
    MapaRuta.write('<table border="0" cellborder="1" cellspacing="0">' + "\n")
    MapaRuta.write('<tr>' + "\n")
    MapaRuta.write('<td>' + "\n")
    MapaRuta.write(valor + "\n")
    MapaRuta.write('</td>' + "\n")
    for i in range(1,kc):
        MapaRuta.write('<td>' + "\n")
        MapaRuta.write(str(i) + "\n")
        MapaRuta.write('</td>' + "\n")
    MapaRuta.write('</tr>' + "\n")
    for i in range(1,kf):
        MapaRuta.write('<tr>' + "\n")
        MapaRuta.write('<td>' + "\n")
        MapaRuta.write(str(i) + "\n")
        MapaRuta.write('</td>' + "\n")
        for j in range(1,kc):
            print(i,j)
            val=li3.buscar1(i,j)
            print(val)
            MapaRuta.write('<td>' + "\n")
            MapaRuta.write(val + "\n")
            MapaRuta.write('</td>' + "\n")
            if(j==columna):
                MapaRuta.write('</tr>' + "\n")

    MapaRuta.write(' </table>>' + "\n")
    MapaRuta.write('  ];' + "\n")
    MapaRuta.write(' }' + "\n")
    MapaRuta.close()
    os.system("dot -Tsvg "r"C:\Users\denni\OneDrive\Desktop\ima3.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima3.svg")
    os.system("dot -Tjpg "r"C:\Users\denni\OneDrive\Desktop\ima3.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima3.jpg")
    os.system("dot -Tpng "r"C:\Users\denni\OneDrive\Desktop\ima3.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima3.png")       
def mostrar1():
    global ima
    global valor
    global fll
    global coll
    kf=int(fll)
    kc=int(coll)
    kf=kf+1
    kc=kc+1
    f=1
    c=1
    fila=int(fll)
    columna=int(coll)
    x=1
    y=1
    flag=False
    quotes='"'
    MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\ima.txt",'w')
    MapaRuta.write('digraph {' + "\n")
    MapaRuta.write('node [shape=plaintext]' + "\n")
    MapaRuta.write('some_node [' + "\n")
    MapaRuta.write('label=<' + "\n")
    MapaRuta.write('<table border="0" cellborder="1" cellspacing="0">' + "\n")
    for i in range(1,kf):
        MapaRuta.write('<tr>' + "\n")
        for j in range(1,kc):
            val=li.buscar1(i,j)
            if(y==1):
                if(x==1):
                    MapaRuta.write('<td>' + "\n")
                    nv=str(c)+"|"+valor+"<br/>"+val
                    MapaRuta.write(quotes+nv+quotes + "\n")
                    MapaRuta.write('</td>' + "\n")
                    x=x+1
                    c=c+1
                    print
                elif(x<=columna):
                    if(x==columna):
                        y=y+1
                        x=1
                        
                        MapaRuta.write('<td>' + "\n")
                        nv=str(c)+"<br/>----<br/>"+"\n"+val
                        MapaRuta.write(quotes+nv+quotes + "\n")
                        MapaRuta.write('</td>' + "\n")
                        c=2
                    else:
                        MapaRuta.write('<td>' + "\n")
                        nv=str(c)+"<br/>----<br/>"+"\n"+val
                        MapaRuta.write(quotes+nv+quotes + "\n")
                        MapaRuta.write('</td>' + "\n")
                        x=x+1
                        c=c+1
            elif(y<=fila):
                if(x==1):
                    MapaRuta.write('<td>' + "\n")
                    nv=str(f)+"| "+val
                    MapaRuta.write(quotes+nv+quotes + "\n")
                    MapaRuta.write('</td>' + "\n")
                    x=x+1
                    
                elif(x<=columna):
                    if(x==columna):
                        x=1
                        c=2
                        f=f+1
                        MapaRuta.write('<td>' + "\n")
                        nv=val
                        MapaRuta.write(quotes+nv+quotes + "\n")
                        MapaRuta.write('</td>' + "\n")
                    else:
                        MapaRuta.write('<td>' + "\n")
                        nv=val
                        MapaRuta.write(quotes+nv+quotes + "\n")
                        MapaRuta.write('</td>' + "\n")


                





        MapaRuta.write('</tr>' + "\n")
    

    MapaRuta.write(' </table>>' + "\n")
    MapaRuta.write('  ];' + "\n")
    MapaRuta.write(' }' + "\n")
    MapaRuta.close()
def mo2():
    global ima2
    global valor2
    global fll2
    global coll2
    kf=int(fll2)
    kc=int(coll2)
    kf=kf+1
    kc=kc+1
    f=1
    c=1
    fila=int(fll2)
    columna=int(coll2)
    x=1
    y=1
    flag=False
    quotes='"'
    MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\ima2.txt",'w')
    MapaRuta.write('digraph {' + "\n")
    MapaRuta.write('node [shape=plaintext]' + "\n")
    MapaRuta.write('some_node [' + "\n")
    MapaRuta.write('label=<' + "\n")
    MapaRuta.write('<table border="0" cellborder="1" cellspacing="0">' + "\n")
    MapaRuta.write('<tr>' + "\n")
    MapaRuta.write('<td>' + "\n")
    MapaRuta.write(valor2 + "\n")
    MapaRuta.write('</td>' + "\n")
    for i in range(1,kc):
        MapaRuta.write('<td>' + "\n")
        MapaRuta.write(str(i) + "\n")
        MapaRuta.write('</td>' + "\n")
    MapaRuta.write('</tr>' + "\n")
    for i in range(1,kf):
        MapaRuta.write('<tr>' + "\n")
        MapaRuta.write('<td>' + "\n")
        MapaRuta.write(str(i) + "\n")
        MapaRuta.write('</td>' + "\n")
        for j in range(1,kc):
            val=li2.buscar1(i,j)
            MapaRuta.write('<td>' + "\n")
            MapaRuta.write(val + "\n")
            MapaRuta.write('</td>' + "\n")
            if(j==columna):
                MapaRuta.write('</tr>' + "\n")

    MapaRuta.write(' </table>>' + "\n")
    MapaRuta.write('  ];' + "\n")
    MapaRuta.write(' }' + "\n")
    MapaRuta.close()
    os.system("dot -Tsvg "r"C:\Users\denni\OneDrive\Desktop\ima2.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima2.svg")
    os.system("dot -Tjpg "r"C:\Users\denni\OneDrive\Desktop\ima2.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima2.jpg")
    os.system("dot -Tpng "r"C:\Users\denni\OneDrive\Desktop\ima2.txt -o "r"C:\Users\denni\OneDrive\Desktop\ima2.png")
def leerimagen1():
    li.eliminar()
    global lista_matriz
    global listaextra
    global original
    global valor
    global fll
    global coll
    original=""
    today = now.strftime("%d/%m/%Y %H:%M:%S")
    reporte=""
    reporte=today + " Nombre Matriz: "+valor
    lleno=0
    vacio=0
    for ii in lista_matriz:
        nn=ii.nombre
        if (nn==valor):
            original=ii.imagen
            fll=ii.fila
            coll=ii.columna
    char=''
    next_char=''
    cc=1
    ff=1
    estado=0
    for i in range(len(original)):
          
        char=original[i]
        try:
         next_char=original[i+1]
        except:
          next_char= ' '
        print(estado, ":", char,":", next_char)
        if(estado==0):
            if(char=='-'):
                li.insertar(ff,cc,char,valor)
                listaextra.append(char)
                cc=cc+1
                vacio=vacio+1
            elif(char=='*'):
                li.insertar(ff,cc,char,valor)
                listaextra.append(char)
                cc=cc+1
                lleno=lleno+1
            elif(char.isspace()):
                estado=1
        elif(estado==1):
            if(char=='-'):
                li.insertar(ff,cc,char,valor)
                listaextra.append(char)
                vacio=vacio+1
                cc=cc+1
            elif(char=='*'):
                li.insertar(ff,cc,char,valor)
                listaextra.append(char)
                lleno=lleno+1
                cc=cc+1
            elif(char.isspace()):
                estado=1
                if(char=='\n'):
                    listaextra.append(char)
                    ff=ff+1
                    cc=1
                    estado=0
    reporte=reporte+", Espacios LLenos: "+str(lleno)+", Espacios Vacios: "+str(vacio)
    listareporte.append(report("matriz",reporte))
    mo1()
def leerimagen2():
    li2.eliminar()
    global lista_matriz
    global segunda
    global valor2
    global fll2
    global coll2
    original=""
    today = now.strftime("%d/%m/%Y %H:%M:%S")
    reporte=""
    lleno=0
    vacio=0
    reporte=today + " Nombre Matriz: "+valor2
    for ii in lista_matriz:
        nn=ii.nombre
        if nn==valor2:
            segunda=ii.imagen
            fll2=ii.fila
            coll2=ii.columna
    char=''
    next_char=''
    cc=1
    ff=1
    estado=0
    for i in range(len(segunda)):
         
        char=segunda[i]
        try:
         next_char=segunda[i+1]
        except:
          next_char= ' '
        print(estado, ":", char,":", next_char)
        if(estado==0):
            if(char=='-'):
                li2.insertar(ff,cc,char,valor2)
                vacio=vacio+1
                cc=cc+1
            elif(char=='*'):
                li2.insertar(ff,cc,char,valor2)
                cc=cc+1
                lleno=lleno+1
            elif(char.isspace()):
                estado=1
                
        elif(estado==1):
            if(char=='-'):
                li2.insertar(ff,cc,char,valor2)
                vacio=vacio+1
                cc=cc+1
            elif(char=='*'):
                li2.insertar(ff,cc,char,valor2)
                lleno=lleno+1
                cc=cc+1
            elif(char.isspace()):
                estado=1
                if(char=='\n'):
                    ff=ff+1
                    cc=1
                    estado=0
    reporte=reporte+", Espacios LLenos: "+str(lleno)+", Espacios Vacios: "+str(vacio)
    listareporte.append(report("matriz",reporte))
    mo2()
def operar():
    global lista_matriz
    global original
    global segunda
    global resultado
    global tipo
    global valor
    global valor2
    listaux=[]
    #"Unión", "Intersección", "Diferencia", "Diferenciasimétrica"
    if(tipo.casefold()=="Unión"):
        print
    elif(tipo.casefold()=="Intersección"):
        print
    elif(tipo.casefold()=="Diferencia"):
        print
    elif(tipo.casefold()=="Diferenciasimétrica"):
        print

if __name__ == "__main__":
    main()
