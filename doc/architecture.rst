.. _architecture:

glmpynet: Architecture and Design
=================================

1. Introduction
---------------

This document outlines the technical architecture of the ``glmpynet`` library. The primary goal of this project is to provide a simple, high-performance, and user-friendly Python interface for the powerful `glmnet` backend, specifically for penalized logistic regression. This document details the relationship between the Python wrapper and the underlying compiled code, as well as the key design decisions made.

2. Core Philosophy: The Wrapper Pattern
---------------------------------------

The fundamental design of `glmpynet` is the **Wrapper Pattern**. The project does not re-implement the core logistic regression or regularization algorithms. Instead, it provides a clean, Pythonic interface that translates user commands into calls to the highly optimized, battle-tested `glmnet` Fortran/C++ library.

This approach provides the best of both worlds:

* **Performance:** Users get the raw computational speed of a compiled backend.
* **Usability:** Users interact with the library through the familiar and intuitive scikit-learn API.

3. Component Layers
-------------------

The architecture can be understood as three distinct layers:

#. **The `glmnet` Backend (The Engine):** This is the original, compiled Fortran/C++ code. Its responsibility is to perform the computationally intensive task of fitting the entire regularization path for an elastic-net model. It is treated as a high-performance "black box."

#. **The Python Wrapper (`glmpynet`) (The Interface):** This is the core of our project. It is a thin layer of Python code responsible for:

   * Preparing and validating data (e.g., converting pandas DataFrames to NumPy arrays).
   * Calling the compiled backend with the correct arguments.
   * Interpreting the results returned from the backend.
   * Presenting those results to the user in a standard, predictable format.

#. **The Scikit-learn API (The Contract):** To ensure a seamless user experience, `glmpynet` strictly adheres to the scikit-learn estimator API. This means our main class implements standard methods like ``.fit()``, ``.predict()``, and ``.predict_proba()``. This adherence is a core design principle, as it guarantees interoperability with the entire scikit-learn ecosystem (e.g., `Pipeline`, `GridSearchCV`).

4. The `LogisticNet` Class: Bridging the Gap
--------------------------------------------

The central component of the wrapper is the ``LogisticNet`` class. It acts as the bridge between the simple, user-friendly scikit-learn API and the more complex `glmnet` backend.

``__init__(self, alpha, n_lambda, ...)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Responsibility:** To capture and store the model's hyperparameters.
* **Mapping:** Parameters like ``alpha`` are stored directly. Other parameters control how the `glmnet` path is computed.

``fit(self, X, y)``
~~~~~~~~~~~~~~~~~~~

This is the most critical method in the wrapper. It orchestrates the entire model training process.

#. **Data Preparation:** It converts the input `X` and `y` into the format expected by the `glmnet` backend (typically a NumPy array).

#. **Path Calculation:** It calls the `glmnet` function to compute the full elastic-net regularization path. This returns a set of coefficients for many different values of the regularization strength, `lambda`.

#. **Model Selection via Cross-Validation:** The key design decision is to **hide the complexity of the regularization path** from the user. The ``fit`` method automatically performs cross-validation *across the computed path* to find the single best `lambda` value (e.g., the one that maximizes AUC or minimizes log-loss).

#. **Store Final Coefficients:** Once the best `lambda` is identified, the corresponding coefficients and intercept are stored as ``self.coef_`` and ``self.intercept_``, respectively. This follows the scikit-learn convention and presents the user with a single, final model.

``predict(self, X)`` and ``predict_proba(self, X)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Responsibility:** To perform inference on new data.
* **Mapping:** These methods are simple. They use the final ``self.coef_`` and ``self.intercept_`` (which were selected during the ``.fit()`` call) to make predictions. They do not need to interact with the `glmnet` backend directly.

5. Data Flow
------------

The data flow is designed to be simple and efficient:

#. The user provides data as a NumPy array or pandas DataFrame.
#. The ``LogisticNet`` class validates this data and converts it into a standard NumPy array.
#. This NumPy array is passed to the compiled `glmnet` backend.
#. The backend returns the results (coefficients for the full path).
#. The Python wrapper processes these results, performs cross-validation, and stores the final model parameters.

6. Key Design Decision: Adopting the Scikit-learn API
------------------------------------------------------

A conscious decision was made to adopt the scikit-learn API rather than creating a direct, 1-to-1 Python port of the R `glmnet` API. The R API exposes the full regularization path to the user, requiring them to manually select a lambda.

While powerful, this approach is not "Pythonic" and would prevent integration with the scikit-learn ecosystem. By choosing to hide this complexity and perform model selection automatically within the ``.fit()`` method, `glmpynet` provides a much more intuitive and user-friendly experience for the vast majority of Python data scientists.
