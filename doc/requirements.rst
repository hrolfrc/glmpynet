.. _requirements:

Requirements
============

To use or develop `glmpynet`, ensure your environment and implementation meet the following requirements.

Software Requirements
---------------------

- **Python**: Version 3.7 or higher. Tested with Python 3.11.
- **Dependencies**:
  - `numpy`: Required for numerical computations.
  - `scikit-learn`: Required for the `LogisticNet` classifier and scikit-learn compatibility.
  - `scipy`: Automatically installed as a dependency of `scikit-learn`.

For development and testing, additional packages are recommended:

- `pytest`: For running unit and integration tests.
- `pytest-cov`: For test coverage reports.
- `pytest-mock`: For mocking in tests.
- `sphinx`: For building documentation.
- `sphinx_rtd_theme`: For the Read the Docs theme in documentation.
- `twine`: For publishing to PyPI.
- `build`: For creating Python package distributions.

These dependencies are listed in `requirements.txt` and `pyproject.toml` for easy installation.

Installation
------------

To install the required dependencies, use the provided `requirements.txt`:

.. code-block:: bash

   pip install -r requirements.txt

Alternatively, install `glmpynet` and its dependencies via `pip`:

.. code-block:: bash

   pip install glmpynet

Hardware Requirements
---------------------

- No specific hardware requirements beyond a standard computer capable of running Python 3.7+.
- For large datasets, ensure sufficient memory (e.g., 4GB RAM or more) for efficient computation with `numpy` and `scikit-learn`.

Scikit-learn Estimator Development Requirements
----------------------------------------------

To ensure `glmpynet` remains compatible with scikit-learn's estimator API, developers must follow these requirements from the `scikit-learn developer guide <https://scikit-learn.org/stable/developers/develop.html>`_:

- **Keyword Arguments with Defaults**: All `__init__` parameters must be keyword arguments with default values, allowing instantiation without arguments (e.g., `LogisticNet()`).
- **No Computation in `__init__`**: The `__init__` method should only assign parameters to attributes, not perform computation.
- **Required Methods**: Classifiers must implement `fit`, `predict`, and optionally `predict_proba`, `get_params`, and `set_params`, inheriting from `BaseEstimator` and `ClassifierMixin`.
- **Attribute Naming**: Learned parameters must have a trailing underscore (e.g., `coef_`, `intercept_`) and be validated with `check_is_fitted`.
- **Input Validation**: Use `check_X_y` in `fit` and `check_array` in `predict`/`predict_proba`, supporting sparse matrices if applicable.
- **Tag Specification**: Implement `__sklearn_tags__` to define capabilities (e.g., `requires_y`, `allow_nan`).
- **Parameter Handling**: `get_params` and `set_params` must handle all `__init__` parameters and support nested estimators.
- **Cloneability**: Estimators must be cloneable via `sklearn.base.clone` for use in `GridSearchCV` and `Pipeline`.
- **No Side Effects**: Methods like `predict` and `predict_proba` must not modify instance state or inputs.
- **Deterministic Behavior**: Estimators should be deterministic unless specified via the `non_deterministic` tag.
- **Testing**: Estimators must pass `check_estimator` tests for API compliance.
- **Documentation**: Include NumPyDoc-formatted docstrings with Parameters, Attributes, and Examples sections.

The `LogisticNet` class meets these requirements, ensuring compatibility with scikit-learn's ecosystem.

Notes
-----

- The `glmpynet` package is currently a facade over `scikit-learn`’s `LogisticRegression`. Future versions will integrate the `glmnet` library, which may introduce additional requirements.
- Ensure your `pip` and `setuptools` are up-to-date to avoid installation issues.