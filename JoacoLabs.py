import random
import tkinter as tk
from tkinter import messagebox

def calculadora_sorpresa(operacion):
    pronosticos = [
        "Serás devorado por tiburones.",
        "Te caerá un rayo.",
        "Serás atacado por un enjambre de abejas.",
        "Te perderás en el bosque y nunca serás encontrado.",
        "Serás abducido por extraterrestres.",
        "Te convertirás en un fantasma y asustarás a la gente.",
        "Te caerás de un acantilado.",
        "Serás atrapado en un tornado.",
        "Te convertirás en un vampiro y vivirás para siempre.",
        "Serás atrapado en un apocalipsis zombi."
    ]

    try:
        resultado = eval(operacion)
        pronostico = random.choice(pronosticos)
        return f"El resultado de la operación es {resultado}. {pronostico}"
    except Exception as e:
        return f"Error en la operación: {e}"

# Ejemplo de uso
operacion = input("Introduce una operación matemática: ")
print(calculadora_sorpresa(operacion))
def realizar_operacion():
    operacion = operacion_var.get()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    
    if operacion == "Suma":
        resultado = num1 + num2
    elif operacion == "Resta":
        resultado = num1 - num2
    elif operacion == "Multiplicación":
        resultado = num1 * num2
    elif operacion == "División":
        if num2 != 0:
            resultado = num1 / num2
        else:
            messagebox.showerror("Error", "No se puede dividir por cero")
            return
    elif operacion == "Operación Sorpresa":
        pronosticos = [
            "Serás devorado por tiburones.",
            "Te caerá un rayo.",
            "Serás atacado por un enjambre de abejas.",
            "Te perderás en el bosque y nunca serás encontrado.",
            "Serás abducido por extraterrestres.",
            "Te convertirás en un fantasma y asustarás a la gente.",
            "Te caerás de un acantilado.",
            "Serás atrapado en un tornado.",
            "Te convertirás en un vampiro y vivirás para siempre.",
            "Serás atrapado en un apocalipsis zombi."
        ]
        resultado = random.choice(pronosticos)
    else:
        messagebox.showerror("Error", "Operación no válida")
        return
    
    messagebox.showinfo("Resultado", f"El resultado de la operación es: {resultado}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora Sorpresa")

tk.Label(root, text="Número 1:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Número 2:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

tk.Label(root, text="Operación:").grid(row=2, column=0)
operacion_var = tk.StringVar(root)
operacion_var.set("Suma")
operaciones_menu = tk.OptionMenu(root, operacion_var, "Suma", "Resta", "Multiplicación", "División", "Operación Sorpresa")
operaciones_menu.grid(row=2, column=1)

tk.Button(root, text="Calcular", command=realizar_operacion).grid(row=3, columnspan=2)

root.mainloop()