import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel
archivo = 'ventas_tienda.xlsx'
df = pd.read_excel(archivo)

# Análisis inicial
print("Primeros datos:")
print(df.head())

# Agregar columna de ingreso total
df['Ingreso Total'] = df['Cantidad'] * df['Precio Unitario']

# Agrupar datos: Ingresos totales por sucursal
ingresos_por_sucursal = df.groupby('Sucursal')['Ingreso Total'].sum().reset_index()

# Visualización: Ingresos totales por sucursal
sns.barplot(data=ingresos_por_sucursal, x='Sucursal', y='Ingreso Total', palette='viridis')
plt.title('Ingresos Totales por Sucursal')
plt.xlabel('Sucursal')
plt.ylabel('Ingreso Total')
plt.tight_layout()
plt.show()

# Visualización: Tendencias de ventas por fecha
df['Fecha'] = pd.to_datetime(df['Fecha'])
ventas_por_fecha = df.groupby('Fecha')['Ingreso Total'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=ventas_por_fecha, x='Fecha', y='Ingreso Total', marker='o', color='b')
plt.title('Tendencia de Ingresos por Fecha')
plt.xlabel('Fecha')
plt.ylabel('Ingreso Total')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
