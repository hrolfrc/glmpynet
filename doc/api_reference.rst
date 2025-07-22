.. _api_reference:

API Reference
=============

This page provides the detailed API documentation for the ``glmpynet`` package.

.. currentmodule:: glmpynet.logistic_regression

LogisticRegression Class
------------------------

The ``LogisticRegression`` class is the main user-facing estimator in the
``glmpynet`` library. It is designed to be a fully compatible, drop-in
replacement for ``sklearn.linear_model.LogisticRegression``, but is
architected to be powered by the high-performance ``glmnetpp`` C++ engine.

.. autoclass:: LogisticRegression
   :members: fit, predict, predict_proba, get_params, set_params

   .. automethod:: __init__
      :noindex:

