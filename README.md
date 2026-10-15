# Ask Your PDF 💬

An AI-powered PDF Question-Answering Chatbot built with **Python, Streamlit, LangChain, Google Gemini, and FAISS**. Upload a PDF document and ask questions about its content to receive AI-generated answers based on relevant text from the document.

🚀 **Live Demo:** [Chat with Your PDF Chatbot](https://chat-with-your-pdf-chatbot.streamlit.app/)

## Features

- **PDF Upload:** Upload PDF documents directly through the web interface.
- **Text Extraction:** Extract text from PDF pages using PyPDF2.
- **Text Chunking:** Split extracted text into manageable chunks with overlapping content.
- **Semantic Search:** Generate embeddings using Google's Gemini embedding model and retrieve relevant text using FAISS.
- **AI-Powered Answers:** Use Google Gemini to answer questions based on retrieved document content.
- **Token Usage Tracking:** Display usage metadata returned by LangChain's callback.

## Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM:** Google Gemini (`gemini-3.7-flash`)
- **Embeddings:** Google Gemini (`models/gemini-embedding-001`)
- **Framework:** LangChain
- **Vector Store:** FAISS
- **PDF Processing:** PyPDF2
- **Environment Variables:** python-dotenv

## How It Works

1. Upload a PDF document.
2. Extract text from its pages.
3. Split the extracted text into chunks of 1,000 characters with 200 characters of overlap.
4. Generate embeddings for the chunks.
5. Store the embeddings in a FAISS vector store.
6. Enter a question about the PDF.
7. Retrieve relevant chunks using similarity search.
8. Pass the retrieved text and question to Google Gemini to generate an answer.
9. Display the answer and token usage metadata.

## Project Structure

```text
ask-your-pdf/
├── app.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/gandharvk422/ask-your-pdf.git
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your Google API Key

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Replace the placeholder with your actual Google API key.

**Security:** Never commit your `.env` file or expose your API key publicly. For Streamlit Community Cloud, configure the key using the app's Secrets settings.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## Usage

1. Open the [live application](https://chat-with-your-pdf-chatbot.streamlit.app/).
2. Upload a PDF document.
3. Enter a question about the document.
4. Read the AI-generated answer.
5. Review the displayed usage metadata.

## Important Notes

- A valid Google API key is required.
- Answers depend on the text extracted from the PDF and the relevant chunks retrieved by similarity search.
- Scanned PDFs without extractable text may require OCR preprocessing.
- The application creates a FAISS vector store from the uploaded document during processing.

## Future Improvements

- Support multiple PDF documents.
- Add conversation history and follow-up questions.
- Improve support for scanned PDFs using OCR.
- Display relevant source passages alongside answers.
- Cache embeddings and retrieval results where appropriate.
- Add error handling for invalid PDFs and API failures.

## License

No license has been specified for this project yet.
