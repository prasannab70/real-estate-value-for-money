# 🏡 Real Estate Value-for-Money Property Recommendation System

A Django-based web application that predicts **total property price** using  
**area (slider), BHK configuration, and location**, and recommends **value-for-money cities** within a state.

---

## 📸 Application Screenshot

![Value for Money Property Recommendation](pic.PNG)

> The above screenshot shows:
> - Area slider
> - BHK selection
> - Predicted property price
> - Value-for-money table
> - Area-based price comparison chart

---

## 🚀 Features

- 🔹 **Area-based price prediction** (slider input)
- 🔹 **BHK factor adjustment**
- 🔹 **Total property price estimation**
- 🔹 **Value Score calculation** to compare affordability
- 🔹 **State-wise value-for-money recommendation**
- 🔹 **Interactive charts** using Chart.js
- 🔹 **Database-backed** (SQLite) with dynamic data growth
- 🔹 **Responsive UI** using Bootstrap

---

## 🧮 Prediction Logic

### Total Property Price:

### Value Score:

Higher value score ⇒ better value for money.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, Bootstrap, Chart.js  
- **Database:** SQLite  
- **Version Control:** Git & GitHub  

---

## ▶️ How to Run the Project

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

