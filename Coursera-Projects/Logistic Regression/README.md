# Logistic_regression
Create and train a logistic model that will be able to predict if a given image is of hand-written digit zero or of hand-written digit one. The model will be able to distinguish between images or zeros and ones, and it will do that with a very high accuracy. 

## Objective :

1. Implement Logistic Regression using Python and Numpy.

2. Apply the implementation to solve binary classification problems.

## Structure :

### Task 1: Introduction

* Introduction to the problem.

* Libraries and helper functions.

### Task 2: Hyperparameters

* Setting initial values for hyperparameters.

### Task 3: Dataset

* Loading the dataset.

* Understanding the shape of the examples.

* Plotting a few examples to visualize the examples and labels in the dataset.

### Task 4: A Mini Batch of Examples

* Get a random mini batch of examples.

* Understanding unrolling 2-dimensional arrays.

* Plotting multiple examples along with their labels.

### Task 5: Create Model

* Start implementing the Logistic Model class.

* Defining an initialization function.

### Task 6: Forward Pass

* Implementing the internal Forward Pass function.

* Understanding the loss function.

* Understanding the shape of weight parameters.

### Task 7: Backward Pass

* Calculating gradients for the weight and bias parameters.

### Task 8: Update Parameters

* Updating the weight and bias parameters with the gradients obtained from backward pass.

### Task 9: Check Model Performance

* Implementing a function which returns predictions given batch of examples.

* Implementing a function which evaluates model performance on a given batch of examples and labels.

* We will check the implementation of the evaluation function on a random batch.

* We will also visualize model performance with a few examples.

### Task 10: Training Loop

* Implementing the training loop. Each training iteration performs the following steps:

* Get a new random batch.

* Perform a forward pass to get activation output.

* Perform a backward pass to get gradients.

* Update the parameters using the gradients.

### Task 11: Training the Model

* We will now create a new instance of the Logistic Model.

* We will evaluate the model before it is trained.

* We will train the model.

* We will evaluate the model after it is trained.

* We will also plot validation accuracies and losses from during the training.

* Finally, we will visualize model performance on a random batch.
