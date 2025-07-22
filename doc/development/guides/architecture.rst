.. _architecture:

Architecture and Design
=================================

1. Introduction
---------------

This document outlines the technical architecture of the `glmpynet` library. The primary goal is to provide a simple, high-performance, and user-friendly Python interface for the `glmnetpp` C++ library, specifically for regularized logistic regression. This document details the relationship between the Python wrapper and the underlying C++ code, as well as key design decisions.

2. Core Philosophy: The Wrapper Pattern
---------------------------------------

The fundamental design of `glmpynet` is the **Wrapper Pattern**. The project does not re-implement logistic regression or regularization algorithms. Instead, it provides a clean, Pythonic interface that translates user commands into calls to the optimized `glmnetpp` C++ library.

This approach provides:
* **Performance**: Leverages `glmnetpp`’s computational speed.
* **Usability**: Offers a familiar `scikit-learn` API that works with minimal configuration.

3. Component Layers
-------------------

The architecture consists of three layers:

#. **The ``glmnetpp`` Backend (The Engine)**: The compiled C++ library (header-only) performs the computationally intensive task of fitting regularized logistic regression models. It is treated as a high-performance black box.

#. **The Python Wrapper ( ``glmpynet`` ) (The Interface)**: A thin layer of Python code responsible for:
   * Preparing and validating data (e.g., converting NumPy arrays to Eigen matrices).
   * Calling the `glmnetpp` backend with default settings.
   * Interpreting and returning results in a `scikit-learn`-compatible format.

#. **The Scikit-learn API (The Contract)**: The `glmpynet.LogisticRegression` class implements `fit` and `predict` methods, ensuring interoperability with `scikit-learn` tools (e.g., pipelines). The initial version uses `glmnetpp`’s default settings (sourced from `glmnet`’s R documentation or online resources).

4. The `LogisticRegression` Class: Bridging the Gap
---------------------------------------------------

The `LogisticRegression` class bridges the `scikit-learn` API and the `glmnetpp` backend.

``__init__(self)``
~~~~~~~~~~~~~~~~~~

* **Responsibility**: Initializes the model with `glmnetpp`’s default settings (no user-specified parameters like `C` or `penalty` in the initial version).
* **Mapping**: Configures the backend to use defaults sourced from `glmnet`’s R documentation or online resources.

``fit(self, X, y)``
~~~~~~~~~~~~~~~~~~~

* **Responsibility**: Trains the model using `glmnetpp`.
* **Process**:
  1. Validates and converts input `X` and `y` to NumPy arrays, then to Eigen matrices for `glmnetpp`.
  2. Calls a `glmnetpp` function (e.g., `elnet_driver`) with default settings.
  3. Stores the resulting coefficients and intercept as `self.coef_` and `self.intercept_`, following `scikit-learn` conventions.

``predict(self, X)``
~~~~~~~~~~~~~~~~~~~~

* **Responsibility**: Makes predictions on new data.
* **Process**: Uses `self.coef_` and `self.intercept_` to compute predictions, without direct `glmnetpp` calls.

5. Data Flow
------------

The data flow is simple:
1. The user provides data as NumPy arrays.
2. The `LogisticRegression` class validates and converts data to Eigen matrices.
3. The `glmnetpp` backend processes the data with default settings.
4. The wrapper returns results (e.g., coefficients, predictions) in a `scikit-learn`-compatible format.

6. Key Design Decision: Adopting the Scikit-learn API
------------------------------------------------------

The `scikit-learn` API was chosen over a direct port of the R `glmnet` API to ensure a Pythonic, user-friendly experience. The initial version simplifies usage by using `glmnetpp`’s defaults, hiding regularization complexity (e.g., `lambda` selection). This ensures seamless integration with `scikit-learn` tools while leveraging `glmnetpp`’s performance.