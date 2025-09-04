import pandas as pd

df = pd.read_csv("estudiante.csv", sep=";", decimal=",")
df["Promedio"] = df[["Nota_1", "Nota_2", "Nota_3"]].mean(axis=1).round(1)

print(df)
idx_max, idx_min = df["Promedio"].idxmax(), df["Promedio"].idxmin()
print(
    f"\nMejor promedio dentro del curso:\n"
    f"-Estudiante: {df.loc[idx_max, 'Nombre']} \n-Promedio de calificaciones: {df.loc[idx_max, 'Promedio']}"
)
print(
    f"Peor promedio dentro del curso:\n"
    f"-Estudiante: {df.loc[idx_min, 'Nombre']} \n-Promedio de calificaciones: {df.loc[idx_min, 'Promedio']}"
)
