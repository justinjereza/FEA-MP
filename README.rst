##############################################
Finite Element Analysis Multiprocessing System
##############################################

Copyright |copy| 2017 by `Professor Torsten Calvi Corporation <http://torstencalvi.com/>`_. All rights reserved.

This project is being done under contract for `Professor Torsten Calvi Corporation <http://torstencalvi.com/>`_. The company has graciously allowed public access to documentation and code related this project.

.. |copy| unicode:: U+000A9 .. COPYRIGHT SIGN

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

Source: http://www.code-aster.org/spip.php?article303

Packaged Code_Aster is not compiled with MPI support.

************************
Code_Aster 12.7 (stable)
************************

The following section is based on a `guide for compiling a Parallel version of Code_Aster <https://sites.google.com/site/codeastersalomemeca/home/code_asterno-heiretuka/parallel-code_aster-12-4-english>`_. It is assumed that all of the following programs will be built from source with the exception of packages listed under `Prerequisites`_.

The following variables should be set:

* ``PREFIX="${HOME}/aster"`` # Use whatever directory you want
* ``CC="mpicc"`` # Assuming `Open MPI`_ has been installed
* ``CPP="mpiCC"`` # Assuming `Open MPI`_ has been installed.
* ``LDFLAGS="-L${PREFIX}/lib"``

The following parameters should be used to configure software:

* ``--prefix="${PREFIX}"``

Make sure that you are always using binaries from ``${PREFIX}/bin``.

TODO
----

* Check if autotools is a viable method for bootstrapping everything from source.

Prerequisites
-------------

The operating system used for this project is Ubuntu 16.04.

The following packages should be installed:

* ``build-essential``
* ``gfortran``

Open MPI
========

| Version: 2.0.2
| Source: https://www.open-mpi.org/software/ompi/v2.0/downloads/openmpi-2.0.2.tar.bz2

``./configure --prefix="${PREFIX}" && make -j4 && make install``

TODO
----

* Check why there are JDK options for ``configure``.
* Investigate building with support for CUDA (``--with-cuda``). AWS has GPU instances available running nVidia Teslas, K520s, and M2050s.

OpenBLAS
========

| Version: 0.2.19
| Source: http://github.com/xianyi/OpenBLAS/archive/v0.2.19.tar.gz

``TARGET="HASWELL" make -j4 && make install``

According to an `R benchmark <http://blog.nguyenvq.com/blog/2014/11/10/optimized-r-and-python-standard-blas-vs-atlas-vs-openblas-vs-mkl/>`_, `OpenBLAS <https://www.openblas.net/>`_ is significantly faster than `Netlib BLAS <http://www.netlib.org/blas/>`_. The `Intel MKL <https://software.intel.com/en-us/intel-mkl>`_ is supposedly the fastest out of all of them.

The following variables should be set:

* ``TARGET="HASWELL"`` # Assuming you are using an Intel Haswell processor. If not, see `TargetList.txt <https://github.com/xianyi/OpenBLAS/blob/develop/TargetList.txt>`_ for other valid targets.

Code_Aster
==========

| Version: 12.7 (stable)
| Source: http://www.code-aster.org/FICHIERS/aster-full-src-12.7.0-1.noarch.tar.gz

The following environmental variables should be set when building from source:
