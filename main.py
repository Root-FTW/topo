import requests
from elevenlabs import generate, set_api_key
from io import BytesIO
import streamlit as st
import feedparser
from bs4 import BeautifulSoup

def should_delete_paragraph(paragraph):
    phrases_to_ignore = [
        "Ya llegaron las playeras oficiales de LEVEL UP",
        "CONSIGUE LA TUYA AQUÍ",
        "Aquí lo puedes ver",
        "Editorial:",
        "Por si te lo perdiste:",
        "VIDEO RELACIONADO:",
        "Ubicación:",
        "VIDEO:",
        "Video relacionado:"
    ]

    for phrase in phrases_to_ignore:
        if phrase in paragraph.get_text():
            return True
    return False

# Configuración de Streamlit
st.set_page_config(
    page_title="Extracción y conversión de noticias a audio", page_icon=":newspaper:"
)
st.title("Extracción y conversión de noticias a audio")

# Ingrese la URL del feed RSS 2.0
rss_url = st.text_input("Ingresa la URL del feed RSS 2.0")

# Ingrese su API key (Elevenlabs)
api_key = st.text_input("Ingresa tu API key de Elevenlabs")

if rss_url:
    feed = feedparser.parse(rss_url)
    entries = feed.entries[:10]

    for entry in entries:
        link = entry.link
        title = entry.title
        content_encoded = entry.content[0].value

        # Reemplazar y eliminar <!doctype html> del contenido
        content_encoded = content_encoded.replace('<!doctype html>', '')

        try:
            p_start = content_encoded.index('<p>')
            p_end = content_encoded.rindex('</p>') + 4
            content_encoded = content_encoded[p_start:p_end]
        except ValueError:
            pass

        content_soup = BeautifulSoup(content_encoded, "html.parser")

        # Eliminar los atributos "alt" de todas las imágenes
        for img_tag in content_soup.find_all("img"):
            img_tag.attrs["alt"] = ""

        # Eliminar todas las etiquetas <figcaption>
        for figcaption_tag in content_soup.find_all("figcaption"):
            figcaption_tag.decompose()

        # Eliminar todas las etiquetas <blockquote>
        for blockquote_tag in content_soup.find_all("blockquote"):
            blockquote_tag.decompose()

        # Eliminar los enlaces con el texto "Fuente"
        for a_tag in content_soup.find_all("a"):
            if "Fuente" in a_tag.get_text():
                a_tag.decompose()
                
        # Eliminar todas las etiquetas <a> con atributo data-cb_gallery
        for a_tag in content_soup.find_all("a", attrs={"data-cb_gallery": True}):
            a_tag.decompose()

        # Eliminar todas las etiquetas <p> que contengan las frases mencionadas
        for p_tag in content_soup.find_all("p"):
            if should_delete_paragraph(p_tag):
                p_tag.decompose()

        text_content = content_soup.get_text()

        # Mostrar Título
        st.write("Título:")
        st.write(f"**{title}**")

        # Mostrar URL
        st.write("URL:")
        st.write(link)

        # Mostrar Cantidad de Caracteres
        texto_completo = title + "\n\n" + text_content
        caracteres = len(texto_completo)
        st.write("Caracteres:")
        st.write(caracteres)

        # Mostrar Contenido
        st.write("Contenido:")
        st.write(text_content)

        if api_key:
            if st.button(f"Extraer y convertir a audio - {title}"):
                # Establecer la API key antes de generar el audio
                set_api_key(api_key)

                st.header(title)

                # Muestra un mensaje de "Cargando..." mientras se genera el audio
                loading_message = st.empty()
                loading_message.text("Cargando...")

                audio = generate(
                    text=texto_completo, voice="Arnold", model="eleven_multilingual_v1"
                )
                sound_file = BytesIO(audio)

                # Elimina el mensaje de "Cargando..." cuando el audio esté listo
                loading_message.empty()

                st.audio(sound_file.getvalue(), format="audio/mp3")

                st.write(text_content)
