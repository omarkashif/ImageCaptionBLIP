# BLIP Fine-Tuned Image Caption Generator

An image captioning application powered by **BLIP (Bootstrapping Language-Image Pre-training)**, fine-tuned on the **Flickr30k dataset**. Built with PyTorch, Hugging Face Transformers, and Gradio to generate natural-language descriptions of uploaded images.

### 🚀 Live Demo

**[Try the Image Caption Generator](https://omarkashif-imagecaption.hf.space/)**

Upload an image and generate a descriptive caption using the fine-tuned model.

### 🛠️ Tech Stack

- **Model:** BLIP (Vision-Language Model)
- **Dataset:** Flickr30k
- **Frameworks:** PyTorch, Hugging Face Transformers
- **Interface:** Gradio
- **Deployment:** Hugging Face Spaces

### ⚡ Quick Start

```bash
git clone https://github.com/omarkashif/ImageCaptionBLIP.git
cd ImageCaptionBLIP
pip install -r requirements.txt
python app.py
```

The Gradio interface will launch locally in your browser.

### 🔍 How It Works

1. **Image Upload:** Users upload an image through the Gradio interface.
2. **Preprocessing:** The BLIP processor prepares the image for inference.
3. **Caption Generation:** The fine-tuned BLIP model generates a natural-language caption using beam search.
4. **Output:** The generated caption is displayed in the interface.

### 🤗 Model

The model is fine-tuned on Flickr30k and hosted on Hugging Face:

**[omarkashif/blip-finetuned-flickr30k](https://huggingface.co/omarkashif/blip-finetuned-flickr30k)**

### 💻 Hardware

Supports GPU acceleration when available, with automatic fallback to CPU inference.
