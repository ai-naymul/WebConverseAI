# WebConverseAI

WebConverseAI is an AI-powered conversational interface that allows users to chat with websites. By leveraging advanced language models and vector storage, it provides a seamless way to interact with the content of any website through a chat interface.

## Features

- **AI Conversations**: Engage in dynamic conversations with AI about website content.
- **Vector Store**: Utilizes `langchain_chroma` and `GoogleGenerativeAIEmbeddings` to convert website content into a vector store for efficient retrieval.
- **Retriever Chain**: Implements a retrieval chain to fetch relevant information based on the conversation context.

## Installation

To set up the project, follow these steps:

1. Clone the repository.
2. Install the required packages:
    ```pip install -r requirements.txt```

3. Set up your `.env` file with the necessary API keys:
    ```GOOGLE_API_KEY=your_google_api_key_here```

Ensure you have this `.env` file listed in your `.gitignore` to keep your keys secure.

## Usage

To start the application, run:
    ```streamlit run Home.py```


Enter a website URL when prompted, and start chatting with the AI about the website's content.

## Dependencies

- Streamlit
- LangChain (Core, Community, Chroma, Google GenAI)
- BeautifulSoup4
- python-dotenv
- ChromaDB

Refer to `requirements.txt` for the complete list of dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.