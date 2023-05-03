import requests
from bs4 import BeautifulSoup
from elevenlabs import generate, set_api_key
from io import BytesIO
import streamlit as st

allowed_domains = ['levelup.com', 'tarreo.com', 'tomatazos.com', 'qore.com', 'sandiegored.com']

st.set_page_config(page_title="Extracción y conversión de noticias a audio", page_icon=":newspaper:")

st.title("Extracción y conversión de noticias a audio")

url = st.text_input("Ingresa la URL del sitio web")

# Aquí el usuario ingresa su API key
api_key = st.text_input("Ingresa tu API key de Elevenlabs")

if url and any(domain in url for domain in allowed_domains):
    # Botón para analizar la cantidad de caracteres en el texto extraído
    if st.button("Analizar"):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        titulo_noticia = soup.find('h1', {'itemprop': 'name headline'}).get_text()
        content = soup.find('div', {'class': 'content', 'id': 'content'})

        contenido_noticia = ""
        for p in content.find_all('p'):
            text = p.get_text().lower()
            if "video relacionado" not in text and "fuente" not in text and "por si te lo perdiste" not in text and "da clic aquí para leer más noticias relacionadas con" not in text and "editorial:" not in text and "entérate:" not in text and "puedes visitar este enlace para conocer todas las noticias relacionadas con" not in text and "busca en este enlace todas las noticias relacionadas con" not in text:
                contenido_noticia += p.get_text() + "\n\n"

        texto_completo = titulo_noticia + "\n\n" + contenido_noticia

        # Muestra la cantidad total de caracteres en el texto extraído
        st.write(f"Total de caracteres en el texto: {len(texto_completo)}")
    # El botón "Extraer y convertir a audio" solo se muestra si el usuario ingresa su clave API
    if api_key:
        if st.button("Extraer y convertir a audio"):
            # Establecer la API key antes de generar el audio
            set_api_key(api_key)

            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            titulo_noticia = soup.find('h1', {'itemprop': 'name headline'}).get_text()
            content = soup.find('div', {'class': 'content', 'id': 'content'})

            contenido_noticia = ""
            for p in content.find_all('p'):
                text = p.get_text().lower()
                if "video relacionado" not in text and "fuente" not in text and "por si te lo perdiste" not in text and "da clic aquí para leer más noticias relacionadas con" not in text and "editorial:" not in text and "entérate:" not in text and "puedes visitar este enlace para conocer todas las noticias relacionadas con" not in text and "busca en este enlace todas las noticias relacionadas con" not in text:
                    contenido_noticia += p.get_text() + "\n\n"

            texto_completo = titulo_noticia + "\n\n" + contenido_noticia

            st.header(titulo_noticia)

            # Muestra un mensaje de "Cargando..." mientras se genera el audio
            loading_message = st.empty()
            loading_message.text("Cargando...")

            audio = generate(text=texto_completo, voice="Arnold", model='eleven_multilingual_v1')
            sound_file = BytesIO(audio)

            # Elimina el mensaje de "Cargando..." cuando el audio esté listo
            loading_message.empty()

            st.audio(sound_file.getvalue(), format='audio/mp3')

            st.write(contenido_noticia)

elif url:
    st.error("La URL ingresada no pertenece a los dominios permitidos.")
