import streamlit as st
import openai
from scripts.constant import *
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI

class Chatbot:
    def __init__(self):
        # Initialise sidebar with openai API key
        self.openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
        openai.api_key = (self.openai_api_key)

        # Personal information
        self.documents = SimpleDirectoryReader(input_files=["bio.txt"]).load_data()
        self.pronoun = info["Pronoun"]
        self.name = info["Name"]

    def ask_bot(self, input_text):
        # define LLM
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0,
            openai_api_key=openai.api_key,
        )
        llm_predictor = LLMPredictor(llm=llm)
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
        
        # load index
        index = GPTVectorStoreIndex.from_documents(self.documents, service_context=service_context)    
        
        # query LlamaIndex and GPT-3.5 for the AI's response
        PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {self.name} in her job search by providing recruiters with relevant and concise information. 
        If you do not know the answer, politely admit it and let recruiters know how to contact {self.name} to get more information directly from {self.pronoun}. 
        Don't put "Buddy" or a breakline in the front of your answer.
        Human: {input}
        """
        
        output = index.as_query_engine().query(PROMPT_QUESTION.format(input=input_text))
        print(f"output: {output}")
        return output.response

    # get the user's input by calling the get_text function
    def get_text(self):
        input_text = st.text_input("After providing OpenAI API Key on the sidebar, you can send your questions and hit Enter to know more about me from my AI agent, Buddy!", key="input")
        return input_text

    def chat(self):
        st.markdown("Chat With Me Now")
        user_input = self.get_text()

        if user_input:
            text = st.text_area('Enter your questions')
        if not self.openai_api_key.startswith('sk-'):
            st.warning('⚠️Please enter your OpenAI API key on the sidebar.', icon='⚠')
        if self.openai_api_key.startswith('sk-'):
            st.info(self.ask_bot(user_input))
