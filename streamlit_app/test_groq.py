import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
print(f"API Key found: {'Yes' if api_key else 'No'}")
if api_key:
    print(f"API Key length: {len(api_key)}")
    print(f"API Key start: {api_key[:4]}...")

try:
    print("\nInitializing ChatGroq with llama-3.3-70b-versatile...")
    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.3-70b-versatile",
        temperature=0.7
    )
    
    print("Sending test message...")
    response = llm.invoke("Hello, are you working?")
    print("\n✅ Response received:")
    print(response.content)
    
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
