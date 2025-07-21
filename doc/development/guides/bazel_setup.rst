.. _bazel_setup:

Bazel Setup and Rationale
=========================

This guide explains the project's use of the `Bazel <https://bazel.build/>`_
build tool and provides the official, recommended instructions for its installation on Debian-based systems like Ubuntu.

Design Decision: Why Bazel?
---------------------------

The decision to use Bazel is inherited from the core C++ engine, ``glmnetpp``.
The ``glmnetpp`` library uses Bazel for all its build, test, and benchmark
operations. By adopting Bazel for our project, we ensure a consistent,
reproducible, and reliable process for compiling the C++ code exactly as its
original authors intended.

Installation using the Official Apt Repository
----------------------------------------------

This is the recommended method for installing a specific, stable version of Bazel. These commands should be run from your terminal.

.. note::
   These instructions require ``sudo`` privileges to modify system package sources.

Step 1: Install Prerequisite Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure your system has the necessary tools to manage new software repositories.

.. code:: bash

   sudo apt update && sudo apt install apt-transport-https curl gnupg -y

Step 2: Add Bazel's GPG Key
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This step securely adds the key that your system will use to verify the authenticity of the Bazel packages.

.. code:: bash

   curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel-archive-keyring.gpg
   sudo mv bazel-archive-keyring.gpg /usr/share/keyrings

Step 3: Add the Bazel Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next, add the Bazel package repository to your system's sources list.

.. code:: bash

   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/bazel-archive-keyring.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list

Step 4: Install Bazel
~~~~~~~~~~~~~~~~~~~~~

Finally, update your package list and install a specific long-term support (LTS) version of Bazel. For this project, we recommend a version from the 7.x series for stability.

.. code:: bash

   sudo apt update && sudo apt install bazel-7.x

To verify a successful installation, run:

.. code:: bash

   bazel --version