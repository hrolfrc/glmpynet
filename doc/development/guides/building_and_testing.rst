.. _building_and_testing:

Building and Testing
====================

This guide covers the essential commands for compiling the ``glmnetpp``
library and running its unit tests to ensure correctness. All commands
are run using `Bazel <https://bazel.build/>`_ from the root of the
``glmnetpp`` directory.

Building the Library
--------------------

The ``bazel build`` command compiles the C++ source code. The ``glmnetpp``
library is header-only, so this step primarily checks for compilation
errors and ensures all dependencies are correctly resolved.

You can build the library in two main configurations:

**1. Optimized (Release) Mode**
This mode compiles the code with full optimizations and should be used for
benchmarking or creating a release version. Use the ``-c opt`` flag.

.. code:: bash

   # Build in optimized mode
   bazel build -c opt //:glmnetpp

**2. Debug Mode**
This mode includes debugging symbols and is useful during development. Use
the ``-c dbg`` flag.

.. code:: bash

   # Build in debug mode
   bazel build -c dbg //:glmnetpp

.. note::
   On Linux, you can specify whether to use ``gcc`` or ``clang`` by adding
   the ``--config=gcc`` or ``--config=clang`` flag to your build command.

Running Unit Tests
------------------

The unit test suite uses the `GoogleTest <https://github.com/google/googletest>`_
framework to verify the logical correctness of the C++ code. Tests should
always be run in **debug mode** (``-c dbg``) to ensure the best possible
error messages and debugging information.

**1. Run All Tests**
To run every test in the project, use the ``//test/...`` wildcard target.

.. code:: bash

   bazel test -c dbg //test/...

**2. Run a Single Test**
When debugging a specific issue, it is much faster to run a single test
target. Replace ``<name-of-test>`` with the name of the test target
defined in the ``test/BUILD.bazel`` file.

.. code:: bash

   bazel test -c dbg //test:<name-of-test>