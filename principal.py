from   tkinter   import *
from   tkinter   import ttk
from   tkinter   import messagebox
from   functools import partial
from   tkinter   import PhotoImage
from   tkinter   import font
import random 
import time  

#[Programa Funcion]===========================================================================================================================

#=======================[Funciones para  Imagenes]
def vector_fondo():
    vec = []
    vec.append(PhotoImage(file= 'texturas/fondo.png'))            #0
    vec.append(PhotoImage(file= 'texturas/boton.png'))            #1
    vec.append(PhotoImage(file= 'texturas/salir.png'))            #2
    vec.append(PhotoImage(file= 'texturas/historia.png'))         #3
    vec.append(PhotoImage(file= 'texturas/fondo_tierra.png'))     #4
    vec.append(PhotoImage(file= 'texturas/sin_corazon.png'))      #5
    vec.append(PhotoImage(file= 'texturas/corazon.png'))          #6
    vec.append(PhotoImage(file= 'texturas/dos_corazon.png'))      #7
    vec.append(PhotoImage(file= 'texturas/tres_corazon.png'))     #8
    return(vec)
#=======================
def vector_imagenes():
    vector=[]
    vector.append(PhotoImage(file= 'texturas_normal/agua.png'))    #0
    vector.append(PhotoImage(file= 'texturas_normal/piso.png'))    #1
    vector.append(PhotoImage(file= 'texturas_normal/arbusto.png')) #2
    vector.append(PhotoImage(file= 'texturas_normal/pasto.png'))   #3
    vector.append(PhotoImage(file= 'texturas_normal/arena.png'))   #4
    vector.append(PhotoImage(file= 'texturas_normal/tesoro.png'))  #5
    vector.append(PhotoImage(file= 'texturas_normal/boom.png'))    #6

    return(vector)
#=======================
def vector_nether():
    vector=[]
    vector.append(PhotoImage(file= 'texturas_nether/0.png'))    #0
    vector.append(PhotoImage(file= 'texturas_nether/1.png'))    #1
    vector.append(PhotoImage(file= 'texturas_nether/2.png'))    #2
    vector.append(PhotoImage(file= 'texturas_nether/3.png'))    #3
    vector.append(PhotoImage(file= 'texturas_nether/4.png'))    #4
    vector.append(PhotoImage(file= 'texturas_nether/5.png'))    #5
    vector.append(PhotoImage(file= 'texturas_nether/6.png'))    #6

    return(vector)

#=======================[Funciones para  Matrices]
def creacion_matriciana(fi,co):
    matriz = [None] * fi
    for n in range (fi):
        matriz[n] = [None] * co

    return(matriz)
#=======================
def leer_mapa(matriz_num,fi,co):
    mapa = open('mapa.txt', 'r', encoding='utf-8')

    fi= int(0)
    linita = mapa.readline()
    while(linita != ''):
        aux = linita.split(',', 8)
        for co in range(8):
            matriz_num[fi][co] = int(aux[co])
        fi += 1
        linita = mapa.readline()
    
    mapa.close()
    
    print('#========================')
    for n in range(8):
        for z in range(8):
            print(matriz_num[z][n], end=' ')
        print()
    print('#========================')
#=======================
def cargamiento_labels(matriz_num, matriz_lbl, fi, co, vec):
    auxiliar = int(0)
    for n in range(fi):
        for z in range(co):
            matriz_lbl[n][z] = Label(image= vec[matriz_num[n][z]])
            matriz_lbl[n][z].place(x= (75*n)+50, y= (75*z)+50, height= 75, width=75)

            if(matriz_num[n][z] == 6):
                auxiliar = random.randint(3,4)
                matriz_lbl[n][z].configure(image = vec[auxiliar])


            app1.update()
#=======================
def cargamiento_numerico(matriz_num):
    for n in range(8):
        for z in range(8):
            matriz_num[n][z] = random.randint(0,4)
    
    for x in range(3):
        f= int(random.randint(0,7))
        c= int(random.randint(0,7))
        matriz_num[f][c] = 5
    
    
    for g in range(3):
        f= int(random.randint(0,7))
        c= int(random.randint(0,7))
        if(matriz_num[f][c] != 5):
            matriz_num[f][c] = 6
        else:
            f= int(random.randint(0,7))
            c= int(random.randint(0,7))
            matriz_num[f][c] = 6

    
    print('#========================')
    for n in range(8):
        for z in range(8):
            print(matriz_num[z][n], end=' ')
        print()
    print('#========================')

#====================[Vectores de Cofres y Puntos]
def vector_puntos():
    puntos = [None]
    puntos[0] = int(0)
    return(puntos)
#====================
def vector_bombas():
    bombas = [None]
    bombas[0] = 3
    return(bombas)


#==========================[Funcion de Movimiento]
def movimiento(event):
    if(event.keysym == 'Up' and posicion[1] > -1+1):
        if(matriz_num[posicion[0]][posicion[1]-1] != 0 and matriz_num[posicion[0]][posicion[1]-1] != 2) :
            personaje.place(x= personaje.winfo_x(), y= personaje.winfo_y()-75)
            posicion[1] -= 1
            print(posicion)
            

    elif(event.keysym == 'Down' and posicion[1] < 8-1):
        if(matriz_num[posicion[0]][posicion[1]+1] != 0 and matriz_num[posicion[0]][posicion[1]+1] != 2)  :
            personaje.place(x= personaje.winfo_x(), y= personaje.winfo_y()+75)
            posicion[1] += 1
            print(posicion)

    elif(event.keysym == 'Left' and posicion[0] > -1+1):
        if(matriz_num[posicion[0]-1][posicion[1]] != 0 and matriz_num[posicion[0]-1][posicion[1]] != 2):
            personaje.place(x= personaje.winfo_x()-75, y= personaje.winfo_y())
            posicion[0] -= 1
            print(posicion)

    elif(event.keysym == 'Right' and posicion[0] < 8-1):
        if(matriz_num[posicion[0]+1][posicion[1]] != 0 and matriz_num[posicion[0]+1][posicion[1]] != 2) :
            personaje.place(x= personaje.winfo_x()+75, y= personaje.winfo_y())
            posicion[0] += 1
            print(posicion)


    #============================================Bombas
    if(matriz_num[posicion[0]][posicion[1]] == 6):
        
        
        personaje.configure(image = vec_perso[1])
        time.sleep(.3)
        app1.update()

        personaje.configure(image = vec_perso[0])
        app1.update()
        
        bombas[0] -= 1
        print(bombas)
        if(bombas[0] == 2):
            vida.configure(image= vector[7])

        elif(bombas[0] == 1):
            vida.configure(image= vector[6])

        elif(bombas[0] == 0):
            vida.configure(image=vector[5])
            messagebox.showerror(title='Perdiste', message='Tocaste 3 de las 3 bombas escondidas\nYa no tienes mas oportunidades')
            app1.destroy()

    #=============================================Cofres
    if(matriz_num[posicion[0]][posicion[1]] == 5):
        auxiliar = int(random.randint(3,4))
        matriz_num[posicion[0]][posicion[1]] = 1
        matriz_lbl[posicion[0]][posicion[1]].configure(image= vector_img[auxiliar])
        puntos[0] +=1
        print(puntos)
        if(puntos[0] == 1):
            puntos_lbl.configure(text= 'Puntos = 1')

        elif(puntos[0] == 2):
            puntos_lbl.configure(text= 'Puntos = 2')

        elif(puntos[0] == 3):

            puntos_lbl.configure(text= 'Puntos = 3')
            messagebox.showinfo(title='Ganaste', message='Felicidades, encontraste los cofres\nAvanzaste al siguiente nivel')
            messagebox.showinfo(title='Ten en cuenta....', message='Ten en cuenta que a partir del segundo nivel los mapas\nse generan de forma aleatoria, si algun mapa te encierra y no\nte deja salir, presiona el boton GENERAR para probar otro mapa')
            ganaste()
            niveles[0] += 1
            generar = Button(text="GENERAR",command=ganaste)
            generar.place(x=700, y=575, height=75, width=180)
          
    app1.update()
#==========================
def ganaste():
    puntos[0] = int(0)
    bombas[0] = int(3)

    posicion[0] = int(0)
    posicion[1] = int(0)

    for n in range(8):
        for z in range(8):
            matriz_lbl[n][z].destroy()
    
    vida.configure(image= vector[8])
    puntos_lbl.configure(text= 'Puntos = 0')

    cargamiento_numerico(matriz_num)

    cargamiento_labels(matriz_num, matriz_lbl, fi, co, vector_img)

    colocamiento_personaje()

    personaje.lift()

    app1.update()
#==========================
def colocamiento_personaje():
    f= int(random.randint(0,7))
    c= int(random.randint(0,7))

    while(matriz_num[f][c] != 1 and matriz_num[f][c] != 3 and matriz_num[f][c] == 4):
        f= int(random.randint(0,7))
        c= int(random.randint(0,7))
    
    posicion[0] = int(f)
    posicion[1] = int(c)
    personaje.place(x=(75*f)+50, y=(75*c)+50, height=75, width=75)



#[Programa Principal]=========================================================================================================================
app1 = Tk()
app1.geometry('950x700+200+0')
app1.title('Busqueda del Tesoro')
vector = vector_fondo()
#======================================================================================Juego
label_fondo = Label(app1,image=vector[4])
label_fondo.place(x=0,y=0, width=950, height=700)

vida = Label(image= vector[8])
vida.place(x=700, y=50, width= 241, height= 75)

puntos_lbl = Label(text= 'Puntos = 0', font= ('Small Fonts', 20) )
puntos_lbl.place(x= 700, y= 150, width=200, height=50)

#===================================[Componentes]
fi= 8
co= 8
matriz_lbl = creacion_matriciana(fi,co)
matriz_num = creacion_matriciana(fi,co)

leer_mapa(matriz_num,fi,co)
vector_img = vector_imagenes()

cargamiento_labels(matriz_num, matriz_lbl, fi, co, vector_img)

niveles = [None]
niveles[0] = int(0)
#===================================[Personaje]
vec_perso = []
vec_perso.append(PhotoImage(file='texturas/personaje.png'))
vec_perso.append(PhotoImage(file='texturas_normal/boom.png'))

posicion = [None] * 2
personaje = Label(image=vec_perso[0])

posicion[0] = 6
posicion[1] = 7

personaje.place(x=(6*75)+50, y=(7*75)+50, height=75, width=75)

bombas = vector_bombas()
puntos = vector_puntos()

vec_nether = vector_nether()

#==================================[Sonidos]

app1.bind('<Key>', movimiento)

app1.mainloop()