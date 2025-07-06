.. _getting_started:

Getting Started
===============

This guide provides the essential steps to install `glmpynet` and run your first penalized logistic regression model.

Installation
------------

The recommended way to install `glmpynet` is from the Python Package Index (PyPI) using `pip`. Ensure you have Python 3.7 or higher installed.

.. code-block:: bash

   pip install glmpynet

This will install the package along with its required dependencies, such as `numpy` and `scikit-learn`.

Quick Start
-----------

Using `glmpynet` is designed to be as straightforward as using any other scikit-learn estimator. The main class, `LogisticNet`, follows the standard `.fit()` and `.predict()` API.

The following example demonstrates how to train a model and make predictions on synthetic data.

.. code-block:: python

   import numpy as np
   from glmpynet import LogisticNet
   from sklearn.datasets import make_classification
   from sklearn.model_selection import train_test_split
   from sklearn.metrics import accuracy_score

    # 1. Generate a synthetic binary classification dataset
    # This creates a more realistic problem than purely random data.
   X, y = make_classification(
       n_samples=1000,
       n_features=20,
       n_informative=5,
       n_redundant=5,
       n_classes=2,
       random_state=42
   )
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

   # 2. Instantiate and fit the model
   # The `alpha` parameter controls the elastic-net mixing:
   # alpha=1.0 is for Lasso (L1) regularization
   # alpha=0.0 is for Ridge (L2) regularization
   # 0 < alpha < 1 is for Elastic-Net
   model = LogisticNet(alpha=0.5)
   model.fit(X_train, y_train)

   # 3. Make predictions on the test set
   y_pred = model.predict(X_test)
   y_pred_proba = model.predict_proba(X_test)

   # 4. Evaluate the model's performance
   accuracy = accuracy_score(y_test, y_pred)
   print(f"Model Accuracy: {accuracy:.2f}")
   print(f"Predicted probabilities for the first 5 samples:\n{y_pred_proba[:5]}")

Next Steps
----------

You have now successfully trained your first `glmpynet` model. To learn more about the model's parameters, advanced usage, and the theory behind penalized regression, please proceed to the :ref:`user_guide`.
