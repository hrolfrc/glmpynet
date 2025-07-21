.. _contributing:

Contributing to glmpynet
========================

Thank you for your interest in contributing to `glmpynet`! This document
outlines the development workflow, coding standards, and process for
submitting changes to ensure the project remains high-quality and maintainable.

The Development Workflow
------------------------

To maintain a stable main branch, all new work must be done on a feature
branch.

1.  **Create a Feature Branch:** Before you start working, create a new
    branch from the `main` branch. A good branch name is descriptive, like
    ``feat/config-command`` or ``fix/reconciler-bug``.

    .. code-block:: bash

       git checkout -b feat/my-new-feature

2.  **Commit Your Changes:** Make small, logical commits. Each commit should
    represent one self-contained change. All commit messages **must**
    follow the `Conventional Commits <https://www.conventionalcommits.org/>`_
    specification (e.g., ``feat(cli): ...``, ``fix(core): ...``, ``docs(guide): ...``).

Code Quality and Style
----------------------

To ensure a consistent and clean codebase, we use standard Python code
formatters and linters. Before committing, please run the following tools
from the project's root directory.

* **Black:** An uncompromising code formatter.

    .. code-block:: bash

       pip install black
       black .

* **Ruff:** An extremely fast Python linter.

    .. code-block:: bash

       pip install ruff
       ruff check . --fix

Testing
-------

All contributions must be accompanied by tests.

* **New Features:** Any new feature must include unit tests that verify its
    correctness.
* **Bug Fixes:** Any bug fix must include a "regression test" that fails
    *before* the fix is applied and passes *after*.
* To run the full test suite, use `pytest`:

    .. code-block:: bash

       pytest

Documentation
-------------

User-facing changes, such as a new command-line flag or a change in
behavior, must be reflected in the Sphinx documentation located in the
``docs/`` directory.

To build the documentation locally and preview your changes, run the
following command from the project root:

.. code-block:: bash

   sphinx-build -b html docs/ docs/_build

You can then open ``docs/_build/index.html`` in your browser.

Submitting a Pull Request
-------------------------

Once your feature is complete and tested, please follow these steps:

1.  Push your feature branch to GitHub.
2.  Open a Pull Request (PR) against the ``main`` branch.
3.  Provide a clear description of the changes in your PR.
4.  Ensure that all automated checks (like CircleCI) pass.