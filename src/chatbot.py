
import streamlit as st
import requests

class Chatbot:
    def __init__(self):
        # Initialise sidebar with Perplexity API key
        self.perplexity_api_key = st.sidebar.text_input('Enter your Perplexity API Key and hit Enter', type="password")

        # Load personal information from a document or define here directly
        self.pronoun = "she"  # Example: Update based on your document
        self.name = "Alice"  # Example: Update based on your document
        self.personal_info = self.load_personal_info("bio.txt")

    def load_personal_info(self, file_path):
        """Load personal information from a text file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            personal_info = file.read()
        return personal_info
    
    def ask_bot(self, input_text):
        # Define the Perplexity AI API URL
        PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"

        # Define the prompt question
        PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {self.name} in his job search by providing recruiters with relevant and concise information. 
        If you do not know the answer, politely admit it and let recruiters know how to contact {self.name} to get more information directly from {self.pronoun}. 
        Don't put "Buddy" or a breakline in the front of your answer. Don't use any formatting styles in your output. 
        Human: {input}
        """

        # Define the headers including the API key
        headers = {
            "Authorization": f"Bearer {self.perplexity_api_key}"
        }

        # Define the data payload for the request, including personal information as context
        data = {
            "model": "pplx-7b-chat",  # Specify the model
            "messages": [
                {"role": "system", "content": PROMPT_QUESTION},
                {"role": "user", "content": self.personal_info + "\n\n" + input_text}
            ]
        }

        # Make the HTTP POST request to Perplexity AI
        response = requests.post(PERPLEXITY_API_URL, headers=headers, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            response_data = response.json()
            # Extract the completion text
            output = response_data.get('choices')[0].get('message').get('content')
            return output
        else:
            return "Sorry, I couldn't fetch a response. Please check your API key and try again."

    def chat(self):
        st.markdown("## Chat With Me Now")
        user_input = st.text_input("After providing your Perplexity API Key on the sidebar, you can send your questions and hit Enter to know more about me from my AI agent, Buddy!", key="input")

        if user_input:
            if not self.perplexity_api_key.startswith('pplx-') and not self.perplexity_api_key == "marcolee":
                st.warning('⚠️ Please enter your Perplexity API key on the sidebar.', icon='⚠️')
            else:
                if self.perplexity_api_key == "marcolee":
                    self.perplexity_api_key = st.secrets["PERPLEXITY_API_KEY"]

                response = self.ask_bot(user_input)
                st.text_area('Response:', value=response, height=100, disabled=True)


if __name__ == '__main__':
    chatbot = Chatbot()
    chatbot.chat()

