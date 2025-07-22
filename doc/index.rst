.. glmpynet documentation master file

Welcome to glmpynet's documentation!
=====================================

**glmpynet** is a Python package providing a scikit-learn-compatible ``LogisticRegression`` API powered by the high-performance ``glmnetpp`` C++ library.

This project bridges the computational speed of ``glmnetpp`` with the ease-of-use of the Python data science ecosystem. It provides a user-friendly hybrid API that accepts both standard Scikit-learn parameters (e.g., ``C``, ``penalty``) for seamless integration and ``glmnet``-native parameters (e.g., ``alpha``) for advanced control.

This documentation guides you through installing the package, using it in data science workflows, and understanding its design.

Project Status
==============

The Python API for ``glmpynet.LogisticRegression`` is now **complete and fully tested** against a mock backend. The next major phase of development is to implement the real C++ binding that connects this API to the ``glmnetpp`` engine.

See the :doc:`development/development_roadmap` for the full development plan.

.. toctree::
   :maxdepth: 2
   :caption: User Documentation:

   getting_started
   usage_guide
   api_reference
   examples

.. toctree::
   :maxdepth: 2
   :caption: Development:

   development/index

.. toctree::
   :maxdepth: 2
   :caption: Project Information:

   project_information

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
