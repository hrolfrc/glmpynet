.. _phase_3_sklearn_api:

Phase 3: Scikit-learn Compatible API
====================================

**Objective:** To create a high-level, user-friendly Python class that
matches the Scikit-learn API and uses the C++ binding for its computations.

Model Name: `LogisticRegression`
--------------------------------

The primary user-facing class will be named ``LogisticRegression``. This
decision is a conscious choice to signal to users that the class is intended
as a direct, high-performance, drop-in replacement for
``sklearn.linear_model.LogisticRegression``.

While this creates the potential for a name conflict if both are imported
into the same namespace, this is a standard and well-understood aspect of
the Python import system. Users who need to compare both can use a standard
aliasing convention:

.. code-block:: python

   from glmpynet import LogisticRegression as GlmnetLogisticRegression
   from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression

The benefit of immediate user familiarity and seamless integration into
existing Scikit-learn workflows far outweighs this manageable risk.

API Design Philosophy: A Hybrid Approach
----------------------------------------

A key design challenge for this project is balancing the user familiarity of
the Scikit-learn API with the unique, high-performance capabilities of the
underlying ``glmnet`` engine. This project will adopt a **hybrid API** to
provide the best of both worlds: simplicity by default, with power on demand.

**Rationale:**
This approach is superior because it serves two distinct user groups without
compromising the experience for either:

1.  **The Scikit-learn User:** For the majority of users, the goal is seamless
    integration. They want to use our ``LogisticRegression`` class in their
    existing ``Pipeline`` and ``GridSearchCV`` workflows. By accepting standard
    parameters like ``C`` and ``penalty``, we provide a frictionless,
    "drop-in" experience.

2.  **The `glmnet` Power User:** A user familiar with the R `glmnet` package
    knows that its real power lies in computing the entire regularization path
    efficiently. Our API provides an "escape hatch" for these users, allowing
    them to bypass the Scikit-learn conventions and pass ``glmnet``-native
    parameters directly to the C++ engine for maximum performance and control.

**Implementation:**
The internal ``fit`` method will be responsible for translating the user-provided
parameters into the format required by the C++ binding, prioritizing the
``glmnet``-native parameters if they are provided.

API Contract
------------

The class will implement the standard Scikit-learn estimator interface.

* **``__init__(self, ...)``:** The constructor will accept both Scikit-learn
  and ``glmnet``-style parameters.

  .. code-block:: python

     def __init__(self,
                  # --- Scikit-learn Style Parameters (The Default) ---
                  penalty='l2',
                  C=1.0,

                  # --- Glmnet-Style Parameters (The "Escape Hatch") ---
                  alpha=None,
                  lambda_path=None,
                  nlambda=100,

                  # --- Other Glmnet Features ---
                  standardize=True,
                  # ... other glmnet parameters
                  ):
         # ...

* **Core Methods:** The class will implement all standard methods:
    * ``fit(self, X, y)``
    * ``predict(self, X)``
    * ``predict_proba(self, X)``
    * ``get_params()`` / ``set_params()``

Future Expansion
----------------

The ``glmnet`` library is capable of more than just logistic regression
(e.g., linear, Poisson, Cox regression). The API will be designed with
this in mind.

A potential future architecture would involve:
* A base class, ``GlmNetEstimator``, that handles the common logic of
    parameter translation and interaction with the C++ binding.
* Specific child classes for different models, such as ``LogisticRegression``,
    ``ElasticNet``, etc., that inherit from the base class.

This ensures that as we expand the library's functionality, we can do so
in a clean, modular, and maintainable way.
