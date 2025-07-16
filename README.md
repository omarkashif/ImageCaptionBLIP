# BLIP Fine‑Tuned Caption Generator

A tiny Gradio demo that turns any image into a descriptive caption using a **BLIP model fine‑tuned on Flickr30k** (`omarkashif/blip-finetuned-flickr30k`).

---

## Quick start

```bash
git clone https://github.com/omarkashif/ImageCaptionBLIP.git
cd ImageCaptionBLIP
pip install -r requirements.txt     # installs torch, transformers, gradio, pillow …
python app.py                       # launches the Gradio app
```

## **How it works**

Model – BLIP fine‑tuned on the Flickr30k captions dataset.

Interface – Simple upload‑and‑caption flow built with Gradio.

Hardware – Runs on GPU if available, otherwise falls back to CPU.




