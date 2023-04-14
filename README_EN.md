# News extraction and conversion to audio

This project uses Python, Streamlit, BeautifulSoup and gTTS to extract news content from specific websites and convert it to audio. The web application created with Streamlit allows users to enter a URL of a supported website and then performs the extraction of the news title and content. Finally, the extracted information is converted to audio using gTTS (Google Text-to-Speech) and played on the page.

## Table of contents
- [Features](#features)
- [Prerequisites](#pre-requisites)
- [Installation](#installation)
- [Deploying in Streamlit](#deploying-your-Application-in-Streamlit-Sharing)
- [Usage](#usage)
- [Allowed domains](#allowed-domains)
- [Contribution](#contribution)
- [License](#license)

## Features
- Extracts news content from selected sites.
- Filters out unwanted or irrelevant text before converting the content.
- Converts extracted text to audio using Google Text-to-Speech (gTTS).
- Plays the resulting audio on the web application page.
- Checks if the entered URL belongs to the allowed domains.

## Prerequisites
- Python 3.6 or higher
- pip (Python Package Manager)

## Installation
1. Clone this repository:
```bash
git clone https://github.com/your_username/Extraccion_y_conversion_de_noticias_a_audio.git
```

2. Change to the project directory:
```bash
cd Extraction_and_conversion_of_news_to_audio
```

3. Install the necessary dependencies:
```bash
pip install -r requirements.txt
```

## Deploying your Application on Streamlit Sharing

[Streamlit Sharing](https://www.streamlit.io/sharing) is a free and easy to use service that allows you to deploy your Streamlit developed applications on the web.

### Steps to deploy your application on Streamlit Sharing:

1. **Upload your project to GitHub**: Make sure your project is in a public GitHub repository. This platform will pull your code directly from the repository to run the application.

2. **Sign up for Streamlit Sharing**: Go to [streamlit.io/sharing](https://www.streamlit.io/sharing) and create an account or log in with your GitHub credentials.

3. **Request an invitation (if you haven't already)**: If this is your first time using Streamlit Sharing, request an invitation. Once you receive it, you will be able to access the control panel.

4. **Go to the control panel**: Log in to Streamlit Sharing and go to the control panel by clicking on the "Go to sharing" button.

5. **Deploy your application**: Click on the "New app" button at the top right of the control panel. Select the repository containing your application, then select the corresponding branch and specify the file containing the Streamlit application (e.g. `app.py`).

6. **Click "Deploy "**: Once you have completed the necessary information, click the "Deploy" button to launch your application. Streamlit Sharing will create a virtual environment and deploy your application in a container. This process may take a few minutes.

## Usage
Run the Streamlit application in your local environment:

```bash
streamlit run app.py
```