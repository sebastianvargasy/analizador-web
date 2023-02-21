import streamlit as st
import requests
from lxml import html

# Página web de destino
url = 'https://www.sochisi.cl'

# Realizar la solicitud HTTP a la página web
response = requests.get(url)

# Analizar el HTML de la página web utilizando lxml
tree = html.fromstring(response.content)

# Extraer los elementos de la página web que deseas
# Por ejemplo, el título de la página:
title = tree.findtext('.//title')

# Extraer otros elementos de la página web
header = tree.findtext('.//h1')
paragraphs = tree.findall('.//p')

# Extraer información de otras páginas del sitio web
about_url = 'https://sochisi.cl/directorio/'
about_response = requests.get(about_url)
about_tree = html.fromstring(about_response.content)
about_header = about_tree.findtext('.//h1')

# Mostrar el resultado en la aplicación de Streamlit
st.write(f"El título de la página es: {title}")
st.write(f"El encabezado de la página es: {header}")
st.write(f"Los párrafos de la página son: {paragraphs}")
st.write(f"El encabezado de la página 'Acerca de' es: {about_header}")
