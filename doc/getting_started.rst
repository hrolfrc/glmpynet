.. _getting_started:

Getting Started
===============

This guide provides the essential steps to install `glmpynet` and run your first regularized logistic regression model using the `glmnetpp` C++ library.

Installation
------------

Install `glmpynet` via PyPI with `pip`. Ensure you have Python 3.8 or higher:

.. code-block:: bash

   pip install glmpynet

This installs `glmpynet` with `numpy`. For development setup, see :ref:`environment`.

Quick Start
-----------

Using `glmpynet` is as straightforward as any scikit-learn estimator. The main class, `LogisticRegression`, follows the standard `.fit()` and `.predict()` API. The initial version uses `glmnetpp`’s default settings (sourced from `glmnet`’s R documentation or online resources) without parameters like `C` or `penalty`.

The following example trains a model on synthetic data.

.. code-block:: python

   import numpy as np
   from glmpynet import LogisticRegression
   from sklearn.datasets import make_classification
   from sklearn.model_selection import train_test_split
   from sklearn.metrics import accuracy_score

   # 1. Generate a synthetic binary classification dataset
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
   model = LogisticRegression()  # Uses glmnetpp defaults
   model.fit(X_train, y_train)

   # 3. Make predictions on the test set
   y_pred = model.predict(X_test)

   # 4. Evaluate the model's performance
   accuracy = accuracy_score(y_test, y_pred)
   print(f"Model Accuracy: {accuracy:.2f}")

Next Steps
----------

You have now trained your first `glmpynet` model. To learn more about usage, examples, and the `glmnetpp`-based architecture, proceed to :ref:`usage_guide` or :ref:`architecture`.