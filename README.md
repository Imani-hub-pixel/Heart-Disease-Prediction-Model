# 10-Year Cardiovascular Disease Risk Prediction

A Machine Learning project that uses Logistic Regression to predict an individual's likelihood of developing Coronary Heart Disease (CHD) within the next 10 years. The project also features an interactive Flask web application that allows users to input health-related information and receive a model-generated prediction.

## 1. Project Overview

Cardiovascular diseases are among the leading causes of death worldwide. Early identification of individuals who may be at risk can support timely medical assessment and preventive interventions.

This project explores the application of Machine Learning in cardiovascular disease risk prediction using the **Framingham Heart Study dataset**.

I developed a Logistic Regression classification model to predict the 10-year risk of Coronary Heart Disease based on demographic, medical, and lifestyle-related factors.

Beyond model development, I integrated the trained model into an interactive web application using Flask, allowing users to enter their information and receive a prediction.

The project was motivated by my interest in applying the Logistic Regression concepts I was learning and understanding how Machine Learning models can be integrated into practical applications.

## 2. Project Objectives

- Perform Exploratory Data Analysis (EDA) to understand the dataset and identify relevant patterns.
- Clean and preprocess the dataset for Machine Learning.
- Develop a Logistic Regression classification model.
- Optimize model hyperparameters using RandomizedSearchCV and GridSearchCV.
- Evaluate model performance using appropriate classification metrics.
- Integrate the trained model into an interactive Flask web application.

## 3. Dataset

The project uses the **Framingham Heart Study dataset**, which contains demographic, behavioural, and medical information collected to investigate cardiovascular disease risk.

The dataset contains 15 predictor variables and one target variable.

### Features Description

| Feature | Description |
|---|---|
| `male` | Gender of the individual |
| `age` | Age in years |
| `education` | Education level |
| `currentSmoker` | Whether the individual currently smokes |
| `cigsPerDay` | Number of cigarettes smoked per day |
| `BPMeds` | Whether the individual takes blood pressure medication |
| `prevalentStroke` | History of stroke |
| `prevalentHyp` | Presence of hypertension |
| `diabetes` | Presence of diabetes |
| `totChol` | Total cholesterol level |
| `sysBP` | Systolic blood pressure |
| `diaBP` | Diastolic blood pressure |
| `BMI` | Body Mass Index |
| `heartRate` | Heart rate |
| `glucose` | Blood glucose level |

**Target Variable: `TenYearCHD`**

The target variable represents whether an individual developed coronary heart disease within the following 10 years.

- `0`: No recorded CHD event within 10 years.
- `1`: CHD event recorded within 10 years.

## 4. Technologies and Libraries

The following technologies and libraries were used:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Statistical data visualization |
| Scikit-learn | Preprocessing, model development, hyperparameter tuning and evaluation |
| Flask | Backend development and model integration |
| HTML | Web application structure |
| CSS | Web application styling |

## 5. Project Workflow

### 5.1 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was conducted to understand the dataset, examine feature distributions, and investigate relationships between variables.

The analysis involved:

- Examining the dataset structure and statistical summaries.
- Identifying missing values and duplicate records.
- Exploring distributions of numerical and categorical features.
- Investigating relationships between predictor variables and the target variable.
- Identifying patterns and potential relationships that could inform model development.

### 5.2 Data Preprocessing

The dataset was prepared for Machine Learning by applying the necessary preprocessing techniques.

This stage involved:

- Handling missing values.
- Encoding categorical variables where necessary.
- Separating independent variables from the target variable.
- Splitting the dataset into training and testing sets.
- Scaling numerical features where required.

### 5.3 Model Development

**Algorithm: Logistic Regression**

Logistic Regression was selected as the classification algorithm because the objective was to predict a binary outcome.

The model learns relationships between the input features and the target variable to estimate the probability of an individual belonging to either of the two classes.

### 5.4 Hyperparameter Optimization

To optimize model performance, I implemented two hyperparameter tuning techniques using Scikit-learn:

**RandomizedSearchCV**

Used to explore different combinations of hyperparameters and identify promising configurations.

**GridSearchCV**

Used to systematically evaluate selected hyperparameter combinations to identify the best-performing configuration within the specified search space.

Cross-validation was incorporated during the tuning process to assess model performance across different training and validation folds.

### 5.5 Model Evaluation

The trained model was evaluated using classification metrics to assess its predictive performance.

The evaluation included:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC Score

These metrics provide different perspectives on classification performance, particularly the model's ability to identify positive CHD cases.

### 5.6 Flask Web Application

To make the trained model accessible beyond the Jupyter Notebook, I developed an interactive web application using Flask.

The application allows users to:

1. Access the web interface.
2. Enter the required demographic, medical, and lifestyle information.
3. Submit their information for prediction.
4. Receive a prediction generated by the trained Logistic Regression model.

The application demonstrates the integration of a Machine Learning model into a web-based interface.

## 6. Application Demonstration

The project includes a demonstration video showing how users interact with the application and receive predictions.

**[Watch the Application Demo](https://github.com/Imani-hub-pixel/Heart-Disease-Prediction-Model/blob/main/10-year%20heart%20disease%20risk%20check%20-%20Google%20Chrome%202026-11-18%2008-06-08%20-%20Trim.mp4)**

## 7. Model Performance

The model was evaluated using multiple classification metrics to obtain a broader understanding of its performance.

| Metric | Score |
|---|---|
| Accuracy | To be updated |
| Precision | To be updated |
| Recall | To be updated |
| F1-score | To be updated |
| ROC-AUC | To be updated |

*The actual evaluation results will be added here.*

## 8. Repository Structure

```text
Heart-Disease-Prediction-Model/
│
├── Notebook/
│   └── cardiovascular_prediction.ipynb
│
├── templates/
│   └── index.html
│
├── application.py
│
├── hyperparameter.PNG
│
├── logisticregcode.PNG
│
└── 10-year-heart-disease-risk-check.mp4
```

### Repository Contents

| File/Directory | Description |
|---|---|
| `Notebook/` | Contains the Jupyter Notebook for EDA, preprocessing, model development and evaluation. |
| `templates/` | Contains HTML templates for the Flask application. |
| `application.py` | Flask application responsible for handling user inputs and generating predictions. |
| `hyperparameter.PNG` | Screenshot of the hyperparameter tuning implementation. |
| `logisticregcode.PNG` | Screenshot of the Logistic Regression implementation. |
| `10-year-heart-disease-risk-check.mp4` | Video demonstration of the interactive application. |

## 9. Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

- Python 3.9 or later
- Git
- pip

### Step 1: Clone the repository

```bash
git clone https://github.com/Imani-hub-pixel/Heart-Disease-Prediction-Model.git
```

### Step 2: Navigate to the project directory

```bash
cd Heart-Disease-Prediction-Model
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### Step 4: Install dependencies

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask
```

### Step 5: Run the application

```bash
python application.py
```

Open the local URL displayed in your terminal to access the web application.

*Note: Ensure that the trained model and any required preprocessing objects are available at the file paths expected by `application.py`.*

## 10. Key Learning Outcomes

Through this project, I gained practical experience in:

- Applying Logistic Regression to a real-world binary classification problem.
- Conducting Exploratory Data Analysis.
- Preparing and transforming data for Machine Learning.
- Performing hyperparameter optimization using RandomizedSearchCV and GridSearchCV.
- Evaluating classification models using multiple performance metrics.
- Integrating a trained Machine Learning model into a Flask web application.
- Understanding the process of taking a Machine Learning model from experimentation to application development.

## 11. Future Improvements

Some areas I would like to explore further include:

- Experimenting with additional classification algorithms and comparing their performance.
- Exploring feature selection techniques to identify the most informative predictors.
- Investigating ways to improve model performance, particularly its ability to identify positive CHD cases.
- Applying model interpretability techniques to understand how different features influence predictions.
- Improving the application's interface and user experience.

## 12. Disclaimer

This project is developed for educational and Machine Learning demonstration purposes only.

The predictions generated by this application are not medical diagnoses and should not be used as a substitute for professional medical advice, clinical assessment, or validated cardiovascular risk assessment tools.

---

## Author

**Faith Chepngeno**

- GitHub: [Imani-hub-pixel](https://github.com/Imani-hub-pixel)
- Project Repository: [10-Year Cardiovascular Disease Risk Prediction](https://github.com/Imani-hub-pixel/Heart-Disease-Prediction-Model)
