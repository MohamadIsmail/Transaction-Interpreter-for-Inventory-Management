# AI-powered Transaction Interpreter for Inventory Management

This is a Streamlit app for demonstrating text classification and parameter extraction using large language models (LLMs).

## Overview

This demo showcases the capabilities of LLMs in two main tasks:

1. **Text Classification**: Classifying input text into predefined categories or labels.
2. **Parameter Extraction**: Extracting relevant parameters or entities from input text.

Users can input text prompts, and the app will utilize pre-trained models to classify the text and extract parameters accordingly.

## Setup

1. **Clone the Repository**: Clone this repository to your local machine.

    ```
    git clone https://github.com/MohamadIsmail/Transaction-Interpreter-for-Inventory-Management.git
    ```

2. **Install Dependencies**: Install the required Python packages using pip.

    ```
    pip install -r requirements.txt
    ```

3. **Run the App**: Start the Streamlit app by running the following command:

    ```
    streamlit run app.py
    ```

4. **Access the App**: Open your web browser and navigate to the URL provided by Streamlit to access the app.

## Usage

1. **Input Text Prompt**: Enter your text prompt into the provided text input box.
2. **Analyze**: Click the "Analyze" button to trigger the text classification and parameter extraction.
3. **View Results**: The app will display the classification result and parameter extraction result.

## Models

1. Replace the placeholders `classification_model` and `question_answering_model` in the `app.py` script with the actual imports of your text classification and parameter extraction models.
2. Replace the placeholder 'api_token' with your personal token.
## Deployment

You can deploy this Streamlit app to various hosting services such as Heroku or Streamlit Sharing.

## Credits

This demo was created by Mohamed Ismail.

## License

This project is licensed under the [MIT License](LICENSE).
