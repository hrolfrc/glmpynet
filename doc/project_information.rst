.. _project_information:

Project Information
===================

This section provides details about the `glmpynet` project, including its dependencies, citation guidance, and how to contribute.

Dependencies
------------

The `glmpynet` library relies on a minimal set of open-source Python packages, installed automatically when you install `glmpynet` via `pip`.

`numpy`
   For efficient numerical operations and array handling.

The `glmnetpp` C++ library is the core dependency, providing high-performance regularized logistic regression. It is precompiled in the `glmpynet` package, requiring no additional setup for users.

Citation
--------

If you use `glmpynet` in your work, please cite it as:

    glmpynet: A scikit-learn-compatible Python package for regularized logistic regression using the glmnetpp C++ library. Available at https://github.com/hrolfrc/glmpynet.

You may also cite the `glmnetpp` library, which `glmpynet` builds upon, following its citation guidelines (see `glmnet`’s R documentation or online resources).

Contributing & License
----------------------

Contributing
~~~~~~~~~~~~

`glmpynet` is open source, and contributions are welcome. Visit the GitHub repository (https://github.com/hrolfrc/glmpynet) to:
- Report bugs or suggest features via the issue tracker.
- Submit pull requests with code, tests, or documentation improvements.
- Review `ROADMAP.md` and `DEVELOPMENT_PLAN.md` for project goals and tasks.

See `CONTRIBUTING.md` in the repository for specific guidelines.

License
~~~~~~~

`glmpynet` is distributed under the MIT License, a permissive open-source license allowing broad use, modification, and distribution. See the `LICENSE` file in the repository for the full text.