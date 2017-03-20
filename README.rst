##############################################
Finite Element Analysis Multiprocessing System
##############################################

Copyright |copy| 2017 by `Professor Torsten Calvi Corporation <http://torstencalvi.com/>`_. All rights reserved.

This project is being done under contract for `Professor Torsten Calvi Corporation <http://torstencalvi.com/>`_. The company has graciously allowed public access to documentation and code related this project.

.. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN

***********************************
Autodesk Inventor Professional 2017
***********************************

Inventor's stress analysis only supports solving linear, static problems. See `stress analysis assumptions <https://knowledge.autodesk.com/support/inventor-products/troubleshooting/caas/sfdcarticles/sfdcarticles/Stress-analysis-assumptions.html>`_.

***************
Ansys AIM R17.0
***************

Seems to be able to do the job. The ability to use it with supercomputing clusters was not investigated.

****************
Salome-Meca 2016
****************

Packaged Code_Aster is not compiled with MPI support.

************************
Code_Aster 12.7 (stable)
************************

The following section is based on a `guide for compiling a Parallel version of Code_Aster <https://sites.google.com/site/codeastersalomemeca/home/code_asterno-heiretuka/parallel-code_aster-12-4-english>`_.

The following environmental variables should be set when building software from source:

* ``LDFLAGS="-L${HOME}/aster/lib"`` # Or use whatever ``PREFIX`` you are using

The following parameters should be used to configure software that will be built from source:

* ``--prefix="${HOME}/aster"`` # Use whatever directory you want

Make sure that you are always using binaries from ``PREFIX``.

Open MPI
========

TODO
----

* Check why there are JDK options for ``configure``.
* Investigate building with support for CUDA (``--with-cuda``). AWS has GPU instances available running nVidia Teslas, K520s, and M2050s.

OpenBLAS
========

According to an `R benchmark <http://blog.nguyenvq.com/blog/2014/11/10/optimized-r-and-python-standard-blas-vs-atlas-vs-openblas-vs-mkl/>`_, OpenBLAS is significantly faster than `Netlib BLAS <http://www.netlib.org/blas/>`_. The `Intel MKL <https://software.intel.com/en-us/intel-mkl>`_ is supposedly the fastest out of all of them.

### Code_Aster (MPI)

The following environmental variables should be set when building from source:

* ``CC=mpicc``
* ``CPP=mpiCC``
