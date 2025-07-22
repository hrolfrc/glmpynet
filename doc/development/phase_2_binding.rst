.. _phase_2_binding:

Phase 2: Python-C++ Binding
===========================

**Objective:** To create a stable, low-level binding that exposes the
necessary ``glmnetpp`` functions and classes to Python, allowing for high-performance
computation driven by a Python interface.

Technical Strategy
------------------

Analysis of the ``glmnetpp`` source code revealed that it is a **header-only
template library**. This means there are no simple, pre-compiled C++ functions
to bind directly. The core logic, such as the ``ElnetDriver``, is heavily
templated and requires instantiation with specific data types.

Therefore, our strategy is to replicate the calling pattern found in the
``lognet_unittest.cpp`` file. We will create a **new C++ source file**
(e.g., ``glmpynet_binding.cpp``) that contains a simple, non-templated
"wrapper" function. This wrapper will be the sole entry point for Python.

The binding itself will be built using **pybind11**, a modern, header-only
library for creating Python bindings for C++ code. This choice is based
on its excellent integration with modern C++, STL data structures, and,
crucially, its seamless support for NumPy arrays.

The C++ Wrapper Function: API Contract
--------------------------------------

The new ``glmpynet_binding.cpp`` file will contain a single, primary
wrapper function with a clear, simple signature designed for Python.

**Proposed Function Signature:**
.. code-block:: cpp

   // Inside glmpynet_binding.cpp
   pybind11::dict fit_logistic_regression(
       pybind11::array_t<double> x,
       pybind11::array_t<double> y,
       double alpha,
       // ... other key parameters like nlam, flmin, etc.
   );

**Internal Logic:**
This function will be responsible for:
1.  Accepting NumPy arrays and scalar parameters from Python.
2.  Converting the NumPy arrays into the ``Eigen::Matrix`` data structures
    that ``glmnetpp`` requires.
3.  Creating a "data pack" of all the other required parameters (``maxit``,
    ``isd``, ``intr``, etc.), setting them to sensible defaults based on the
    original R library.
4.  Calling the complex, templated ``glmnetpp::transl::lognet`` function with
    all the prepared data.
5.  Extracting the key results (e.g., the coefficient matrix ``ca`` and the
    intercept vector ``a0``) from the output.
6.  Packaging these results into a Python dictionary and returning it.

Key Challenges
--------------

1.  **Data Marshaling:** The primary technical task is the efficient and
    correct conversion of data between Python/NumPy and C++/Eigen. This
    includes handling data types, matrix dimensions, and memory layout
    (e.g., row-major vs. column-major).

2.  **Parameter Mapping:** We must carefully analyze the numerous parameters
    of the ``transl::lognet`` function and determine which ones should be
    exposed to the Python user and which should be set to fixed, sensible
    defaults.

3.  **Error Handling:** The C++ wrapper must catch any exceptions thrown by
    the ``glmnetpp`` engine and translate them into Python exceptions to
    ensure the binding is robust.
