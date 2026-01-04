import os
HF_API_TOKEN_ENV = "HF_API_TOKEN"


def _get_hf_token() -> str:
    """
    Retrieve Hugging Face API token from environment variables.
    """
    token = os.getenv(HF_API_TOKEN_ENV)
    if not token:
        raise RuntimeError(
            "Hugging Face API token not found. "
            "Please set HF_API_TOKEN environment variable."
        )
    return token