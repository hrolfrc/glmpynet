.. _getting_started:

Getting Started
===============

This guide provides the essential steps to install `glmpynet` and run your first regularized logistic regression model. It is designed to get you up and running in under five minutes.

For a complete reference of all commands and options, please see the :doc:`usage_guide`.

Installation
------------

`glmpynet` is distributed via the Python Package Index (PyPI) and can be installed easily using ``pip``. Ensure you have Python 3.8 or higher installed.

.. code-block:: bash

   pip install glmpynet

This command will install `glmpynet` and its necessary dependencies, such as NumPy and Scikit-learn. For a full development setup, which includes the C++ toolchain, please see the :doc:`development/guides/environment_setup` guide.

Quick Start
-----------

Using `glmpynet` is as straightforward as any Scikit-learn estimator. The main class, ``LogisticRegression``, follows the standard ``.fit()`` and ``.predict()`` API and accepts familiar parameters like ``penalty`` and ``C``.

The following example trains a model on a synthetic dataset.

.. code-block:: python

   from glmpynet.logistic_regression import LogisticRegression
   from sklearn.datasets import make_classification
   from sklearn.model_selection import train_test_split
   from sklearn.metrics import accuracy_score

   # 1. Generate a synthetic binary classification dataset
   X, y = make_classification(
       n_samples=1000,
       n_features=50,
       n_informative=10,
       random_state=42
   )
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

   # 2. Instantiate and fit the model using familiar sklearn parameters
   model = LogisticRegression(penalty='l1', C=0.5)
   model.fit(X_train, y_train)

   # 3. Make predictions on the test set
   y_pred = model.predict(X_test)

   # 4. Evaluate the model's performance
   accuracy = accuracy_score(y_test, y_pred)
   print(f"Model Accuracy: {accuracy:.2f}")