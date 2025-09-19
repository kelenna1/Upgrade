import os
import sys
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_URL = "https://openrouter.ai/api/v1/chat/completions"  # Fixed: Added the correct endpoint
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in your .env file")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def ask(question: str) -> str:
    """
    Send a question to the OpenRouter API and return the model's response.
    """
    data = {
        "model": "openai/gpt-3.5-turbo",  # Changed to a more reliable model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
    }
    
    try:
        print(f"Sending request to: {API_URL}")  # Debug print
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        
        # Debug prints
        print(f"Status code: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        print(f"Raw response: {response.text[:200]}...")  # First 200 chars
        
        response.raise_for_status()
        
        # Check if response is empty
        if not response.text.strip():
            return "Error: Empty response from API"
        
        try:
            result = response.json()
        except ValueError as json_error:
            return f"JSON parsing error: {json_error}. Response: {response.text[:200]}"
        
        # Check if the expected structure exists
        if "choices" not in result or not result["choices"]:
            return f"Unexpected response structure: {result}"
        
        return result["choices"][0]["message"]["content"].strip()
        
    except requests.exceptions.HTTPError as e:
        return f"HTTP error {response.status_code}: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"
    except (KeyError, IndexError) as e:
        return f"Response parsing error: {e}. Response: {response.text[:200]}"

if __name__ == "__main__":  # Fixed: Double underscores
    # If a question is passed from terminal, use it; otherwise use default
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = "What is the capital of France?"
    
    answer = ask(question)
    print("\nQuestion:", question)
    print("Answer:", answer)