# glmpynet: Project Roadmap

This document outlines the development plan for `glmpynet`. With the initial documentation and API stubs in place for binary logistic regression, this roadmap focuses on implementing the core functionality and expanding the library to support the other powerful models offered by the `glmnet` backend.

## Foundational Priority: Core Implementation & Quality

This is the ongoing priority to ensure the project is robust, reliable, and maintainable.

### 1. Implement the `LogisticNet` Core

* **Goal:** To build the working backend for the `LogisticNet` class, including the interface to the compiled `glmnet` code and the automatic cross-validation for lambda selection.
* **Status:** In progress.

### 2. Increase Test Coverage to >90%

* **Goal:** To ensure all critical application logic is verified by automated tests, providing confidence in the correctness of the wrapper.
* **Strategy:**
  * Write unit tests for all data preparation and result parsing logic.
  * Create integration tests that verify the interaction with the `glmnet` backend using small, controlled datasets.
  * Ensure all scikit-learn compatibility checks are passed.

## Priority 1: Linear Regression (Gaussian Models)

This is the most common use case for `glmnet` after logistic regression and is the highest priority for expansion.

### Create a `LinearNet` Estimator

* **Goal:** To provide a scikit-learn compatible regressor for performing regularized linear regression.
* **Implementation Steps:**
  1. Create a new `LinearNet` class that inherits from `sklearn.base.RegressorMixin`.
  2. Implement the `.fit()` method to call the `glmnet` backend with the "gaussian" family option.
  3. Implement the `.predict()` method to return continuous value predictions.
  4. Add comprehensive tests to verify its performance and scikit-learn compatibility.

## Priority 2: Multi-Class Classification

This feature extends the library's classification capabilities beyond binary problems.

### Enhance `LogisticNet` or Create `MultinomialNet`

* **Goal:** To support multi-class classification using the multinomial logistic regression capabilities of `glmnet`.
* **Implementation Steps:**
  1. Decide on the best API: either add multi-class handling to the existing `LogisticNet` or create a new, dedicated `MultinomialNet` class.
  2. Implement the `.fit()` method to call the `glmnet` backend with the "multinomial" family option.
  3. Ensure that `.predict()` and `.predict_proba()` correctly handle multi-class outputs (e.g., shape of `(n_samples, n_classes)` for probabilities).
  4. Add tests for multi-class scenarios.

## Priority 3: Other `glmnet` Models

These features would round out the library, providing wrappers for the more specialized models available in `glmnet`.

### 1. Add Cox Proportional Hazards Model

* **Goal:** To provide a wrapper for survival analysis.
* **Action:** Create a `CoxNet` class that interfaces with `glmnet`'s "cox" family, designed for time-to-event data.

### 2. Add Poisson Regression Model

* **Goal:** To provide a wrapper for modeling count data.
* **Action:** Create a `PoissonNet` class that interfaces with `glmnet`'s "poisson" family.