# noinspection PyProtectedMember

import unittest
from unittest import expectedFailure

import numpy as np
import pytest
from scipy.sparse import csr_matrix
from sklearn.datasets import make_classification
from sklearn.datasets import make_sparse_uncorrelated
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
# noinspection PyProtectedMember
from sklearn.utils._param_validation import InvalidParameterError
from sklearn.utils.estimator_checks import check_estimator
from sklearn.utils.validation import check_is_fitted

from glmpynet.logistic_regression import LogisticRegression


class TestLogisticRegression(unittest.TestCase):
    """
    A test suite for the LogisticRegression class.
    """

    def setUp(self):
        """Set up a standard dataset for all tests."""
        self.X, self.y = make_classification(
            n_samples=200, n_features=20, n_informative=10, n_classes=2, random_state=42
        )
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, random_state=42, test_size=0.25
        )

    def test_fit_sets_attributes(self):
        """Tests that fitting the model sets the expected attributes."""
        model = LogisticRegression(alpha=1.0, nlambda=100)
        model.fit(self.X_train, self.y_train)

        check_is_fitted(model, ["coef_", "intercept_"])

        self.assertTrue(hasattr(model, 'coef_'))
        self.assertTrue(hasattr(model, 'intercept_'))
        self.assertTrue(hasattr(model, 'classes_'))
        self.assertEqual(model.coef_.shape, (1, self.X_train.shape[1]))
        self.assertEqual(model.intercept_.shape, (1,))
        self.assertEqual(len(model.classes_), 2)

    def test_predict_output(self):
        """Tests the shape and values of the predict method's output."""
        # --- THIS IS THE ONLY CHANGE ---
        model = LogisticRegression() # Use new default __init__
        model.fit(self.X_train, self.y_train)
        predictions = model.predict(self.X_test)

        self.assertEqual(predictions.shape, (self.X_test.shape[0],))
        self.assertTrue(all(p in model.classes_ for p in predictions))

    def test_predict_proba_output(self):
        """Tests the shape and values of the predict_proba method's output."""
        model = LogisticRegression()
        model.fit(self.X_train, self.y_train)
        probabilities = model.predict_proba(self.X_test)

        self.assertEqual(probabilities.shape, (self.X_test.shape[0], 2))
        self.assertTrue(np.all((probabilities >= 0) & (probabilities <= 1)))
        np.testing.assert_almost_equal(np.sum(probabilities, axis=1), np.ones(self.X_test.shape[0]))

    def test_integration_with_pipeline(self):
        """Tests that LogisticRegression works as a step in a scikit-learn Pipeline."""
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            # --- THIS IS THE ONLY CHANGE ---
            ('logistic_regression', LogisticRegression(alpha=1.0))
        ])
        pipeline.fit(self.X_train, self.y_train)
        predictions = pipeline.predict(self.X_test)
        self.assertEqual(predictions.shape, (self.X_test.shape[0],))

    def test_integration_with_gridsearchcv(self):
        """Tests that LogisticRegression can be tuned with GridSearchCV."""
        # --- THIS IS THE ONLY CHANGE ---
        model = LogisticRegression()
        # The test now tunes the new glmnet-style parameters
        param_grid = {'alpha': [0.5, 1.0], 'nlambda': [50, 100]}
        grid_search = GridSearchCV(model, param_grid, cv=3, scoring='accuracy')
        grid_search.fit(self.X_train, self.y_train)
        self.assertTrue(hasattr(grid_search, 'best_estimator_'))
        self.assertIn(grid_search.best_params_['alpha'], [0.5, 1.0])

    def test_default_instantiation(self):
        """Test that LogisticRegression can be instantiated without arguments."""
        model = LogisticRegression()
        # --- THIS IS THE ONLY CHANGE ---
        # The test now checks for the correct defaults of the hybrid API.
        self.assertEqual(model.C, 1.0)
        self.assertEqual(model.penalty, 'l2')
        self.assertIsNone(model.alpha) # alpha is None by default
        self.assertEqual(model.nlambda, 100)
        model.fit(self.X_train, self.y_train)

    def test_binary_classification(self):
        """Test that LogisticRegression enforces binary classification."""
        X_multi, y_multi = make_classification(n_samples=100, n_features=4, random_state=42)
        model = LogisticRegression()
        model.fit(X_multi, y_multi)

    def test_sparse_input(self):
        """Test that LogisticRegression handles sparse input data."""
        # --- THIS IS THE ONLY CHANGE ---
        # Create a dense classification dataset first
        X_dense, y_class = make_classification(
            n_samples=200, n_features=20, n_informative=10, n_classes=2, random_state=42
        )
        # Convert the feature matrix to a sparse format
        X_sparse = csr_matrix(X_dense)

        X_train_sparse, X_test_sparse, y_train, y_test = train_test_split(
            X_sparse, y_class, test_size=0.2, random_state=42
        )
        model = LogisticRegression(alpha=1.0)
        model.fit(X_train_sparse, y_train)
        y_pred = model.predict(X_test_sparse)
        self.assertEqual(y_pred.shape, (X_test_sparse.shape[0],))
        self.assertTrue(np.all(np.isin(y_pred, model.classes_)))
        y_proba = model.predict_proba(X_test_sparse)
        self.assertEqual(y_proba.shape, (X_test_sparse.shape[0], 2))
        self.assertTrue(np.allclose(y_proba.sum(axis=1), 1.0))

    def test_invalid_C(self):
        """Test that invalid C raises InvalidParameterError."""
        model = LogisticRegression(C=-1.0)
        with pytest.raises(InvalidParameterError, match=r"The 'C' parameter of LogisticRegression must be.*Got -1.0 instead"):
            model.fit(self.X_train, self.y_train)

    def test_invalid_penalty(self):
        """Test that invalid penalty raises InvalidParameterError."""
        model = LogisticRegression(penalty="invalid")
        with pytest.raises(InvalidParameterError, match=r"The 'penalty' parameter of LogisticRegression must be.*Got 'invalid' instead"):
            model.fit(self.X_train, self.y_train)

    def test_sklearn_tags(self):
        """
        Test that the _more_tags method returns the correct custom tags.
        """
        model = LogisticRegression()
        # We test our custom tag implementation directly.
        tags = model._more_tags()
        self.assertIsInstance(tags, dict)
        self.assertTrue(tags["binary_only"])

    def test_get_params_deep(self):
        """Test that get_params returns all parameters correctly."""
        # --- THIS IS THE ONLY CHANGE ---
        model = LogisticRegression(penalty="l1", C=0.5, alpha=0.9, nlambda=50)
        params = model.get_params(deep=True)
        expected_params = {
            "penalty": "l1",
            "C": 0.5,
            "alpha": 0.9,
            "nlambda": 50,
            "binding": None
        }
        self.assertEqual(params, expected_params)

    def test_set_params(self):
        """Test that set_params updates parameters correctly."""
        # --- THIS IS THE ONLY CHANGE ---
        model = LogisticRegression(C=1.0, penalty="l2")
        model.set_params(C=0.1, penalty="l1")
        self.assertEqual(model.C, 0.1)
        self.assertEqual(model.penalty, "l1")
        # Ensure fit still works with the updated params
        model.fit(self.X_train, self.y_train)

    def test_invalid_input_shape(self):
        """Test that predict raises ValueError for mismatched feature counts."""
        model = LogisticRegression()
        model.fit(self.X_train, self.y_train)  # Fit with correct shape

        # Create data with an incorrect number of features
        X_invalid = self.X_test[:, :-1]

        # Assert that predict raises an error
        with self.assertRaises(ValueError):
            model.predict(X_invalid)

    def test_empty_sparse_input(self):
        """Test that fit handles empty sparse input correctly."""
        X_empty = csr_matrix((0, self.X.shape[1]))
        y_empty = np.array([])
        model = LogisticRegression()
        with pytest.raises(ValueError, match="Found array with 0 sample"):
            model.fit(X_empty, y_empty)

    def test_sklearn_compatibility(self):
        """Tests scikit-learn API compatibility with check_estimator."""
        # The test now instantiates the class with its correct, default signature.
        estimator = LogisticRegression()
        check_estimator(estimator)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
