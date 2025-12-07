# 🧠 Assignment Problem Optimization using the Genetic Algorithm

An interactive Python + Streamlit project that solves the **Assignment Problem** using a fully customized **Genetic Algorithm (GA)**. This application allows users to input their own cost matrix and generates optimized assignments with real-time results.

---

## 🚀 Features

- ✅ Custom user input for cost matrix (dynamic size)
- 🧬 Genetic Algorithm implemented from scratch:
  - **Selection**
  - **Crossover**
  - **Mutation**
  - **Fitness Evaluation**
- 📊 Real-time optimization via **Streamlit UI**
- ⚙️ Adjustable GA parameters: population size, generations, mutation rate
- 🔁 Visual feedback on optimized assignments and costs

---

## 📌 Problem Overview

The **Assignment Problem** is a classical optimization problem where `n` agents are assigned to `n` tasks at minimum total cost.  
We solve this using a **Genetic Algorithm**, inspired by the natural selection process.

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Interface:** Streamlit  
- **Libraries:** NumPy, random, Streamlit  
- **Algorithm:** Genetic Algorithm

---

## 📥 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/assignment-ga-streamlit.git

# Navigate to the folder
cd assignment-ga-streamlit

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
