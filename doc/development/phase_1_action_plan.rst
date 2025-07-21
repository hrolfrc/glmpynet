.. _phase_1_action_plan:

Phase 1: `glmnetpp` Foundation Action Plan
===========================================

Objective
---------

This document provides a step-by-step checklist to verify the development environment, achieve a stable build, and confirm the correctness and performance of the ``glmnetpp`` C++ core engine.

Each task is linked to a requirement identifier from the :doc:`phase_1_analysis` document.

Action Plan
-----------

### 1. Environment & Dependency Verification

* **Goal:** Confirm that the full suite of stated and discovered system-level dependencies is correctly installed and configured.

* **Tasks:**
    * [ ] **Activate Conda Environment:** Ensure the ``glmnetpp`` Conda environment is active.
        * *Verifies: (R-SYS-03)*
    * [ ] **Verify Core Binaries:** Confirm that ``bazel``, ``gcc``/``clang``, and ``Rscript`` are all available in the system ``PATH``.
        * *Verifies: (R-SYS-01), (R-SYS-02), (R-SYS-04)*
    * [ ] **Verify R Environment Paths:** Run the following commands and confirm that each returns a valid, non-empty path.
        * *Verifies: (R-SYS-04)*
        .. code:: bash

           Rscript -e "cat(Sys.getenv('R_INCLUDE_DIR'))"
           Rscript -e "cat(Sys.getenv('R_HOME'))"

### 2. Generate the `.bazelrc` Configuration

* **Goal:** Create the local ``.bazelrc`` file that contains the specific compiler and toolchain configuration for the development machine.

* **Tasks:**
    * [ ] **Run Generation Script:** Execute the ``generate_bazelrc`` Python script from the root of the ``glmnetpp`` directory.
        * *Fulfills: (R-BLD-03)*
        .. code:: bash

           python3 generate_bazelrc
    * [ ] **Inspect Generated File:** Open the newly created ``.bazelrc`` file and visually inspect its contents to ensure the paths to the Conda and R installations are correct for your system.

### 3. Build the Library

* **Goal:** Achieve a successful, clean build of the ``glmnetpp`` C++ library.

* **Tasks:**
    * [ ] **Execute Build Command:** Run the Bazel build command, specifying the correct compiler configuration.
        * *Verifies: (R-BLD-01), (R-BLD-02), (R-CPP-03)*
        .. code:: bash

           # For GCC
           bazel build //:glmnetpp --config=gcc

           # For Clang
           bazel build //:glmnetpp --config=clang
    * [ ] **Debug and Iterate:** If the build fails, analyze the error output, apply targeted fixes, and re-run the build command until it completes successfully.

### 4. Run Unit Tests

* **Goal:** Ensure the C++ code is logically correct by running the full unit test suite.

* **Tasks:**
    * [ ] **Execute Test Suite:** Run the Bazel test command in debug mode.
        * *Verifies: (R-CPP-01)*
        .. code:: bash

           bazel test -c dbg //test/...
    * [ ] **Debug Failures:** If any tests fail, analyze the logs and debug until all tests pass.

### 5. Run Benchmarks

* **Goal:** Confirm that the performance benchmark suite compiles and executes correctly.

* **Tasks:**
    * [ ] **List Benchmarks:** List all available benchmark targets to identify a candidate to run.
        * *Verifies: (R-CPP-02)*
        .. code:: bash

           bazel query "kind(cc_binary, //benchmark/...)"
    * [ ] **Execute a Benchmark:** Select one benchmark from the list and run it in optimized mode to confirm successful execution.
        .. code:: bash

           bazel run -c opt //benchmark:<name-of-a-benchmark-from-list>
