# News Extraction and Audio Conversion

[English](./README_EN.md) | [Español](./README.md)

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
git clone https://github.com/Root-FTW/News_Extraction_and_Audio_Conversion.git
```

2. Change to the project directory:
```bash
cd News_Extraction_and_Audio_Conversion
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Deploying your Application on Streamlit Sharing

[Streamlit Sharing](https://www.streamlit.io/sharing) is a free and easy-to-use service that allows you to deploy your Streamlit-developed applications on the web.

### Steps to deploy your application on Streamlit Sharing:

1. **Upload your project to GitHub**: Make sure your project is in a public GitHub repository. This platform will pull your code directly from the repository to run the application.

2. **Sign up for Streamlit Sharing**: Go to [streamlit.io/sharing](https://www.streamlit.io/sharing) and create an account or sign in with your GitHub credentials.

3. **Request an invitation (if you haven't already)**: If it's your first time using Streamlit Sharing, request an invitation. Once received, you'll gain access to the dashboard.

4. **Go to the dashboard**: Sign in to Streamlit Sharing and head to the dashboard by clicking on the "Go to sharing" button.

5. **Deploy your application**: Click on the "New app" button in the top right corner of the dashboard. Select the repository containing your application, then choose the corresponding branch and specify the file containing the Streamlit application (for example, `app.py`).

6. **Click on "Deploy"**: Once you have filled in the necessary information, click the "Deploy" button to launch your application. Streamlit Sharing will create a virtual environment and deploy your application in a container. This process may take a few minutes.

## Usage
Run the Streamlit application in your local environment:

```bash
streamlit run app.py
```