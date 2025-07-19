.. _requirements:

Requirements
============

To use or develop `glmpynet`, ensure your environment meets the following requirements.

Software Requirements for Users
-------------------------------

- **Python**: Version 3.8 or higher. Tested with Python 3.11.

Installation for Users
----------------------

Install `glmpynet` via PyPI with `pip`, which automatically installs `numpy`:

.. code-block:: bash

   pip install glmpynet

The package includes the precompiled `glmnetpp` C++ library, requiring no additional setup.

Software Requirements for Developers
------------------------------------

To build `glmpynet` from source or run tests, additional tools are required:
- **Conda**: For environment management, with `mamba` recommended for faster package installation.
- **Bazel**: For building `glmpynet` and `glmnetpp` (header-only C++ library).
- **C++ Toolchain**: GCC 9.3.0+ or Clang 10.0.0+, with OpenMP and Eigen libraries.
- **Dependencies**:
  - `numpy`: For numerical computations.
  - `pybind11`: For binding `glmnetpp` to Python.
  - `pytest`: For running unit and integration tests.
  - `pytest-cov`: For test coverage reports.
  - `pytest-mock`: For mocking in tests.
  - `sphinx`: For building documentation.
  - `sphinx_rtd_theme`: For the Read the Docs theme.
  - `twine`: For publishing to PyPI.
  - `build`: For creating Python package distributions.

These dependencies are listed in `requirements.txt` and `pyproject.toml`.

Installation for Developers
---------------------------

Set up a Conda environment and install dependencies:

.. code-block:: bash

   mamba env create -f environment.yml
   conda activate glmpynet
   pip install -r requirements.txt

See :ref:`development_guide` for detailed Conda and Bazel setup instructions.

Hardware Requirements
---------------------

- No specific hardware requirements beyond a standard computer capable of running Python 3.8+.
- For large datasets, ensure sufficient memory (e.g., 4GB RAM or more) for efficient computation with `glmnetpp` and `numpy`.
- Developers building from source need a system capable of compiling C++ code.

Scikit-learn Estimator Development Requirements
-----------------------------------------------

To ensure `glmpynet.LogisticRegression` remains compatible with `scikit-learn`’s estimator API, developers must follow these requirements from the `scikit-learn developer guide <https://scikit-learn.org/stable/developers/develop.html>`_:

- **Keyword Arguments with Defaults**: The `__init__` method has no parameters in the initial version (uses `glmnetpp` defaults), allowing instantiation without arguments (e.g., `LogisticRegression()`).
- **No Computation in `__init__`**: The `__init__` method only assigns attributes.
- **Required Methods**: Implements `fit` and `predict`, inheriting from `BaseEstimator` and `ClassifierMixin`. Future versions may add `predict_proba`, `get_params`, and `set_params`.
- **Attribute Naming**: Learned parameters use a trailing underscore (e.g., `coef_`, `intercept_`) and are validated with `check_is_fitted`.
- **Input Validation**: Uses `check_X_y` in `fit` and `check_array` in `predict`, supporting NumPy arrays (sparse matrix support planned).
- **Tag Specification**: Implements `__sklearn_tags__` for capabilities (e.g., `requires_y`, `allow_nan`).
- **Parameter Handling**: Future `get_params` and `set_params` will handle parameters when added.
- **Cloneability**: Ensures cloneability via `sklearn.base.clone` for `Pipeline` and `GridSearchCV`.
- **No Side Effects**: `predict` does not modify instance state or inputs.
- **Deterministic Behavior**: Ensures deterministic results unless specified via the `non_deterministic` tag.
- **Testing**: Must pass `check_estimator` tests for API compliance.
- **Documentation**: Includes NumPyDoc-formatted docstrings with Parameters, Attributes, and Examples sections.

The `LogisticRegression` class meets these requirements for the defaults-only implementation.

Notes
-----

- `glmpynet` uses the `glmnetpp` C++ library, with default settings sourced from `glmnet`’s R documentation or online resources.
- Users only need `pip` and Python 3.8+ for installation, as `glmnetpp` and `numpy` are handled by the PyPI package.
- Developers should ensure `mamba`, `bazel`, and `pip` are up-to-date to avoid build issues.
- Future versions will add support for parameters (e.g., `C`, `penalty`) and features like multi-class classification.