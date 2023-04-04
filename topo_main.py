import requests
from bs4 import BeautifulSoup
import streamlit as st

# Lista de dominios permitidos
allowed_domains = ['example.com', 'bbc.com', 'nytimes.com']

# Configurar la página de Streamlit
st.set_page_config(page_title="Extracción de noticias", page_icon=":newspaper:")

# Título de la página
st.title("Extracción de noticias")

# Campo de entrada para ingresar la URL del sitio web
url = st.text_input("Ingresa la URL del sitio web")

# Verificar si se ha ingresado una URL y si la URL pertenece a la lista de dominios permitidos
if url and any(domain in url for domain in allowed_domains):
    # Botón para iniciar la extracción de noticias
    if st.button("Extraer noticias"):

        # Realizar una petición GET a la página web
        response = requests.get(url)

        # Crear un objeto BeautifulSoup a partir del contenido HTML de la página
        soup = BeautifulSoup(response.content, 'html.parser')

        # Buscar el título de la noticia
        titulo_noticia = soup.find('h1', {'itemprop': 'name headline'}).get_text()

        # Seleccionar el elemento con la clase "content" y el identificador "content"
        content = soup.find('div', {'class': 'content', 'id': 'content'})

        # Extraer el contenido de los elementos <p> que no contienen texto no deseado
        contenido_noticia = ""
        for p in content.find_all('p'):
            text = p.get_text().lower()
            if "video relacionado" not in text and "fuente" not in text and "por si te lo perdiste" not in text and "da clic aquí para leer más noticias relacionadas con" not in text and "editorial:" not in text and "entérate:" not in text and "puedes visitar este enlace para conocer todas las noticias relacionadas con" not in text and "busca en este enlace todas las noticias relacionadas con" not in text:
                contenido_noticia += p.get_text() + "\n\n"

        # Mostrar el título de la noticia y el contenido extraído
        st.header(titulo_noticia)
        st.write(contenido_noticia)
elif url:
    # Mostrar mensaje de error si la URL no pertenece a la lista de dominios permitidos
    st.error("La URL ingresada no pertenece a los dominios permitidos.")
