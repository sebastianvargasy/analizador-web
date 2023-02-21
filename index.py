import streamlit as st
import requests
from bs4 import BeautifulSoup

# Página web de destino
url = 'https://www.sochisi.cl'

# Realizar la solicitud HTTP a la página web
response = requests.get(url)

# Analizar el HTML de la página web utilizando Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Extraer los elementos de la página web que deseas
# Por ejemplo, el título de la página:
title = soup.find('title').text

# Mostrar el resultado en la aplicación de Streamlit
st.write(f"El título de la página es: {title}")
