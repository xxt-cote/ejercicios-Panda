import pandas as pd

df = pd.read_csv("estudiante.csv", sep=";", decimal=",")
if df.empty:
    print("Error: No hay estudiantes en la lista.")
else:
    notas_cols = ["Nota_1", "Nota_2", "Nota_3"]
    df[notas_cols] = df[notas_cols].abs()
    df["Promedio"] = df[notas_cols].mean(axis=1).round(1)
    df_ordenado = df.sort_values(by="Promedio", ascending=False).reset_index(drop=True)
    print(df_ordenado[["Nombre", "Promedio"]])
