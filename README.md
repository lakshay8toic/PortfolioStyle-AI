# PortfolioStyle AI: Hotel Photo Style Standardizer

An AI-powered hotel photography standardization system developed for hotel chains to establish a cohesive, luxury visual identity across multi-property portfolios. Utilizes **Stable Diffusion Inpainting** and **ControlNet** to harmonize lighting, color temperature, and ambiance while strictly preserving architectural and room structures.

---

## 🌐 Live Interactive Website

👉 **[Click Here to Open Live Website](https://lakshay8toic.github.io/PortfolioStyle-AI/)**

Experience the live interactive standardization pipeline, explore before-and-after results across hotel categories, and inspect 1:1 structural edge preservation.

---

## ⚡ One-Click Local Web App

You can run and explore the full interactive visual UI locally in just **one click**:

```bash
# Option 1: Run the executable launcher
./run_app.sh

# Option 2: Or directly with python
python3 app.py
```
This automatically starts the local server and opens **`http://localhost:8000`** in your default web browser!

---

## 📁 Repository Structure

```
PortfolioStyle-AI/
├── app.py                           # One-click web server & browser launcher
├── run_app.sh                       # Double-clickable shell launcher
├── index.html                       # Modern dark-mode UI with live comparisons
├── data/
│   ├── raw/                         # Input hotel photos (Lobby, Deluxe Room, Exterior, Poolside)
│   └── processed/                   # Statistical analysis JSON logs
├── src/
│   ├── generate_sample_dataset.py   # Dataset creation helper
│   ├── dataset_analysis.py          # Week 1: Image statistics, luminance & tone analysis
│   ├── standardization_pipeline.py  # Standalone runnable pipeline & comparison generator
│   ├── sd_controlnet_pipeline.py    # Week 2: Full PyTorch/Diffusers ControlNet inpainting
│   └── convert_bmp_to_png.py        # Web asset converter
├── notebooks/
│   └── PortfolioStyle_AI_Pipeline.ipynb # Interactive Jupyter Notebook (Google Colab ready)
├── deliverables/
│   ├── Deliverable_1_Hotel_Image_Dataset_Preparation_Report.md
│   ├── Deliverable_2_Hotel_Image_Style_Standardization_Pipeline.md
│   ├── Deliverable_3_Standardized_Hotel_Image_Portfolio.md
│   └── Deliverable_4_Final_PortfolioStyle_AI_Project_Report.md
├── outputs/
│   ├── standardized/                # Processed standardized photos
│   └── comparisons/                 # Before & After side-by-side comparison images
└── docs/
    └── TEACHER_EXPLANATION_GUIDE.md # Simple question & answer guide for viva/presentation
```

---

## 📊 Deliverables Mapping (MySkillWallet Portal)

1. **#1 Hotel Image Dataset Preparation Report:** [Deliverable 1](deliverables/Deliverable_1_Hotel_Image_Dataset_Preparation_Report.md)
2. **#2 Hotel Image Style Standardization Pipeline:** [Deliverable 2](deliverables/Deliverable_2_Hotel_Image_Style_Standardization_Pipeline.md)
3. **#3 Standardized Hotel Image Portfolio:** [Deliverable 3](deliverables/Deliverable_3_Standardized_Hotel_Image_Portfolio.md)
4. **#4 Final PortfolioStyle AI Project Report:** [Deliverable 4](deliverables/Deliverable_4_Final_PortfolioStyle_AI_Project_Report.md)
