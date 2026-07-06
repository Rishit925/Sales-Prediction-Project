# 📈 Advertising Sales Prediction

This project predicts product sales based on advertising budgets allocated to **TV, Radio, and Newspaper** channels. It uses Machine Learning to analyze the relationship between advertising expenditure and sales, allowing users to estimate expected sales for different marketing budgets.

The project compares **Linear Regression** and **Random Forest Regressor** models. Based on evaluation metrics, **Random Forest** achieved better predictive performance and was selected as the final model for deployment.

## 🚀 Live Demo

🌐 **Streamlit Application:**  
https://sales-prediction-project-25ec5a9sywsqueucirufnx.streamlit.app/

---

## 📌 Project Features

- Predict product sales using advertising budgets.
- Data preprocessing and feature scaling.
- Comparison of multiple Machine Learning models.
- Performance evaluation using MAE, RMSE, R² Score, and Cross-Validation.
- Interactive web application built with Streamlit.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib

---

## 📂 Project Workflow

### 1. Data Exploration
- Loaded the Advertising dataset.
- Explored the dataset using descriptive statistics.
- Checked for missing values and duplicate records.
- Performed Exploratory Data Analysis (EDA) using visualizations.

### 2. Data Preprocessing
- Selected TV, Radio, and Newspaper as input features.
- Selected Sales as the target variable.
- Split the dataset into training and testing sets.
- Applied StandardScaler to normalize the feature values.

### 3. Model Building
Two regression models were trained and evaluated:
- Linear Regression
- Random Forest Regressor

### 4. Model Evaluation
Models were compared using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
- Cross Validation R² Score

Random Forest achieved the highest accuracy and was selected as the final model.

### 5. Deployment
The trained model and scaler were saved using Joblib and integrated into a Streamlit web application where users can enter advertising budgets and receive an instant sales prediction.

---

## 📊 Model Performance

| Model | MAE | RMSE | R² Score | CV R² |
|--------|-----:|------:|---------:|------:|
| Linear Regression | 1.46 | 1.78 | 0.899 | 0.859 |
| **Random Forest** | **0.62** | **0.77** | **0.981** | **0.969** |

**Final Model Selected:** Random Forest Regressor

---

## 📁 Project Structure

```text
Sales-Prediction-Project/
│── app.py
│── Sales_Prediction.ipynb
│── Advertising.csv
│── sales_prediction_model.pkl
│── scaler.pkl
│── requirements.txt
└── README.md
```

---

## ▶️ Run the Project Locally

Clone the repository:

```bash
git clone https://github.com/Rishit925/Sales-Prediction-Project.git
```

Navigate to the project folder:

```bash
cd Sales-Prediction-Project
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📈 Conclusion

The Random Forest Regressor outperformed Linear Regression on this dataset, achieving an **R² Score of approximately 0.98**, indicating excellent predictive performance. The deployed Streamlit application provides a simple interface for estimating product sales based on advertising budgets, making the model easy to interact with and demonstrate.

---

## 👨‍💻 Author

**Rishit Mahindru**

If you found this project useful, feel free to ⭐ the repository.
