from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.question_answering import load_qa_chain
from langchain_core.callbacks import get_usage_metadata_callback

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask Your PDF")
    st.header("Ask your PDF 💬")
    
    # Uploading the PDF file
    pdf = st.file_uploader("Upload your PDF", type = "pdf")
    
    # Extract the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
        )
        chunks = text_splitter.split_text(text)
        
        # Create embeddings
        embeddings = GoogleGenerativeAIEmbeddings(model = "models/gemini-embedding-001")
        knowledge_base = FAISS.from_texts(chunks, embeddings)
        
        # Show user input
        user_question = st.text_input("Ask a question about your PDF.")
        
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            
            llm = ChatGoogleGenerativeAI(model = "gemini-3.7-flash")
            chain = load_qa_chain(llm, chain_type='stuff')
            with get_usage_metadata_callback() as cb:
                response = chain.run(input_documents = docs, question = user_question)
                st.write(response)
            
                st.divider()
                st.write(cb)

if __name__ == '__main__':
    main()