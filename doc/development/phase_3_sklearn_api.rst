.. _phase_3_sklearn_api:

Phase 3: Scikit-learn Compatible API
====================================

**Objective:** To create a high-level, user-friendly Python class that
matches the Scikit-learn API and uses the C++ binding for its computations.

Initial Model: `LogisticNet`
----------------------------

The first and primary goal is to create a class, ``LogisticNet``, that serves
as a drop-in replacement for ``sklearn.linear_model.LogisticRegression``.

**API Contract:**
The class will implement the standard Scikit-learn estimator interface:
* ``__init__(self, ...)``: Will accept key regularization parameters
    compatible with ``glmnet``, such as ``alpha`` (for elastic net mixing)
    and ``lambda`` (the regularization strength).
* ``fit(self, X, y)``: The core training method.
* ``predict(self, X)``: To make class predictions.
* ``predict_proba(self, X)``: To get class probabilities.
* ``get_params()`` / ``set_params()``: For compatibility with Scikit-learn
    tools like ``GridSearchCV``.

Future Expansion
----------------

The ``glmnet`` library is capable of more than just logistic regression
(e.g., linear, Poisson, Cox regression). The API will be designed with
this in mind.

A potential future architecture would involve:
* A base class, ``GlmNetEstimator``, that handles the common logic of
    interacting with the C++ binding.
* Specific child classes for different models, such as ``LogisticNet``,
    ``ElasticNet``, etc., that inherit from the base class.

This ensures that as we expand the library's functionality, we can do so
in a clean, modular, and maintainable way.