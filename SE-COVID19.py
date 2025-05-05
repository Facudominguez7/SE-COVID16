import tkinter as tk
from tkinter import messagebox

# Lista de síntomas posibles
sintomas_validos = [
    "fiebre",
    "tos seca",
    "pérdida del olfato",
    "pérdida del gusto",
    "dolor de cabeza",
    "dolor muscular"
]

def diagnosticar():
    seleccionados = [sintomas_validos[i] for i in range(len(sintomas_validos)) if var_sintomas[i].get()]
    if "fiebre" in seleccionados and "tos seca" in seleccionados and ("pérdida del olfato" in seleccionados or "pérdida del gusto" in seleccionados):
        resultado = "Alto riesgo de COVID-19. Se recomienda aislamiento y consulta médica urgente."
    elif "fiebre" in seleccionados and "dolor de cabeza" in seleccionados and "dolor muscular" in seleccionados:
        resultado = "Síntomas compatibles con COVID-19, pero no concluyentes. Se recomienda seguimiento."
    else:
        resultado = "Síntomas no compatibles con COVID-19. Se sugiere control médico si los síntomas persisten."
    messagebox.showinfo("Diagnóstico", resultado)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Diagnóstico COVID-19")

# Instrucciones
tk.Label(ventana, text="Seleccione los síntomas del paciente:").pack(pady=10)

# Crear checkboxes para los síntomas
var_sintomas = [tk.BooleanVar() for _ in sintomas_validos]
for i, sintoma in enumerate(sintomas_validos):
    tk.Checkbutton(ventana, text=sintoma, variable=var_sintomas[i]).pack(anchor="w")

# Botón para diagnosticar
tk.Button(ventana, text="Diagnosticar", command=diagnosticar).pack(pady=20)

# Iniciar la aplicación
ventana.mainloop()