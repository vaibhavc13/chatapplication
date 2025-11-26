# GrokChatX 🤖

A modern, powerful AI chat application built with **Python** and **Streamlit**.

GrokChatX provides a unified interface to interact with multiple AI providers, including **Grok (xAI)** and **HuggingFace**, with a focus on privacy, ease of use, and a clean UI.

![GrokChatX Demo](https://via.placeholder.com/800x400?text=GrokChatX+Streamlit+UI)

## ✨ Features

- **Multi-Provider Support**: 
  - **Groq** (Llama 3.3 70B)
- **Secure API Key Management**:
  - Keys are loaded from `.env` file
  - Never exposed in the UI or logs
- **Chat History**:
  - Persistent conversation history using SQLite
  - Create new chats, switch between chats, and delete old ones
- **Clean UI**:
  - Built with Streamlit for a responsive, dark-mode friendly interface
  - Real-time feedback and loading states

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- API Keys for [Groq](https://console.groq.com/keys) and/or [HuggingFace](https://huggingface.co/settings/tokens)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/GrokChatX.git
    cd GrokChatX
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r streamlit_app/requirements.txt
    ```

3.  **Run the application**:
    ```bash
    python -m streamlit run streamlit_app/app.py
    ```

## ⚙️ Configuration

### API Keys

Configure your API keys using a `.env` file:

1.  Navigate to the `streamlit_app` directory.
2.  Create a `.env` file (or copy from `.env.example`).
3.  Add your keys:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    HF_API_KEY=your_hf_key_here
    ```
4.  Restart the app - keys will be loaded automatically.

> **Get API Keys:**
> - Groq: https://console.groq.com/keys
> - HuggingFace: https://huggingface.co/settings/tokens

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Framework**: [LangChain](https://langchain.com/)
- **Database**: SQLite
- **Models**: Groq (Llama 3.3), HuggingFace (Gemma 2)

## 📂 Project Structure

```
GrokChatX/
├── streamlit_app/
│   ├── app.py              # Main application entry point
│   ├── ai_service.py       # AI provider routing logic
│   ├── db_service.py       # Database management
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # Example environment variables
└── README.md               # Documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
