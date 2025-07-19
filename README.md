# glmpynet

[![CircleCI](https://circleci.com/gh/hrolfrc/glmpynet.svg?style=shield)](https://circleci.com/gh/hrolfrc/glmpynet)
[![ReadTheDocs](https://readthedocs.org/projects/glmpynet/badge/?version=latest)](https://glmpynet.readthedocs.io/en/latest/)
[![Codecov](https://codecov.io/gh/hrolfrc/glmpynet/branch/master/graph/badge.svg)](https://codecov.io/gh/hrolfrc/glmpynet)

## glmnetpp-based Logistic Regression for Scikit-Learn

**glmpynet** is a Python package that provides a scikit-learn-compatible LogisticRegression API powered by the high-performance `glmnetpp` C++ library, focusing on regularized logistic regression for binary classification. The initial version uses `glmnetpp`’s default settings (sourced from `glmnet`’s R documentation or online resources) for core methods (`fit`, `predict`), with parameters like `C` and `penalty` planned for later releases.

This project bridges the computational speed of `glmnetpp` with the ease-of-use of the Python data science ecosystem, acting as a drop-in replacement for `sklearn.linear_model.LogisticRegression`.

## Key Features

* **High Performance**: Leverages the optimized `glmnetpp` C++ backend for fitting models, suitable for large datasets.
* **Scikit-learn Compatible**: Implements `fit` and `predict` methods, enabling seamless integration with `sklearn` pipelines and tools.
* **Robust Development**: Built with Bazel and Conda for reproducible builds, with comprehensive `glmnetpp` testing for reliability.

## Installation

Once released, install `glmpynet` via pip:

    pip install glmpynet

## Quick Start

Using `glmpynet` is as simple as any scikit-learn estimator.

    import numpy as np
    from glmpynet import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    # 1. Generate synthetic data
    X, y = np.random.rand(100, 10), np.random.randint(0, 2, 100)
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # 2. Instantiate and fit the model
    model = LogisticRegression()  # Uses glmnetpp defaults
    model.fit(X_train, y_train)

    # 3. Make predictions
    y_pred = model.predict(X_test)

    # 4. Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

## Project Status

`glmpynet` is in early development, focusing on drafting Sphinx documentation, validating the `glmnetpp` environment with all tests, and implementing a minimal `LogisticRegression` with default settings. Future releases will add parameters (e.g., `C`, `penalty`) and advanced features like multi-class support. See `ROADMAP.md` for details.

## Contributing

Contributions are welcome! See `CONTRIBUTING.md` for guidelines on reporting bugs, suggesting features, or submitting pull requests.

## License

This project is distributed under the MIT License.