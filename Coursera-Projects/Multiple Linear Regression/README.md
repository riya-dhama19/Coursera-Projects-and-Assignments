# Multiple_Linear_Regression

This Project I did on Coursera Project Network .

Build and evaluate multiple linear regression models using Python

## Objectives:

1. Build univariate and multivariate linear regression models using scikit-learn

2. Perform Exploratory Data Analysis (EDA) and data visualization with seaborn

3. Evaluate model fit and accuracy using numerical measures such as R² and RMSE

4. Model interaction effects in regression using basic feature engineering techniques

## Structure :

### Task 1: Introduction and Overview

* Importing Essential Libraries

### Task 2: Load the Data

* Load the very popular Advertising dataset about various costs incurred on advertising by different media such as through TV, radio, newspaper, and the sales for a particular product 

### Task 3: Relationship between Features and Target

* Apply seaborn to create scatter plots of each of the three features and the target. This will allow to make a qualitative observations about the linear or non-linear relationships between the features and the target.

### Task 4: Multiple Linear Regression Model

We will extend the simple linear regression model to include multiple features. Our approach will give each predictor a separate slope coefficient in a single model. This way, we can avoid the drawbacks of fitting a separate simple linear model to each predictor. In this task, we use scikit-learn's LinearRegression( ) estimator to calculate the multiple regression coefficient estimates when TV, radio, and newspaper advertising budgets are used to predict sales revenue. Lastly, we will compare and contrast the coefficient estimates from multiple regression to those from simple linear regression.

### Task 5: Feature Selection

* We will use feature selection to determine which predictors are associated with the response, so as to fit a single model involving only those features. We will use R², the most common numerical measure of model fit and understand its limitations.

### Task 6: Model Evaluation Using Train/Test Split and Model Metrics

* Split the data into a training set and a testing set using the train_test_split( ) helper function from sklearn.metrics. 

* Create two separate models, one of which uses all predictors, while the other excludes newspaper. We fit the training set to the estimator and make predictions on the testing set. 

* Model fit and the accuracy of the predictions will be evaluated using R² and RMSE. Visual assessment of our models will involve comparing the residual behaviors and the prediction errors using Yellowbrick. 

* Yellowbrick is an open source, pure Python project that extends the scikit-learn API with visual analysis and diagnostic tools.

### Task 7: Interaction Effect (Synergy) in Regression Analysis

From our previous analysis of the residuals, we concluded that we need to incorporate interaction terms due to the non-additive relationship between the features and target. A simple method to extend our model to allow for interaction effects is to include a third feature by taking the product of the other two features in our model. This feature will have its separate slope coefficient which can be interpreted as the increase in the effectiveness of radio advertising for a one unit increase in TV advertising or vice versa.
