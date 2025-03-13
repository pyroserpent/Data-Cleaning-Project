# 📊 Data Cleaning Project

## 📌 Project Overview
This project focuses on **cleaning and standardizing messy datasets** using **Python, pandas, and regex** in **Jupyter Lab**. The goal is to improve **data quality, consistency, and usability** for further analysis.

---

## 📂 Project Structure
```
📂 data-cleaning-project/
│── 📂 data/
│   ├── raw_data.csv  # Original dataset
│   └── cleaned_data.csv  # Cleaned dataset (saved from Jupyter)
│
│── 📂 notebooks/
│   └── data_cleaning.ipynb  # Jupyter Notebook with cleaning steps
│
│── 📂 scripts/
│   └── clean_phone_numbers.py  # Python script for phone number formatting
│
│── 📝 README.md  # Project documentation
```

---

## 📝 Key Cleaning Tasks
✔ **Handled missing values** (`NaN`, `"N/A"`, `"None"`)
✔ **Standardized phone numbers** to **`(XXX) XXX XXXX`** format  
✔ **Removed invalid phone numbers** and ensured correct length  
✔ **Saved cleaned data as both CSV and Excel files**  

---

## 🚀 How to Use

### **Option 1: Run in Jupyter Lab**
1. Clone the repository using **GitHub Desktop** or via the command line:
   ```sh
   git clone https://github.com/pyroserpent/data-cleaning-project.git
   ```
2. Open **Jupyter Lab** and navigate to:
   ```sh
   notebooks/data_cleaning.ipynb
   ```
3. Run the notebook to execute all cleaning steps.

### **Option 2: Use the Cleaning Script**
If you only need to clean phone numbers, you can import the script:
```python
from scripts.clean_phone_numbers import clean_phone_number

clean_phone_number("123-456-7890")  # Output: (123) 456 7890
```

---

## 📝 Author
👤 **Ziaul Chowdhury**  
👉 [GitHub Profile](https://github.com/pyroserpent)  

---

## ⚡ Future Enhancements
- Add **more data validation rules**  
- Expand support for **international phone numbers**  
- Implement **automated data cleaning pipelines**  

---