[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/umn51FOU)
# Assignment: House Price Prediction
House price prediction is a crucial task in the field of data science and machine learning. It involves building a model that can estimate the price of a house based on various features or attributes associated with the property. The prediction of house prices is valuable for both homebuyers and sellers

<img src="./conf/house-price-prediction.jpeg" alt="house-price-prediction.jpeg" style="display: block;
  margin-left: auto;
  margin-right: auto;
  height: 300px;
  width: 100%">

  [](./conf/house-price-prediction.jpeg)


<aside>

**NOTE!** 

- This is an **individual** assignment.
- Be ready to do additional googling to complete this exercise, if necessary.
- Feel free to explore, experiment, and ask questions if you encounter any challenges. 
</aside>


## House Price Prediction Model
In this assignment, you will have the exciting opportunity to build a cool regression model that predicts house prices. As a data scientist, your task is to analyze a dataset containing various features of houses and their corresponding prices. By harnessing the power of machine learning, you will develop a model that can ACCURATELY estimate house prices based on the given features and EVALUATE the model.


> **Task**: Build a regression model to predict house prices based on various features and evaluate the model using multiple evaluation metrics.

##  Dataset
The dataset contains information about houses and their prices. The features included are:

- **Price**: The price of the house.
- **Area**: The total area of the house in square feet.
- **Bedrooms**: The number of bedrooms in the house.
- **athrooms**: The number of bathrooms in the house.
- **Stories**: The number of stories in the house.
- **Mainroad**: Whether the house is connected to the main road (Yes/No).
- **Guestroom**: Whether the house has a guest room (Yes/No).
- **Basement**: Whether the house has a basement (Yes/No).
- **Hot water heating**: Whether the house has a hot water heating system (Yes/No).
- **Airconditioning**: Whether the house has an air conditioning system (Yes/No).
- **Parking**: The number of parking spaces available within the house.
- **Prefarea**: Whether the house is located in a preferred area (Yes/No).
- **Furnishing status**: The furnishing status of the house (Fully Furnished, Semi-Furnished, Unfurnished).

### Repository
[![Click to open the project](https://img.shields.io/static/v1?label=Open%20Project&message=House%20Price%20Prediction&color=blue)](https://github.com/kiboschool/house-price-prediction.git)


### TODOs

- Load the dataset into a pandas DataFrame.
- Perform data exploration and preprocessing, including handling missing values and encoding categorical variables.
- Split the dataset into features (X) and target (y), where y is the 'Price' column.
- Split the dataset into training and testing sets using train-test split (e.g., 80% training and 20% testing).
- Build a regression model using scikit-learn (e.g., Linear Regression, Random Forest, or any other suitable model).
- Train the model on the training data using the fit method.
- Make predictions on the test data using the predict method.
- Evaluate the model using the following metrics:
    - Precision
    - Recall
    - F1 Score
    - Confusion Matrix
    - Mean Absolute Error (MAE)
    - Mean Squared Error (MSE)
    - Root Mean Squared Error (RMSE)
    - R-squared (R²)
- Complete the assignment using the `notebook` in the repository.
    - Push your solution back to Github once completed.
- Submit your notebook on **[Gradescope](https://www.gradescope.com/courses/544001/assignments)**
    - Look for **Week 7 - House Price Prediction** under assignments

### HINTS
- Utilize pandas library for data manipulation and preprocessing.
- Use scikit-learn library to build and train the regression model.
- Since this is a regression tasks, focus on MAE, MSE, RMSE, and R-squared. You can use the `mean_absolute_error`, `mean_squared_error`, `mean_squared_error`, and `r2_score` functions from the `sklearn.metrics` module.
- Apply k-fold cross-validation by using scikit-learn's cross_val_score function. You can use the `cross_val_score` function from the `sklearn.model_selection` module.
- Use the pandas `get_dummies` function for one-hot encoding categorical variables.
- Consider feature scaling if necessary, using MinMaxScaler or StandardScaler from scikit-learn.


**Note**: Make sure to properly interpret the evaluation metrics to understand the model's performance. The goal is to build a model that accurately predicts house prices and minimizes the error between predicted and actual prices. 

## `Good luck with the assignment` 🤝
