import pandas as pd


df = pd.read_csv("estudiante.csv", sep=";", decimal=",")
aprobados = (df[["Nota_1", "Nota_2", "Nota_3"]] >= 4.0).all(axis=1)
cantidad_aprobados = aprobados.sum()
print(
    f"Cantidad de estudiantes que aprobaron todas sus asignaturas: {cantidad_aprobados}"
)
