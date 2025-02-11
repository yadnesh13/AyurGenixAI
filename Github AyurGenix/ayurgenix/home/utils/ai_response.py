import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer (replace with LLaMA 3.1 1B checkpoint if available)
MODEL_NAME = "meta-llama/Llama-3-1B"  # Replace with actual model path if fine-tuned
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load model and tokenizer once to avoid reloading for each request
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(DEVICE)

def generate_ayurvedic_response(user_query: str) -> str:
    """
    Generates an Ayurvedic health response based on the user's query.

    Args:
        user_query (str): User's input message.

    Returns:
        str: AI-generated response.
    """
    try:
        # Tokenize input
        inputs = tokenizer(user_query, return_tensors="pt").to(DEVICE)

        # Generate response
        output_tokens = model.generate(**inputs, max_length=250, temperature=0.7)

        # Decode and return response
        response_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
        return response_text

    except Exception as e:
        return f"Error generating response: {str(e)}"
