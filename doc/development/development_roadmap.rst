.. _development_roadmap:

glmpynet: Development Roadmap
=============================

Project Vision
--------------

`glmpynet` is a Python package delivering a high-performance ``LogisticRegression`` implementation using the ``glmnetpp`` C++ library, designed to mirror ``scikit-learn``’s ``LogisticRegression`` API for user familiarity.

Key objectives:

* **Performance**: Utilize ``glmnetpp``’s optimized C++ solvers for fast logistic regression.
* **Reliability**: Ensure robustness through comprehensive testing, error handling, and bug isolation.
* **Reproducibility**: Use Bazel and Conda for consistent builds and environments.
* **User Familiarity**: Provide a ``scikit-learn``-like API that works with minimal configuration.

Development Strategy
--------------------

The project will follow a phased, incremental development model that prioritizes a stable foundation and clear design before implementation.

1.  **Foundation First:** We will begin by rigorously analyzing, building, and testing the core ``glmnetpp`` C++ engine to ensure a reliable foundation.
2.  **API-First Design:** For each subsequent layer (the Python binding and the Scikit-learn API), we will first create documentation that defines the API contract. This ensures the implementation is guided by a clear and well-understood design.
3.  **Incremental Implementation:** Each phase is broken down into small, testable tasks that can be completed and verified independently.

Phased Roadmap
--------------

### Phase 1: `glmnetpp` Foundation Verification

* **Goal:** To systematically verify, debug, and confirm that the core C++ engine can be reliably built, tested, and benchmarked.
* **Key Activities:**
    * Perform a static analysis of the Bazel build system to uncover all true dependencies and requirements.
    * Follow a detailed action plan to verify the environment, generate the ``.bazelrc``, and achieve a successful build.
    * Execute the full C++ unit test suite to confirm correctness.
    * Execute the C++ benchmark suite to establish a performance baseline.
* **Deliverable:** A stable, reproducible build of the ``glmnetpp`` library and a complete set of passing tests.
* **Detailed Plan:** See :doc:`phase_1_analysis` and :doc:`phase_1_action_plan`.

### Phase 2: Python-C++ Binding

* **Goal:** To create a stable, low-level binding that exposes the necessary ``glmnetpp`` functions to Python.
* **Key Activities:**
    * Design the binding's API, focusing initially on the functions required for logistic regression.
    * Implement the binding using ``pybind11``, with a focus on efficient data marshaling between NumPy and Eigen.
    * Write unit tests to verify that the bound C++ functions can be called correctly from Python.
* **Deliverable:** A compiled Python extension module that wraps the core ``glmnetpp`` solver.
* **Detailed Plan:** See :doc:`phase_2_binding`.

### Phase 3: Scikit-learn API Implementation

* **Goal:** To create a high-level, user-friendly ``LogisticNet`` class that is a drop-in replacement for ``scikit-learn``’s ``LogisticRegression``.
* **Key Activities:**
    * Implement the ``fit``, ``predict``, and ``predict_proba`` methods, using the C++ binding for all computations.
    * Ensure full compatibility with the Scikit-learn ecosystem by passing the ``check_estimator`` tests.
    * Implement robust error handling and input validation.
* **Deliverable:** A fully tested and documented ``LogisticNet`` Python class.
* **Detailed Plan:** See :doc:`phase_3_sklearn_api`.

### Phase 4: CI/CD and Public Release

    * **Goal:** To automate the build and test process and deliver a stable, installable package to users.
    * **Key Activities:**
        * Configure a CircleCI pipeline to replicate the Conda/Bazel environment and run all C++ and Python tests on every commit.
        * Package the project for distribution on PyPI.
        * Publish the first official version.
    * **Deliverable:** A publicly available package on PyPI and a green CI pipeline.

Known Risks & Open Questions
----------------------------

This project involves integrating with a complex C++ library whose build system has already proven to be incompletely documented. This introduces several known risks and open questions that will be addressed during Phase 1.

* **Build System Instability:** The initial build failures demonstrate that the Bazel configuration is fragile and may contain other undiscovered issues.
* **Test Suite Integrity:** A foundational assumption is that the ``glmnetpp`` test suite is complete and correct. We may discover that the tests themselves are broken or that the most critical logic is not covered.
* **Binding Complexity:** The exact ``glmnetpp`` functions to bind for logistic regression are not yet identified. This will require code-level analysis of the C++ library.
* **API Alignment:** A key challenge in Phase 3 will be aligning ``glmnetpp``’s internal parameters (e.g., for regularization) with ``scikit-learn``’s user-facing parameters (e.g., ``C``).

Future Enhancements
-------------------

Once the core functionality is delivered, future work will focus on expanding the library's capabilities.

* **Full API Support:** Extend the binding to support all ``scikit-learn`` ``LogisticRegression`` parameters (e.g., ``C``, ``penalty``).
* **Multi-Class Support:** Implement support for multi-class classification.
* **Additional Models:** Add support for other models available in ``glmnet``, such as linear or Poisson regression.
