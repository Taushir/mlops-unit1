# MLOps Unit 1 Project

## 📌 Project Overview
This project demonstrates a simple Machine Learning workflow using the Iris dataset.

The objective is to follow a standard MLOps-friendly project structure and ensure reproducibility using Python and Git.

---

## 📂 Project Structure

mlops-unit1/
│
├── data/
├── models/
│   └── iris_model.pkl
├── src/
│   └── ml_model.py
├── requirements.txt
├── README.md
└── .gitignore

---

## 🔁 Reproducibility

To recreate the project environment:

1. Clone repository:
   git clone https://github.com/Taushir/mlops-unit1.git

2. Navigate into project:
   cd mlops-unit1

3. Create virtual environment:
   python -m venv venv

4. Activate environment (Windows):
   venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run the project:
   cd src
   python ml_model.py

---

## 📊 Output

- Model Accuracy printed in terminal
- Trained model saved in models/ folder