.. _phase_2_binding:

Phase 2: Python-C++ Binding
===========================

**Objective:** To create a stable, low-level binding that exposes the
necessary ``glmnetpp`` functions and classes to Python, allowing for high-performance
computation driven by a Python interface.

Technical Strategy
------------------

The binding layer will be built using **pybind11**, a modern, header-only
library for creating Python bindings for C++ code. This choice is based
on its excellent integration with modern C++, STL data structures, and,
crucially, its seamless support for NumPy arrays.

Key Challenges
--------------

1.  **Data Marshaling:** The primary task is to efficiently convert data
    between Python and C++. This will involve:
    * Mapping NumPy arrays (the standard for data in Scikit-learn) to
        ``Eigen::Matrix`` objects, which are used by ``glmnetpp``.
    * Ensuring data is passed by reference where possible to avoid
        unnecessary copies, which is critical for performance.

2.  **API Design:** The binding will not expose the entire ``glmnetpp``
    library. Instead, it will be a targeted wrapper around the specific
    functions required to train a regularized logistic regression model.

Initial Functions to Bind
-------------------------

Based on the goal of replicating ``LogisticRegression``, the initial
binding will need to expose C++ functions that allow us to:

* Initialize the core ``glmnetpp`` solver with model parameters.
* Pass training data (X and y) to the solver.
* Execute the fitting algorithm.
* Retrieve the calculated coefficients (the model weights).