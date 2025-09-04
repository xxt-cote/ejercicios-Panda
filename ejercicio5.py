import pandas as pd

df = pd.read_csv("estudiante.csv", sep=";", decimal=",")
df["Promedio"] = df[["Nota_1", "Nota_2", "Nota_3"]].mean(axis=1).round(1)
df_ordenado = df.sort_values(by="Promedio", ascending=False)
print(df_ordenado[["Nombre", "Promedio"]].reset_index(drop=True))
