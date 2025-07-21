.. _benchmarking:

Benchmarking the C++ Core
=========================

This guide covers how to run the performance benchmarks for the ``glmnetpp``
C++ engine. Benchmarking is a crucial step for measuring the computational
speed of our core algorithms and for detecting performance regressions as the
code evolves.

The suite uses the `Google Benchmark <https://github.com/google/benchmark>`_
library. For accurate results, all benchmarks must be compiled and run in
**optimized mode** (``-c opt``).

Listing Available Benchmarks
----------------------------

Before running a benchmark, you may want to see a list of all available
benchmark targets. You can get this list by running a `bazel query` from
the root of the ``glmnetpp`` directory.

.. code:: bash

   bazel query "kind(cc_binary, //benchmark/...)"

This command will print a list of all runnable binary targets within the
``benchmark`` directory.

Running a Benchmark
-------------------

To compile and run a specific benchmark, use the ``bazel run`` command.
You must specify the compilation mode as ``-c opt`` to ensure the code is
optimized for speed.

.. code:: bash

   bazel run -c opt //benchmark:<name-of-benchmark>

For example, if the query above returned a target named
``//benchmark:elnet_benchmark``, you would run it as follows:

.. code:: bash

   bazel run -c opt //benchmark:elnet_benchmark

Interpreting the Results
------------------------

The output will be a standard Google Benchmark report, which typically
includes the name of the function being benchmarked, the number of
iterations, the average time per iteration (in nanoseconds, microseconds,
etc.), and potentially the data throughput.

The primary goal is to establish a performance baseline and to compare the
results of new code changes against that baseline to ensure we are not
introducing performance regressions.