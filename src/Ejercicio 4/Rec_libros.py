import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import numpy as np



# Define key
KEY = '7KxZi4LBpNUr6DBwuRYDfpAEmbn7I6v0'

# URL lista
best_seller_lista_URL = f'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={KEY}'
BEST_SELLER_BOOKS_URL = 'https://api.nytimes.com/svc/books/v3/lists.json'

########################3
## Funcion guardarla en st cache para que se guarde internamente desde el comienzo
################################
@st.cache_data
def list_name():
	response = requests.get(best_seller_lista_URL)
	return response.json()['results']

# Función para obtener los libros de una lista específica de Best Sellers
def best_books_sellers(lista_nombres_decod, date="current"):
	params = {
		'api-key': KEY,
		'list': lista_nombres_decod,
		'published_date': date
	}
	response = requests.get(BEST_SELLER_BOOKS_URL, params=params)
	books = response.json()['results']
	book_df = pd.DataFrame([book['book_details'][0] for book in books])
	print(book_df , '--------------------books seleccionadoss-----------------------------')
	np.random.seed(2024)
	book_df['precio'] = np.random.randint(0, 1000, size=len(book_df))
	book_df['rango_precio'] = pd.cut(book_df['precio'], bins=[0, 200, 400, 800, float('inf')], labels=["0-200", "201-400", "401-800", "800+"])
	
	generations = ['Boomers', 'Gen X', 'Millennials', 'Gen Z']
	book_df['rango_generacion'] = np.random.choice(generations, size=len(book_df))
	return book_df


# Título de la aplicación
st.title("Consulta de Best Sellers del New York Times")


########################3
## Filtro por lista
################################
best_seller_lista = list_name()


lista_nombres = [info['display_name'] for info in best_seller_lista]
lista_seleccionada = st.selectbox("Selecciona una lista de Best Sellers:", lista_nombres)



lista_seleccionada = next(
	(info['list_name_encoded'] for info in best_seller_lista if info['display_name'] == lista_seleccionada), None
)


########################3
## Filtros fecha, por mes
################################

date_choice = st.radio("¿Quieres ver la lista del Fecha actual o de un Fecha en específico?", ["Fecha Actual", "Fecha Específico"])
if date_choice == "Fecha Específico":
	selected_date = st.date_input("Selecciona una fecha")
	date = datetime(selected_date.year, selected_date.month, 1).strftime("%Y-%m-%d")
else:
	current_date = datetime.now()
	date = datetime(current_date.year, current_date.month, 1).strftime("%Y-%m-%d")


print('--------------------dates _filtro-------------------------------', date)

########################3
## Filtros nuevos
################################
precio_selecc = st.selectbox("Selecciona el rango de precio", ["0-200", "201-400", "401-800", "800+"])
edad_selecc = st.selectbox("Selecciona el rango edad", ["Boomers", "Gen X", "Millennials", "Gen Z"])




########################3
## Acitvar botón
################################
if st.button("Consultar libros de la lista seleccionada"):
	books_df = best_books_sellers(lista_seleccionada, date)
	print(books_df, "----------prueba")
	bookd_df_filtrado = books_df[
		(books_df['rango_precio'] == precio_selecc) &
		(books_df['rango_generacion'] == edad_selecc)
	]
	## Base ya filtrada
	if not bookd_df_filtrado.empty:
		st.write(f"### Resultados para la lista **{lista_seleccionada}** ({date[:7]})")
		for _, book in bookd_df_filtrado.iterrows():
			st.write(f"#### {book['title']} por {book['author']}")
			st.write(f"**Descripción:** {book['description']}")
			st.write(f"**Precio estimado:** ${book['precio']}")
			st.write(f"**Rango de precio:** {book['rango_precio']}")
			st.write(f"**EDAD:** {book['rango_generacion']}")
			st.write("---")
	else:
		st.write("No se encontraron libros.")