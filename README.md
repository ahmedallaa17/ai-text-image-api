# 🖼️ AI Text-to-Image API

A clean, production-ready **Text-to-Image REST API** built with **FastAPI** and powered by **Hugging Face Inference API (SDXL)**.

This project demonstrates a proper backend architecture for AI services, with clear separation of concerns, secure configuration, and extensible design.

---

## 🚀 Features

* Generate images from text prompts using Stable Diffusion XL
* Clean **layered architecture** (client / service / route)
* Secure API token handling via environment variables
* Swagger UI for easy testing
* JSON response with Base64-encoded images
* Hugging Face **Inference API** (no local models, no Spaces)

---

## 🧱 Project Architecture

```
ai-text-image-api/
├── app/
│   ├── clients/
│   │   └── huggingface_client.py
│   ├── services/
│   │   └── image_service.py
│   ├── routes/
│   │   └── image_routes.py
│   ├── schemas/
│   │   └── image.py
│   ├── config/
│   │   └── settings.py
│   └── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Layer Responsibilities

* **Client**
  Handles communication with Hugging Face Inference API only.

* **Service**
  Contains business logic (image generation, base64 conversion, error wrapping).

* **Routes**
  Exposes HTTP endpoints and maps service errors to HTTP responses.

* **Schemas**
  Input validation and response models.

---

## 🛠️ Tech Stack

* **Python 3.12**
* **FastAPI**
* **Hugging Face Inference API**
* **Stable Diffusion XL**
* **Requests**
* **Pydantic**

---

## 🔐 Environment Variables

The API token is **never hardcoded**.

Set your Hugging Face token as an environment variable:

```bash
export HF_API_TOKEN=hf_xxxxxxxxxxxxxxxxx
```

Make sure it is available in the same terminal where you run the server.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ai-text-image-api.git
cd ai-text-image-api

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

## ▶️ Running the Server

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Usage

### Endpoint

`POST /generate-image`

### Request Body

```json
{
  "prompt": "A cinematic photo of a futuristic city at sunset"
}
```

### Response (200 OK)

```json
{
  "image_base64": "iVBORw0KGgoAAAANSUhEUgAA...",
  "mime_type": "image/png"
}
```

The image is returned as **raw Base64**, making the API frontend-agnostic.

---

## ⚠️ Error Handling

* If image generation fails, the API returns:

  * `500 Internal Server Error`
  * Message: `"Failed to generate image"`

Errors from Hugging Face are safely wrapped and not exposed directly.

---

## 👤 Author

**Eng / Ahmed Alaa Mohamed**


