# glmpynet DEVELOPMENT PLAN

## Objective
Establish a clear project foundation by drafting Sphinx documentation, validating the `glmnetpp` environment, and creating a minimal `glmpynet.LogisticRegression` implementation with default settings. This plan covers the first milestone from `ROADMAP.md`, focusing on documentation and validation, and starts the second milestone (minimal binding).

## Steps
1. **Draft Sphinx Documentation**:
   - Create a Sphinx project structure for `glmpynet`.
   - Document:
     - **Introduction**: Overview of `glmpynet` as a `glmnetpp`-powered, `scikit-learn`-compatible `LogisticRegression` package.
     - **Installation**: Instructions for setting up Conda with `mamba`, Python 3.8+, Bazel, GCC/Clang, OpenMP, and Eigen, based on `glmnetpp`’s `README.md`.
     - **Usage**: Basic example of `glmpynet.LogisticRegression` with `fit` and `predict`, using `glmnetpp`’s default settings (sourced from `glmnet`’s R documentation or online resources). Note that parameters like `C`, `penalty` are not yet supported.
     - **Architecture**: Describe `glmpynet` as a Python binding to `glmnetpp` via `pybind11`, built with Bazel/Conda.
     - **Development**: Outline environment setup, validation, and contribution guidelines.
   - Review and refine documentation for clarity and alignment.
   - **Success Criterion**: Sphinx documentation is complete, accessible, and reflects the defaults-only approach.

2. **Set Up Conda Environment**:
   - Install `mamba` for faster package management.
   - Create the `glmnetpp` environment (`mamba env create`), installing Python 3.8+, Bazel, a C++ toolchain (GCC 9.3.0+ or Clang 10.0.0+), OpenMP, and Eigen.
   - Verify the environment: Activate (`conda activate glmnetpp`) and check versions (`python --version`, `g++ --version`, `bazel --version`).
   - **Success Criterion**: Environment is set up and dependencies are installed correctly.

3. **Validate `glmnetpp` Build and Tests**:
   - Clone or use the local `glmnetpp` repository, ensuring the `WORKSPACE` file includes dependencies (e.g., Eigen, GoogleTest).
   - Build `glmnetpp`: Run `bazel build //:glmnetpp` for the header-only library.
   - Run *all* tests: Execute `bazel test -c dbg //test/...` to confirm the library’s functionality.
   - Debug failures (e.g., missing dependencies, OpenMP issues) using `glmnetpp`’s `README.md` guidance.
   - **Success Criterion**: All `glmnetpp` tests pass, confirming a functional C++ library.

4. **Create Minimal `LogisticRegression` Binding**:
   - Set up a Bazel `WORKSPACE` and `BUILD` file for `glmpynet`, adding `pybind11_bazel` and `rules_conda`.
   - Write a `glmpynet.cpp` file to bind a core `glmnetpp` function (e.g., `elnet_driver`) to `glmpynet.LogisticRegression`, implementing `fit` and `predict` with `glmnetpp`’s default settings (sourced from `glmnet`’s R documentation or online resources).
   - Build: Run `bazel build //:glmpynet`.
   - Test: Write a Python script with `pytest` to call `fit` and `predict`, comparing outputs to `scikit-learn`’s default `LogisticRegression` for a simple dataset.
   - **Success Criterion**: Binding works, producing correct predictions with defaults.

5. **Update Documentation**:
   - Update Sphinx with minimal binding usage details and validation results.
   - Update `ROADMAP.md` to reflect completion of Milestone 1 and progress on Milestone 2.
   - Refine `DEVELOPMENT_PLAN.md` for next steps (e.g., full API, CI setup).
   - **Success Criterion**: Documentation reflects the current state and next steps.

## Notes
- **Defaults**: `glmnetpp`’s default settings will be sourced from `glmnet`’s R documentation or online resources, ensuring the minimal binding works without user-specified parameters.
- **Testing**: Running all `glmnetpp` tests ensures comprehensive validation, as per feedback, avoiding partial testing risks.
- **Debugging**: Use `glmnetpp`’s `README.md`, test suite, or headers to resolve issues during validation or binding.
- **Next Steps**: After this plan, move to the full `LogisticRegression` API (Milestone 3), adding parameters and error handling.

**Analysis**:
- **Changes Made**: Reordered steps to prioritize Sphinx drafting (Step 1) before validation (Steps 2-3). Removed prioritization of logistic regression tests, specifying *all* tests. Adjusted steps to reflect defaults-only binding.
- **Alignment with Goals**: The plan supports simplicity (defaults-only binding), robustness (full `glmnetpp` testing), and momentum (actionable steps). Drafting Sphinx first ensures clarity, addressing your goal of a concrete plan.
- **Previous Failure**: Prioritizing documentation and full testing avoids the environment issues that stalled the `setuptools` attempt.
- **Bug Isolation**: Running all `glmnetpp` tests ensures C++ issues are caught early, per your feedback, supporting your concern about distinguishing bugs.

### Sphinx Documentation Outline

**Purpose**: Provide user- and developer-facing documentation for `glmpynet`, covering installation, usage, architecture, and development, focusing on the defaults-only `LogisticRegression` and `glmnetpp`-only backend.

**Outline**:

- **Introduction**:
  - Overview: `glmpynet` is a Python package providing a high-performance `LogisticRegression` using `glmnetpp`’s C++ backend, compatible with `scikit-learn`’s API.
  - Goals: Fast, reliable logistic regression with minimal configuration.
  - Initial Scope: Core methods (`fit`, `predict`) with `glmnetpp`’s default settings (sourced from `glmnet`’s R documentation or online resources).

- **Installation**:
  - Prerequisites: Python 3.8+, Conda (`mamba`), Bazel, C++ toolchain (GCC 9.3.0+ or Clang 10.0.0+), OpenMP, Eigen.
  - Steps:
    - Install `mamba` and create `glmnetpp` environment (`mamba env create`).
    - Install Bazel and dependencies.
    - Build `glmpynet` (once available) via `bazel build` and install with `pip`.
  - Troubleshooting: Common issues (e.g., missing `python3-dev`, Conda activation).

- **Usage**:
  - Quickstart:
    - Example: `from glmpynet import LogisticRegression; model = LogisticRegression(); model.fit(X, y); model.predict(X)`.
    - Note: Uses `glmnetpp`’s defaults; parameters like `C`, `penalty` not yet supported.
  - Basic Use Case: Binary classification with NumPy arrays, mirroring `scikit-learn`.
  - Future Plans: Full API with parameters in later versions.

- **Architecture**:
  - Overview: `glmpynet` binds `glmnetpp`’s C++ functions (e.g., `elnet_driver`) to Python via `pybind11`, built with Bazel/Conda.
  - Data Flow: NumPy arrays converted to Eigen matrices for `glmnetpp`, results returned to Python.
  - Initial Scope: Defaults-only `LogisticRegression` with `fit` and `predict`.

- **Development Guide**:
  - Environment Setup: Conda/Bazel instructions from `glmnetpp`’s `README.md`.
  - Validation: Build `glmnetpp` (`bazel build //:glmnetpp`) and run all tests (`bazel test -c dbg //test/...`).
  - Binding: Create `pybind11` binding for `LogisticRegression` with defaults.
  - Testing: Use `pytest` to verify Python binding against `scikit-learn` defaults.
  - Contributing: Guidelines for adding features, tests, and documentation.

- **FAQ**:
  - How does `glmpynet` differ from `scikit-learn`’s `LogisticRegression`? (Uses `glmnetpp` for performance, initially defaults-only.)
  - When will parameters like `C`, `penalty` be supported? (Planned for Milestone 3.)
  - How to troubleshoot build issues? (Check Conda/Bazel setup, consult `glmnetpp`’s `README.md`.)

**Analysis**:
- **Alignment with Goals**: The Sphinx outline supports simplicity (defaults-only usage), robustness (documents testing and validation), and clarity (explains `glmnetpp`-only approach). Drafting first ensures alignment, per your preference.
- **Defaults Focus**: Notes that `LogisticRegression` uses `glmnetpp`’s defaults (from R documentation or online), aligning with your instruction.
- **Previous Failure**: Documents the Conda/Bazel setup to avoid environment issues, building on the lesson from the `setuptools` failure.
- **Momentum**: Concise, focused content ensures quick drafting, enabling a smooth transition to validation.

### Integration and Rationale
- **Running All Tests**: Specifying `bazel test -c dbg //test/...` for all `glmnetpp` tests ensures comprehensive validation, addressing your concern about incomplete testing. This strengthens bug isolation and confirms the library’s reliability, per your goal of a verified foundation.
- **Sphinx First**: Drafting Sphinx before validation aligns us on the project’s scope (defaults-only, `glmnetpp`-only) and documents the environment setup, reducing the risk of errors during validation. It supports your goal of a concrete plan and prevents misalignment like the previous failure.
- **Defaults-Only Approach**: Using `glmnetpp`’s defaults (sourced from R documentation or online) simplifies the binding and documentation, aligning with your suggestion to avoid parameters initially and ensuring momentum.
- **Robustness and Compatibility**: Full `glmnetpp` testing and planned CI integration (in `DEVELOPMENT_PLAN.md`) ensure reliability and catch tool evolution issues, per your concerns.
- **Momentum**: The concise drafts and clear steps maintain progress, addressing the previous failure’s stall.

### Potential Risks and Mitigations
1. **Documentation Effort**:
   - **Risk**: Drafting Sphinx first may delay validation.
   - **Mitigation**: The outline is minimal and focused, prioritizing essential sections (installation, usage) to balance effort and progress.
2. **Default Settings Uncertainty**:
   - **Risk**: `glmnetpp`’s defaults may differ from `scikit-learn`’s, affecting usability.
   - **Mitigation**: Sphinx notes defaults are `glmnetpp`-based, and Step 4 tests against `scikit-learn` outputs to ensure compatibility.
3. **Validation Failures**:
   - **Risk**: `glmnetpp` tests may fail due to environment issues.
   - **Mitigation**: Sphinx documents the setup, and `DEVELOPMENT_PLAN.md` includes debugging guidance, leveraging `glmnetpp`’s `README.md`.