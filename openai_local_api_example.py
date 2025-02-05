from openai import OpenAI

# Configure the client to use Ollama's local endpoint
client = OpenAI(
    base_url="http://localhost:11434/v1",  # Ollama server address
    api_key="no-api-key-needed",  # Ollama doesn't require an API key
)


# Example chat completion with deepseek-r1:1.5b
def get_model_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="deepseek-r1:1.5b",  # Specify the model you host in Ollama
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content
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
