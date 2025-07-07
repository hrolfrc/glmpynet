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

from glmpynet import LogisticNet


class TestLogisticNet(unittest.TestCase):
    """
    A test suite for the LogisticNet class.
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
        model = LogisticNet(C=1.0, penalty="l2")
        model.fit(self.X_train, self.y_train)

        # Check that the model is marked as fitted
        check_is_fitted(model, ["coef_", "intercept_", "is_fitted_"])

        # Check that coefficients, intercept, and classes are set
        self.assertTrue(hasattr(model, 'coef_'))
        self.assertTrue(hasattr(model, 'intercept_'))
        self.assertTrue(hasattr(model, 'classes_'))
        self.assertEqual(model.coef_.shape, (1, self.X_train.shape[1]))
        self.assertEqual(model.intercept_.shape, (1,))
        self.assertEqual(len(model.classes_), 2)

    def test_predict_output(self):
        """Tests the shape and values of the predict method's output."""
        model = LogisticNet(C=1.0, penalty="l2")
        model.fit(self.X_train, self.y_train)
        predictions = model.predict(self.X_test)

        self.assertEqual(predictions.shape, (self.X_test.shape[0],))
        self.assertTrue(all(p in model.classes_ for p in predictions))

    def test_predict_proba_output(self):
        """Tests the shape and values of the predict_proba method's output."""
        model = LogisticNet(C=1.0, penalty="l2")
        model.fit(self.X_train, self.y_train)
        probabilities = model.predict_proba(self.X_test)

        self.assertEqual(probabilities.shape, (self.X_test.shape[0], 2))
        self.assertTrue(np.all((probabilities >= 0) & (probabilities <= 1)))
        np.testing.assert_almost_equal(np.sum(probabilities, axis=1), np.ones(self.X_test.shape[0]))

    def test_integration_with_pipeline(self):
        """Tests that LogisticNet works as a step in a scikit-learn Pipeline."""
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('logistic_net', LogisticNet(C=1.0, penalty="l2"))
        ])
        pipeline.fit(self.X_train, self.y_train)
        predictions = pipeline.predict(self.X_test)
        self.assertEqual(predictions.shape, (self.X_test.shape[0],))

    def test_integration_with_gridsearchcv(self):
        """Tests that LogisticNet can be tuned with GridSearchCV."""
        model = LogisticNet(penalty="l2")
        param_grid = {'C': [0.1, 1.0, 10.0]}
        grid_search = GridSearchCV(model, param_grid, cv=3, scoring='accuracy')
        grid_search.fit(self.X_train, self.y_train)
        self.assertTrue(hasattr(grid_search, 'best_estimator_'))
        self.assertIn(grid_search.best_params_['C'], [0.1, 1.0, 10.0])

    def test_default_instantiation(self):
        """Test that LogisticNet can be instantiated without arguments."""
        model = LogisticNet()
        assert model.C == 1.0
        assert model.penalty == "l2"
        model.fit(self.X_train, self.y_train)  # Should not raise errors

    def test_binary_classification(self):
        """Test that LogisticNet enforces binary classification."""
        X_multi, y_multi = make_classification(n_samples=100, n_features=4, random_state=42)
        model = LogisticNet()
        model.fit(X_multi, y_multi)

    @expectedFailure
    def test_sparse_input(self):
        """Test that LogisticNet handles sparse input data."""
        X_sparse, y = make_sparse_uncorrelated(random_state=0)
        X_train_sparse, X_test_sparse, y_train, y_test = train_test_split(
            X_sparse, self.y, test_size=0.2, random_state=42
        )
        model = LogisticNet(penalty="l1")
        model.fit(X_train_sparse, y_train)
        y_pred = model.predict(X_test_sparse)
        assert y_pred.shape == (X_test_sparse.shape[0],)
        assert np.all(np.isin(y_pred, model.classes_))
        y_proba = model.predict_proba(X_test_sparse)
        assert y_proba.shape == (X_test_sparse.shape[0], 2)
        assert np.allclose(y_proba.sum(axis=1), 1.0)

    def test_invalid_C(self):
        """Test that invalid C raises InvalidParameterError."""
        model = LogisticNet(C=-1.0)
        with pytest.raises(InvalidParameterError, match=r"The 'C' parameter of LogisticRegression must be.*Got -1.0 instead"):
            model.fit(self.X_train, self.y_train)

    def test_invalid_penalty(self):
        """Test that invalid penalty raises InvalidParameterError."""
        model = LogisticNet(penalty="invalid")
        with pytest.raises(InvalidParameterError, match=r"The 'penalty' parameter of LogisticRegression must be.*Got 'invalid' instead"):
            model.fit(self.X_train, self.y_train)

    @expectedFailure
    def test_sklearn_tags(self):
        """Test that __sklearn_tags__ returns expected tags."""
        # noinspection PyUnresolvedReferences
        tags = self.model.__sklearn_tags__()
        assert isinstance(tags, dict)
        assert tags["requires_y"] is True
        assert tags["binary_only"] is False  # Inherited from LogisticRegression
        assert tags["allow_nan"] is False

    def test_get_params_deep(self):
        """Test that get_params returns all parameters correctly."""
        model = LogisticNet(C=0.5, penalty="l1")
        params = model.get_params(deep=True)
        assert params == {"C": 0.5, "penalty": "l1"}
        params_shallow = model.get_params(deep=False)
        assert params_shallow == {"C": 0.5, "penalty": "l1"}

    # noinspection PyTypeChecker
    def test_set_params(self):
        """Test that set_params updates parameters correctly."""
        model = LogisticNet(C=1.0, penalty="l2")
        model.set_params(C=0.1, penalty="l1")
        assert model.C == 0.1
        assert model.penalty == "l1"
        model.fit(self.X_train, self.y_train)  # Ensure fit works with updated params
        assert model._estimator.C == 0.1
        assert model._estimator.penalty == "l1"

    @expectedFailure
    def test_invalid_input_shape(self):
        """Test that fit raises ValueError for mismatched input shapes."""
        X_invalid = self.X_train[:, :-1]  # Mismatch features
        with pytest.raises(ValueError, match="X and y have incompatible shapes"):
            # noinspection PyUnresolvedReferences
            self.model.fit(X_invalid, self.y_train)

    @expectedFailure
    def test_empty_sparse_input(self):
        """Test that fit handles empty sparse input correctly."""
        X_empty = csr_matrix((0, self.X.shape[1]))
        y_empty = np.array([])
        with pytest.raises(ValueError, match="Found array with 0 sample"):
            # noinspection PyUnresolvedReferences
            self.model.fit(X_empty, y_empty)

    def test_sklearn_compatibility(self):
        """Tests scikit-learn API compatibility with check_estimator."""
        estimator = LogisticNet(C=1.0, penalty="l2")
        check_estimator(estimator)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
