.. glmpynet documentation master file

Welcome to glmpynet's documentation!
=====================================

**glmpynet** is a Python package providing a scikit-learn-compatible LogisticRegression API powered by the high-performance `glmnetpp` C++ library, focusing on regularized logistic regression for binary classification. The initial version uses `glmnetpp`’s default settings (sourced from `glmnet`’s R documentation or online resources) with core methods (`fit`, `predict`), with parameters like `C` and `penalty` planned for later releases. Built with Bazel and Conda for reproducibility, `glmpynet` ensures reliability through rigorous `glmnetpp` validation.

This documentation guides you through installing the package, using it in data science workflows, and understanding its design. Future versions may support multi-class classification and additional `glmnetpp` features.

Project Status
==============

`glmpynet` is in early development, focusing on validating the `glmnetpp` environment and implementing a minimal `LogisticRegression` with default settings. See the `ROADMAP` for details.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   usage_guide
   api_reference
   examples
   notebooks/index
   environment
   architecture
   development_guide
   project_information

Indices and tables
==================

Use the following to navigate the documentation:
* :ref:`genindex` - Alphabetical list of terms and classes
* :ref:`modindex` - List of `glmpynet` modules and functions
* :ref:`search` - Find specific topics or keywords