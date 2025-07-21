.. _environment_setup:

Environment Setup
=================

This guide provides step-by-step instructions for creating a consistent
and reproducible development environment for the `glmpynet` project. The
environment is managed using Conda.

Prerequisites
-------------

Before you begin, ensure you have a Conda installation available on your
system. We recommend installing either the full **Anaconda Distribution**
(if you want a comprehensive scientific Python environment) or the lightweight
**Miniconda** (if you prefer a minimal installation).

You can find installers and instructions on the `official Conda website <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`_.

Step 1: Create the Conda Environment
-------------------------------------

The project includes an ``environment.yml`` file that specifies all the
necessary dependencies, including the C++ toolchain, Bazel, and Python
packages.

1.  Navigate to the root directory of the ``glmpynet`` project in your
    terminal.

2.  Run the following command to create the environment from the file.
    This will download and install all required packages into an
    isolated environment named ``glmnetpp``.

    .. code:: bash

       conda env create -f environment.yml

    This step may take several minutes, as Conda needs to resolve and
    download a number of large packages.

.. note::
   **What about Mamba?**

   You may see ``mamba`` used in some project documentation. Mamba is a
   fast, parallel re-implementation of the Conda package manager. It uses
   the same commands and environment files but can be significantly
   faster at resolving dependencies.

   If you have Mamba installed, you can use it as a drop-in replacement
   for the command above for a much faster setup:

   .. code:: bash

      mamba env create -f environment.yml

   However, **Mamba is not required**. Standard ``conda`` will always work.

Step 2: Activate the Environment
--------------------------------

Once the environment is created, you must activate it before you can
begin development.

.. code:: bash

   conda activate glmnetpp

Your terminal prompt should now be prefixed with ``(glmnetpp)``,
indicating that you are inside the correct environment.

Step 3: Verify the Installation
-------------------------------

To ensure all core tools were installed correctly, you can run the
following commands and check their output.

.. code:: bash

   # Check the Bazel version
   bazel --version

   # Check the C++ compiler version (on Linux)
   gcc --version
   clang --version

With the environment activated, you are now ready to proceed with the
project's development plan.