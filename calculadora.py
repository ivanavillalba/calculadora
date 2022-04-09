import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")

ingreso_numeros = tk.Entry(ventana, font=("calibri, 20")) 
ingreso_numeros.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

indice = 0
def click_boton(valor):
    global indice
    ingreso_numeros.insert(indice, valor)
    indice += 1

def borrar():
    ingreso_numeros.delete(0, "end")
    indice = 0

def hacer_op():
    op = ingreso_numeros.get()
    res = eval(op)
    ingreso_numeros.delete(0, "end")
    ingreso_numeros.insert(0, res)
    indice = 0

boton_1 = tk.Button(ventana, text="1", width=5, height=2, command=lambda: click_boton(1))
boton_2 = tk.Button(ventana, text="2", width=5, height=2, command=lambda: click_boton(2))
boton_3 = tk.Button(ventana, text="3", width=5, height=2, command=lambda: click_boton(3))
boton_4 = tk.Button(ventana, text="4", width=5, height=2, command=lambda: click_boton(4))
boton_5 = tk.Button(ventana, text="5", width=5, height=2, command=lambda: click_boton(5))
boton_6 = tk.Button(ventana, text="6", width=5, height=2, command=lambda: click_boton(6))
boton_7 = tk.Button(ventana, text="7", width=5, height=2, command=lambda: click_boton(7))
boton_8 = tk.Button(ventana, text="8", width=5, height=2, command=lambda: click_boton(8))
boton_9 = tk.Button(ventana, text="9", width=5, height=2, command=lambda: click_boton(9))
boton_0 = tk.Button(ventana, text="0", width=13, height=2, command=lambda: click_boton(0))

boton_borrar = tk.Button(ventana, text="AC", width=5, height=2, command=lambda: borrar()) 
boton_parentesis_ap = tk.Button(ventana, text="(", width=5, height=2, command=lambda: click_boton("(")) 
boton_parentesis_ci = tk.Button(ventana, text=")", width=5, height=2, command=lambda: click_boton(")")) 
boton_punto = tk.Button(ventana, text=".", width=5, height=2, command=lambda: click_boton("."))

boton_div = tk.Button(ventana, text="/", width=5, height=2, command=lambda: click_boton("/"))
boton_multi = tk.Button(ventana, text="*", width=5, height=2, command=lambda: click_boton("*"))
boton_suma = tk.Button(ventana, text="+", width=5, height=2, command=lambda: click_boton("+"))
boton_resta = tk.Button(ventana, text="-", width=5, height=2, command=lambda: click_boton("-"))
boton_igual = tk.Button(ventana, text="=", width=5, height=2, command=lambda: hacer_op())

boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis_ap.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis_ci.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton_7.grid(row=2, column=0, padx=5, pady=5)
boton_8.grid(row=2, column=1, padx=5, pady=5)
boton_9.grid(row=2, column=2, padx=5, pady=5)
boton_multi.grid(row=2, column=3, padx=5, pady=5)


boton_4.grid(row=3, column=0, padx=5, pady=5)
boton_5.grid(row=3, column=1, padx=5, pady=5)
boton_6.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=3, column=3, padx=5, pady=5)

boton_3.grid(row=4, column=0, padx=5, pady=5)
boton_2.grid(row=4, column=1, padx=5, pady=5)
boton_1.grid(row=4, column=2, padx=5, pady=5)
boton_resta.grid(row=4, column=3, padx=5, pady=5)

boton_0.grid(row=5, column=0, padx=5, pady=5, columnspan=2)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)


ventana.mainloop()