.. _examples:

Examples
========

This section provides practical examples of how to use `glmpynet` and compares its behavior to standard scikit-learn estimators.

Example 1: Feature Selection with Lasso
---------------------------------------

One of the primary advantages of using a regularized regression model is its ability to perform automatic feature selection. When using an L1 penalty (Lasso regularization), ``LogisticRegression`` can shrink the coefficients of irrelevant features to zero.

This example compares ``glmpynet.LogisticRegression`` with scikit-learn's standard ``LogisticRegression`` on a dataset with many redundant features.

The Code
~~~~~~~~

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from sklearn.datasets import make_classification
   from sklearn.model_selection import train_test_split
   from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression
   from glmpynet.logistic_regression import LogisticRegression as GlmpynetLogisticRegression

   # 1. Create a synthetic dataset with many non-informative features
   X, y = make_classification(
       n_samples=1000,
       n_features=50,
       n_informative=5,  # Only 5 features are actually useful
       n_redundant=25,   # 25 features are linear combinations of informative ones
       n_classes=2,
       random_state=42
   )
   X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

   # 2. Train a standard scikit-learn Logistic Regression model (Ridge default)
   sklearn_lr = SklearnLogisticRegression(solver='liblinear')
   sklearn_lr.fit(X_train, y_train)

   # 3. Train a glmpynet LogisticRegression model with Lasso regularization
   glmpynet_lasso = GlmpynetLogisticRegression(penalty='l1', C=1.0)
   glmpynet_lasso.fit(X_train, y_train)

   # 4. Compare the number of non-zero coefficients
   sklearn_coeffs = np.count_nonzero(sklearn_lr.coef_)
   glmpynet_coeffs = np.count_nonzero(glmpynet_lasso.coef_)

   print(f"Scikit-learn LogisticRegression non-zero coefficients: {sklearn_coeffs}")
   print(f"glmpynet LogisticRegression (Lasso) non-zero coefficients: {glmpynet_coeffs}")
   print(f"\nNote: The Lasso model correctly identified a small subset of important features.")

   # 5. Visualize the coefficients
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

   ax1.stem(sklearn_lr.coef_[0])
   ax1.set_title("Scikit-learn LogisticRegression Coefficients")
   ax1.set_xlabel("Feature Index")
   ax1.set_ylabel("Coefficient Value")

   ax2.stem(glmpynet_lasso.coef_[0])
   ax2.set_title("glmpynet LogisticRegression (Lasso) Coefficients")
   ax2.set_xlabel("Feature Index")

   plt.suptitle("Comparison of Model Coefficients")
   plt.show()

