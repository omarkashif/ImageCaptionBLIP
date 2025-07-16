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

Open the link Gradio prints in your terminal, upload an image, and enjoy the caption!

## **How it works**

Model – BLIP fine‑tuned on the Flickr30k captions dataset.

Interface – Simple upload‑and‑caption flow built with Gradio.

Hardware – Runs on GPU if available, otherwise falls back to CPU.

## **Requirements**

Python ≥ 3.9

torch • transformers • gradio • pillow
(They’re all listed in requirements.txt.)


@inproceedings{li2022blip,
  title={Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation},
  author={Li, Junnan and Li, Dongxu and Xiong, Caiming and Hoi, Steven},
  booktitle={International conference on machine learning},
  pages={12888--12900},
  year={2022},
  organization={PMLR}
}
