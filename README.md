# Extracción y conversión de noticias a audio

Este proyecto utiliza Python, Streamlit, BeautifulSoup y gTTS para extraer contenido de noticias de sitios web específicos y convertirlo en audio. La aplicación web creada con Streamlit permite a los usuarios ingresar una URL de un sitio web soportado y, luego, realiza la extracción del título y el contenido de la noticia. Por último, la información extraída se convierte en audio utilizando gTTS (Google Text-to-Speech) y se reproduce en la página.

## Tabla de contenidos
- [Características](#características)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
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

## Uso
Ejecute la aplicación Streamlit en su entorno local:

```bash
streamlit run app.py
