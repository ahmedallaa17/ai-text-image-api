import os
from typing import Optional
import requests
from app.utils.config import _get_hf_token as get_hf_token


HF_API_TOKEN_ENV = "HF_API_TOKEN"
MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
HF_INFERENCE_URL = (f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}")

def generate_image_bytes(prompt: str) -> bytes:
        token = get_hf_token()

        headers = {"Authorization": f"Bearer {token}","Accept": "image/png",}

        payload = {"inputs": prompt}
        
        response = requests.post(
            HF_INFERENCE_URL,
            headers=headers,
            json=payload,
            timeout=60,
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Hugging Face Inference API error "
                f"(status {response.status_code}): {response.text}"
            )

        return response.content