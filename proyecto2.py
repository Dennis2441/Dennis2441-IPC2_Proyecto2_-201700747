from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import xml.dom.minidom
import numpy as np
from xml.dom import minidom
from xml.dom.minidom import Node

import os
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
ima=""
ima2=""
ima3=""
listaextra=[]
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
                        linea=linea+val
                        f1=f1+1
                    else:
                        linea=linea+val
                        f1=0
                else:
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
        return(final)
    def lineahorizontal(self,fila,columna,f11,c11,ele):
        linea=''
        jump=''
        final=''
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
                        linea=linea+val
                        c1=c1+1
                    else:
                        linea=linea+val
                        c1=0
                else:
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
        return(final)
    def Limpiar(self,fila,columna,f11,c11,f22,c22):
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
        for i in range(1,jk):
            for j in range(1, kj):
                val=self.buscar1(i,j)

                if val==None:
                    pass
                elif(i==f1 and j==c1):
                    if(c1<c2):
                        val="-"
                        linea=linea+val
                        c1=c1+1
                        if(c1==c2):
                            c1=aux
                            f1=f1+1
                            if(f1>f2):
                                f1=0
                            


                else:
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
        return(final)
    def rectangulo(self,fila,columna,f11,c11,f22,c22):
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
                            linea=linea+val
                            c1=c3
                        elif(c1==c3):
                            val="*"
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
                            linea=linea+val
                            c1=c1+1
                            if(c1==c2):
                                c1=0
                                estado=0

                    
                else:
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
        linea=''
        jump=''
        final=''
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        f1=int(f11)
        c1=int(c11)
        aux=int(c11)
        f2=int(ele)
        c2=int(ele)
        flag=False
        flag2=False
        n=1
        estado=0
        for i in range(1,jk):
            for j in range(1, kj):
                val=self.buscar1(i,j)
                print("linea:"+linea)
                if val==None:
                    pass
                elif(i==f1 and j==c1):
                    print()
                else:
                    linea=linea+val
            salto=linea+'\n'
            final=final+salto
            linea=''
            print("final: \n"+final)
        return(final)
    def vertical(self,fila,columna):
        linea=''
        jump=''
        final=''
        jk=int(fila)
        jk=jk+1
        kj=int(columna)
        kj=kj+1
        cab=self.ecolumnas.primero
        
        return(final)
                
        




                    







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
        menubar.add_command(label='Reportes')
        
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
    raiz=Tk()
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
            
            
            valor=combo.get()
            valor2=combo2.get()
            
            if valor=="":
                if valor=="":
                    messagebox.showinfo("matriz","Escoger matriz orginal antes de operar")
            else:
                leerimagen1()
                global ima
                global fll
                global coll
                ima=""
                ima= li.matrizp(fll,coll)
                valor=valor+'\n'
                ttk.Label(raiz, text ="Original: "+ valor +str(ima), 
                font = ("Times New Roman", 25)).grid(column=0,
                row=50)
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
                valor2=valor2+'\n'
                ttk.Label(raiz, text ="Segunda:  "+ valor2 +str(ima2), 
                font = ("Times New Roman", 25)).grid(column=1,
                row=50)
        
        
        def rotacion():
            global lista_matriz
            global original
            global segunda
            global valor
            
            
            au=cb2.get()
            if valor=="":
                if valor=="":
                    messagebox.showinfo("matriz","Escoger matriz orginal antes de operar")
            elif(au==""):
                messagebox.showinfo("matriz","Escoger Rotacion")
            else:
                global ima3
                global fll
                global coll
                ima3=li.vertical(fll,coll)
                au=au+'\n'
                ttk.Label(raiz, text ="Rotacion: "+ au +str(ima3), 
                font = ("Times New Roman", 25)).grid(column=2,
                row=50)
        def extra():
            global lista_matriz
            global original
            global segunda
            global valor
            global ima3
            global fll
            global coll
            
            lim=str(limpiar.get())
            ho=str(horizontal.get())
            ve=str(vertical.get())
            re=str(rectangulo.get())
            tri=str(triangulo.get())

            if valor=="":
                if valor=="":
                    messagebox.showinfo("matriz","Escoger matriz orginal antes de operar")
            elif(lim !=''):
                print()
                oo=[]
                f11=""
                f22=""
                c11=""
                c22=""
                oo=lim.split(",")
                f11=oo[0]
                c11=oo[1]
                f22=oo[2]
                c22=oo[3]    
                print(f11,c11,f22,c22)
                ima3=li.Limpiar(fll,coll,f11,c11,f22,c22)
                valor=valor
                ttk.Label(raiz, text ="Limpiar : "+ valor +str(ima3), 
                font = ("Times New Roman", 25)).grid(column=3,
                row=50)
                #ima3=li.Limpiar()
            elif(ho !=''):
                print
                hh=[]
                f11=""
                c11=""
                ele=""
                hh=ho.split(",")
                f11=hh[0]
                c11=hh[1]
                ele=hh[2]
                ima3=li.lineahorizontal(fll,coll,f11,c11,ele)
                ttk.Label(raiz, text ="Linea Horizontal : "+ valor +str(ima3), 
                font = ("Times New Roman", 25)).grid(column=3,
                row=50)
            elif(ve !=''):
                print
                vv=[]
                f11=""
                c11=""
                ele=""
                vv=ve.split(",")
                f11=vv[0]
                c11=vv[1]
                ele=vv[2]
                ima3=li.lineavertical(fll,coll,f11,c11,ele)
                ttk.Label(raiz, text ="Linea Horizontal : "+ valor +str(ima3), 
                font = ("Times New Roman", 25)).grid(column=3,
                row=50)
            elif(re !=''):
                rr=[]
                f11=""
                f22=""
                c11=""
                c22=""
                rr=re.split(",")
                f11=rr[0]
                c11=rr[1]
                f22=rr[2]
                c22=rr[3]    
                print(f11,c11,f22,c22)
                ima3=li.rectangulo(fll,coll,f11,c11,f22,c22)
                valor=valor
                ttk.Label(raiz, text ="Rectangulo : "+ valor +str(ima3), 
                font = ("Times New Roman", 25)).grid(column=3,
                row=50)
            elif(tri !=''):
                print
                tt=[]
                f11=""
                c11=""
                ele=""
                tt=tri.split(",")
                f11=tt[0]
                c11=tt[1]
                ele=tt[2]
                ima3=li.triangul(fll,coll,f11,c11,ele)
                ttk.Label(raiz, text ="Linea Horizontal : "+ valor +str(ima3), 
                font = ("Times New Roman", 25)).grid(column=3,
                row=50)
            else:
                messagebox.showinfo("matriz","Llenar Datos Porfavor")
            

        B = ttk.Button(raiz, text ="Seleccionar",command=verlo)
        B2 = ttk.Button(raiz, text ="Seleccionar", command=verlo2)
        B3 = ttk.Button(raiz, text ="Seleccionar")
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

def leerimagen1():
    global lista_matriz
    global listaextra
    global original
    global valor
    global fll
    global coll
    original=""
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
            elif(char=='*'):
                li.insertar(ff,cc,char,valor)
                listaextra.append(char)
                cc=cc+1
            elif(char.isspace()):
                estado=1
        elif(estado==1):
            if(char=='-'):
                li.insertar(ff,cc,char,valor)
                listaextra.append(char)
                cc=cc+1
            elif(char=='*'):
                li.insertar(ff,cc,char,valor)
                listaextra.append(char)
                cc=cc+1
            elif(char.isspace()):
                estado=1
                if(char=='\n'):
                    listaextra.append(char)
                    ff=ff+1
                    cc=1
                    estado=0
    
def leerimagen2():
    global lista_matriz
    global segunda
    global valor2
    global fll2
    global coll2
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
                cc=cc+1
            elif(char=='*'):
                li2.insertar(ff,cc,char,valor2)
                cc=cc+1
            elif(char.isspace()):
                estado=1
                
        elif(estado==1):
            if(char=='-'):
                li2.insertar(ff,cc,char,valor2)
                cc=cc+1
            elif(char=='*'):
                li2.insertar(ff,cc,char,valor2)
                cc=cc+1
            elif(char.isspace()):
                estado=1
                if(char=='\n'):
                    ff=ff+1
                    cc=1
                    estado=0
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
