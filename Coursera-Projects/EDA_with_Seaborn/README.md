# EDA_with_Seaborn

## Objectives : 

In this we are going to focus on two learning objectives:

1. Produce data visualizations with Seaborn.

2. Apply graphical techniques used in exploratory data analysis (EDA).

## Structure :

### Task 1: Introduction and Importing the Data

* We will import essential libraries such as NumPy, pandas, Seaborn, and matplotlib.

* We use pandas to load the Breast Cancer Wisconsin (Diagnostic) Data Set.

### Task 2: Separate Target from Features

* Explore the characteristics of its attributes and instances.

* We will drop columns that cannot be used for analysis and classification.

* The target contains the diagnosis with binary class labels, M or B, for malignant and benign tumors respectively.

### Task 3: Diagnosis Distribution Visualization

* We will use Seaborn's countplot() method to visualize the target distributions.

* We will also generate descriptive statistics about the features that summarize the central tendency, dispersion and shape of the data set's distribution.

### Task 4: Visualizing Standardized Data with Seaborn

* Standardize the data before proceeding with further analysis and visualization.

To begin feature analysis, we use Seaborn's violinplot() method. Violin plots are similar to box plots, except that they also show the probability density of the data at different values, usually smoothed by a kernel density estimator.

### Task 5: Violin Plots and Box Plots

* We are using violin plots and box plots to identify features that best separate the data for classification.

* Box plots are especially useful in identifying outliers in the data.

* Using violin plots, we are also able to infer whether certain features are correlated.

### Task 6: Using Joint Plots for Feature Comparison

* Joint plots come in handy to illustrate the relationship between two features.

* We use seaborn's jointplot() method to draw a scatter plot with marginal histograms and kernel density fits. We can examine the relationship between any two features using the Pearson correlation coefficient of the regression through our scatter plot.

### Task 7: Observing the Distribution of Values and their Variance with Swarm Plots

* Seaborn's swarmplot() method. A swarm plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.

### Task 8: Observing all Pairwise Correlations

* A good way to identify correlations between features is to visualize the correlation matrix as a heatmap.
