# Text-to-Voice Translator

This project is a Django-based web application that converts text to speech, supporting multiple languages using Google Translate API. Users can input text in any language and listen to the speech in their preferred language.

Live Website: [translatee.pythonanywhere.com](http://translatee.pythonanywhere.com/)

## Features

- **Text-to-Speech**: Convert text input to voice in various languages.
- **Multiple Language Support**: Supports all the languages available through Google Translate API.
- **Easy Interface**: Simple and intuitive UI where users can input text and listen to the output speech.
- **Powered by Google Translate**: Uses the Google Translate API to translate text and Google Text-to-Speech for audio conversion.

## Technologies Used

- **Django**: The web framework used to build the application.
- **Google Translate API**: Used to translate the text to the required language.
- **Google Text-to-Speech (gTTS)**: Used for converting translated text to speech.
- **HTML/CSS/JavaScript**: For the frontend design and interactivity.

## Setup and Installation

### Prerequisites

Before setting up the project locally, make sure you have the following installed:

- Python 3.x
- Django
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**

   ```bash
    git clone https://github.com/wajidkorkani/Text-To-Voice.git
    cd Text-To-Voice/Text_To_Voice
    pip install -r requirements.txt
    python manage.py runserver
    ```