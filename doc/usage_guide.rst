.. _usage_guide:

Usage Guide
===========

This guide provides an overview of how to use `glmpynet` for
regularized logistic regression. It covers the hybrid API, integration with
Scikit-learn, and the configuration system.

API Philosophy: A Hybrid Approach
---------------------------------

``glmpynet.LogisticRegression`` is designed to be a seamless, high-performance
replacement for ``sklearn.linear_model.LogisticRegression``. To achieve this,
it provides a user-friendly hybrid API.

* **Simplicity by Default:** For most use cases, you can interact with the
  class using familiar Scikit-learn parameters like ``C`` and ``penalty``.
  This ensures smooth integration with tools like ``GridSearchCV``.

* **Glmnet on Request:** For advanced users who want to access the full power
  of the ``glmnet`` engine, the class also provides an "escape hatch" to use
  ``glmnet``-native parameters like ``alpha`` and ``nlambda`` directly.

The ``fit`` method automatically translates the user-provided parameters into
the format required by the C++ backend.

Basic Usage
-----------

For most users, the API will feel identical to Scikit-learn's.

Example: L1 Regularization (Lasso)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to train a model with an L1 penalty and make
predictions, including getting class probabilities.

.. code-block:: python

   from glmpynet.logistic_regression import LogisticRegression
   from sklearn.datasets import make_classification
   from sklearn.model_selection import train_test_split

   # 1. Generate a synthetic binary classification dataset
   X, y = make_classification(random_state=42)
   X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

   # 2. Instantiate and fit the model with sklearn-style parameters
   model = LogisticRegression(penalty='l1', C=0.5)
   model.fit(X_train, y_train)

   # 3. Make predictions
   y_pred = model.predict(X_test)

   # 4. Get class probabilities
   y_proba = model.predict_proba(X_test)
   print("Predicted probabilities for the first 5 samples:")
   print(y_proba[:5])

Advanced Usage: Direct `glmnet` Parameters
------------------------------------------

If you are an advanced user familiar with the R `glmnet` package, you can
bypass the Scikit-learn style parameters and control the solver directly
by providing ``alpha``. If ``alpha`` is provided, the ``penalty`` parameter
is ignored.

.. code-block:: python

   # Instantiate the model using the glmnet 'alpha' parameter for elastic net
   # This is equivalent to penalty='l1'
   model_glmnet = LogisticRegression(alpha=1.0)
   model_glmnet.fit(X_train, y_train)

Integration with Scikit-learn
-----------------------------

``glmpynet.LogisticRegression`` is a fully compliant Scikit-learn estimator
and works seamlessly with tools like ``Pipeline`` and ``GridSearchCV``.

Example: Using with GridSearchCV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from sklearn.model_selection import GridSearchCV
   from sklearn.pipeline import Pipeline
   from sklearn.preprocessing import StandardScaler

   # Create a pipeline
   pipeline = Pipeline([
       ('scaler', StandardScaler()),
       ('model', LogisticRegression())
   ])

   # Define a parameter grid to search over
   param_grid = {
       'model__penalty': ['l1', 'l2'],
       'model__C': [0.1, 1.0, 10.0]
   }

   # Set up and run the grid search
   grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
   grid_search.fit(X_train, y_train)

   print(f"Best parameters found: {grid_search.best_params_}")
   print(f"Best cross-validation score: {grid_search.best_score_:.2f}")
