import unittest

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.utils.validation import check_is_fitted

from glmpynet.logistic_net import LogisticNet


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

    # def test_sklearn_compatibility(self):
    #     """Tests scikit-learn API compatibility with check_estimator."""
    #     estimator = LogisticNet(C=1.0, penalty="l2")
    #     check_estimator(estimator)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
