import os
from google import genai
from dotenv import load_dotenv

# Initialize environment variables for secure credential management
load_dotenv()

# Securely fetch API key from local .env environment
API_KEY = os.getenv("GEMINI_API_KEY")

# Priority model list
# Includes automated failover logic to ensure high availability
GEMINI_MODELS = [
    "gemini-3.1-flash-lite-preview", 
    "gemini-3.1-flash", 
    "gemini-2.0-flash-lite", 
    "gemini-2.5-flash-lite", 
    "gemini-flash-lite-latest"
]

# Optimized medical assistant prompt for patient-centric simplification
PROMPT = """You are a medical assistant. Simplify this medical text for a non-medical person.
Use reassuring language, highlight abnormal values, and provide 3-4 lifestyle suggestions.
Output format: # 📋 Summary, # ⚠️ Key Findings, # 💡 Suggestions."""

def stream_analysis(text):
    """
    Leverages Gemini LLM to process and simplify medical jargon.
    
    Args:
        text: The raw OCR text extracted from the medical document.
        
    Yields:
        str: Streamed tokens of the simplified report.
    """
    if not API_KEY:
        yield "❌ Configuration Error: GEMINI_API_KEY not found in .env."
        return

    # Initialize the Gemini client
    client = genai.Client(api_key=API_KEY)
    success = False
    
    # Failover loop: If one model is busy or fails, try the next generation model
    for model in GEMINI_MODELS:
        try:
            # Native streaming for responsive 'typewriter' effect in the UI
            for chunk in client.models.generate_content_stream(model=model, contents=[PROMPT, text]):
                if chunk.text:
                    yield chunk.text
            success = True
            break # Exit loop once successful generation is completed
        except Exception:
            # Log failure silently and attempt the next model in the priority list
            continue
            
    if not success:
        yield "❌ Medical Analysis Service is currently unavailable. Please check connectivity."
