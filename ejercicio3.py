import pandas as pd

df = pd.read_csv("estudiante.csv", sep=";", decimal=",")
todas_notas = pd.concat([df["Nota_1"], df["Nota_2"], df["Nota_3"]])
moda = todas_notas.mode()
print(f"La(s) nota(s) más frecuente(s) es/son: {moda.values.tolist()}")
