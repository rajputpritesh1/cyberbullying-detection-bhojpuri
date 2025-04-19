# 🚨 Cyberbullying Detection in Bhojpuri Text

This project detects cyberbullying in Bhojpuri user-generated content using Logistic Regression and TF-IDF features.

## 🧠 Features
- Works with Devanagari script (Bhojpuri)
- Detects bullying vs. non-bullying
- Model trained on real Bhojpuri text
- Clean Flask web interface for prediction

## 📁 Dataset
- Source: YouTube, Facebook, Forums, Blogs
- Size: 9241 rows
- Format: Text (Bhojpuri) + Label (0/1)

## ⚙️ Tech Stack
- Python
- Scikit-learn
- Flask
- TF-IDF
- Logistic Regression

## 🚀 Run Locally
```bash
git clone https://github.com/rajputpritesh1/cyberguard.git
cd cyberguard
pip install -r requirements.txt
python app.py
