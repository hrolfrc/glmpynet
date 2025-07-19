.. _api_reference:

API Reference
=============

This page describes the `glmpynet` API, focusing on the `LogisticRegression` class, designed to be compatible with the scikit-learn ecosystem. The initial version provides a minimal API with `fit` and `predict` methods, using `glmnetpp`’s default settings (sourced from `glmnet`’s R documentation or online resources) for regularized logistic regression. Future versions will add methods like `predict_proba` and parameter support (e.g., `C`, `penalty`).

.. currentmodule:: glmpynet

LogisticRegression Class
------------------------

.. autoclass:: LogisticRegression
   :members:

   .. automethod:: __init__
      :noindex:
      Initializes the model with no parameters, using `glmnetpp`’s default settings.

   .. automethod:: fit
      :noindex:
      Fits the model to training data, converting inputs to Eigen matrices for `glmnetpp` and storing coefficients as `coef_` and `intercept_`.

   .. automethod:: predict
      :noindex:
      Predicts class labels (0 or 1) for new data using the fitted model.