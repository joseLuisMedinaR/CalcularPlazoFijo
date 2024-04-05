'''
CREADO POR JOSE LUIS MEDINA RASPANTE
PARA PODER CALCULAR LAS GANANCIAS SEGUN LOS DIAS Y TASAS DE INTERES
QUE UNO ELIJA
'''
###### 16-04-2023 ######
import tkinter as tk

###### VENTANA PRINCIPAL ######
ventana = tk.Tk()
ventana.title("Calcular Plazo Fijo")
ventana.geometry("400x560+700+100")
ventana.minsize(width=400, height=560)
ventana.resizable(False, False)
ventana.config(bg="lightblue")
###### VOY A USAR UN SOLO ARCHIVO .ICO Y ES MUY IMPORTANTE QUE EL ARCHIVO VAYA CON EL EJECUTABLE PARA QUE FUNCIONE ######

# LINEA PARA EL ICONO EN WINDOWS
# ventana.iconbitmap(".\plazoFijo.png")

# LINEA PARA EL ICONO EN LINUX
icon_path = "plazoFijo.png"  # Ruta al archivo .ico
icon = tk.PhotoImage(file=icon_path)
ventana.tk.call("wm", "iconphoto", ventana._w, icon)

####### FUNCIONES #######
def borrar():

    ventana.minsize(width=400, height=560)
    entrada_efectivo["state"] = "normal"
    entrada_dias["state"] = "normal"
    entrada_tasa["state"] = "normal"
    boton_simular["state"] = "normal"
    entrada_efectivo.delete(0, tk.END)
    entrada_dias.delete(0, tk.END)
    entrada_tasa.delete(0, tk.END)
    interes_ganado.config(text="")
    efectivo_total.config(text="")
    rotulo_error.config(text="")

def calcular():
    try:
        rotulo_error.config(text="")
        entradaEfectivo = entrada_efectivo.get()
        entradaDias = entrada_dias.get()
        entradaTasa = entrada_tasa.get()
        
        # Verificar que los campos no estén vacíos
        if not entradaEfectivo:
            raise ValueError("Efectivo")
        elif not entradaDias:
            raise ValueError("Días")
        elif not entradaTasa:
            raise ValueError("Tasa de Interés")
        
        # Convertir a float y verificar que los valores sean numéricos
        efectivo = float(entradaEfectivo)
        dias = float(entradaDias)
        tasa = float(entradaTasa)
        
        # Verificar que los valores sean positivos
        if efectivo <= 0 or dias <= 0 or tasa <= 0:
            raise ValueError("Los valores deben ser mayores que cero")
        
        # Convertir la tasa de porcentaje a decimal
        tasa_decimal = tasa / 100
        
        if dias < 30:
            ventana.minsize(width=400, height=610)
            rotulo_error.config(text="La cantidad de Días debe ser de 30 o más.")
        else:
            ventana.minsize(width=400, height=560)
            resultado_ganado = round((efectivo * (tasa_decimal * dias / 365)), 2)
            resultado_total = round(resultado_ganado + efectivo, 2)
        
            # Ajustar el tamaño de la fuente según el valor del resultado
            if resultado_ganado > 99999.99:
                interes_ganado.config(font="consolas 13 bold")
                efectivo_total.config(font="consolas 15 bold")
            elif resultado_ganado > 999999.99:
                interes_ganado.config(font="consolas 11 bold")
                efectivo_total.config(font="consolas 13 bold")
            else:
                interes_ganado.config(font="consolas 18 bold")
                efectivo_total.config(font="consolas 18 bold")
        
    except ValueError as ve:
        campo_faltante = str(ve).lower()
        if campo_faltante == "efectivo":
            entrada_efectivo.focus_set()
        elif campo_faltante == "días":
            entrada_dias.focus_set()
        elif campo_faltante == "tasa de interés":
            entrada_tasa.focus_set()
        ventana.minsize(width=400, height=610)
        rotulo_error.config(text="Complete el campo {} por favor.".format(ve))
    finally:        
        if 'resultado_ganado' in locals() and 'resultado_total' in locals():
            interes_ganado.config(text=resultado_ganado)
            efectivo_total.config(text=resultado_total)
            entrada_efectivo.config(state="disabled")
            entrada_dias.config(state="disabled")
            entrada_tasa.config(state="disabled")
            boton_simular.config(state="disabled")

####### LABEL TITULO #######
rotulo_titulo = tk.Label(ventana,
    text="Simulador de Plazo Fijo",
    bg="lightblue",
    fg="black",
    font="consolas 18 bold",
    relief= tk.GROOVE,
    bd=2,
    padx=10,
    pady=10
    )
rotulo_titulo.pack(padx=20,pady=20)

####### CUADRO ESPACIO #######
cuadro_espacio = tk.Frame(ventana,
    height=20,
    bg="lightblue"
    )
cuadro_espacio.pack()

####### FRAME PRIMERO #######
cuadro1 = tk.Frame(ventana,
    bg="lightblue"
    )

####### LABEL EFECTIVO #######
rotulo_primero = tk.Label(cuadro1,
    text="Efectivo:        ",
    bg="lightblue",
    font="consolas 18 bold"
    )
rotulo_primero.pack(side=tk.LEFT,padx=10,pady=10)

####### ENTRADA EFECTIVO #######
entrada_efectivo = tk.Entry(cuadro1,
    bg="white",
    font="consolas 18 bold",
    relief=tk.SUNKEN,
    bd=3,
    width=10,
    state="normal",
    justify=tk.RIGHT
    )
entrada_efectivo.pack(side=tk.LEFT, padx=10, pady=10)

cuadro1.pack()

####### FRAME SEGUNDO #######
cuadro2 = tk.Frame(ventana,
    bg="lightblue"
    )

####### LABEL DIAS #######
rotulo_segundo = tk.Label(cuadro2,
    text="Días:            ",
    bg="lightblue",
    font="consolas 18 bold"
    )
rotulo_segundo.pack(side=tk.LEFT,padx=10,pady=10)

####### ENTRADA DIAS #######
entrada_dias = tk.Entry(cuadro2,
    bg="white",
    font="consolas 18 bold",
    relief=tk.SUNKEN,
    bd=3,
    width=10,
    state="normal",
    justify=tk.RIGHT
    )
entrada_dias.pack(side=tk.LEFT, padx=10, pady=10)

cuadro2.pack()

####### FRAME TERCERO #######
cuadro3 = tk.Frame(ventana,
    bg="lightblue"
    )

####### LABEL TASA #######
rotulo_tercero = tk.Label(cuadro3,
    text="Tasa de Interés: ",
    bg="lightblue",
    font="consolas 18 bold"
    )
rotulo_tercero.pack(side=tk.LEFT,padx=10,pady=10)

####### ENTRADA TASA #######
entrada_tasa = tk.Entry(cuadro3,
    bg="white",
    font="consolas 18 bold",
    relief=tk.SUNKEN,
    bd=3,
    width=10,
    state="normal",
    justify=tk.RIGHT
    )
entrada_tasa.pack(side=tk.LEFT, padx=10, pady=10)

cuadro3.pack()

####### FRAME CUARTO #######
cuadro4 = tk.Frame(ventana,
    bg="lightblue"
    )

####### LABEL TASA #######
rotulo_cuarto = tk.Label(cuadro4,
    text="Interés Obtenido:",
    bg="lightblue",
    font="consolas 18 bold"
    )
rotulo_cuarto.pack(side=tk.LEFT,padx=10,pady=10)

####### ENTRADA TASA #######
interes_ganado = tk.Label(cuadro4,
    text="",
    bg="lightgreen",
    font="consolas 18 bold",
    relief=tk.SUNKEN,
    bd=3,
    width=10,
    state="normal",
    justify=tk.RIGHT,
    anchor=tk.E
    )
interes_ganado.pack(side=tk.LEFT, padx=10, pady=10)

cuadro4.pack()

####### FRAME QUINTO #######
cuadro5 = tk.Frame(ventana,
    bg="lightblue"
    )

####### LABEL EFECTIVO TOTAL #######
rotulo_cuarto = tk.Label(cuadro5,
    text="Efectivo Total:",
    bg="lightblue",
    font="consolas 18 bold"
    )
rotulo_cuarto.pack(side=tk.LEFT,padx=10,pady=10)

####### SALIDA DE EFECTIVO TOTAL #######
efectivo_total = tk.Label(cuadro5,
    text="",
    bg="lightgreen",
    font="consolas 18 bold",
    relief=tk.SUNKEN,
    bd=3,
    width=10,
    state="normal",
    justify=tk.RIGHT,
    anchor=tk.E
    )
efectivo_total.pack(side=tk.LEFT, padx=10, pady=10)

cuadro5.pack()

####### FRAME SEXTO #######
cuadro6 = tk.Frame(ventana,
    bg="lightblue"
    )

####### BOTON BORRAR #######
boton_borrar = tk.Button(cuadro6,
    text="Borrar",
    bg= "grey",
    font="consolas 18 bold",
    width=10,
    command=borrar
    )
boton_borrar.pack(side=tk.LEFT, padx=20,pady=20)
boton_borrar.bind('<Return>', lambda event=None: boton_borrar.invoke())  # Enlace de evento para Enter
boton_borrar.bind('<KP_Enter>', lambda event=None: boton_borrar.invoke())  # Enlace de evento para Enter del teclado numérico

####### BOTON CALCULAR #######
boton_simular = tk.Button(cuadro6,
    text="Simular",
    bg= "orange",
    font="consolas 18 bold",
    width=10,
    state="normal",
    command=calcular
    )
boton_simular.pack(side=tk.LEFT, padx=20,pady=20)
boton_simular.bind('<Return>', lambda event=None: boton_simular.invoke())  # Enlace de evento para Enter
boton_simular.bind('<KP_Enter>', lambda event=None: boton_simular.invoke())  # Enlace de evento para Enter del teclado numérico

cuadro6.pack()

####### FIRMA #######
####### FRAME DE LA FIRMA #######
cuadroFirma = tk.Frame(ventana,
    bg="lightblue"
    )

####### LABEL DE LA FIRMA #######
rotulo_firma = tk.Label(cuadroFirma,
    text="CREADO POR JOSE LUIS MEDINA RASPANTE",
    bg="lightblue",
    font="consolas 10 bold"
    )
rotulo_firma.pack(padx=10,pady=10)

cuadroFirma.pack()

####### FRAME SEPTIMO #######
cuadro7 = tk.Frame(ventana,
    bg="lightblue"
    )

####### LABEL ERROR #######
rotulo_error = tk.Label(cuadro7,
    text="",
    bg="lightblue",
    font="consolas 10 bold"
    )
rotulo_error.pack(side=tk.LEFT,padx=10,pady=10)

cuadro7.pack()

####### BUCLE PRINCIPAL PROGRAMA #######
ventana.mainloop()