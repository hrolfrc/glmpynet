import pytest
from sklearn.datasets import load_iris
from logistic_net import LogisticNet


@pytest.fixture
def data():
    return load_iris(return_X_y=True)


def test_template_classifier(data):
    """Check the internals and behavior of `LogisticNet`."""
    X, y = data
    clf = LogisticNet()
    clf.fit(X, y)
    y_pred = clf.predict(X)
    print(y_pred)
    print(y_pred.shape)
    print(X.shape)
    assert y_pred.shape[0] == (X.shape[0])
