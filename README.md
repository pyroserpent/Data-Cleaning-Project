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

📝 Key Cleaning Tasks

✔ Handled missing values (NaN, "N/A", "None")

✔ Standardized phone numbers to (XXX) XXX XXXX format

✔ Removed invalid phone numbers and ensured correct length

✔ Cleaned names by removing special characters and numbers

✔ Saved cleaned data as both CSV and Excel files
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

## 📊 Sample Cleaned Data
The cleaned dataset is available in:
- 📄 [`customer_call_cleaned_data.csv`](https://github.com/pyroserpent/Data-Cleaning-Project/blob/main/data/customer_call_cleaned_data.csv)
- 📄 [`customer_call_cleaned_data.xlsx`](https://github.com/pyroserpent/Data-Cleaning-Project/blob/main/data/customer_call_cleaned_data.xlsx)

**Example of Before & After Data Cleaning:**

| Name     | Phone Number        | Address                 |
|----------|--------------------|-------------------------|
| John Doe | 1 (800) 555-0199   | 123 Main St, NY        |
| Alice B. | 987-654-3210 ext 7 | 456 Elm St, LA         |
| Mike T.  | N/A                | 789 Pine St, SF        |

🔽 **After Cleaning** 🔽

| Name     | Phone Number       | Address                 |
|----------|-------------------|-------------------------|
| John Doe | (800) 555 0199    | 123 Main St, NY        |
| Alice B. | (987) 654 3210    | 456 Elm St, LA         |
| Mike T.  | None              | 789 Pine St, SF        |

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