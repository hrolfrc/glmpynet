.. _getting_started:

Getting Started
===============

This guide provides the essential steps to install `glmpynet` and run your first regularized logistic regression model using the `glmnetpp` C++ library.

Installation
------------

The recommended way to install `glmpynet` is from the Python Package Index (PyPI) using `pip`. Ensure you have Python 3.8 or higher, Conda (with `mamba` recommended), Bazel, and a C++ toolchain (GCC 9.3.0+ or Clang 10.0.0+) installed.

.. code-block:: bash

   pip install glmpynet

This will install the package with dependencies like `numpy`. For development, set up a Conda environment with `mamba`, Bazel, OpenMP, and Eigen, as detailed in :ref:`development_guide`.

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

You have now trained your first `glmpynet` model. To learn more about usage, examples, and the `glmnetpp`-based architecture, proceed to the :ref:`usage_guide` or :ref:`architecture`.