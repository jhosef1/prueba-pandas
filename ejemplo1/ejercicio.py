import pandas as pd # type: ignore

# Nombre del archivo CSV
archivo_csv = "empleados.csv"

# Leer CSV
df = pd.read_csv(archivo_csv)

# Mostrar lista de empleados
print("📋 Lista de empleados:")
print(df)

# Contar empleados
cantidad = len(df)
print(f"\n👥 Total de empleados: {cantidad}")
