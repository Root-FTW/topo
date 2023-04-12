# News Extraction and Audio Conversion

This project uses Python, Streamlit, BeautifulSoup, and gTTS to extract news content from specific websites and convert it into audio. The web app created with Streamlit allows users to enter a URL from a supported website, then extracts the news title and content. Finally, the extracted information is converted into audio using gTTS (Google Text-to-Speech) and played on the page.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Deploying on Streamlit](#deploying-your-app-on-streamlit-sharing)
- [Usage](#usage)
- [Allowed Domains](#allowed-domains)
- [Contribution](#contribution)
- [License](#license)

## Features
- Extracts news content from selected sites.
- Filters out unwanted or irrelevant text before converting the content.
- Converts the extracted text into audio using Google Text-to-Speech (gTTS).
- Plays the resulting audio on the web app's page.
- Checks if the entered URL belongs to the allowed domains.

## Prerequisites
- Python 3.6 or higher
- pip (Python Package Manager)

## Installation
1. Clone this repository:
```bash
git clone https://github.com/your_username/News_Extraction_and_Audio_Conversion.git
```

2. Change to the project directory:
```bash
cd News_Extraction_and_Audio_Conversion
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Deploying your App on Streamlit Sharing

[Streamlit Sharing](https://www.streamlit.io/sharing) is a free and easy-to-use service that allows you to deploy your Streamlit-developed apps on the web.

### Steps to deploy your app on Streamlit Sharing:

1. **Upload your project to GitHub**: Make sure your project is
