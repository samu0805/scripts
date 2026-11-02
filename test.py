import pandas as pd

print("Pandas version:", pd.__version__)

df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Marta"],
    "edad": [22, 25, 21]
})
print(df)
print("\nPromedio de edad:", df["edad"].mean())