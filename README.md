# DeepSeek-R1-local-API-in-Action

This repository demonstrates how to use the DeepSeek-R1 language model locally through Ollama, leveraging both the OpenAI and LangChain libraries.

## Prerequisites

- [Ollama](https://ollama.ai/) installed on your system

## Setup Instructions

1. Install Ollama
   ```bash
   # For macOS M series
   Download from https://ollama.com/download
   
   # For Linux
   curl https://ollama.ai/install.sh | sh
   ```

2. Pull and Run the DeepSeek-R1 Model
   ```bash
   ollama run deepseek-r1:1.5b
   ```

   for other models, you can find here: [https://ollama.com/library/deepseek-r1](https://ollama.com/library/deepseek-r1)
   

3. Set up Python Environment
   ```bash
   # Create and activate virtual environment
   python3.12 -m venv .venv
   source .venv/bin/activate
   
   # Install requirements
   pip install -r requirements.txt
   ```

## Usage Examples

### 1. Using OpenAI Library
The `openai_local_api_example.py` demonstrates how to use the OpenAI library with locally hosted DeepSeek-R1

```bash
python openai_local_api_example.py
```

### 2. Using LangChain Library
The `langchain_local_api_example.py` demonstrates how to use the LangChain library with locally hosted DeepSeek-R1

```bash
python langchain_local_api_example.py
```
