.. _building_glmpynet:

Building glmpynet
=================

This document provides instructions for building the `glmpynet` Python package, which offers a scikit-learn-compatible `LogisticRegression` API powered by the `glmnetpp` C++ library. The initial version focuses on a minimal binding with default settings sourced from `glmnet`’s R documentation or online resources.

Steps to Build glmpynet
-----------------------

1. **Set Up Bazel**:
   - Ensure a `MODULE.bazel` file includes dependencies like `pybind11_bazel` and `rules_conda`.
   - Path: `/home/rolf/Downloads/glmnet_4.1-10/glmpynet/MODULE.bazel`.

2. **Write the Binding**:
   - Implement `glmpynet.cpp` to bind a `glmnetpp` function (e.g., `elnet_driver`) to `LogisticRegression` with `fit` and `predict` methods, using default settings.

3. **Build**:
   - Run:
   .. code-block:: bash

       bazel build //:glmpynet

4. **Test Locally**:
   - Run:
   .. code-block:: bash

        pytest tests/

   - Compare outputs to `scikit-learn`’s `LogisticRegression` defaults.

.. note::
   Building `glmpynet` requires a validated `glmnetpp` library. See :ref:`validating_glmnetpp` for details.