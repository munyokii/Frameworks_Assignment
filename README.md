# 📊 CORD-19 Metadata Explorer

This project provides a simple end-to-end pipeline for exploring the **CORD-19 metadata dataset** using **Python, Pandas, Matplotlib, and Streamlit**.  

It includes:
- **Data Loading and Exploration**  
- **Data Cleaning and Preparation**  
- **Analysis and Visualization**  
- **Interactive Streamlit App**  
- **Documentation & Reflection**

---

## 🚀 Features
- Load and clean `metadata.csv` from the CORD-19 dataset
- Explore research publications by year, journal, and source
- Generate visualizations:
  - 📈 Publications per year  
  - 📊 Top journals publishing COVID-19 research  
  - ☁️ Word cloud of paper titles  
  - 📦 Distribution of papers by source
- Interactive **Streamlit web app** for filtering and visualizing the dataset

---

## 📥 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/munyokii/Frameworks_Assignment.git
cd Frameworks_Assignment
```

### 2. Create a Virtual Environment (recommended)
```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
---

## 📊 Usage

### Run Python Script (Analysis & Visualizations)
```bash
python cord19.py
```
This runs the pipeline (load → clean → analyze → save visualizations). Don't forget to uncomment the function calls

### Run Streamlit App (Interactive Dashboard)
```bash
streamlit run cord19.py
```
This launches the interactive **CORD-19 Data Explorer** in your browser.

---

## 🗂 Data
- You can use my sample data in data directory or 
- Download the [CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)  
- Place it in the project data directory then run the application.

---

## 📝 Reflection

- The dataset contains **many missing values**, especially in `abstract`.  
- **Cleaning** is necessary to ensure accurate results.  
- **Year extraction** allows easy time-series analysis.  
- **Word clouds** provide quick insights into research themes.  
- **Streamlit** makes it easy to share findings interactively.  
- Challenge: The dataset is **large**, so sampling or filtering may be required for performance.

---
