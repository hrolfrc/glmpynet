.. _user_guide:

User Guide
==========

Welcome to the `glmpynet` User Guide. This guide provides a practical walkthrough of how to use the ``LogisticNet`` estimator to solve binary classification problems, integrating it seamlessly with the scikit-learn ecosystem.

Basic Usage: Fitting and Predicting
-----------------------------------

At its core, ``LogisticNet`` behaves just like any other scikit-learn classifier. You instantiate the model, then use the ``.fit()`` method with your training data and the ``.predict()`` method to make predictions.

.. code-block:: python

   from glmpynet import LogisticNet
   from sklearn.datasets import make_classification
   from sklearn.model_selection import train_test_split

   # 1. Create a synthetic dataset
   X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
   X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

   # 2. Initialize and fit the model
   model = LogisticNet()
   model.fit(X_train, y_train)

   # 3. Make predictions
   predictions = model.predict(X_test)
   print(f"First 10 predictions: {predictions[:10]}")

   # 4. Predict probabilities
   probabilities = model.predict_proba(X_test)
   print(f"First 5 predicted probabilities:\n{probabilities[:5]}")


Understanding Regularization
----------------------------

The primary power of ``glmnet``, and therefore ``LogisticNet``, is its use of **elastic-net regularization**, which is a combination of L1 (Lasso) and L2 (Ridge) penalties. This is controlled by the ``alpha`` parameter.

* **Lasso Regression (`alpha=1.0`):** This penalty can shrink some feature coefficients to exactly zero, effectively performing automatic feature selection. It is useful when you have many features and suspect some are redundant or irrelevant.
* **Ridge Regression (`alpha=0.0`):** This penalty shrinks coefficients towards zero but does not set them exactly to zero. It is effective at handling multicollinearity (when features are highly correlated).
* **Elastic-Net (`0 < alpha < 1`):** This combines the properties of both, providing a balance between feature selection and handling correlated features.

``LogisticNet`` simplifies the process by automatically finding the best regularization strength (lambda) via cross-validation during the ``.fit()`` call.

Inspecting the Fitted Model
---------------------------

After fitting, you can inspect the model's learned parameters just as you would with a scikit-learn model. The optimal coefficients and intercept found during cross-validation are stored as attributes.

.. code-block:: python

   # Assuming 'model' is the fitted model from the previous example

   # Access the coefficients (weights) for each feature
   print(f"Model coefficients shape: {model.coef_.shape}")
   print(f"Number of non-zero coefficients: {np.count_nonzero(model.coef_)}")

   # Access the intercept (bias) term
   print(f"Model intercept: {model.intercept_}")


Using `LogisticNet` in a Scikit-learn Pipeline
----------------------------------------------

A major advantage of ``LogisticNet`` is its compatibility with scikit-learn `Pipeline` objects. This allows you to chain data preprocessing steps (like scaling) with your model. It is highly recommended to scale your data before using a penalized regression model.

.. code-block:: python

   from sklearn.pipeline import Pipeline
   from sklearn.preprocessing import StandardScaler

   # Create a pipeline that first scales the data, then fits the model
   pipeline = Pipeline([
       ('scaler', StandardScaler()),
       ('logistic_net', LogisticNet(alpha=0.8))
   ])

   # Fit the entire pipeline on the training data
   pipeline.fit(X_train, y_train)

   # Make predictions using the pipeline
   # The test data is automatically scaled before prediction
   pipeline_preds = pipeline.predict(X_test)

   print(f"Pipeline accuracy: {accuracy_score(y_test, pipeline_preds):.2f}")


Hyperparameter Tuning with GridSearchCV
---------------------------------------

You can use scikit-learn's ``GridSearchCV`` to find the best hyperparameters for ``LogisticNet``, such as the optimal ``alpha`` value.

.. code-block:: python

   from sklearn.model_selection import GridSearchCV

   # Define the pipeline
   pipeline = Pipeline([
       ('scaler', StandardScaler()),
       ('logistic_net', LogisticNet())
   ])

   # Define the parameter grid to search over
   # We will search for the best alpha value
   param_grid = {
       'logistic_net__alpha': [0.1, 0.5, 0.9, 1.0]
   }

   # Set up and run the grid search with 5-fold cross-validation
   grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='roc_auc')
   grid_search.fit(X_train, y_train)

   # Print the best parameters found
   print(f"Best alpha value: {grid_search.best_params_['logistic_net__alpha']}")
   print(f"Best cross-validated AUC score: {grid_search.best_score_:.2f}")

This demonstrates how ``LogisticNet`` can be fully integrated into a standard machine learning workflow, leveraging the power of the scikit-learn ecosystem.
