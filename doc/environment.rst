.. _environment:

Environment Setup
================

This page describes how to set up the Conda environment for using or developing `glmpynet`, a Python package providing a scikit-learn-compatible `LogisticRegression` API powered by `glmnetpp` for regularized logistic regression.

User Environment
---------------

To use `glmpynet`, you need Python 3.8 or higher. Install via PyPI:

.. code-block:: bash

   pip install glmpynet

This installs `glmpynet` and `numpy`, with the precompiled `glmnetpp` C++ library included, requiring no additional setup.

Developer Environment
--------------------

To develop `glmpynet` (e.g., build, test, or contribute), set up a Conda environment with the following dependencies:
- Python 3.8
- Bazel (for building `glmpynet` and `glmnetpp`)
- GCC 9.3.0+ or Clang 10.0.0+ (with OpenMP and Eigen)
- Python packages: `numpy`, `pandas`, `scikit-learn`, `pybind11`, `pytest`, `pytest-cov`, `pytest-mock`, `sphinx`, `sphinx_rtd_theme`, `nbsphinx`, `twine`, `build`

**Setup Instructions**:

1. **Install Miniconda**:
   - Download from https://docs.conda.io/en/latest/miniconda.html for your platform (Linux, macOS, Windows).
   - Install:
     .. code-block:: bash

        bash Miniconda3-latest-<platform>.sh

   - Open a new terminal to ensure Conda is available (`(base)` prompt).

2. **Create or Update the Environment**:
   - Save `environment.yml` (available in the project root) or use the one below.
   - Create or update the `glmpynet` environment:
     .. code-block:: bash

        conda env update -f environment.yml --prune
        conda activate glmpynet

3. **Verify Setup**:
   - Check versions:
     .. code-block:: bash

        python --version  # Should show 3.8.x
        bazel --version
        g++ --version  # or clang --version
        python -c "import numpy, pandas, sklearn, nbsphinx, pybind11"

**environment.yml**:

.. code-block:: yaml

   name: glmpynet
   channels:
     - conda-forge
     - defaults
   dependencies:
     - python=3.8
     - bazel
     - gcc>=9.3.0  # or clang>=10.0.0 for macOS
     - openmp
     - eigen
     - numpy
     - pandas
     - scikit-learn
     - pybind11
     - pytest
     - pytest-cov
     - pytest-mock
     - sphinx
     - sphinx_rtd_theme
     - nbsphinx
     - twine
     - build

Scikit-learn Estimator Guidelines
--------------------------------

To ensure `glmpynet.LogisticRegression` is compatible with `scikit-learn`, developers must follow these guidelines from the `scikit-learn developer guide <https://scikit-learn.org/stable/developers/develop.html>`_:
- **Keyword Arguments**: The `__init__` method has no parameters (uses `glmnetpp` defaults), allowing instantiation without arguments (e.g., `LogisticRegression()`).
- **No Computation in `__init__`**: Only assign attributes.
- **Required Methods**: Implement `fit` and `predict`, inheriting from `BaseEstimator` and `ClassifierMixin`. Future versions may add `predict_proba`, `get_params`, `set_params`.
- **Attribute Naming**: Use trailing underscores (e.g., `coef_`, `intercept_`) and validate with `check_is_fitted`.
- **Input Validation**: Use `check_X_y` in `fit` and `check_array` in `predict`, supporting NumPy arrays (sparse matrix support planned).
- **Testing**: Pass `check_estimator` tests for API compliance.
- **Documentation**: Include NumPyDoc docstrings with Parameters, Attributes, and Examples.

See :ref:`development_guide` for building and testing instructions.