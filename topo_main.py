import requests
from bs4 import BeautifulSoup
from google.cloud import texttospeech
import os

# Configurar la página de Streamlit
st.set_page_config(page_title="Extracción de noticias", page_icon=":newspaper:")

# Lista de dominios permitidos
allowed_domains = ['levelup.com', 'tarreo.com', 'tomatazos.com', 'qore.com', 'sandiegored.com']

# Campo de entrada para ingresar las credenciales de autenticación de Google Cloud Text-to-Speech en formato JSON
credenciales_texto = st.text_area("Ingresa tus credenciales de autenticación de Google Cloud Text-to-Speech en formato JSON")

# Si se ha ingresado un valor en el campo de texto, establece las credenciales de autenticación
if credenciales_texto:
    # Escribir las credenciales en un archivo temporal
    with open("credenciales.json", "w") as file:
        file.write(credenciales_texto)

    # Establecer las credenciales de autenticación de Google Cloud Text-to-Speech
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credenciales.json"

# Función para convertir el contenido extraído de la URL a un archivo de audio
def synthesize_text_to_audio(text_to_synthesize):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text_to_synthesize)

    # Build the voice request, select the language code ("en-US") and the ssml voice gender ("female")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-F",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    # Select the type of audio file returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary
    with open("noticia.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)

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
        content =
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

    # Convertir el contenido extraído de la URL a audio
    synthesize_text_to_audio(contenido_noticia)

    # Mostrar un mensaje de éxito
    st.success("¡La noticia ha sido extraída y convertida a audio!")
elif url:
# Mostrar mensaje de error si la URL no pertenece a la lista de dominios permitidos
st.error("La URL ingresada no pertenece a los dominios permitidos.")
