# 💳 Credit Card Fraud Detection System

> **Machine learning–powered fraud detection** — from exploratory analysis to a live prediction web app.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

---

## 🎯 Why This Project Matters

Credit card fraud costs the global economy **billions of dollars every year**. Real-world fraud datasets are extremely imbalanced — in this project, fraudulent transactions make up only **0.17%** of all records. Building a model that works on such skewed data is a core challenge in applied machine learning and fintech.

This project demonstrates an **end-to-end ML workflow**: data exploration, handling class imbalance, model training, evaluation, and deployment behind a simple web interface.

---

## ✨ Highlights

| What I Built | Why It Stands Out |
|---|---|
| **Full ML pipeline** | Load → explore → balance → train → evaluate → deploy |
| **Imbalanced data handling** | Random undersampling to create a balanced training set |
| **Logistic Regression model** | Interpretable baseline with strong test performance |
| **Interactive Streamlit app** | Real-time fraud/legitimate predictions from user input |
| **Jupyter notebook** | Documented EDA and step-by-step model development |

---

## 📊 Results at a Glance

| Metric | Score |
|---|---|
| **Training Accuracy** | ~95.7% |
| **Test Accuracy** | ~94.4% |
| **Dataset Size** | 284,807 transactions |
| **Fraud Cases** | 492 (0.17%) |
| **Features** | 30 (Time, V1–V28, Amount) |

---

## 🛠️ Tech Stack

```
Python · Pandas · NumPy · scikit-learn · Streamlit · Jupyter Notebook
```

- **Data & Analysis** — Pandas, NumPy  
- **Machine Learning** — scikit-learn (Logistic Regression, train/test split, accuracy metrics)  
- **Deployment** — Streamlit web application  
- **Documentation** — Jupyter notebook with EDA and model walkthrough  

---

## 🔄 Project Workflow

```mermaid
flowchart LR
    A[📁 creditcard.csv] --> B[🔍 EDA & Data Cleaning]
    B --> C[⚖️ Undersampling]
    C --> D[📐 Train / Test Split]
    D --> E[🤖 Logistic Regression]
    E --> F[📈 Model Evaluation]
    F --> G[🌐 Streamlit App]
```

1. **Explore** — Inspect 284K+ transactions, check missing values, analyze class distribution  
2. **Balance** — Undersample legitimate transactions to match fraud count  
3. **Train** — Fit Logistic Regression on 80% of balanced data (stratified split)  
4. **Evaluate** — Measure accuracy on held-out test set  
5. **Deploy** — Serve predictions through a Streamlit UI  

---

## 📁 Project Structure

```
CREDIT CARD FRAUD DETECTION SYSTEM WITH ML/
│
├── creditcard.csv                                          # Dataset
├── Credit Card Fraud Detection using Machine Learning-checkpoint.ipynb
│                                                           # EDA + model development
├── app.py                                                  # Streamlit web application
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher  
- `pip` package manager  

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/CREDIT-CARD-FRAUD-DETECTION-SYSTEM-WITH-ML.git
cd "CREDIT CARD FRAUD DETECTION SYSTEM WITH ML"

# Install dependencies
pip install pandas numpy scikit-learn streamlit jupyter
```

### Run the Web App

```bash
streamlit run app.py
```

Open the URL shown in your terminal (usually `http://localhost:8501`) to use the fraud detection interface.

### Explore the Notebook

```bash
jupyter notebook "Credit Card Fraud Detection using Machine Learning-checkpoint.ipynb"
```

---

## 🧠 Skills Demonstrated

- **Exploratory Data Analysis (EDA)** — dataset profiling, class imbalance analysis  
- **Feature Engineering Awareness** — working with PCA-transformed features (V1–V28)  
- **Imbalanced Classification** — undersampling strategy for skewed labels  
- **Model Training & Validation** — stratified train/test split, accuracy evaluation  
- **ML Deployment** — packaging a trained model into a user-facing Streamlit app  
- **End-to-End Thinking** — from raw CSV to interactive product  

---

## 📦 Dataset

This project uses the **[Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)** dataset from Kaggle / ULB MLG.

| Column | Description |
|---|---|
| `Time` | Seconds elapsed between transaction and first transaction in dataset |
| `V1` – `V28` | PCA-transformed features (anonymized for confidentiality) |
| `Amount` | Transaction amount |
| `Class` | Target — `0` = legitimate, `1` = fraud |

> **Note:** The dataset does not contain missing values and is ready for modeling after balancing.

---

## 🔮 Future Enhancements

- [ ] Add precision, recall, F1-score, and ROC-AUC (better metrics for imbalanced data)  
- [ ] Compare models (Random Forest, XGBoost, Isolation Forest)  
- [ ] Try SMOTE or other oversampling techniques  
- [ ] Persist trained model with `joblib` for faster app startup  
- [ ] Add `requirements.txt` and Docker support  

---

## 👤 Author

**Himanshu Gautam**

Built as a hands-on machine learning project showcasing data science fundamentals and real-world fintech problem solving.

---

<p align="center">
  <sub>If you found this project interesting, feel free to ⭐ star the repo or reach out to connect!</sub>
</p>
