# CryptoWhiz Chat

Welcome to **CryptoWhiz**, your personal chat assistant for cryptocurrency-related inquiries! This Streamlit application allows users to interact with a language model to get insights and answers related to cryptocurrencies.

## Features

- **User Authentication**: Enter your username to start chatting.
- **Interactive Chat Interface**: Ask questions and receive responses from the CryptoWhiz agent.
- **Persistent Chat History**: Your queries and the agent's responses are stored for the current session.

## Requirements

To run this application, you need to have the following installed:

- Python 3.7 or higher
- Streamlit

All required libraries are listed in the `requirements.txt` file. You can install them using pip:

```bash
pip install -r requirements.txt
```

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Dhiraj223/CryptoInfluencer
   cd CryptoInfluencer
   ```

2. Install the required packages if you haven't done so already:

   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run streamlit-ui/app.py
   ```

4. Open your web browser and navigate to the URL provided in the terminal (usually `http://localhost:8501`).

## Usage

- Upon opening the app, you will see a sidebar to enter your username.
- Once you enter your username, type your query in the text input box.
- Click the **Send** button to receive a response from the CryptoWhiz agent.
- Type "quit" to exit the chat.