## Flight Prices Prediction Project

### Overview

This Machine Learning project focuses on predicting flight ticket prices based on various input parameters such as Airlines Name, Source, Destination, Time of flight, Duration of flight, and No. of stops. The model achieves an impressive accuracy of 80%, ensuring reliable predictions for potential travelers.

### Input Parameters

1. **Airlines Name**: The name of the airline providing the flight service.
2. **Source**: The departure location of the flight.
3. **Destination**: The arrival location of the flight.
4. **Time of flight**: The departure time of the flight.
5. **Duration of flight**: The total duration of the flight.
6. **No. of stops**: The number of stops the flight makes before reaching the destination.

### Project Workflow

1. **Data Collection**:
   - The dataset containing flight information including Airlines Name, Source, Destination, Time of flight, Duration of flight, No. of stops, and corresponding prices was obtained from a reliable source.

2. **Data Cleaning**:
   - Missing values and outliers were handled to ensure the dataset's integrity.

3. **Data Visualization**:
   - Utilizing Python libraries like Matplotlib and Seaborn, exploratory data analysis (EDA) was performed to gain insights into the relationships between features and the target variable (flight prices).

4. **Feature Engineering**:
   - Additional features were derived or transformed to enhance the model's predictive power. This step involved techniques like one-hot encoding for categorical variables and scaling for numerical ones.

5. **Feature Selection**:
   - Relevant features were selected based on their importance in predicting flight prices, using techniques such as Recursive Feature Elimination (RFE) or feature importance from tree-based models.

6. **Model Training**:
   - Various regression models were considered and trained on the preprocessed data. Common models like Linear Regression, Lasso, Ridge, DTR, RFR, XGBR, LGBR were employed for this purpose.

7. **Model Hyper-parameter Tuning**:
   - Grid Search or Randomized Search was used to fine-tune the hyperparameters of the chosen model, optimizing its performance.

8. **Model Evaluation**:
   - Metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R2) were used to assess the model's performance.

### Tools and Software Used

1. **Python** ([Download Python](https://www.python.org/downloads/)): Python is the primary programming language used for this project.
2. **Jupyter Notebook** ([Download Jupyter Notebook](https://jupyter.org/install)): Jupyter Notebook was employed for interactive data exploration, visualization, and model development.
3. **Visual Studio Code (VS Code)** ([Download VS Code](https://code.visualstudio.com/download)): VS Code was used as an alternative environment for coding, providing a robust text editor with integrated version control.

### Python Libraries

The following Python libraries were instrumental in the successful implementation of this project:

- Pandas: For data manipulation and preprocessing.
- Matplotlib and Seaborn: For data visualization and EDA.
- Scikit-learn: For machine learning tasks including model training, evaluation, and hyper-parameter tuning.
- XGBoost, Random Forest, and Gradient Boosting: For implementing regression models.

### Conclusion

This Flight Prices Prediction project showcases a comprehensive pipeline from data collection and preprocessing to model training and evaluation. The achieved accuracy of 80% demonstrates the effectiveness of the developed model in accurately predicting flight ticket prices. The project emphasizes the importance of data quality, exploratory data analysis, and proper model selection for successful machine learning implementations in real-world scenarios.