# PortfolioStyle AI: Hotel Photo Style Standardizer

An AI-powered hotel photography standardization system developed for hotel chains to establish a cohesive, luxury visual identity across multi-property portfolios. Utilizes **Stable Diffusion Inpainting** and **ControlNet** to harmonize lighting, color temperature, and ambiance while strictly preserving architectural and room structures.

---

## 📁 Repository Structure

```
PortfolioStyle-AI/
├── data/
│   ├── raw/                 # Input hotel photos (Lobby, Deluxe Room, Exterior, Poolside)
│   └── processed/           # Statistical analysis JSON logs
├── src/
│   ├── generate_sample_dataset.py   # Dataset creation helper
│   ├── dataset_analysis.py          # Week 1: Image statistics, luminance & tone analysis
│   ├── standardization_pipeline.py  # Standalone runnable pipeline & comparison generator
│   └── sd_controlnet_pipeline.py    # Week 2: Full PyTorch/Diffusers ControlNet inpainting
├── notebooks/
│   └── PortfolioStyle_AI_Pipeline.ipynb # Interactive Jupyter Notebook (Google Colab ready)
├── deliverables/
│   ├── Deliverable_1_Hotel_Image_Dataset_Preparation_Report.md
│   ├── Deliverable_2_Hotel_Image_Style_Standardization_Pipeline.md
│   ├── Deliverable_3_Standardized_Hotel_Image_Portfolio.md
│   └── Deliverable_4_Final_PortfolioStyle_AI_Project_Report.md
├── outputs/
│   ├── standardized/        # Processed standardized photos
│   └── comparisons/         # Before & After side-by-side comparison images
└── docs/
    └── TEACHER_EXPLANATION_GUIDE.md # Simple question & answer guide for viva/presentation
```

---

## 🚀 Quickstart

### 1. Run Statistical Dataset Analysis (Week 1)
```bash
python3 src/dataset_analysis.py
```

### 2. Run Image Standardization Pipeline (Weeks 2 & 3)
```bash
python3 src/standardization_pipeline.py
```
This processes all raw property photos and saves the standardized outputs and comparisons into `outputs/`.

### 3. Open in Jupyter or Google Colab
Open `notebooks/PortfolioStyle_AI_Pipeline.ipynb` in VS Code, JupyterLab, or upload to Google Colab.

---

## 📊 Deliverables Mapping (MySkillWallet Portal)

1. **#1 Hotel Image Dataset Preparation Report:** [Deliverable 1](file:///Users/lakshay/.gemini/antigravity/scratch/PortfolioStyle-AI/deliverables/Deliverable_1_Hotel_Image_Dataset_Preparation_Report.md)
2. **#2 Hotel Image Style Standardization Pipeline:** [Deliverable 2](file:///Users/lakshay/.gemini/antigravity/scratch/PortfolioStyle-AI/deliverables/Deliverable_2_Hotel_Image_Style_Standardization_Pipeline.md)
3. **#3 Standardized Hotel Image Portfolio:** [Deliverable 3](file:///Users/lakshay/.gemini/antigravity/scratch/PortfolioStyle-AI/deliverables/Deliverable_3_Standardized_Hotel_Image_Portfolio.md)
4. **#4 Final PortfolioStyle AI Project Report:** [Deliverable 4](file:///Users/lakshay/.gemini/antigravity/scratch/PortfolioStyle-AI/deliverables/Deliverable_4_Final_PortfolioStyle_AI_Project_Report.md)
