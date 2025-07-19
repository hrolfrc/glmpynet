.. _development_guide:

Development Guide
=================

This guide provides instructions for developers to set up the environment, validate the `glmnetpp` C++ library, build the `glmpynet` package, and contribute to the project. `glmpynet` is a Python package offering a scikit-learn-compatible `LogisticRegression` API powered by `glmnetpp`, focusing on regularized logistic regression with default settings in its initial version.

Environment Setup
-----------------

To develop `glmpynet`, set up a Conda environment with `mamba` and Bazel:

1. **Install Conda and `mamba`**:
   - Download and install Miniconda or Anaconda.
   - Install `mamba` for faster package management:
   .. code-block:: bash

        conda install mamba -c conda-forge

2. **Create the Environment**:
   - Use the provided `environment.yml` to create the `glmpynet` environment:
   .. code-block:: bash

        mamba env create -f environment.yml
        conda activate glmpynet

3. **Install Dependencies**:
   - Install Python 3.8+, Bazel, a C++ toolchain (GCC 9.3.0+ or Clang 10.0.0+), OpenMP, Eigen, and Python packages (`numpy`, `pybind11`, `pytest`, `sphinx`, etc.):
   .. code-block:: bash

        pip install -r requirements.txt

4. **Verify Setup**:
   - Check versions to ensure compatibility:
   .. code-block:: bash

        python --version
        bazel --version
        g++ --version  # or clang --version

See :ref:`requirements` for a full list of dependencies.

Validating glmnetpp
-------------------

Before developing, validate the `glmnetpp` library to ensure a reliable foundation:

1. **Clone or Use glmnetpp**:
   - Clone the `glmnetpp` repository or use a local copy.
   - Ensure the `WORKSPACE` file includes dependencies (e.g., Eigen, GoogleTest).

2. **Build glmnetpp**:
   - Run:
   .. code-block:: bash

        bazel build //:glmnetpp

3. **Run All Tests**:
   - Execute the full test suite to confirm functionality:
   .. code-block:: bash

        bazel test -c dbg //test/...

   - Debug failures using `glmnetpp`’s `README.md` (e.g., missing Eigen or OpenMP).

Building glmpynet
-----------------

To build the minimal `LogisticRegression` binding:

1. **Set Up Bazel**:
   - Create a `WORKSPACE` and `BUILD` file for `glmpynet`, including `pybind11_bazel` and `rules_conda`.

2. **Write the Binding**:
   - Implement `glmpynet.cpp` to bind a `glmnetpp` function (e.g., `elnet_driver`) to `LogisticRegression` with `fit` and `predict`, using default settings (sourced from `glmnet`’s R documentation or online resources).

3. **Build**:
   - Run:
   .. code-block:: bash

        bazel build //:glmpynet

4. **Test Locally**:
   - Use `pytest` to test the binding:
   .. code-block:: bash

        pytest tests/

   - Compare outputs to `scikit-learn`’s `LogisticRegression` defaults on a simple dataset.

Contributing
------------

To contribute:
- **Report Bugs**: Use the GitHub issue tracker.
- **Suggest Features**: Submit feature requests via issues, referencing `ROADMAP.md`.
- **Submit Pull Requests**: Fork the repository, create a branch, and submit a pull request with tests and documentation updates. Follow `CONTRIBUTING.md` guidelines.
- **Update Documentation**: Edit Sphinx files (e.g., `index.rst`, `usage_guide.rst`) and verify with:
.. code-block:: bash

     sphinx-build -b html docs/ docs/_build

Next Steps
----------

- Review :ref:`architecture` for the `glmnetpp`-based design.
- See :ref:`requirements` for dependency details.
- Check `ROADMAP.md` and `DEVELOPMENT_PLAN.md` for project milestones and tasks.