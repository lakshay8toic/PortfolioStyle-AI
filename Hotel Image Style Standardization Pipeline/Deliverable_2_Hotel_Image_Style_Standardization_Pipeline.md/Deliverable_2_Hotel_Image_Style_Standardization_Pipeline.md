# Deliverable 2: Hotel Image Style Standardization Pipeline

**Project Title:** PortfolioStyle AI: Hotel Photo Style Standardizer  
**Module:** Generative AI Group Projects (Self-Paced)  
**Deliverable Type:** Week 2 Milestone Submission  

---

## 1. Pipeline Architecture Overview
Standard text-to-image or naive image-to-image models fail on real-estate and hotel portfolios because they alter structural elements (e.g., changing window positions, turning twin beds into king beds, or altering architectural columns).

To prevent this, **PortfolioStyle AI** designs a dual-conditioned Generative AI workflow:
1. **Generative Backbone:** **Stable Diffusion Inpainting (SD 1.5 / SDXL)** to resynthesize ambient lighting, wall tones, textures, and atmospheric color grading.
2. **Spatial Structural Conditioning:** **ControlNet (Canny / Lineart)** to lock in exact architectural boundaries.

```
[ Input Hotel Photo ] ──┬──> [ ControlNet Canny Preprocessor ] ──> [ Edge Map ]
                         │                                              │
                         │                                              ▼
                         └──> [ Atmosphere / Mask Generator ] ──> [ SD Inpainting Engine ]
                                                                        ▲
                                 [ Prompt: 3200K Luxury Warm Glow ] ────┘
                                                                        │
                                                                        ▼
                                                          [ Standardized Hotel Image ]
```

---

## 2. Model Configuration & Hyperparameters

| Component | Architecture / Setting | Value / Parameter | Purpose |
| :--- | :--- | :--- | :--- |
| **Diffusion Base** | `runwayml/stable-diffusion-inpainting` | Latent Diffusion Model | Generates photorealistic textures and lighting |
| **Conditioning** | `lllyasviel/control_v11p_sd15_canny` | ControlNet v1.1 | Enforces 1:1 structural preservation |
| **ControlNet Scale** | $w_{control}$ | **0.85** | High structural lock prevents furniture drift |
| **Classifier-Free Guidance (CFG)** | $s_{cfg}$ | **7.5** | Balances prompt adherence with photo fidelity |
| **Denoising Strength** | $\eta_{denoise}$ | **0.45 – 0.55** | Sufficient to replace lighting without altering physical objects |
| **Scheduler** | `UniPCMultistepScheduler` | 30 steps | Fast, high-fidelity convergence in ~4 seconds/image |

---

## 3. Style Definition & Prompt Engineering Strategy
A unified hotel brand style was codified using positive and negative prompt engineering templates:

### Target Positive Prompt:
> *"Luxury 5-star hotel interior photography, warm architectural lighting, golden ambient glow 3200K, Architectural Digest editorial style, soft natural shadows, sharp focus, 8k resolution, photorealistic, balanced highlights, premium materials."*

### Negative Prompt (Exclusion Controls):
> *"cold harsh fluorescent lighting, blue tint, washed out, muddy shadows, distorted architecture, mutated furniture, altered window frame, crooked walls, blurry, low resolution, oversaturated, text, watermark."*

---

## 4. Pipeline Execution Script & Reproducibility
The end-to-end Python script is structured modularly in `src/standardization_pipeline.py` and `src/sd_controlnet_pipeline.py`:
- Pure standard library fallback ensures local execution on any system.
- Full GPU-accelerated PyTorch/Diffusers script provides direct deployment to Google Colab with single-command reproducibility.
