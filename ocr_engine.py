import ollama

# Configuration for the vision model
# We use glm-ocr for high-accuracy local medical text extraction
OCR_MODEL = 'glm-ocr:latest'

# Optimized parameters for low-latency recognition
MODEL_OPTIONS = {
    'num_ctx': 16384,
    'temperature': 0,
    'num_predict': 4096,
    'repeat_penalty': 1.1,
    'top_p': 0.00001
}

def stream_ocr(image_bytes):
    """
    Performs Local OCR via Ollama.
    
    Args:
        image_bytes: The raw bytes of the uploaded medical document.
        
    Yields:
        str: Chunks of recognized text for real-time UI streaming.
    """
    try:
        # Initializing local chat session with vision capabilities
        response = ollama.chat(
            model=OCR_MODEL,
            messages=[{
                'role': 'user', 
                'content': 'Text Recognition:', 
                'images': [image_bytes]
            }],
            options=MODEL_OPTIONS,
            stream=True
        )
        
        # Iterating through streaming chunks from the local model
        for chunk in response:
            if 'message' in chunk and 'content' in chunk['message']:
                yield chunk['message']['content']
                
    except Exception as e:
        # Graceful error handling for local service interruptions
        yield f"OCR Engine Error: Ensure Ollama service is active. Details: {e}"
