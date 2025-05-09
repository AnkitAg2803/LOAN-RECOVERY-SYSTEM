# Smart Loan Recovery System

This project comprises a loan recovery prediction system, leveraging machine learning to assess the recovery status of loans. It includes data processing, model training (as seen in the Jupyter Notebook), and a Streamlit application for user interaction and predictions.

## Files Included

* **`LOAN RECOVERY SYSTEM.ipynb`**:  A Jupyter Notebook containing the data analysis, preprocessing, model training, and evaluation steps.
* **`App.py`**: A Streamlit application providing a user interface to input loan-related information and receive loan recovery predictions.
* **`Smart Loan Recovery System.csv`**: The dataset used for training the loan recovery prediction model.
* `loan_default_model.joblib`:  The trained machine learning model (Random Forest in `App.py`) for predicting loan recovery.
* `label_encoders.joblib`:  Saved label encoders used to handle categorical features.

## Project Description

The goal of this project is to develop a system that can predict the likelihood of loan recovery based on various borrower and loan characteristics.  This system can assist financial institutions in prioritizing recovery efforts and implementing appropriate strategies.

The `LOAN RECOVERY SYSTEM.ipynb` notebook walks through the process of:

* **Data Loading and Exploration:** Loading the dataset (`Smart Loan Recovery System.csv`) and exploring its structure and initial statistics.
* **Data Preprocessing:** Cleaning, transforming, and preparing the data for model training. This may include handling missing values, encoding categorical features, and feature scaling (note: the notebook may contain the initial steps, while `App.py` uses saved encoders).
* **Model Training:** Training a machine learning model (likely a classification model) to predict the loan recovery status.  The notebook shows the initial model building, while `App.py` uses a pre-trained Random Forest model.
* **Model Evaluation:** Assessing the performance of the trained model using appropriate metrics.

The `App.py` file provides a user-friendly interface built with Streamlit:

* **User Input:** The app takes key loan and borrower information as input from the user (e.g., age, gender, income, loan amount).
* **Prediction:** The input data is processed and fed into the pre-trained machine learning model (`loan_default_model.joblib`) to predict the loan recovery status.
* **Result Display:** The app displays the prediction result to the user.

## Data Dictionary

The `Smart Loan Recovery System.csv` dataset contains the following columns:

Borrower_ID:  Unique identifier for the borrower.
Age: Age of the borrower.
Gender: Gender of the borrower.
Employment_Type:  Employment type of the borrower (e.g., Salaried, Self-Employed).
* **Monthly_Income:** Monthly income of the borrower.
  Num_Dependents: Number of dependents the borrower has.
  Loan_ID: Unique identifier for the loan.
Loan_Amount: Amount of the loan.
  Loan_Tenure: Duration of the loan (in months).
  Interest_Rate: Interest rate on the loan.
  Loan_Type: Type of loan (e.g., Home, Auto, Personal).
  Collateral_Value:** Value of the collateral securing the loan.
  Outstanding_Loan_Amount: Remaining amount to be paid on the loan.
  Monthly_EMI: Monthly Equated Monthly Installment.
  Payment_History: Borrower's loan payment history.
  Num_Missed_Payments: Number of payments missed by the borrower.
Days_Past_Due:** Number of days the loan payment is past due.
  Recovery_Status: Status of loan recovery (target variable).
 Collection_Attempts: Number of collection attempts made.
Collection_Method:** Method used for loan collection.
  Legal_Action_Taken:** Whether legal action was taken.

## Installation and Usage

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install the required Python libraries:**

    ```bash
    pip install pandas numpy scikit-learn streamlit joblib
    ```

3.  **Run the Streamlit application:**

    ```bash
    streamlit run App.py
    ```

4.  **Access the application in your browser:** The Streamlit app will open in your default web browser.

## Dependencies

* Python 3.x
* pandas
* numpy
* scikit-learn
* streamlit
* joblib

## Model

The Streamlit app (`App.py`) uses a pre-trained Random Forest model (`loan_default_model.joblib`) for loan recovery prediction.  The model was trained using the data and methodology outlined in `LOAN RECOVERY SYSTEM.ipynb`.

##  Important Notes

* Ensure that all the necessary files (`loan_default_model.joblib`, `label_encoders.joblib`, and `Smart Loan Recovery System.csv`) are in the same directory as `App.py`.
* The `App.py` script handles some missing input values by assigning default values to ensure compatibility with the model.
* The accuracy and reliability of the predictions depend on the quality and representativeness of the training data.

## Future Enhancements

* Improve model performance by exploring different algorithms and hyperparameter tuning.
* Add more comprehensive error handling and input validation to the Streamlit app.
* Implement a data visualization dashboard to provide more insights into loan recovery patterns.
* Integrate with a database for real-time data updates.

## Author

\[ANKIT AGRAWAL]

## License

\[Choose a License, e.g., MIT License]
