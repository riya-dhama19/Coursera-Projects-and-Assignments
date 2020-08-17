# Logistic_regression_with_numpy_and_python
Build logistic regression models from scratch using NumPy and Python, without the use of machine learning frameworks such as scikit-learn and statsmodels.

### Objective:

### Task 1: Introduction and Project Overview

* Introduction to the data set and the problem overview.

### Task 2: Load the Data and Import Libraries

* Load the dataset using pandas.

* Import essential modules and helper functions from NumPy and Matplotlib.

* Explore the pandas dataframe using the head() and info() functions.

### Task 3: Visualize the Data

* For this dataset, we can use a scatter plot using Seaborn to visualize the data, since it has only two variables: scores for test 1, scores for test 2.

### Task 4: Define the Logistic Sigmoid Function 𝜎(𝑧)

* We can interpret the output of the logistic sigmoid function as a probability, since this function outputs in the range 0 to 1 for any input.

* We can threshold the function at 50% to make our classification.

* If the output is greater than or equal to 0.5, we classify it as passed, and less than 0.5 as failed.

* The maximal uncertainty, we can easily see if we plug in 0 as the input. So when the model is most uncertain it tells you the data point has a 50% probability of being in either of the classes.

### Task 5: Compute the Cost Function 𝐽(𝜃) and Gradient
 
### Task 6: Cost and Gradient at Initialization

* Initialize the cost and gradient before any optimization steps.

### Task 7: Implement Gradient Descent from scratch in Python

### Task 8: Plotting the Convergence of 𝐽(𝜃)

* Plot how the cost function varies with the number of iterations.

### Task 8: Plotting the Decision Boundary

### Task 9: Predictions Using the Optimized 𝜃 Values

* Use our final values for 𝜃 to make predictions.
