import streamlit as st
import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt


# Cargar el archivo de promociones desde la carpeta "data"
@st.cache_data
def load_data():
    # Usar una ruta relativa para acceder al archivo en la carpeta "data"
    file_path = os.path.join('data', 'Prueba_Promociones.csv')
    return pd.read_csv(file_path)


# Cargar datos y convertir columnas necesarias
promotions_data = load_data()
promotions_data['Fecha'] = pd.to_datetime(promotions_data['Fecha'], format='%d-%m-%y %H:%M', errors='coerce')
promotions_data['Semana'] = promotions_data['Fecha'].dt.isocalendar().week

# Título de la aplicación
st.title("Proyección de Inventario")

# Entradas del usuario
st.sidebar.header("Parámetros de Entrada")


# Obtener opciones únicas de las columnas de categoría, uso y SKU
categorias = promotions_data['Categoria'].unique()
usos = promotions_data['Uso'].unique()
skus = promotions_data['SKU'].unique()

# Crear listas desplegables con opciones
fecha_inicio = st.sidebar.text_input("Fecha de inicio (YYYY-MM-DD)", "2024-01-01")
fecha_fin = st.sidebar.text_input("Fecha de fin (YYYY-MM-DD)", "2024-12-31")
categoria = st.sidebar.selectbox("Categoría del producto", categorias)
uso = st.sidebar.selectbox("Uso del producto", usos)
sku = st.sidebar.selectbox("SKU del producto", skus)
porcentaje_incremento = st.sidebar.number_input("Porcentaje de incremento (decimal)", 0.1)
inventario_inicial = st.sidebar.number_input("Inventario inicial", 100)

# Convertir fechas a datetime
fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d') if fecha_inicio else None
fecha_fin_dt = datetime.strptime(fecha_fin, '%Y-%m-%d') if fecha_fin else None

# Condiciones para el filtrado


fecha_condicion = (
    (promotions_data['Fecha'] >= fecha_inicio_dt) & (promotions_data['Fecha'] <= fecha_fin_dt) 
    if fecha_inicio_dt and fecha_fin_dt else
    (promotions_data['Fecha'] >= fecha_inicio_dt) if fecha_inicio_dt else
    (promotions_data['Fecha'] <= fecha_fin_dt)
)

modelo_condicion = promotions_data['Modelo'] != "real"
uso_categoria_condicion = (
    (promotions_data['Uso'] == uso) if uso else
    (promotions_data['Categoria'] == categoria) if categoria else
    True
)

# Aplicar ajuste en 'Piezas' según porcentaje
promotions_data.loc[fecha_condicion & modelo_condicion & uso_categoria_condicion, 'Piezas Ajuste'] = promotions_data['Piezas'] * (1 + porcentaje_incremento)

# Filtrar datos específicos para el SKU seleccionado
sku_data = promotions_data[promotions_data['SKU'] == sku].copy()
sku_data = sku_data.sort_values(by='Fecha')
sku_data['Inventario'] = inventario_inicial



# Proyección de inventario
for i in range(1, len(sku_data)):
    sku_data.loc[sku_data.index[i], 'Inventario'] = sku_data.loc[sku_data.index[i - 1], 'Inventario'] - sku_data.loc[sku_data.index[i], 'Piezas Ajuste']

# Identificar la primera fecha con inventario negativo
fecha_negativa = sku_data[sku_data['Inventario'] < 0].iloc[0]['Fecha'] if not sku_data[sku_data['Inventario'] < 0].empty else None

# Mostrar resultados en tabla
st.subheader("Resultados de la Proyección de Inventario")

if fecha_negativa:
    st.warning(f"El inventario se vuelve negativo el: {fecha_negativa}")
else:
    st.success("El inventario no se vuelve negativo en el periodo seleccionado.")


st.subheader("Gráfica de Decrecimiento del Inventario")

plt.figure(figsize=(10, 6))
plt.plot(sku_data['Fecha'], sku_data['Inventario'], marker='o', linestyle='-', color='b')
plt.axhline(0, color='red', linestyle='--', label='Nivel de Inventario Cero')
plt.title("Proyección del Inventario en el Tiempo")
plt.xlabel("Fecha")
plt.ylabel("Inventario")
plt.legend()


st.pyplot(plt)