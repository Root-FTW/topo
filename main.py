import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from io import BytesIO
import streamlit as st

# Lista de dominios permitidos
# List of allowed domains
allowed_domains = ['levelup.com', 'tarreo.com', 'tomatazos.com', 'qore.com', 'sandiegored.com']

# Configurar la página de Streamlit
# Configuring the Streamlit page
st.set_page_config(page_title="Extracción y conversión de noticias a audio", page_icon=":newspaper:")

# Título de la página
# Page title
st.title("Extracción y conversión de noticias a audio")

# Campo de entrada para ingresar la URL del sitio web
# Input field for entering the URL of the web site
url = st.text_input("Ingresa la URL del sitio web")

# Verificar si se ha ingresado una URL y si la URL pertenece a la lista de dominios permitidos
# Check if a URL has been entered and if the URL belongs to the list of allowed domains
if url and any(domain in url for domain in allowed_domains):
    # Botón para iniciar la extracción y conversión de noticias
    # Button to start news extraction and conversion
    if st.button("Extraer y convertir a audio"):
        # Realizar una petición GET a la página web
        # Make a GET request to the web page
        response = requests.get(url)

        # Crear un objeto BeautifulSoup a partir del contenido HTML de la página
        # Create a BeautifulSoup object from the HTML content of the page.
        soup = BeautifulSoup(response.content, 'html.parser')

        # Buscar el título de la noticia
        # Search for the title of the news item
        titulo_noticia = soup.find('h1', {'itemprop': 'name headline'}).get_text()

        # Seleccionar el elemento con la clase "content" y el identificador "content"
        # Select the element with the class "content" and the identifier "content".
        content = soup.find('div', {'class': 'content', 'id': 'content'})

        # Extraer el contenido de los elementos <p> que no contienen texto no deseado
        # Extract the content of <p> elements that do not contain unwanted text.
        contenido_noticia = ""
        for p in content.find_all('p'):
            text = p.get_text().lower()
            if "video relacionado" not in text and "fuente" not in text and "por si te lo perdiste" not in text and "da clic aquí para leer más noticias relacionadas con" not in text and "editorial:" not in text and "entérate:" not in text and "puedes visitar este enlace para conocer todas las noticias relacionadas con" not in text and "busca en este enlace todas las noticias relacionadas con" not in text:
                contenido_noticia += p.get_text() + "\n\n"

        # Combinar el título de la noticia con el contenido de la noticia
        # Combine the title of the news item with the content of the news item.
        texto_completo = titulo_noticia + "\n\n" + contenido_noticia

        # Mostrar el título de la noticia
        # Show the title of the news item
        st.header(titulo_noticia)

        # Convertir el contenido completo a habla y guardar el archivo de sonido en un objeto de flujo de bytes
        # Convert the entire content to speech and save the sound file as a byte stream object
        sound_file = BytesIO()
        tts = gTTS(texto_completo, lang='es', tld='com.mx')
        tts.write_to_fp(sound_file)

        # Reproducir el archivo de sonido en la aplicación web
        # Playing the sound file in the web application
        st.audio(sound_file.getvalue(), format='audio/mp3')

        # Mostrar el contenido extraído
        # Show the extracted content.
        st.write(contenido_noticia)
       
elif url:
    # Mostrar mensaje de error si la URL no pertenece a la lista de dominios permitidos
    # Show error message if the URL does not belong to the list of allowed domains
    st.error("La URL ingresada no pertenece a los dominios permitidos.")
