import requests
from bs4 import BeautifulSoup
import os
from google.cloud import texttospeech

# Configurar la credencial de autenticación del cliente de Text-to-Speech de Google Cloud.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "daring-harmony-379101-6a518e6f8c41.json"

# Lista de dominios permitidos
allowed_domains = ['levelup.com', 'tarreo.com', 'tomatazos.com', 'qore.com', 'sandiegored.com']

# Función para sintetizar texto en voz y guardar como archivo MP3
def synthesize_text(text, filename):
    # Crear un cliente de Text-to-Speech de Google Cloud.
    client = texttospeech.TextToSpeechClient()

    # Establecer el texto de entrada que se va a sintetizar.
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Configurar el parámetro de selección de voz para que use la voz "en-US-Wavenet-F" de género femenino en inglés estadounidense.
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-F",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    # Configurar el parámetro de codificación de audio para que utilice el formato MP3.
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Sintetizar el texto utilizando el cliente de Text-to-Speech de Google Cloud y los parámetros configurados.
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Escribir el archivo MP3 sintetizado en el mismo directorio que el archivo PDF.
    with open(f"{filename}.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to the original file directory')

# Configurar la página de Streamlit.
st.set_page_config(page_title="Extracción de noticias", page_icon=":newspaper:")

# Mostrar el título de la página.
st.title("Extracción de noticias")

# Campo de entrada para ingresar la URL del sitio web.
url = st.text_input("Ingresa la URL del sitio web")

# Verificar si se ha ingresado una URL y si la URL pertenece a la lista de dominios permitidos.
if url and any(domain in url for domain in allowed_domains):

    # Botón para iniciar la extracción de noticias.
    if st.button("Extraer noticias"):
        # Realizar una petición GET a la página web.
        response = requests.get(url)

        # Crear un objeto BeautifulSoup a partir del contenido HTML de la página.
        soup = BeautifulSoup(response.content, 'html.parser')

        # Buscar el título de la noticia.
        titulo_noticia = soup.find('h1', {'itemprop': 'name headline'}).get_text()

        # Seleccionar el elemento con la clase "content" y el identificador "content".
        content = soup.find('div', {'class': 'content',
    # Extraer el contenido de los elementos <p> que no contienen texto no deseado.
    contenido_noticia = ""
    for p in content.find_all('p'):
        text = p.get_text().lower()
        if "video relacionado" not in text and "fuente" not in text and "por si te lo perdiste" not in text and "da clic aquí para leer más noticias relacionadas con" not in text and "editorial:" not in text and "entérate:" not in text and "puedes visitar este enlace para conocer todas las noticias relacionadas con" not in text and "busca en este enlace todas las noticias relacionadas con" not in text:
            contenido_noticia += p.get_text() + "\n\n"

    # Mostrar el título de la noticia y el contenido extraído.
    st.header(titulo_noticia)
    st.write(contenido_noticia)

    # Llamar a la función synthesize_text() para convertir el contenido extraído en audio y guardarlo como archivo MP3.
    synthesize_text(contenido_noticia, titulo_noticia)
elif url:
# Mostrar mensaje de error si la URL no pertenece a la lista de dominios permitidos.
st.error("La URL ingresada no pertenece a los dominios permitidos.")
