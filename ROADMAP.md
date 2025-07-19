# glmpynet ROADMAP

## Project Vision
`glmpynet` is a Python package delivering a high-performance `LogisticRegression` implementation using the `glmnetpp` C++ library, designed to mirror `scikit-learn`’s `LogisticRegression` API for user familiarity. Key objectives:
- **Performance**: Utilize `glmnetpp`’s optimized C++ solvers for fast logistic regression.
- **Reliability**: Ensure robustness through comprehensive testing, error handling, and bug isolation.
- **Reproducibility**: Use Bazel and Conda for consistent builds and environments.
- **User Familiarity**: Provide a `scikit-learn`-like API that works with minimal configuration.

The initial version focuses on core methods (`fit`, `predict`) using `glmnetpp`’s default settings (sourced from `glmnet`’s R documentation or online resources), deferring parameters like `C` and `penalty` to later phases.

## Milestones
1. **Establish Documentation and Validate `glmnetpp` Environment**:
   - Draft Sphinx documentation covering installation, usage (defaults-only `LogisticRegression`), and architecture.
   - Set up a Conda environment with `mamba`, installing Python 3.8+, Bazel, a C++ toolchain (GCC 9.3.0+ or Clang 10.0.0+), OpenMP, and Eigen, per `glmnetpp`’s `README.md`.
   - Build `glmnetpp` using `bazel build //:glmnetpp` (header-only library).
   - Run *all* `glmnetpp` tests (`bazel test -c dbg //test/...`) to confirm the library’s functionality.
   - **Goal**: Create clear documentation and ensure a reliable C++ foundation.

2. **Minimal `LogisticRegression` Binding**:
   - Create a `pybind11` binding for a core `glmnetpp` function (e.g., `elnet_driver`) to implement `glmpynet.LogisticRegression` with `fit` and `predict` methods.
   - Use `glmnetpp`’s default settings (sourced from `glmnet`’s R documentation or online resources).
   - Test locally with Python (`pytest`) to verify compatibility with `scikit-learn`’s default `LogisticRegression` behavior.
   - Update Sphinx documentation with usage details.
   - **Goal**: Deliver a functional, minimal `LogisticRegression` that works out of the box.

3. **Full `LogisticRegression` API**:
   - Extend the binding to support all `scikit-learn` `LogisticRegression` methods (`score`, `predict_proba`) and parameters (`C`, `penalty`, `max_iter`), mapping to `glmnetpp` equivalents.
   - Implement robust error handling (e.g., input validation, C++ exception handling, logging).
   - Test against `scikit-learn` benchmarks for correctness.
   - Update Sphinx documentation with full API details.
   - **Goal**: Provide a complete, `scikit-learn`-compatible API with enhanced reliability.

4. **CI/CD and PyPI Release**:
   - Set up CircleCI to replicate the Conda/Bazel environment, build `glmnetpp` and `glmpynet`, and run all `glmnetpp` tests and Python tests.
   - Package `glmpynet` for PyPI, ensuring reproducible builds.
   - Release the initial defaults-only version to PyPI.
   - **Goal**: Deliver a stable, tested package to users.

5. **Enhancements**:
   - Add advanced features (e.g., multi-class support, custom `glmnetpp` parameters).
   - Optimize performance (e.g., tune `glmnetpp` solvers).
   - Expand Sphinx documentation with advanced use cases and benchmarks.
   - **Goal**: Enhance functionality for broader adoption.

## Timeline (Tentative)
- **Milestone 1**: 2-3 weeks (Sphinx documentation, environment setup, `glmnetpp` validation).
- **Milestone 2**: 2-3 weeks (minimal binding and testing).
- **Milestone 3**: 3-4 weeks (full API and error handling).
- **Milestone 4**: 2-3 weeks (CI/CD and PyPI release).
- **Milestone 5**: Ongoing (enhancements).

## Open Questions
- Specific `glmnetpp` functions to bind for logistic regression.
- Alignment of `glmnetpp`’s default settings with `scikit-learn`’s defaults.
- Platform-specific build considerations (e.g., Linux vs. macOS).

**Analysis**:
- **Changes Made**: Added Sphinx drafting to Milestone 1 and removed prioritization of logistic regression tests, specifying *all* tests (`bazel test -c dbg //test/...`). Extended Milestone 1’s timeline slightly to account for documentation.
- **Alignment with Goals**: The roadmap supports simplicity (defaults-only initial binding), robustness (full `glmnetpp` testing), and momentum (clear milestones). It aligns with your emphasis on a verified library and avoids the previous failure’s environment issues.
