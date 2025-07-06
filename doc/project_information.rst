.. _project_information:

Project Information
===================

This final section provides supplementary information about the ``glmpynet`` project, including its software dependencies, guidance on how to cite the library in your own work, and details on contributing.

Dependencies
------------

The ``glmpynet`` library relies on a small set of well-maintained, open-source Python packages, which will be installed automatically when you install ``glmpynet`` via ``pip``.

``numpy``
   For efficient numerical operations and array handling.

``scikit-learn``
   For compatibility with the broader machine learning ecosystem and for utility functions.

``glmnet``
   The core dependency, which provides the compiled Fortran backend for high-performance model fitting.

How to Cite glmpynet
--------------------

If you use ``glmpynet`` in your research and would like to cite it, please use the following BibTeX entry. Citing software helps the developers and maintainers justify their work and secure funding for future development.

.. code-block:: bibtex

   @misc{glmpynet_2025,
     author       = {Rolf Carlson},
     title        = {glmpynet: glmnet-based Logistic Regression for Scikit-Learn},
     year         = {2025},
     publisher    = {GitHub},
     url          = {https://github.com/hrolfrc/glmpynet},
     doi          = {A_ZENODO_DOI_IF_AVAILABLE}
   }

Contributing & License
----------------------

Contributing
~~~~~~~~~~~~

This project is open source and contributions are welcome. If you would like to contribute, please visit the project’s GitHub repository. You can contribute by reporting bugs, suggesting new features, or submitting pull requests with code improvements. Please consult the ``CONTRIBUTING.md`` file in the repository for specific guidelines.

License
~~~~~~~

The ``glmpynet`` library is distributed under the MIT License. This is a permissive open-source license that allows for broad use, modification, and distribution. Please see the ``LICENSE`` file in the source repository for the full text of the license.
