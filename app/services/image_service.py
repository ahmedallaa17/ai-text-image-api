from app.clients.huggingface_client import generate_image_bytes
import base64

class ImageGenerationError(Exception):
    """
    Raised when image generation fails at the service level.
    """
    pass

def generate_image_from_prompt(prompt: str) -> dict:
    try:
        image_bytes = generate_image_bytes(prompt)
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')
        return {"encoded_image": encoded_image,
                "mime_type": "image/png"}
    except Exception as e:
        raise ImageGenerationError(f"Failed to generate image: {str(e)}")