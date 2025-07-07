import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score
from glmpynet import LogisticNet


class TestLogisticNetE2E:
    def setup_method(self):
        self.X, self.y = make_classification(
            n_samples=1000, n_features=50, n_informative=25, n_classes=2, random_state=42
        )
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )

    def test_pipeline_grid_search(self):
        """Test LogisticNet in a Pipeline with GridSearchCV."""
        pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("logistic_net", LogisticNet())
        ])
        param_grid = {
            "logistic_net__C": [0.1, 1.0, 10.0],
            "logistic_net__penalty": ["l1", "l2"]
        }
        grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring="accuracy")
        grid_search.fit(self.X_train, self.y_train)
        assert grid_search.best_params_["logistic_net__C"] in [0.1, 1.0, 10.0]
        assert grid_search.best_params_["logistic_net__penalty"] in ["l1", "l2"]
        y_pred = grid_search.predict(self.X_test)
        assert y_pred.shape == (self.X_test.shape[0],)
        accuracy = accuracy_score(self.y_test, y_pred)
        assert accuracy > 0.7  # Reasonable threshold for synthetic data

    def test_performance_metrics(self):
        """Test performance metrics for LogisticNet."""
        model = LogisticNet(penalty="l1")
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        assert accuracy > 0.7  # Baseline for synthetic data
        y_proba = model.predict_proba(self.X_test)[:, 1]
        roc_auc = roc_auc_score(self.y_test, y_proba)
        assert roc_auc > 0.7  # Baseline for synthetic data
        non_zero_coefs = np.sum(model.coef_ != 0)
        assert non_zero_coefs < self.X.shape[1]  # L1 penalty should yield sparse coefficients
