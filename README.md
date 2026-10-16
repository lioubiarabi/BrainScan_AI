# BrainScan_AI: Deep Learning MRI Brain Tumor Classification

BrainScan_AI is an end-to-end medical computer vision project designed to detect and classify brain tumors from magnetic resonance imaging (MRI) scans. The system categorizes scans into four distinct diagnostic classes:
- **Glioma**
- **Meningioma**
- **Pituitary**
- **No Tumor**

---

## 📁 Project Architecture

```
BrainScan_AI/
├── data/
│   ├── raw/                  # Raw MRI image directories per class
│   │   ├── glioma/
│   │   ├── meningioma/
│   │   ├── notumor/
│   │   └── pituitary/
│   └── processed/            # Processed artifacts (dataset_splits.npz)
├── notebooks/
│   └── exploratory_eda.ipynb # Data exploration, preprocessing & splitting
├── src/
│   ├── __init__.py
│   └── data_loader.py        # Dataset scanning and path extraction
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules for datasets & environments
└── README.md                 # Project documentation
```

---

## 📊 Dataset Overview

The dataset contains **7,023** MRI scans distributed across four classes:
- **Glioma**: Malignant primary brain tumors originating in glial cells
- **Meningioma**: Typically benign tumors arising from meningeal coverings
- **Pituitary**: Tumors located in the pituitary gland region
- **No Tumor**: Healthy brain MRI control group

---

## ⚙️ Data Preprocessing Pipeline

The pipeline implemented in [`notebooks/exploratory_eda.ipynb`](notebooks/exploratory_eda.ipynb) performs:
1. **Dynamic Resizing & Color Normalization**:
   - Resizes all scans to a uniform dimension of `224 × 224`.
   - Converts OpenCV BGR images to RGB.
   - Applies adaptive interpolation (`cv2.INTER_AREA` for downsampling, `cv2.INTER_LINEAR` for upsampling).
   - Scales pixel intensities to `[0.0, 1.0]`.
2. **Label Encoding**: Categorical targets are converted into integer indices `(0–3)` using `scikit-learn.LabelEncoder`.
3. **Stratified Splitting**: 80/20 train/test split preserving exact class ratios (`stratify=y`).
4. **Compressed Export**: Exports `X_train`, `X_test`, `y_train`, `y_test` into `data/processed/dataset_splits.npz`.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/lioubiarabi/BrainScan_AI.git
cd BrainScan_AI
```

### 2. Set up the Python environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux / macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Run Exploratory Data Analysis & Preprocessing
Launch Jupyter Notebook to view or re-run the pipeline:
```bash
jupyter notebook notebooks/exploratory_eda.ipynb
```
