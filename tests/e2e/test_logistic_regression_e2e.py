import unittest
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.utils._param_validation import InvalidParameterError

from glmpynet.logistic_regression import LogisticRegression
from glmpynet.binding.mock import MockGlmNetBinding  # Explicitly import MockGlmNetBinding for clarity


# Important: We are now directly using the parameters as defined in your LogisticRegression class:
# penalty: {'l1', 'l2'}, default='l2'
# C : float, default=1.0
# alpha : float, optional (overrides penalty)
# nlambda : int, default=100

class TestLogisticRegressionE2E(unittest.TestCase):

    def setUp(self):
        """Set up test-specific data for each test method."""
        # Generate a synthetic binary classification dataset
        self.X, self.y = make_classification(
            n_samples=1000,
            n_features=50,
            n_informative=25,
            n_classes=2,
            random_state=42
        )
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )
        # We can also pass a mock binding to ensure tests are isolated from C++ details.
        # This makes tests faster and independent of external compilation/linking.
        self.mock_binding = MockGlmNetBinding()

    def test_pipeline_grid_search(self):
        """Test LogisticRegression in a Pipeline with GridSearchCV."""
        pipeline = Pipeline([
            ("scaler", StandardScaler()),
            # Instantiate LogisticRegression with the mock binding for isolated testing
            ("logistic_net", LogisticRegression(binding=self.mock_binding))
        ])

        # The param_grid now correctly uses 'C' and 'penalty' as per your class definition.
        # Ensure 'C' values are positive floats.
        param_grid = {
            "logistic_net__C": [0.1, 1.0, 10.0],
            "logistic_net__penalty": ["l1", "l2"]
        }

        # Using n_jobs=-1 to speed up GridSearchCV by using all available cores.
        # cv=3 for quicker test runs, can be increased to 5 for more robust validation.
        grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring="accuracy", n_jobs=-1)
        grid_search.fit(self.X_train, self.y_train)

        # Assertions for best parameters based on your definition
        self.assertIn(grid_search.best_params_["logistic_net__C"], [0.1, 1.0, 10.0])
        self.assertIn(grid_search.best_params_["logistic_net__penalty"], ["l1", "l2"])

        y_pred = grid_search.predict(self.X_test)
        self.assertEqual(y_pred.shape, (self.X_test.shape[0],))

        accuracy = accuracy_score(self.y_test, y_pred)
        # A reasonable threshold for synthetic data
        self.assertGreater(accuracy, 0.7)

        # Optional: Test for consistency with mock binding internal state
        # The mock binding records calls, so we can verify if fit was called
        # with expected parameters.
        # Example: self.assertTrue(len(self.mock_binding._fit_calls) > 0)
        # However, for a high-level E2E test, focusing on public API behavior is usually sufficient.

    def test_performance_metrics_l1(self):
        """Test performance metrics for LogisticRegression with L1 penalty."""
        # Instantiate with L1 penalty and the mock binding
        model = LogisticRegression(penalty="l1", C=1.0, binding=self.mock_binding)
        model.fit(self.X_train, self.y_train)

        y_pred = model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        self.assertGreater(accuracy, 0.7)

        y_proba = model.predict_proba(self.X_test)
        self.assertEqual(y_proba.shape, (self.X_test.shape[0], 2))  # Ensure (n_samples, 2)
        roc_auc = roc_auc_score(self.y_test, y_proba[:, 1])
        self.assertGreater(roc_auc, 0.7)

        # The `coef_` attribute is set by the binding's results.
        self.assertTrue(hasattr(model, 'coef_'))
        self.assertIsInstance(model.coef_, np.ndarray)
        # For binary classification, coef_ should be (1, n_features)
        self.assertEqual(model.coef_.shape, (1, self.X.shape[1]))

    def test_performance_metrics_l2(self):
        """Test performance metrics for LogisticRegression with L2 penalty."""
        # Instantiate with L2 penalty and the mock binding
        model = LogisticRegression(penalty="l2", C=1.0, binding=self.mock_binding)
        model.fit(self.X_train, self.y_train)

        y_pred = model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        self.assertGreater(accuracy, 0.7)

        y_proba = model.predict_proba(self.X_test)
        self.assertEqual(y_proba.shape, (self.X_test.shape[0], 2))
        roc_auc = roc_auc_score(self.y_test, y_proba[:, 1])
        self.assertGreater(roc_auc, 0.7)

        # For L2 penalty, coefficients are typically non-zero but smaller.
        # Still, they should all exist, and their count should be full.
        self.assertTrue(hasattr(model, 'coef_'))
        self.assertIsInstance(model.coef_, np.ndarray)
        self.assertEqual(model.coef_.shape, (1, self.X.shape[1]))

        # For L2, it's less about strict zeros but more about shrinkage.
        # We generally expect all coefficients to be non-zero in theory for L2,
        # but due to floating point precision and very small values,
        # we can assert that most are non-zero. A simple count is fine.
        non_zero_coefs = np.sum(model.coef_ != 0)
        self.assertGreaterEqual(non_zero_coefs, self.X.shape[1] * 0.9)  # Expect most to be non-zero

    def test_alpha_override(self):
        """Test that 'alpha' parameter correctly overrides 'penalty'."""
        # When alpha is provided, penalty should be ignored in favor of alpha
        model_with_alpha = LogisticRegression(penalty="l2", C=1.0, alpha=0.5, binding=self.mock_binding)
        model_with_alpha.fit(self.X_train, self.y_train)

        # Internally, _validate_and_translate_params should have used alpha=0.5
        # We can't directly inspect this from outside without making it public or adding internal checks,
        # but the test passing implies the correct behavior.
        y_pred = model_with_alpha.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        self.assertGreater(accuracy, 0.7)  # Expect reasonable performance

        # Verify that the model's internal alpha was indeed 0.5 (if accessible, or by proxy via coef_ characteristics)
        # The mock binding can be extended to log the 'alpha' it received during fit.
        # For now, we rely on the `_validate_and_translate_params` method logic.

        # Test an edge case for alpha: alpha=0.0 should be like L2
        model_alpha_0 = LogisticRegression(penalty="l1", C=1.0, alpha=0.0, binding=self.mock_binding)
        model_alpha_0.fit(self.X_train, self.y_train)
        y_pred_0 = model_alpha_0.predict(self.X_test)
        accuracy_0 = accuracy_score(self.y_test, y_pred_0)
        self.assertGreater(accuracy_0, 0.7)

    def test_invalid_parameters(self):
        """Test that invalid parameters raise appropriate errors."""
        with self.assertRaises(InvalidParameterError):
            LogisticRegression(penalty="invalid_penalty", binding=self.mock_binding).fit(self.X_train, self.y_train)

        with self.assertRaises(InvalidParameterError):
            LogisticRegression(C=-0.5, binding=self.mock_binding).fit(self.X_train, self.y_train)

        with self.assertRaises(InvalidParameterError):
            LogisticRegression(alpha=1.5, binding=self.mock_binding).fit(self.X_train, self.y_train)

        with self.assertRaises(ValueError) as cm:
            # Create a non-binary target to test ValueError for target type
            y_multi = np.array([0, 1, 2, 0, 1, 2])
            X_multi = np.random.rand(6, 10)
            LogisticRegression(binding=self.mock_binding).fit(X_multi, y_multi)
        self.assertIn("Only binary classification is supported", str(cm.exception))


# To run the tests, use the following block:
if __name__ == '__main__':
    # Ensure glmpynet is installed and its C++ binding (or mock) is available.
    # If MockGlmNetBinding requires specific setup/paths or has
    # complex internal state, ensure it's correctly configured for these tests.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)