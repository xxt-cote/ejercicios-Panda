import pandas as pd

df = pd.read_csv("estudiante.csv", sep=";", decimal=",")
Nota_baja = (df[["Nota_1", "Nota_2", "Nota_3"]] < 4.0).any(axis=1)
porcentaje = round((Nota_baja.sum() / len(df)) * 100)
print(f"Porcentaje de estudiantes con al menos una nota bajo 4.0: {porcentaje}%")
