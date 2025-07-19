.. _usage_guide:

Usage Guide
===========

This guide explains how to use `glmpynet` to train and predict with regularized logistic regression models, designed to be as simple as using `scikit-learn`’s `LogisticRegression`. The initial version of `glmpynet` uses the `glmnetpp` C++ library with default settings (sourced from `glmnet`’s R documentation or online resources) for binary classification, without user-specified parameters like `C` or `penalty`.

Basic Usage
-----------

The `glmpynet.LogisticRegression` class provides a `scikit-learn`-compatible API with `fit` and `predict` methods. It works out of the box with `glmnetpp`’s default settings, making it easy to integrate into data science workflows.

Example: Binary Classification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to train a model and make predictions on a synthetic dataset.

.. code-block:: python

   import numpy as np
   from glmpynet import LogisticRegression
   from sklearn.datasets import make_classification
   from sklearn.model_selection import train_test_split
   from sklearn.metrics import accuracy_score

   # Generate a synthetic binary classification dataset
   X, y = make_classification(
       n_samples=1000,
       n_features=20,
       n_informative=5,
       n_redundant=5,
       n_classes=2,
       random_state=42
   )
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

   # Instantiate and fit the model
   model = LogisticRegression()  # Uses glmnetpp defaults
   model.fit(X_train, y_train)

   # Make predictions
   y_pred = model.predict(X_test)

   # Evaluate accuracy
   accuracy = accuracy_score(y_test, y_pred)
   print(f"Model Accuracy: {accuracy:.2f}")

Key Points
~~~~~~~~~~

* **Data Input**: `X` should be a NumPy array or compatible format (e.g., pandas DataFrame, converted internally to NumPy). `y` should be a binary classification target (0 or 1).
* **Defaults**: The model uses `glmnetpp`’s default settings for regularization and other parameters, sourced from `glmnet`’s R documentation or online resources.
* **Output**: `predict` returns class labels (0 or 1). Future versions will add `predict_proba` for probabilities and parameters like `C` or `penalty`.

Integration with Scikit-learn
-----------------------------

`glmpynet.LogisticRegression` is designed to work seamlessly with `scikit-learn` tools, such as pipelines and cross-validation.

Example: Using with a Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from sklearn.pipeline import Pipeline
   from sklearn.preprocessing import StandardScaler

   # Create a pipeline
   pipeline = Pipeline([
       ('scaler', StandardScaler()),
       ('model', LogisticRegression())
   ])

   # Fit the pipeline
   pipeline.fit(X_train, y_train)

   # Predict and evaluate
   y_pred = pipeline.predict(X_test)
   accuracy = accuracy_score(y_test, y_pred)
   print(f"Pipeline Accuracy: {accuracy:.2f}")

Next Steps
----------

To explore practical examples, see :ref:`examples`. For Jupyter notebooks with detailed workflows, visit :ref:`notebooks`. To understand the `glmnetpp`-based design, check :ref:`architecture`.