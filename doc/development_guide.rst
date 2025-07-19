.. _development_guide:

Development Guide
================

This guide provides instructions for developers to build, test, and contribute to `glmpynet`, a Python package offering a scikit-learn-compatible `LogisticRegression` API powered by `glmnetpp`, focusing on regularized logistic regression with default settings in its initial version.

Environment Setup
----------------

See :ref:`environment` for instructions to set up the Conda environment using `environment.yml`, including Python 3.8, Bazel, GCC/Clang, and Python packages (`numpy`, `pandas`, `scikit-learn`, etc.).

Validating glmnetpp
-------------------

Before developing, validate the `glmnetpp` library:

1. **Clone or Use glmnetpp**:
   - Clone the `glmnetpp` repository or use a local copy.
   - Ensure the `WORKSPACE` file includes dependencies (e.g., Eigen, GoogleTest).

2. **Build glmnetpp**:
   - Run:
     .. code-block:: bash

        bazel build //:glmnetpp

3. **Run All Tests**:
   - Execute:
     .. code-block:: bash

        bazel test -c dbg //test/...

   - Debug failures using `glmnetpp`’s `README.md`.

Building glmpynet
-----------------

To build the minimal `LogisticRegression` binding:

1. **Set Up Bazel**:
   - Create a `WORKSPACE` and `BUILD` file, including `pybind11_bazel` and `rules_conda`.

2. **Write the Binding**:
   - Implement `glmpynet.cpp` to bind a `glmnetpp` function (e.g., `elnet_driver`) to `LogisticRegression` with `fit` and `predict`, using default settings (sourced from `glmnet`’s R documentation or online resources).

3. **Build**:
   - Run:
     .. code-block:: bash

        bazel build //:glmpynet

4. **Test Locally**:
   - Run:
     .. code-block:: bash

        pytest tests/

   - Compare outputs to `scikit-learn`’s `LogisticRegression` defaults.

Contributing
------------

To contribute:
- Report bugs or suggest features via the GitHub issue tracker (https://github.com/hrolfrc/glmpynet).
- Submit pull requests with code, tests, or documentation updates, following `CONTRIBUTING.md`.
- Review `ROADMAP.md` and `DEVELOPMENT_PLAN.md` for project tasks.
- Update documentation:
  .. code-block:: bash

     sphinx-build -b html docs/ docs/_build

Next Steps
----------

- Review :ref:`architecture` for the `glmnetpp`-based design.
- See :ref:`environment` for dependency and setup details.
- Check `ROADMAP.md` and `DEVELOPMENT_PLAN.md` for milestones.