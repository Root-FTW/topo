# Extracción y conversión de noticias a audio

[English](./README_EN.md) | [Español](./README.md)

Este proyecto utiliza Python, Streamlit, BeautifulSoup y gTTS para extraer contenido de noticias de sitios web específicos y convertirlo en audio. La aplicación web creada con Streamlit permite a los usuarios ingresar una URL de un sitio web soportado y, luego, realiza la extracción del título y el contenido de la noticia. Por último, la información extraída se convierte en audio utilizando gTTS (Google Text-to-Speech) y se reproduce en la página.

## Tabla de contenidos
- [Características](#características)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Desplegar en Streamlit](#Desplegando-tu-Aplicación-en-Streamlit-Sharing)
- [Uso](#uso)
- [Dominios permitidos](#dominios-permitidos)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Características
- Extrae el contenido de las noticias de sitios seleccionados.
- Filtra texto no deseado o irrelevante antes de convertir el contenido.
- Convierte el texto extraído en audio usando Google Text-to-Speech (gTTS).
- Reproduce el audio resultante en la página de la aplicación web.
- Verifica si la URL ingresada pertenece a los dominios permitidos.

## Requisitos previos
- Python 3.6 o superior
- pip (Administrador de paquetes de Python)

## Instalación
1. Clone este repositorio:
```bash
git clone https://github.com/your_username/Extraccion_y_conversion_de_noticias_a_audio.git
```

2. Cambie al directorio del proyecto:
```bash
cd Extraccion_y_conversion_de_noticias_a_audio
```

3. Instale las dependencias necesarias:
```bash
pip install -r requirements.txt
```

## Desplegando tu Aplicación en Streamlit Sharing

[Streamlit Sharing](https://www.streamlit.io/sharing) es un servicio gratuito y fácil de usar que te permite desplegar tus aplicaciones desarrolladas con Streamlit en la web.

### Pasos para desplegar tu aplicación en Streamlit Sharing:

1. **Sube tu proyecto a GitHub**: Asegúrate de que tu proyecto esté en un repositorio público de GitHub. Esta plataforma extraerá tu código directamente desde el repositorio para ejecutar la aplicación.

2. **Regístrate en Streamlit Sharing**: Dirígete a [streamlit.io/sharing](https://www.streamlit.io/sharing) y crea una cuenta o inicia sesión con tus credenciales de GitHub.

3. **Solicita una invitación (si aún no lo has hecho)**: Si es la primera vez que utilizas Streamlit Sharing, solicita una invitación. Una vez que la recibas, podrás acceder al panel de control.

4. **Dirígete al panel de control**: Inicia sesión en Streamlit Sharing y ve al panel de control haciendo clic en el botón "Go to sharing" ("Ir a compartir").

5. **Despliega tu aplicación**: Haz clic en el botón "New app" ("Nueva aplicación") en la parte superior derecha del panel de control. Selecciona el repositorio que contiene tu aplicación, luego selecciona la rama correspondiente y especifica el archivo que contiene la aplicación de Streamlit (por ejemplo, `app.py`).

6. **Haz clic en "Deploy"**: Una vez que hayas completado la información necesaria, haz clic en el botón "Deploy" ("Desplegar") para lanzar tu aplicación. Streamlit Sharing creará un entorno virtual y desplegará tu aplicación en un contenedor. Este proceso puede tardar unos minutos.

## Uso
Ejecute la aplicación Streamlit en su entorno local:

```bash
streamlit run app.py
