# Lista de síntomas posibles
sintomas_validos = [
    "fiebre",
    "tos seca",
    "pérdida del olfato",
    "pérdida del gusto",
    "dolor de cabeza",
    "dolor muscular"
]
 
print("Seleccione los síntomas del paciente marcando los números separados por coma:")
for i, sintoma in enumerate(sintomas_validos, start=1):
    print(f"{i}. {sintoma}")
 
# Ingreso de datos
entrada = input("\nEjemplo: 1,2,3\nIngrese los números correspondientes: ")
numeros = entrada.split(',')
 
# Obtener los síntomas seleccionados
sintomas = []
for num in numeros:
    num = num.strip()
    if num.isdigit():
        indice = int(num) - 1
        if 0 <= indice < len(sintomas_validos):
            sintomas.append(sintomas_validos[indice])
 
# Lógica de diagnóstico
if "fiebre" in sintomas and "tos seca" in sintomas and ("pérdida del olfato" in sintomas or "pérdida del gusto" in sintomas):
    print("\n>> Alto riesgo de COVID-19. Se recomienda aislamiento y consulta médica urgente.")
elif "fiebre" in sintomas and "dolor de cabeza" in sintomas and "dolor muscular" in sintomas:
    print("\n>> Síntomas compatibles con COVID-19, pero no concluyentes. Se recomienda seguimiento.")
else:
    print("\n>> Síntomas no compatibles con COVID-19. Se sugiere control médico si los síntomas persisten.")
