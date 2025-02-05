from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

# Configure the Ollama client to use local endpoint
llm = ChatOllama(
    base_url="http://localhost:11434",  # Ollama server address
    model="deepseek-r1:1.5b",  # Specify the model you host in Ollama
)


def get_model_response(prompt: str) -> str:
    try:
        messages = [HumanMessage(content=prompt)]
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    prompt = "Explain quantum computing to 10 year old students"
    response = get_model_response(prompt)
    if response:
        print("Model Response:")
        print(response)
