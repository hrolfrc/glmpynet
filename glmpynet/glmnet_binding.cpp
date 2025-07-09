#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/eigen.h>
#include <Eigen/Dense>
#include <Eigen/Sparse>
#include "glmnet/glmnet_4_1_9/glmnetpp/include/glmnetpp_bits/elnet_driver.hpp"
#include "glmnet/glmnet_4_1_9/glmnetpp/include/glmnetpp_bits/logit_driver.hpp"
#include "glmnet/glmnet_4_1_9/glmnetpp/include/glmnetpp_bits/multi_driver.hpp"
#include "glmnet/glmnet_4_1_9/glmnetpp/include/glmnetpp_bits/fish_driver.hpp"
#include "glmnet/glmnet_4_1_9/glmnetpp/include/glmnetpp_bits/cox_driver.hpp"
#include "glmnet/glmnet_4_1_9/glmnetpp/include/glmnetpp_bits/mrel_driver.hpp"

namespace py = pybind11;

void elnet(
    double alpha, int nobs, int nvars, py::array_t<double> X, py::array_t<double> y,
    py::array_t<double> weights, int nlam, py::array_t<double> lambda_path,
    int max_iter, double tol, bool relax, py::array_t<double> coef
) {
    Eigen::Map<Eigen::MatrixXd> X_eigen(X.mutable_data(), nobs, nvars);
    Eigen::Map<Eigen::VectorXd> y_eigen(y.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> weights_eigen(weights.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> lambda_eigen(lambda_path.mutable_data(), nlam);
    Eigen::Map<Eigen::VectorXd> coef_eigen(coef.mutable_data(), nvars);

    glmnetpp::GaussElNetDriver<double> driver;
    if (relax) {
        // Handle relaxed fit (placeholder; requires additional outputs)
        driver.fit(alpha, X_eigen, y_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    } else {
        driver.fit(alpha, X_eigen, y_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    }
}

void lognet(
    double alpha, int nobs, int nvars, py::array_t<double> X, py::array_t<double> y,
    py::array_t<double> weights, int nlam, py::array_t<double> lambda_path,
    int max_iter, double tol, bool relax, py::array_t<double> coef
) {
    Eigen::Map<Eigen::MatrixXd> X_eigen(X.mutable_data(), nobs, nvars);
    Eigen::Map<Eigen::VectorXd> y_eigen(y.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> weights_eigen(weights.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> lambda_eigen(lambda_path.mutable_data(), nlam);
    Eigen::Map<Eigen::VectorXd> coef_eigen(coef.mutable_data(), nvars);

    glmnetpp::LogitElNetDriver<double> driver;
    if (relax) {
        driver.fit(alpha, X_eigen, y_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    } else {
        driver.fit(alpha, X_eigen, y_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    }
}

void multnet(
    double alpha, int nobs, int nvars, py::array_t<double> X, py::array_t<double> y,
    py::array_t<double> weights, int nlam, py::array_t<double> lambda_path,
    int max_iter, double tol, bool relax, py::array_t<double> coef
) {
    Eigen::Map<Eigen::MatrixXd> X_eigen(X.mutable_data(), nobs, nvars);
    Eigen::Map<Eigen::MatrixXd> y_eigen(y.mutable_data(), nobs, y.shape()[1]); // Multi-class
    Eigen::Map<Eigen::VectorXd> weights_eigen(weights.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> lambda_eigen(lambda_path.mutable_data(), nlam);
    Eigen::Map<Eigen::VectorXd> coef_eigen(coef.mutable_data(), nvars * y.shape()[1]);

    glmnetpp::MultiElNetDriver<double> driver;
    if (relax) {
        driver.fit(alpha, X_eigen, y_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    } else {
        driver.fit(alpha, X_eigen, y_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    }
}

void fishnet(
    double alpha, int nobs, int nvars, py::array_t<double> X, py::array_t<double> y,
    py::array_t<double> weights, int nlam, py::array_t<double> lambda_path,
    int max_iter, double tol, bool relax, py::array_t<double> coef
) {
    Eigen::Map<Eigen::MatrixXd> X_eigen(X.mutable_data(), nobs, nvars);
    Eigen::Map<Eigen::VectorXd> y_eigen(y.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> weights_eigen(weights.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> lambda_eigen(lambda_path.mutable_data(), nlam);
    Eigen::Map<Eigen::VectorXd> coef_eigen(coef.mutable_data(), nvars);

    glmnetpp::FishElNetDriver<double> driver;
    if (relax) {
        driver.fit(alpha, X_eigen, y_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    } else {
        driver.fit(alpha, X_eigen, y_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    }
}

void coxnet(
    double alpha, int nobs, int nvars, py::array_t<double> X, py::array_t<double> time,
    py::array_t<double> status, py::array_t<double> weights, int nlam,
    py::array_t<double> lambda_path, int max_iter, double tol, bool relax,
    py::array_t<double> coef
) {
    Eigen::Map<Eigen::MatrixXd> X_eigen(X.mutable_data(), nobs, nvars);
    Eigen::Map<Eigen::VectorXd> time_eigen(time.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> status_eigen(status.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> weights_eigen(weights.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> lambda_eigen(lambda_path.mutable_data(), nlam);
    Eigen::Map<Eigen::VectorXd> coef_eigen(coef.mutable_data(), nvars);

    glmnetpp::CoxElNetDriver<double> driver;
    if (relax) {
        driver.fit(alpha, X_eigen, time_eigen, status_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    } else {
        driver.fit(alpha, X_eigen, time_eigen, status_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    }
}

void mrelnet(
    double alpha, int nobs, int nvars, py::array_t<double> X, py::array_t<double> y,
    py::array_t<double> weights, int nlam, py::array_t<double> lambda_path,
    int max_iter, double tol, bool relax, py::array_t<double> coef
) {
    Eigen::Map<Eigen::MatrixXd> X_eigen(X.mutable_data(), nobs, nvars);
    Eigen::Map<Eigen::MatrixXd> y_eigen(y.mutable_data(), nobs, y.shape()[1]);
    Eigen::Map<Eigen::VectorXd> weights_eigen(weights.mutable_data(), nobs);
    Eigen::Map<Eigen::VectorXd> lambda_eigen(lambda_path.mutable_data(), nlam);
    Eigen::Map<Eigen::VectorXd> coef_eigen(coef.mutable_data(), nvars * y.shape()[1]);

    glmnetpp::MultiGaussElNetDriver<double> driver;
    if (relax) {
        driver.fit(alpha, X_eigen, y_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    } else {
        driver.fit(alpha, X_eigen, y_eigen, weights_eigen, nlam, lambda_eigen, max_iter, tol, coef_eigen);
    }
}

PYBIND11_MODULE(_glmnet, m) {
    m.def("elnet", &elnet, "GLMNet Gaussian regression");
    m.def("lognet", &lognet, "GLMNet logistic regression");
    m.def("multnet", &multnet, "GLMNet multinomial regression");
    m.def("fishnet", &fishnet, "GLMNet Poisson regression");
    m.def("coxnet", &coxnet, "GLMNet Cox regression");
    m.def("mrelnet", &mrelnet, "GLMNet multi-response Gaussian regression");
}