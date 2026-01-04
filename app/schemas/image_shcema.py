from pydantic import BaseModel, Field

class ImageGenerationRequest(BaseModel):
    text_prompt: str = Field(..., description="The text prompt to generate the image from",min_length=1)

class ImageGenerationResponse(BaseModel):
    encoded_image: str
    mime_type: str