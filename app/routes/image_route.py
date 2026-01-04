from fastapi import APIRouter, HTTPException, status
from app.schemas.image_shcema import ImageGenerationRequest, ImageGenerationResponse
from app.services.image_service import generate_image_from_prompt, ImageGenerationError

router = APIRouter()
@router.post("/generate-image", response_model=ImageGenerationResponse, status_code=status.HTTP_200_OK)
def generate_image_endpoint(request: ImageGenerationRequest):
    try:
        return generate_image_from_prompt(request.text_prompt)

    except ImageGenerationError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate image",
        )