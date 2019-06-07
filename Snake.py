from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pygame
from pygame.locals import *
import time
import random
import sys
import threading
import pickle
import webbrowser as wb
from reportlab.pdfgen import canvas

#                                 - Ventanas -
ventana_inicio = Tk()
ventana_inicio.title ("Just a another Snake Game")
ventana_inicio.geometry ("700x400")
ventana_inicio.configure(bg="#0A768D")
ventana_inicio.resizable(False,False)
ventana_inicio.withdraw()

ventana_configuracion = Toplevel()
ventana_configuracion.title ("Configuracion")
ventana_configuracion.geometry ("1200x600")
ventana_configuracion.configure(bg="#0A768D")
ventana_configuracion.resizable(False,False)
ventana_configuracion.withdraw()

ventana_calificaciones = Toplevel()
ventana_calificaciones.title ("Tabla de Calificaciones")
ventana_calificaciones.geometry ("800x600")
ventana_calificaciones.configure(bg="#0A768D")
ventana_calificaciones.resizable(False,False)
ventana_calificaciones.withdraw()

ventana_ayuda = Toplevel()
ventana_ayuda.title ("Ayuda")
ventana_ayuda.geometry ("800x600")
ventana_ayuda.configure(bg="#0A768D")
ventana_ayuda.resizable(False,False)
ventana_ayuda.withdraw()

ventana_acerca = Toplevel()
ventana_acerca.title ("Acerca de")
ventana_acerca.geometry ("800x600")
ventana_acerca.configure(bg="#0A768D")
ventana_acerca.resizable(False,False)
ventana_acerca.withdraw()
#---------------------------------------------------------------
#Ventana de Login

ventana_init = Toplevel()
ventana_init.title ("Just a Another Snake Game")
ventana_init.geometry ("500x300")
ventana_init.configure(bg="#0A768D")
ventana_init.resizable(False,False)

ventana_login = Toplevel()
ventana_login.title ("Login")
ventana_login.geometry ("600x400")
ventana_login.configure(bg="#0A768D")
ventana_login.resizable(False,False)
ventana_login.withdraw()

ventana_iniciar = Toplevel()
ventana_iniciar.title ("Iniciar Sesion")
ventana_iniciar.geometry ("800x400")
ventana_iniciar.configure(bg="#0A768D")
ventana_iniciar.resizable(False,False)
ventana_iniciar.withdraw()

ventana_1 = Tk()
ventana_1.title("Perdiste")
ventana_1.geometry ("500x400")
ventana_1.configure(bg="#0A768D")
ventana_1.resizable(False,False)
ventana_1.withdraw()

ventana_gj = Tk()
ventana_gj.title("Guardar Juego")
ventana_gj.geometry ("600x300")
ventana_gj.configure(bg="#0A768D")
ventana_gj.resizable(False,False)
ventana_gj.withdraw()

ventana_cj = Tk()
ventana_cj.title("Cargar Juego")
ventana_cj.geometry ("800x400")
ventana_cj.configure(bg="#0A768D")
ventana_cj.resizable(False,False)
ventana_cj.withdraw()



#                              - Variables o imagenes -
global direc_perfil

borde = PhotoImage(file="imagenes\Borde.png")
lupa = PhotoImage(file="imagenes\lupa.png")
direc_perfil = "imagenes\cuadro_blanco.png"
imagen_perfil = PhotoImage(file=direc_perfil)

#_----------------------------- Variables Configuracion -----------------------
global parametros_juego
global tamaño_matriz
global multi
global parametros_nuevo
global paredes_juego
global Manzana
global Cab_Hor
global Cab_Ver
global Cola_Hor
global Cola_Ver
global Curva
global Fondo
global Pared
global rojo
global nick
global score
global rank_1
global rank_2
global musica_fondo
global musica_manzana
global musica_ganar
global chocar_1
global chocar_2

musica_fondo = ""
musica_manzana = ""
musica_ganar = ""
chocar_1 = ""
chocar_2 = ""

rojo = (255,0,0)

rank_1 = IntVar()
rank_2 = IntVar()

nick = "User"
tamaño = IntVar()
paredes = IntVar()
paredes_juego = "no"
parametros_juego = (420,420)
parametros_nuevo = (440,490)
tamaño_matriz = 5
multi = 1

Manzana = "imagenes\punto.png"
Cab_Hor = "imagenes\cabeza horizontal.png"
Cab_Ver = "imagenes\cabeza vertical.png"
Cola_Hor = "imagenes\seccion_horizontal.png"
Cola_Ver = "imagenes\seccion_vertical.png"
Curva = "imagenes\curva.png"
Fondo = "imagenes\Marco.png"
Pared = "imagenes\seccion_horizontal 1.png"

#                                   - Funciones -
#----------------------------------- Funciones Ranking ----------------------------------
def crear_pdf():
    s = rank_1.get()
    
    c = canvas.Canvas("Top 10.pdf")
    c.setFont('Helvetica', 20)
    c.drawString(200,750,"Registro del Top 10")

    if s==1:
        lista = obtener_1()
        c.drawString(180,720,"Top 10 en el modo 14x14")
        
    elif s==2:
        lista = obtener_2()
        c.drawString(180,720,"Top 10 en el modo 16x16")
        
    elif s==3:
        lista = obtener_3()
        c.drawString(180,720,"Top 10 en el modo 18x18")
        
    else:
        lista = obtener_4()
        c.drawString(180,720,"Top 10 en el modo 20x20")

    c.drawString(150,640,"Posicion")
    c.drawString(250,640,"Score")
    c.drawString(350,640,"Nickname")
    
    cont = 1   
    y = 600
    for parte in lista:
        c.drawString(190,y,str(cont))

        c.drawString(230,y," | ")

        c.drawString(250,y,parte[1])

        c.drawString(330,y," | ")

        c.drawString(350,y,parte[0])
        
        y = y-30
        cont = cont+1
        
        
    
    c.save()
    
    wb.open_new("Top 10.pdf")

    
def verificar_top():
    s = rank_1.get()
    
    if s==1:
        x = obtener_1()
    elif s==2:
        x = obtener_2()
    elif s==3:
        x = obtener_3()
    else:
        x = obtener_4()
        
    yei = 80
    for lista in x:
        name = lista[0]
        scor = lista [1]

        l1 = Label(ventana_calificaciones,text=scor,bg="#0A768D",fg="white",font=("Arial Black",14))
        l1.place(x=400,y=yei)

        l1 = Label(ventana_calificaciones,text=name,bg="#0A768D",fg="white",font=("Arial Black",14))
        l1.place(x=480,y=yei)

        yei = yei+30
        
def ranking(s):
    global score
    global nick
    
    if s==1:
        x = obtener_1()
    elif s==2:
        x = obtener_2()
    elif s==3:
        x = obtener_3()
    else:
        x = obtener_4()
    ind = 0
    for elemento in x:
        if int(elemento[1]) < int(score):
            x.insert(ind,[nick,score])
            break
        ind = ind+1
        
    x = x[0:10]
    print(x)
    if s==1:
        guardar_1(x)
    elif s==2:
        guardar_2(x)
    elif s==3:
        guardar_3(x)
    else:
        guardar_4(x)
    
        
def guardar_1(l):
    archivo = open("14x14","wb")
    pickle.dump(l,archivo)
    archivo.close()

def guardar_2(l):
    archivo = open("16x16","wb")
    pickle.dump(l,archivo)
    archivo.close()

def guardar_3(l):
    archivo = open("18x18","wb")
    pickle.dump(l,archivo)
    archivo.close()

def guardar_4(l):
    archivo = open("20x20","wb")
    pickle.dump(l,archivo)
    archivo.close()


def obtener_1():
    f=open("14x14","rb") # abrir archivo para leer datos
    while True:
        try: # controlar EOF
            x=pickle.load(f) # leer datos
            return (x)
        except EOFError:
            f.close()
            break  # cerrar archivo print ("Fin")

def obtener_2():
    f=open("16x16","rb") # abrir archivo para leer datos
    while True:
        try: # controlar EOF
            x=pickle.load(f) # leer datos
            return (x)
        except EOFError:
            f.close()
            break  # cerrar archivo print ("Fin")

def obtener_3():
    f=open("18x18","rb") # abrir archivo para leer datos
    while True:
        try: # controlar EOF
            x=pickle.load(f) # leer datos
            return (x)
        except EOFError:
            f.close()
            break  # cerrar archivo print ("Fin")

def obtener_4():
    f=open("20x20","rb") # abrir archivo para leer datos
    while True:
        try: # controlar EOF
            x=pickle.load(f) # leer datos
            return (x)
        except EOFError:
            f.close()
            break  # cerrar archivo print ("Fin")
#----------------------------------- Funciones Partida ----------------------------------
def guardar():
    pygame.quit()
    ventana_gj.deiconify()
    ventana_gj.update()
    

def guardar_partida(snake):
    archivo = open("archivos\guardar_snake","wb")
    pickle.dump(snake,archivo)
    archivo.close()
    
def agregar_partida():
    global pos_cuerpo
    global pos_cabeza_x
    global pos_cabeza_y
    global direccion
    global score
    
    user = str(textbox_nombre_partida.get())
    contraseña = str(textbox_part_cont_1.get())
    contraseña_1 = str(textbox_part_cont_2.get())
    archivo_1 = obtener()
    partidas = archivo_1.keys()
    
    if user in partidas:
        l = archivo_1[user]
        contra = l[0]
        if contraseña == contraseña_1:
            if contraseña == contra:
                messagebox.showinfo("Information","El usuario existe, se guardara la partida")

                snake = [direccion,pos_cabeza_x,pos_cabeza_y,pos_cuerpo]
                archivo_1[user] = [contraseña,snake,score]
                ventana_login.withdraw()
                ventana_inicio.deiconify()
                ventana_inicio.update()
                guardar_partida(archivo_1)
                
            else:
                messagebox.showinfo("Information","El usuario coincide pero las contraseñas no")
        else:
            messagebox.showinfo("Information","El usuario coincide pero las contraseñas no")
    elif contraseña != contraseña_1:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
    elif verificar_contraseña(contraseña) == False:
        messagebox.showerror("Error", "La contraseña no es segura")
    else:
        snake = [direccion,pos_cabeza_x,pos_cabeza_y,pos_cuerpo]
        
        archivo_1[user] = [contraseña,snake,score]
        ventana_login.withdraw()
        ventana_inicio.deiconify()
        ventana_inicio.update()
        guardar_partida(archivo_1)


#------------------------------ cargar partida ----------------------------------------
def cargar_juego():
    ventana_inicio.withdraw()
    ventana_cj.deiconify()

    partidas = obtener()
    llaves = partidas.keys()

    frame_1 = Frame(ventana_cj,bd=2,relief=SUNKEN,width=400,heigh=400)
    frame_1.place(x=10,y=10)
    
    listbox_1 = Listbox(frame_1,width=30,heigh=10,font=("Arial",14))
    listbox_1.pack()
    scroll_1 = Scrollbar(frame_1)
    colocar_scrollbar(listbox_1,scroll_1)

    cargar_listbox(llaves,listbox_1)

    boton_1 = Button(ventana_cj,text="Seleccionar",bg="Orange",fg="White",font=("Arial Black",14),width=10,command=lambda:imprimir_1(listbox_1))
    boton_1.place(x=10,y=300)

    boton_2 = Button(ventana_cj,text="Cancelar",bg="Orange",fg="White",font=("Arial Black",14),width=10,command=lambda:cancelar(ventana_cg,ventana_inicio))
    boton_2.place(x=200,y=300)

    boton_3 = Button(ventana_cj,text="Acceder",bg="Orange",fg="White",font=("Arial Black",14),width=10,command=lambda:verificar_cont_c(contraseña_2,nick_a,snake_body,score_aux))
    boton_3.place(x=600,y=300)

def imprimir_1(listbox):
    global nick_a
    global contraseña_2
    global snake_body
    global score_aux
    
    ind = listbox.curselection()
    if listbox.curselection() != ():
        nick_a = listbox.get(ind)
        nicknames = obtener()
        lista = nicknames[nick_a]
        contraseña_2 = lista[0]
        snake_body = lista[1]
        score_aux = lista[2]

        nickL = Label(ventana_cj,text=nick_a,bg="#0A768D",fg="White",font=("Arial Black",14),width=15)
        nickL.place(x=470,y=80)

def verificar_cont_c(contraseña,n,imag,s):
    global nick_a
    global snake_body
    global score
    texto = textbox_enter_cg.get()
    if texto != contraseña:
        messagebox.showerror("Error", "La contraseña no es correcta")
    else:
        nick_a = n
        snake_body = imag
        score = s
        
        ventana_cj.withdraw()
        abrir_ventana_continuar_juego()
        

#----------------------------------- Funciones Login ------------------------------------
#------------------------------------ Abrir cuenta --------------------------------------
def abrir_cuentas():
    ventana_init.withdraw()
    ventana_iniciar.deiconify()
    nicknames = obtener_nicknames()
    nicks = nicknames.keys()

    frame = Frame(ventana_iniciar,bd=2,relief=SUNKEN,width=400,heigh=400)
    frame.place(x=10,y=10)
    
    listbox = Listbox(frame,width=30,heigh=10,font=("Arial",14))
    listbox.pack()
    scroll = Scrollbar(frame)
    colocar_scrollbar(listbox,scroll)

    cargar_listbox(nicks,listbox)

    boton_1 = Button(ventana_iniciar,text="Seleccionar",bg="Orange",fg="White",font=("Arial Black",14),width=10,command=lambda:imprimir(listbox))
    boton_1.place(x=10,y=300)

    boton_2 = Button(ventana_iniciar,text="Cancelar",bg="Orange",fg="White",font=("Arial Black",14),width=10,command=lambda:cancelar(ventana_iniciar,ventana_init))
    boton_2.place(x=200,y=300)

    boton_3 = Button(ventana_iniciar,text="Acceder",bg="Orange",fg="White",font=("Arial Black",14),width=10,command=lambda:verificar_cont(contraseña_1,nick_1,dir_ima))
    boton_3.place(x=600,y=300)


def imprimir(listbox):
    global nick_1
    global contraseña_1
    global dir_ima
    ind = listbox.curselection()
    if listbox.curselection() != ():
        nick_1 = listbox.get(ind)
        nicknames = obtener_nicknames()
        lista = nicknames[nick_1]
        contraseña_1 = lista[0]
        dir_ima = lista[1]

        nickL = Label(ventana_iniciar,text=nick_1,bg="#0A768D",fg="White",font=("Arial Black",14),width=15)
        nickL.place(x=470,y=80)
        
        
def cargar_listbox(lista,listbox):
    for nick in lista:
        listbox.insert(END,nick)

def colocar_scrollbar(listbox,scrollbar):
    scrollbar.config(command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.pack(side=LEFT, fill=Y)

def verificar_cont(contraseña,n,imag):
    global nick
    global direc_perfil
    texto = textbox_enter.get()
    if texto != contraseña:
        messagebox.showerror("Error", "La contraseña no es correcta")
    else:
        nick = n
        direc_perfil = dir_ima

        nickL1 = Label(ventana_inicio,text="Bienvenido " + nick,bg="#0A768D",fg="White",font=("Arial Black",14),width=15)
        nickL1.place(x=20,y=10)
        
        ventana_iniciar.withdraw()
        ventana_inicio.deiconify()
#------------------------------------ Crear Cuenta --------------------------------------
def cambiar_imagen_perfil():
    global direc_perfil
    direc_perfil = askopenfilename()
    ventana_login.update()

def agregar_nickname():
    global direc_perfil
    global nick 
    nick = str(textbox_nombre.get())
    contraseña = str(textbox_contraseña.get())
    contraseña_2 = str(textbox_contraseña_5.get())
    archivo = obtener_nicknames()
    nicknames = archivo.keys()
    
    if nick in nicknames:
        messagebox.showerror("Error", "El usuario que intento ingresar ya existe")
    elif contraseña_2 != contraseña:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
    elif verificar_contraseña(contraseña) == False:
        messagebox.showerror("Error", "La contraseña no es segura")
    else:
        archivo[nick] = [contraseña,direc_perfil]
        ventana_login.withdraw()
        ventana_inicio.deiconify()
        ventana_inicio.update()
        guardar_nicknames(archivo)

def obtener_nicknames():
    f=open("nicknames","rb") # abrir archivo para leer datos
    while True:
        try: # controlar EOF
            x=pickle.load(f) # leer datos
            return (x)
        except EOFError:
            f.close()
            break  # cerrar archivo print ("Fin")

def guardar_nicknames(archivo):
    a = open("nicknames","wb")
    print(archivo)
    pickle.dump(archivo,a)
    a.close()

def verificar_contraseña(contraseña):
    if len(contraseña)<8:
        return False
    else:
        return validar_aux(contraseña,0,0,0,0)

def validar_aux(contraseña,c1,c2,c3,c4):
    mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    minus = "abcdefghijklmnñopqrstuvwxyz"
    num = "0123456789"

    if contraseña == "":
        if c1 < 1:
            return False
        elif c2 < 1:
            return False
        elif c3 < 1:
            return False
        elif c4 < 1:
            return False
        else:
            return True
    else:
        d = contraseña[0]
        cant = contraseña.count(d)

        if cant > 2:
            return False
        elif d in mayus:
            c1 = c1+1
        elif d in minus:
            c2 = c2+1
        elif d in num:
            c3 = c3+1
        else:
            c4 = c4+1

    return validar_aux(contraseña[1:],c1,c2,c3,c4)
            
            
#------------------------------- Funciones Configuracion ----------------------------------
def abrir_directorio_1():
    global Manzana
    Manzana = askopenfilename()

def abrir_directorio_2():
    global Cab_Hor
    Cab_Hor = askopenfilename()

def abrir_directorio_3():
    global Cab_Ver
    Cab_Ver = askopenfilename()

def abrir_directorio_4():
    global Cola_Hor
    Cola_Hor = askopenfilename()

def abrir_directorio_5():
    global Cola_Ver
    Cola_Ver = askopenfilename()

def abrir_directorio_6():
    global Curva
    Curva = askopenfilename()

def abrir_directorio_7():
    global Fondo
    Fondo = askopenfilename()

def abrir_directorio_8():
    global Pared
    Pared = askopenfilename()

def abrir_directorio_9():
    global musica_fondo
    musica_fondo = askopenfilename()

def abrir_directorio_10():
    global musica_manzana
    musica_manzana = askopenfilename()

def abrir_directorio_11():
    global musica_ganar
    musica_ganar = askopenfilename()

def abrir_directorio_12():
    global chocar_1
    chocar_1 = askopenfilename()

def abrir_directorio_13():
    global chocar_2
    chocar_2 = askopenfilename()


def abrir_ventana_configuracion():
    ventana_inicio.withdraw()
    ventana_configuracion.update()
    ventana_configuracion.deiconify()

    boton_1 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_1())
    boton_1.place(x=600,y=90)

    boton_2 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_2())
    boton_2.place(x=600,y=130)

    boton_3 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_3())
    boton_3.place(x=600,y=170)

    boton_4 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_4())
    boton_4.place(x=600,y=210)

    boton_5 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_5())
    boton_5.place(x=600,y=250)

    boton_6 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_6())
    boton_6.place(x=600,y=290)

    boton_7 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_7())
    boton_7.place(x=600,y=330)

    boton_8 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_8())
    boton_8.place(x=600,y=370)

    boton_9 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_9())
    boton_9.place(x=1000,y=90)

    boton_10 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_10())
    boton_10.place(x=1000,y=130)

    boton_11 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_11())
    boton_11.place(x=1000,y=170)

    boton_12 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_12())
    boton_12.place(x=1000,y=290)

    boton_13 = Button(ventana_configuracion,image=lupa,command=lambda:abrir_directorio_13())
    boton_13.place(x=1000,y=330)
    
    
def guardar_valores_configuracion():
    global parametros_juego
    global parametros_nuevo
    global paredes_juego
    global tamaño_matriz
    global multi
    
    tamaño_matriz = tamaño.get()
    paredes_matriz = paredes.get()

    if tamaño_matriz == 1:
        parametros_juego = (420,420)
        parametros_nuevo = (440,490)
    elif tamaño_matriz == 2:
        parametros_juego = (480,480)
        parametros_nuevo = (500,550)
    elif tamaño_matriz == 3:
        parametros_juego = (540,540)
        parametros_nuevo = (560,610)
    elif tamaño_matriz == 4:
        parametros_juego = (600,600)
        parametros_nuevo = (620,670)

    elif tamaño_matriz == 5:
        multi = 1
        parametros_juego = (420,420)
        parametros_nuevo = (440,490)

    if paredes_matriz == 1:
        paredes_juego = "si"
    elif paredes_matriz == 2:
        paredes_juego = "no"  
    
    ventana_configuracion.withdraw()
    ventana_inicio.deiconify()
#------------------------------- Funciones del Juego ---------------------------------------
def salir():
    ventana_1.withdraw()
    pygame.quit()
    ventana_inicio.deiconify()

def modo_multi(n):
    global multi
    if n==0:
        abrir_ventana_juego()
    elif n==1:
        multi = multi+1
    elif n==2:
        multi = multi-1

    if multi > 4:
        multi = 1
    if multi < 1:
        multi = 4

    cambiar_tamaño()
    ventana_1.withdraw()
    abrir_ventana_juego()
    
def cambiar_tamaño():
    global tamaño_matriz
    global parametros_juego
    global parametros_nuevo
    
    if multi == 1:
        parametros_juego = (420,420)
        parametros_nuevo = (440,490)
    elif multi == 2:
        parametros_juego = (480,480)
        parametros_nuevo = (500,550)
    elif multi == 3:
        parametros_juego = (540,540)
        parametros_nuevo = (560,610)
    elif multi == 4:
        parametros_juego = (600,600)
        parametros_nuevo = (620,670)

def abrir_ventana_juego():
    global paredes_juego
    global parametros_juego
    global parametros_nuevos
    global Fondo
    global Pared
    global Manzana
    global Cab_Hor
    global Cab_Ver
    global Cola_Hor
    global Cola_Ver
    global Curva
    global pos_cuerpo
    global direccion
    global pos_cabeza_x
    global pos_cabeza_y
    global pos_manzana_x
    global pos_manzana_y
    global score
    global musica_fondo

    ventana_inicio.withdraw()

    pygame.init()
    
    texto = pygame.font.SysFont("Arial",16)
    rojo = pygame.Color(250,0,0)
    
    Game = pygame.display.set_mode(parametros_nuevo)
    pygame.display.set_caption("Just a another Snake Game")
        
    fondo_pantalla = pygame.image.load(Fondo)
    fondo_pantalla = pygame.transform.scale(fondo_pantalla,parametros_juego)

    pared_pantalla = pygame.image.load(Pared)  
    pared_pantalla = pygame.transform.scale(pared_pantalla,parametros_nuevo)
    
    if paredes_juego == "si":
        modo_juego = "con paredes"
        Game.blit(pared_pantalla,(0,0))
        Game.blit(fondo_pantalla,(10,60))
    else:
        if paredes_juego == "no":
            modo_juego = "sin paredes"
        Game.blit(fondo_pantalla,(10,60))

    Manzana_juego = pygame.image.load(Manzana)
    Manzana_juego = pygame.transform.scale(Manzana_juego, (20,20))

    cabeza_horizontal = pygame.image.load(Cab_Hor)
    cabeza_horizontal = pygame.transform.scale(cabeza_horizontal,(20,20))

    cabeza_vertical = pygame.image.load(Cab_Ver)
    cabeza_vertical = pygame.transform.scale(cabeza_vertical,(20,20))

    cola_horizontal = pygame.image.load(Cola_Hor)
    cola_horizontal = pygame.transform.scale(cola_horizontal, (20,20))

    cola_vertical = pygame.image.load(Cola_Ver)
    cola_vertical = pygame.transform.scale(cola_vertical, (20,20))

    curva_juego = pygame.image.load(Curva)
    curva_juego = pygame.transform.scale(curva_juego, (20,20))

    pos_cabeza_x = (parametros_juego[0]//20)//2 * 20 + 10
    pos_cabeza_y = (parametros_juego[1]//20)//2 * 20 

    pos_manzana_x = round(random.randrange(10,parametros_nuevo[0]-10)/10.0)*10.0
    pos_manzana_y = round(random.randrange(70,parametros_nuevo[1]-10)/10.0)*10.0
    
    pos_cuerpo = [[(pos_cabeza_x-20,pos_cabeza_y),"derecha"], [(pos_cabeza_x-40,pos_cabeza_y),"derecha"], [(pos_cabeza_x-60,pos_cabeza_y),"derecha"], [(pos_cabeza_x-80,pos_cabeza_y),"derecha"]]

    rectangulo = cabeza_horizontal.get_rect()
    rectangulo_manzana = Manzana_juego.get_rect()    
    
    direccion = "derecha"
    mov = True
    vel = 5
    vel_cons = 20
    score = "0"

    if musica_fondo != "":
        pygame.mixer.music.load(musica_fondo)
        pygame.mixer.music.play(-1)
        
    if musica_manzana != "":
        sonido_1 = pygame.mixer.Sound(musica_manzana)

    if chocar_1 != "":
        sonido_2 = pygame.mixer.Sound(chocar_1)

    if chocar_2 != "":
        sonido_3 = pygame.mixer.Sound(chocar_2)
            
    def mensaje(text,color,lugar):
        pantalla_texto = texto.render(text,True,color)
        Game.blit(pantalla_texto,lugar)

    def pausar_juego():
        pausa = True
        while pausa==True:
            mensaje("Presione Space para seguir jugando o G para guardar y salir del juego",rojo,(0,40))
            pygame.display.update()
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_SPACE:
                        pausa=False
                        pygame.display.update()
                    if evento.key == K_g:
                        guardar()
                        juego = False
                        

    
    #Start Game

    juego = True

    while juego == True:

        Game.fill((0,0,0))
        reloj = pygame.time.Clock()
        reloj.tick(120)
        
        if paredes_juego == "si":
            modo_juego = "con paredes"
            Game.blit(pared_pantalla,(0,0))
            Game.blit(fondo_pantalla,(10,60))
    
        else:
            if paredes_juego == "no":
                modo_juego = "sin paredes"
                Game.blit(fondo_pantalla,(10,60))
        

        cant = len(pos_cuerpo)-1
        cont = 0

        for parte in pos_cuerpo:
            posx = parte[0][0]
            posy = parte[0][1]

            if parte[1] == "derecha":
                Game.blit(cola_horizontal,(posx,posy))
                    
            elif parte[1] == "izquierda":
                cola_1 = pygame.transform.rotate(cola_horizontal,180)
                Game.blit(cola_1,(posx,posy))
                    
            elif parte[1] == "arriba":
                Game.blit(cola_vertical,(posx,posy))
                              
            else:
                cola_2 = pygame.transform.rotate(cola_vertical,180)
                Game.blit(cola_2,(posx,posy))
            cont = cont + 1

            
        while cant >= 0:
            pos_cuerpo[cant] = pos_cuerpo[cant-1]
            cant = cant-1

        
        Game.blit(Manzana_juego,(pos_manzana_x,pos_manzana_y))
        rectangulo.left, rectangulo.top = (pos_cabeza_x,pos_cabeza_y)
        rectangulo_manzana.left , rectangulo_manzana.top = (pos_manzana_x,pos_manzana_y)
        mensaje("Puntuacion:",rojo,(0,0))
        mensaje(score,rojo,(150,0))

                
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                ventana_inicio.deiconify()

            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    posicionx = pos_cabeza_x- vel
                if evento.key == K_RIGHT:
                    posicionx = pos_cabeza_x+ vel
                if evento.key == K_UP:
                    posiciony = pos_cabeza_y-vel
                if evento.key == K_DOWN:
                    posiciony = pos_cabeza_y+vel
                if evento.key == K_SPACE:
                    pausar_juego()
                
            if evento.type == pygame.KEYUP:
                if evento.key == K_RIGHT:
                    direccion = "derecha"
                
                if evento.key == K_LEFT:
                    direccion = "izquierda"
            
                if evento.key == K_UP:
                    direccion = "arriba"
                    
                if evento.key == K_DOWN:
                    direccion = "abajo"



                    
        if mov == True:
            if modo_juego == "sin paredes":
                
                if direccion == "derecha":
                    if pos_cabeza_x < parametros_juego[0] - 10:                       
                        pos_cabeza_x = pos_cabeza_x+vel_cons
                    else:
                        pos_cabeza_x = 10
                elif direccion == "izquierda":
                    if pos_cabeza_x > 10:                       
                        pos_cabeza_x = pos_cabeza_x-vel_cons
                    else:
                        pos_cabeza_x = parametros_juego[0] - 10
                        
                elif direccion == "arriba":
                    if pos_cabeza_y >= 70:
                        pos_cabeza_y = pos_cabeza_y-vel_cons
                    else:
                        pos_cabeza_y = parametros_nuevo[1]-30
                        
                elif direccion == "abajo":
                    if pos_cabeza_y < parametros_nuevo[1]-30:
                        pos_cabeza_y = pos_cabeza_y + vel_cons
                    else:
                        pos_cabeza_y = 60
                        
            else:
                if direccion == "derecha":
                    if pos_cabeza_x <= parametros_juego[0] - 30:                       
                        pos_cabeza_x= pos_cabeza_x+vel_cons
                    else:
                        pygame.mixer.music.stop()
                        if chocar_2 != "":
                            sonido_3.play()
                            time.sleep(3)
                        juego = False
                        transicion()
                        break
                              
                elif direccion == "izquierda":
                    if pos_cabeza_x >= 10:                       
                        pos_cabeza_x = pos_cabeza_x-vel_cons   
                    else:
                        pygame.mixer.music.stop()
                        if chocar_2 != "":
                            sonido_3.play()
                            time.sleep(3)
                        juego = False
                        transicion()
                        break
                    
                elif direccion == "arriba":
                    if  pos_cabeza_y >= 70:
                        pos_cabeza_y = pos_cabeza_y-vel_cons
                    else:
                        pygame.mixer.music.stop()
                        if chocar_2 != "":
                            sonido_3.play()
                            time.sleep(3)
                        juego = False
                        transicion()
                        break
                    
                elif direccion == "abajo":
                    if pos_cabeza_y <= parametros_nuevo[1]-30:
                        pos_cabeza_y = pos_cabeza_y + vel_cons
                    else:
                        pygame.mixer.music.stop()
                        if chocar_2 != "":
                            sonido_3.play()
                            time.sleep(3)
                        juego = False
                        transicion()
                        break

        if rectangulo.colliderect(rectangulo_manzana):
            pos_manzana_x = round(random.randrange(10,parametros_nuevo[0]-10)/10.0)*10.0
            pos_manzana_y = round(random.randrange(70,parametros_nuevo[1]-10)/10.0)*10.0
            if pos_manzana_x > parametros_juego[0] or pos_manzana_x < 10:
                pos_manzana_x = round(random.randrange(10,parametros_nuevo[0]-10))
            if pos_manzana_y > parametros_nuevo[0]-10 or pos_manzana_y < 60:
                pos_manzana_y = round(random.randrange(70,parametros_nuevo[1]-10))
            largo = len(pos_cuerpo)
            pos_cuerpo.append(pos_cuerpo[largo-1])
            score = str(int(score)+1)
            
            if musica_manzana != "":
                sonido_1.play()
            


        for x in pos_cuerpo:                                    
            if (pos_cabeza_x,pos_cabeza_y) == x[0]:
                pygame.mixer.music.stop()
                if chocar_1 != "":
                    sonido_2.play()
                    time.sleep(3)
                juego = False
                transicion()
                
                break

            

        if direccion == "derecha":
            pos_cuerpo[0] = [(pos_cabeza_x,pos_cabeza_y),direccion]
            Game.blit(cabeza_horizontal,(pos_cabeza_x,pos_cabeza_y))
            
        if direccion == "izquierda":
            pos_cuerpo[0] = [(pos_cabeza_x,pos_cabeza_y),direccion]
            cabeza_1 = pygame.transform.flip(cabeza_horizontal,True,False)
            Game.blit(cabeza_1,(pos_cabeza_x,pos_cabeza_y))
            
        if direccion == "arriba":
            pos_cuerpo[0] = [(pos_cabeza_x,pos_cabeza_y),direccion]
            Game.blit(cabeza_vertical,(pos_cabeza_x,pos_cabeza_y))
        if direccion == "abajo":
            pos_cuerpo[0] = [(pos_cabeza_x,pos_cabeza_y),direccion]
            cabeza_2 = pygame.transform.rotate(cabeza_vertical,180)
            Game.blit(cabeza_2,(pos_cabeza_x,pos_cabeza_y))
        time.sleep(0.1)
        reloj = pygame.time.Clock()
        reloj.tick(120)

        pygame.display.update()
        pygame.display.flip()
                                        




    
def transicion():
    if tamaño_matriz == 5:            
        ventana_1.deiconify()

        lab_1 = Label(ventana_1,text="Perdiste",bg="#0A768D",fg="White",font=("Arial Black",20),width=15)
        lab_1.place(x=100,y=40)

        boton_j_1 = Button(ventana_1,text="Continuar en el mismo nivel",bg="Orange",fg="White",font=("Arial Black",14),width=23,command=lambda:modo_multi(0))
        boton_j_1.place(x=30,y=100)

        boton_j_2 = Button(ventana_1,text="Siguiente nivel",bg="Orange",fg="White",font=("Arial Black",14),width=13,command=lambda:modo_multi(1))
        boton_j_2.place(x=30,y=150)

        boton_j_3 = Button(ventana_1,text="Nivel anterior",bg="Orange",fg="White",font=("Arial Black",14),width=13,command=lambda:modo_multi(2))
        boton_j_3.place(x=30,y=200)

        boton_j_4 = Button(ventana_1,text="Menu principal",bg="Orange",fg="White",font=("Arial Black",14),width=13,command=lambda:salir())
        boton_j_4.place(x=30,y=250)

        pygame.quit()
        
        if multi == 1:
            ranking(1)
        elif multi == 2:
            ranking(2)
        elif multi == 3:
            ranking(3)
        else:
            ranking(4)
    else:
        ventana_inicio.deiconify()
        pygame.quit()
        
        if tamaño_matriz == 1:
            ranking(1)
        elif tamaño_matriz == 2:
            ranking(2)
        elif tamaño_matriz == 3:
            ranking(3)
        else:
            ranking(4)
        

#------------------------------- Funciones Continuar Juego -------------------------------- 
def abrir_ventana_continuar_juego():
    global paredes_juego
    global parametros_juego
    global parametros_nuevos
    global Fondo
    global Pared
    global Manzana
    global Cab_Hor
    global Cab_Ver
    global Cola_Hor
    global Cola_Ver
    global Curva
    global pos_cuerpo
    global direccion
    global pos_cabeza_x
    global pos_cabeza_y
    global pos_manzana_x
    global pos_manzana_y
    global snake_body
    global score

    
    ventana_inicio.withdraw()

    pygame.init()

    texto = pygame.font.SysFont("Arial",16)
    rojo = pygame.Color(250,0,0)

    Game = pygame.display.set_mode(parametros_nuevo)
    pygame.display.set_caption("Just a another Snake Game")
        
    fondo_pantalla = pygame.image.load(Fondo)
    fondo_pantalla = pygame.transform.scale(fondo_pantalla,parametros_juego)

    pared_pantalla = pygame.image.load(Pared)  
    pared_pantalla = pygame.transform.scale(pared_pantalla,parametros_nuevo)
    
    if paredes_juego == "si":
        modo_juego = "con paredes"
    
    else:
        if paredes_juego == "no":
            modo_juego = "sin paredes"

    lista = snake_body
    
    Game.blit(pared_pantalla,(0,0))
    Game.blit(fondo_pantalla,(10,60))

    Manzana_juego = pygame.image.load(Manzana)
    Manzana_juego = pygame.transform.scale(Manzana_juego, (20,20))

    cabeza_horizontal = pygame.image.load(Cab_Hor)
    cabeza_horizontal = pygame.transform.scale(cabeza_horizontal,(20,20))

    cabeza_vertical = pygame.image.load(Cab_Ver)
    cabeza_vertical = pygame.transform.scale(cabeza_vertical,(20,20))

    cola_horizontal = pygame.image.load(Cola_Hor)
    cola_horizontal = pygame.transform.scale(cola_horizontal, (20,20))

    cola_vertical = pygame.image.load(Cola_Ver)
    cola_vertical = pygame.transform.scale(cola_vertical, (20,20))

    curva_juego = pygame.image.load(Curva)
    curva_juego = pygame.transform.scale(curva_juego, (20,20))

    pos_cabeza_x = lista[1]
    pos_cabeza_y = lista[2]

    pos_manzana_x = round(random.randrange(10,parametros_nuevo[0]-10)/10.0)*10.0
    pos_manzana_y = round(random.randrange(70,parametros_nuevo[1]-10)/10.0)*10.0
    
    pos_cuerpo = lista[3]
    print (pos_cuerpo)
    
    rectangulo = cabeza_horizontal.get_rect()
    rectangulo_manzana = Manzana_juego.get_rect()    

    score = score
    
    direccion = lista[0]
    mov = True
    vel = 5
    vel_cons = 20

    if musica_fondo != "":
        pygame.mixer.music.sound(musica_fondo)
        pygame.mixer.music.play()
        

    def mensaje(text,color,lugar):
        pantalla_texto = texto.render(text,True,color)
        Game.blit(pantalla_texto,lugar)

    def pausar_juego():
        pausa = True
        while pausa==True:
            mensaje("Presione Space para seguir jugando o G para guardar y salir del juego",rojo,(0,40))
            pygame.display.update()
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_SPACE:
                        pausa=False
                        pygame.display.update()
                    if evento.key == K_g:
                        guardar()
                        juego = False

                        
    #Start Game

    juego = True

    while juego == True:

        Game.fill((0,0,0))
        reloj = pygame.time.Clock()
        reloj.tick(120)
        
        if paredes_juego == "si":
            modo_juego = "con paredes"
    
        else:
            if paredes_juego == "no":
                modo_juego = "sin paredes"

        Game.blit(pared_pantalla,(0,0))
        Game.blit(fondo_pantalla,(10,60))
        

        cant = len(pos_cuerpo)-1
        cont = 0

        for parte in pos_cuerpo:
            posx = parte[0][0]
            posy = parte[0][1]

            if parte[1] == "derecha":
                Game.blit(cola_horizontal,(posx,posy))
                    
            elif parte[1] == "izquierda":
                cola_1 = pygame.transform.rotate(cola_horizontal,180)
                Game.blit(cola_1,(posx,posy))
                    
            elif parte[1] == "arriba":
                Game.blit(cola_vertical,(posx,posy))
                              
            else:
                cola_2 = pygame.transform.rotate(cola_vertical,180)
                Game.blit(cola_2,(posx,posy))
            cont = cont + 1

            
        while cant >= 0:
            pos_cuerpo[cant] = pos_cuerpo[cant-1]
            cant = cant-1

        
        Game.blit(Manzana_juego,(pos_manzana_x,pos_manzana_y))
        rectangulo.left, rectangulo.top = (pos_cabeza_x,pos_cabeza_y)
        rectangulo_manzana.left , rectangulo_manzana.top = (pos_manzana_x,pos_manzana_y)
        mensaje("Puntuacion:",rojo,(0,0))
        mensaje(score,rojo,(150,0))

                
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                ventana_inicio.deiconify()

            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    posicionx = pos_cabeza_x- vel
                if evento.key == K_RIGHT:
                    posicionx = pos_cabeza_x+ vel
                if evento.key == K_UP:
                    posiciony = pos_cabeza_y-vel
                if evento.key == K_DOWN:
                    posiciony = pos_cabeza_y+vel
                if evento.key == K_SPACE:
                    pausar_juego()
                
            if evento.type == pygame.KEYUP:
                if evento.key == K_RIGHT:
                    direccion = "derecha"
                
                if evento.key == K_LEFT:
                    direccion = "izquierda"
            
                if evento.key == K_UP:
                    direccion = "arriba"
                    
                if evento.key == K_DOWN:
                    direccion = "abajo"



                    
        if mov == True:
            if modo_juego == "sin paredes":
                
                if direccion == "derecha":
                    if pos_cabeza_x < parametros_juego[0] - 10:                       
                        pos_cabeza_x = pos_cabeza_x+vel_cons
                    else:
                        pos_cabeza_x = 10
                elif direccion == "izquierda":
                    if pos_cabeza_x > 10:                       
                        pos_cabeza_x = pos_cabeza_x-vel_cons
                    else:
                        pos_cabeza_x = parametros_juego[0] - 10
                        
                elif direccion == "arriba":
                    if pos_cabeza_y >= 70:
                        pos_cabeza_y = pos_cabeza_y-vel_cons
                    else:
                        pos_cabeza_y = parametros_nuevo[1]-30
                        
                elif direccion == "abajo":
                    if pos_cabeza_y < parametros_nuevo[1]-30:
                        pos_cabeza_y = pos_cabeza_y + vel_cons
                    else:
                        pos_cabeza_y = 60
                        
            else:
                if direccion == "derecha":
                    if pos_cabeza_x <= parametros_juego[0] - 30:                       
                        pos_cabeza_x= pos_cabeza_x+vel_cons
                    else:
                        juego = False
                        print("perdiste mi hermano")
                        transicion()
                        break
                              
                elif direccion == "izquierda":
                    if pos_cabeza_x >= 10:                       
                        pos_cabeza_x = pos_cabeza_x-vel_cons   
                    else:
                        juego = False
                        transicion()
                        break
                    
                elif direccion == "arriba":
                    if  pos_cabeza_y >= 70:
                        pos_cabeza_y = pos_cabeza_y-vel_cons
                    else:
                        juego = False
                        transicion()
                        break
                    
                elif direccion == "abajo":
                    if pos_cabeza_y <= parametros_nuevo[1]-30:
                        pos_cabeza_y = pos_cabeza_y + vel_cons
                    else:
                        juego = False
                        transicion()
                        break

        if rectangulo.colliderect(rectangulo_manzana):
            pos_manzana_x = round(random.randrange(10,parametros_nuevo[0]-10)/10.0)*10.0
            pos_manzana_y = round(random.randrange(70,parametros_nuevo[1]-10)/10.0)*10.0
            if pos_manzana_x > parametros_juego[0] or pos_manzana_x < 10:
                pos_manzana_x = round(random.randrange(10,parametros_nuevo[0]-10))
            if pos_manzana_y > parametros_nuevo[0]-10 or pos_manzana_y < 60:
                pos_manzana_y = round(random.randrange(70,parametros_nuevo[1]-10))
            largo = len(pos_cuerpo)
            pos_cuerpo.append(pos_cuerpo[largo-1])
            score = str(int(score)+1)


        for x in pos_cuerpo:                                    
            if (pos_cabeza_x,pos_cabeza_y) == x[0]:
                juego = False
                transicion()
                
                break

            

        if direccion == "derecha":
            pos_cuerpo[0] = [(pos_cabeza_x,pos_cabeza_y),direccion]
            Game.blit(cabeza_horizontal,(pos_cabeza_x,pos_cabeza_y))
            
        if direccion == "izquierda":
            pos_cuerpo[0] = [(pos_cabeza_x,pos_cabeza_y),direccion]
            cabeza_1 = pygame.transform.flip(cabeza_horizontal,True,False)
            Game.blit(cabeza_1,(pos_cabeza_x,pos_cabeza_y))
            
        if direccion == "arriba":
            pos_cuerpo[0] = [(pos_cabeza_x,pos_cabeza_y),direccion]
            Game.blit(cabeza_vertical,(pos_cabeza_x,pos_cabeza_y))
        if direccion == "abajo":
            pos_cuerpo[0] = [(pos_cabeza_x,pos_cabeza_y),direccion]
            cabeza_2 = pygame.transform.rotate(cabeza_vertical,180)
            Game.blit(cabeza_2,(pos_cabeza_x,pos_cabeza_y))
        time.sleep(0.1)
        reloj = pygame.time.Clock()
        reloj.tick(120)

        pygame.display.update()
        pygame.display.flip()

    

def obtener():
    f=open("archivos\guardar_snake","rb") # abrir archivo para leer datos
    while True:
        try: # controlar EOF
            x=pickle.load(f) # leer datos
            return (x)
        except EOFError:
            f.close()
            break  # cerrar archivo print ("Fin")

        
#------------------------------- Funciones Calificaciones ----------------------------------
def abrir_ventana_calificaciones():
    ventana_inicio.withdraw()
    ventana_calificaciones.update()
    ventana_calificaciones.deiconify()
#------------------------------- Funciones Ayuda ----------------------------------
def abrir_ventana_ayuda():
    ventana_inicio.withdraw()
    ventana_ayuda.update()
    ventana_ayuda.deiconify()
    wb.open_new("manual\manual_de_usuario_snake.pdf")
#------------------------------- Funciones Acerca De ----------------------------------
def abrir_ventana_acerca():
    ventana_inicio.withdraw()
    ventana_acerca.update()
    ventana_acerca.deiconify()
#------------------------------- Funciones Globales ----------------------------------
def cancelar(ventana_1,ventana_2):
    ventana_1.withdraw()
    ventana_2.update()
    ventana_2.deiconify()

def crear_cuenta():
    ventana_init.withdraw()
    ventana_login.deiconify()


#                                - Elementos -
#--------------------------- Ventana Inicio ----------------------------------------------
titulo_1 = Label(ventana_inicio,text="Just a another ",bg="#0A768D",fg="White",font=("Arial Black",25))
titulo_1.place(x=60,y=40)

titulo_2 = Label(ventana_inicio,text="Snake Game",bg="#0A768D",fg="Orange",font=("Arial Black",25))
titulo_2.place(x=340,y=40)

titulo_2 = Label(ventana_inicio,image=borde)
titulo_2.place(x=0,y=100)

version = Label(ventana_inicio,text="version 2.0",bg="#0A768D",fg="White",font=("Arial Black",7))
version.place(x=620,y=370)

boton_jugar = Button(ventana_inicio,text="Jugar",bg="Orange",fg="White",width=10,font=("Arial Black",14),command=lambda:abrir_ventana_juego())
boton_jugar.place(x=60,y=150)

boton_cont_jugar = Button(ventana_inicio,text="Continuar Juego",bg="Orange",fg="White",width=15,font=("Arial Black",14),command=lambda:cargar_juego())
boton_cont_jugar.place(x=250,y=150)

boton_top_10 = Button(ventana_inicio,text="Top 10",bg="Orange",fg="White",width=10,font=("Arial Black",14),command=lambda:abrir_ventana_calificaciones())
boton_top_10.place(x=500,y=150)

boton_conf = Button(ventana_inicio,text="Configuracion Juego",bg="Orange",fg="White",width=19,font=("Arial Black",14),command=lambda:abrir_ventana_configuracion())
boton_conf.place(x=60,y=225)

boton_salir = Button(ventana_inicio,text="Cerrar sesion",bg="Orange",fg="White",width=15,font=("Arial Black",14),command=lambda:cancelar(ventana_inicio,ventana_init))
boton_salir.place(x=60,y=300)

boton_ayuda = Button(ventana_inicio,text="Ayuda",bg="Orange",fg="White",width=10,font=("Arial Black",14),command=lambda:abrir_ventana_ayuda())
boton_ayuda.place(x=500,y=225)

boton_acerca_de = Button(ventana_inicio,text="Acerca De",bg="Orange",fg="White",width=10,font=("Arial Black",14),command=lambda:abrir_ventana_acerca())
boton_acerca_de.place(x=500,y=300)
#--------------------------- Ventana de Configuracion ------------------------------------
R1 = Radiobutton(ventana_configuracion,text="14x14",value = 1,variable=tamaño,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R1.place(x=60,y=90)

R2 = Radiobutton(ventana_configuracion,text="16x16",value = 2,variable=tamaño,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R2.place(x=60,y=130)

R3 = Radiobutton(ventana_configuracion,text="18x18",value=3,variable=tamaño,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R3.place(x=60,y=170)

R4 = Radiobutton(ventana_configuracion,text="20x20",value=4,variable=tamaño,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R4.place(x=60,y=210)

R5 = Radiobutton(ventana_configuracion,text="Multitamaño",value=5,variable=tamaño,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R5.place(x=60,y=250)

etiqueta_tamaño = Label(ventana_configuracion,text="Tamaño",bg="#0A768D",fg="Orange",font=("Arial Black",18))
etiqueta_tamaño.place(x=60,y=40)

etiqueta_imagenes = Label(ventana_configuracion,text="Imagenes",bg="#0A768D",fg="Orange",font=("Arial Black",18))
etiqueta_imagenes.place(x=450,y=40)

etiqueta_modo = Label(ventana_configuracion,text="Modo",bg="#0A768D",fg="Orange",font=("Arial Black",18))
etiqueta_modo.place(x=60,y=290)

R5 = Radiobutton(ventana_configuracion,text="Con Paredes",value=1,variable=paredes,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R5.place(x=60,y=330)

R6 = Radiobutton(ventana_configuracion,text="Sin Paredes",value=2,variable=paredes,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R6.place(x=60,y=370)

etiqueta_manzana = Label(ventana_configuracion,text="Manzana",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_manzana.place(x=350,y=90)

etiqueta_cab_hor = Label(ventana_configuracion,text="Cabeza Horizontal",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_cab_hor.place(x=350,y=130)

etiqueta_cab_ver = Label(ventana_configuracion,text="Cabeza Vertical",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_cab_ver.place(x=350,y=170)

etiqueta_cola_hor = Label(ventana_configuracion,text="Cola Horizontal",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_cola_hor.place(x=350,y=210)

etiqueta_cola_ver = Label(ventana_configuracion,text="Cola Vertical",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_cola_ver.place(x=350,y=250)

etiqueta_cola_curva = Label(ventana_configuracion,text="Cola Curva",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_cola_curva.place(x=350,y=290)

etiqueta_fondo = Label(ventana_configuracion,text="Fondo",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_fondo.place(x=350,y=330)

etiqueta_fondo = Label(ventana_configuracion,text="Pared",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_fondo.place(x=350,y=370)

etiqueta_music = Label(ventana_configuracion,text="Musica",bg="#0A768D",fg="Orange",font=("Arial Black",18))
etiqueta_music.place(x=800,y=40)

etiqueta_music = Label(ventana_configuracion,text="Musica durante el juego",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_music.place(x=700,y=90)

etiqueta_music = Label(ventana_configuracion,text="Al comerse una manzana",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_music.place(x=700,y=130)

etiqueta_music = Label(ventana_configuracion,text="Al ganar",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_music.place(x=700,y=170)

etiqueta_music = Label(ventana_configuracion,text="Cuando la culebra choca",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_music.place(x=700,y=250)

etiqueta_music = Label(ventana_configuracion,text="Contra ella",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_music.place(x=730,y=290)

etiqueta_music = Label(ventana_configuracion,text="Contra una pared",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_music.place(x=730,y=330)

boton_conf_ok = Button(ventana_configuracion,text="Guardar",bg="Orange",fg="White",font=("Arial Black",14),command=lambda:guardar_valores_configuracion())
boton_conf_ok.place(x=60,y=500)

boton_conf_canc = Button(ventana_configuracion,text="Cancelar",bg="Orange",fg="White",font=("Arial Black",14),command=lambda:cancelar(ventana_configuracion,ventana_inicio))
boton_conf_canc.place(x=300,y=500)
#-------------------------- Ventana Calificaciones-------------------------------------------------
etiqueta_tamaño = Label(ventana_calificaciones,text="Tamaño:",bg="#0A768D",fg="Orange",font=("Arial Black",18))
etiqueta_tamaño.place(x=60,y=40)

etiqueta_modo = Label(ventana_calificaciones,text="Modo:",bg="#0A768D",fg="Orange",font=("Arial Black",18))
etiqueta_modo.place(x=60,y=290)

R1 = Radiobutton(ventana_calificaciones,text="14x14",value = 1,variable=rank_1,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R1.place(x=60,y=90)

R2 = Radiobutton(ventana_calificaciones,text="16x16",value = 2,variable=rank_1,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R2.place(x=60,y=130)

R3 = Radiobutton(ventana_calificaciones,text="18x18",value=3,variable=rank_1,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R3.place(x=60,y=170)

R4 = Radiobutton(ventana_calificaciones,text="20x20",value=4,variable=rank_1,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R4.place(x=60,y=210)

R6 = Radiobutton(ventana_calificaciones,text="Con Paredes",value=1,variable=rank_2,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R6.place(x=60,y=330)

R7 = Radiobutton(ventana_calificaciones,text="Sin Paredes",value=2,variable=rank_2,bg="#0A768D",fg="White",font=("Arial Black",14),selectcolor="#8F730F")
R7.place(x=60,y=370)

boton_cali_salir = Button(ventana_calificaciones,text="verificar",bg="Orange",fg="White",font=("Arial Black",14),width=12,command=lambda:verificar_top())
boton_cali_salir.place(x=60,y=450)

boton_cali_salir = Button(ventana_calificaciones,text="Salir",bg="Orange",fg="White",font=("Arial Black",14),width=12,command=lambda:cancelar(ventana_calificaciones,ventana_inicio))
boton_cali_salir.place(x=60,y=500)

boton_cali_salir = Button(ventana_calificaciones,text="Crear PDF",bg="Orange",fg="White",font=("Arial Black",14),width=12,command=lambda:crear_pdf())
boton_cali_salir.place(x=600,y=500)

#      La tabla en si
etiqueta_tamaño = Label(ventana_calificaciones,text="Posicion",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=300,y=40)

etiqueta_tamaño = Label(ventana_calificaciones,text="Score",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=400,y=40)

etiqueta_tamaño = Label(ventana_calificaciones,text="Nombre",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=480,y=40)

etiqueta_tamaño = Label(ventana_calificaciones,text="1",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=330,y=80)

etiqueta_tamaño = Label(ventana_calificaciones,text="2",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=330,y=110)

etiqueta_tamaño = Label(ventana_calificaciones,text="3",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=330,y=140)

etiqueta_tamaño = Label(ventana_calificaciones,text="4",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=330,y=170)

etiqueta_tamaño = Label(ventana_calificaciones,text="5",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=330,y=200)

etiqueta_tamaño = Label(ventana_calificaciones,text="6",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=330,y=230)

etiqueta_tamaño = Label(ventana_calificaciones,text="7",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=330,y=260)

etiqueta_tamaño = Label(ventana_calificaciones,text="8",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=330,y=290)

etiqueta_tamaño = Label(ventana_calificaciones,text="9",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=330,y=320)

etiqueta_tamaño = Label(ventana_calificaciones,text="10",bg="#0A768D",fg="white",font=("Arial Black",14))
etiqueta_tamaño.place(x=320,y=350)





#------------------------------------------- Ayuda ----------------------------------------------
boton_cali_salir = Button(ventana_ayuda,text="Salir",bg="Orange",fg="White",font=("Arial Black",14),width=12,command=lambda:cancelar(ventana_ayuda,ventana_inicio))
boton_cali_salir.place(x=60,y=500)
#------------------------------------------ Acerca De --------------------------------------------
etiqueta_acerca = Label(ventana_acerca,text="Just a Another Snake Game",bg="#0A768D",fg="Orange",font=("Arial Black",18))
etiqueta_acerca.place(x=60,y=40)

etiqueta_acerca = Label(ventana_acerca,text="Version 2.0",bg="#0A768D",fg="Orange",font=("Arial Black",18))
etiqueta_acerca.place(x=60,y=80)

etiqueta_acerca = Label(ventana_acerca,text="Creado por: Rolbin Méndez",bg="#0A768D",fg="Orange",font=("Arial Black",18))
etiqueta_acerca.place(x=60,y=120)

boton_cali_salir = Button(ventana_acerca,text="Salir",bg="Orange",fg="White",font=("Arial Black",14),width=12,command=lambda:cancelar(ventana_acerca,ventana_inicio))
boton_cali_salir.place(x=60,y=500)
#-------------------------------- Ventana de Login ----------------------------------------
etiqueta_2 = Label(ventana_login,text="Crear un Nickname",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_2.place(x=30,y=40)

etiqueta_2 = Label(ventana_login,text="Ingrese su Nickname",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_2.place(x=30,y=80)

textbox_nombre = Entry(ventana_login,width=25)
textbox_nombre.place(x=430,y=90)

etiqueta_2 = Label(ventana_login,text="Ingrese su Contraseña",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_2.place(x=30,y=120)

textbox_contraseña = Entry(ventana_login,width=25,show="*")
textbox_contraseña.place(x=430,y=130)

etiqueta_2 = Label(ventana_login,text="Ingrese su Contraseña nuevamente",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_2.place(x=30,y=150)

textbox_contraseña_5 = Entry(ventana_login,width=25,show="*")
textbox_contraseña_5.place(x=430,y=160)

etiqueta_3 = Label(ventana_login,text="Ingrese una imagen",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_3.place(x=30,y=180)

etiqueta_2 = Button(ventana_login,image=lupa,width=50,heigh=50,command=lambda:cambiar_imagen_perfil())
etiqueta_2.place(x=300,y=190)

boton_crear_nickname = Button(ventana_login,text="Aceptar",bg="Orange",fg="White",font=("Arial Black",14),width=10,command=lambda:agregar_nickname())
boton_crear_nickname.place(x=400,y=300)

boton_salir_nickname = Button(ventana_login,text="Cancelar",bg="Orange",fg="White",font=("Arial Black",14),width=10,command=lambda:cancelar(ventana_login,ventana_init))
boton_salir_nickname.place(x=100,y=300)


#------------------------------ Ventana Init ----------------------------------------------------------
etiqueta_4 = Label(ventana_init,text="Bienvenido a Snake Game",bg="#0A768D",fg="White",font=("Arial Black",18))
etiqueta_4.place(x=80,y=40)

titulo_3 = Label(ventana_init,image=borde)
titulo_3.place(x=0,y=90)

boton_imagen_init = Button(ventana_init,text="Crear una Cuenta",bg="Orange",fg="White",font=("Arial Black",14),width=20,command=lambda:crear_cuenta())
boton_imagen_init.place(x=20,y=160)

boton_imagen_init = Button(ventana_init,text="Iniciar Sesion",bg="Orange",fg="White",font=("Arial Black",14),width=13,command=lambda:abrir_cuentas())
boton_imagen_init.place(x=300,y=160)
#---------------------------- Ventana guardar -----------------------------------------------------------
etiqueta_2 = Label(ventana_gj,text="Guardar una partida",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_2.place(x=30,y=40)

etiqueta_2 = Label(ventana_gj,text="Ingrese un nickname",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_2.place(x=30,y=80)

textbox_nombre_partida = Entry(ventana_gj,width=25)
textbox_nombre_partida.place(x=430,y=90)

etiqueta_2 = Label(ventana_gj,text="Ingrese una Contraseña",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_2.place(x=30,y=120)

textbox_part_cont_1 = Entry(ventana_gj,width=25,show="*")
textbox_part_cont_1.place(x=430,y=130)

etiqueta_2 = Label(ventana_gj,text="Ingrese una Contraseña nuevamente",bg="#0A768D",fg="White",font=("Arial Black",14))
etiqueta_2.place(x=30,y=150)

textbox_part_cont_2 = Entry(ventana_gj,width=25,show="*")
textbox_part_cont_2.place(x=430,y=160)

boton_crear_nickname = Button(ventana_gj,text="Aceptar",bg="Orange",fg="White",font=("Arial Black",14),width=10,command=lambda:agregar_partida())
boton_crear_nickname.place(x=400,y=220)

boton_salir_nickname = Button(ventana_gj,text="Cancelar",bg="Orange",fg="White",font=("Arial Black",14),width=10,command=lambda:cancelar(ventana_gj,ventana_inicio))
boton_salir_nickname.place(x=100,y=220)
#------------------------ ventana_inicio --------------------------}
bienv_1 = Label(ventana_iniciar,text="Bienvenido:",bg="#0A768D",fg="White",font=("Arial Black",14))
bienv_1.place(x=500,y=40)

ing_cont = Label(ventana_iniciar,text="Ingrese su contraseña",bg="#0A768D",fg="White",font=("Arial Black",14))
ing_cont.place(x=450,y=120)

textbox_enter = Entry(ventana_iniciar,width=25,show="*")
textbox_enter.place(x=500,y=180)

#------------------------ ventana_cargar --------------------------}
bienv_1 = Label(ventana_cj,text="Bienvenido:",bg="#0A768D",fg="White",font=("Arial Black",14))
bienv_1.place(x=500,y=40)

ing_cont = Label(ventana_cj,text="Ingrese su contraseña",bg="#0A768D",fg="White",font=("Arial Black",14))
ing_cont.place(x=450,y=120)

textbox_enter_cg = Entry(ventana_cj,width=25,show="*")
textbox_enter_cg.place(x=500,y=180)


#a = open("archivos\guardar_snake","b")
#pickle.dump({},a)
#a.close()
    
#                          - Inicio del Programa -

ventana_init.mainloop()
































