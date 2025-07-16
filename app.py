import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load fine-tuned model from HF Hub
model = BlipForConditionalGeneration.from_pretrained("omarkashif/blip-finetuned-flickr30k").to(device)
processor = BlipProcessor.from_pretrained("omarkashif/blip-finetuned-flickr30k")

def generate_caption(image):
    image = image.convert("RGB")
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        output = model.generate(**inputs, max_length=40, num_beams=5)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

# Gradio UI
gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="BLIP Fine-Tuned Caption Generator",
    description="Upload an image to generate a caption using a BLIP model fine-tuned on Flickr30k."
).launch()
