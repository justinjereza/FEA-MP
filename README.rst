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

It seems to be able to do the job. The ability to use it with supercomputing clusters was not investigated.

***********
Salome-Meca
***********

| Version: 2016.1
| Source: http://www.code-aster.org/FICHIERS/SALOME-MECA-2016-LGPL-1.tgz

Packaged Code_Aster is not compiled with MPI support.

************************
Code_Aster 12.7 (stable)
************************

The following section is based on a `guide for compiling a Parallel version of Code_Aster <https://sites.google.com/site/codeastersalomemeca/home/code_asterno-heiretuka/parallel-code_aster-12-4-english>`_. It is assumed that all of the following programs will be built from source with the exception of packages listed under `Prerequisites`_.

The following variables should be set::

    PREFIX="${HOME}/aster"                  # Use whatever directory you want
    CC="mpicc"                              # Assuming Open MPI has been installed
    CPP="mpiCC"                             # Assuming Open MPI has been installed.
    CFLAGS="-I${PREFIX}/include -O2 -fopenmp"
    LDFLAGS="-L${PREFIX}/lib"

The following parameters should be used to configure software::

--prefix="${PREFIX}"

Make sure that you are always using binaries from ``${PREFIX}/bin``.

Prerequisites
-------------

The operating system used for this project is a minimal Ubuntu 16.04 installation.

The following packages should be installed::

    build-essential
    gfortran

TODO
----

* Check possible performance gains by using the ``-Ofast`` CFLAG
* Check if autotools is a viable method for bootstrapping everything from source.
* Investigate the probability that using the `Intel C++ and Fortran Compilers <https://software.intel.com/en-us/intel-compilers>`_ will give better performance.

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

We assume that your ``TARGET`` is an Intel Haswell processor. If not, see `TargetList.txt <https://github.com/xianyi/OpenBLAS/blob/develop/TargetList.txt>`_ for other valid targets.

According to an `R benchmark <http://blog.nguyenvq.com/blog/2014/11/10/optimized-r-and-python-standard-blas-vs-atlas-vs-openblas-vs-mkl/>`_, `OpenBLAS <https://www.openblas.net/>`_ is significantly faster than `Netlib BLAS <http://www.netlib.org/blas/>`_. The `Intel MKL <https://software.intel.com/en-us/intel-mkl>`_ is supposedly the fastest out of all of them.

The following variables should be set::

    USE_OPENMP=1
    OMP_NUM_THREADS=4 # Not sure if this is used during compile-time or run-time
    TARGET="HASWELL"

ScaLAPACK
=========

| Version: 2.0.2
| Source: http://www.netlib.org/scalapack/scalapack-2.0.2.tgz
| Installer: http://www.netlib.org/scalapack/scalapack_installer.tgz

Copy ``SLmake.inc.example`` to ``SLmake.inc`` and add or edit the following::

    PREFIX = $(ENV{HOME})/aster
    FCFLAGS = -I$(PREFIX)/include -L$(PREFIX)/lib -O3 -fopenmp
    CCFLAGS = -I$(PREFIX)/include -L$(PREFIX)/lib -O3 -fopenmp
    BLASLIB = $(PREFIX)/lib/libopenblas.a
    LAPACKLIB = $(PREFIX)/lib/libopenblas.a

Run ``make``.

| You can specify the BLAS libraries in cmake with ``cmake -DBLAS_LIBRARIES="$PREFIX/lib/libopenblas.a" -DLAPACK_LIBRARIES="$PREFIX/lib/libopenblas.a" .``
| Just ``cmake .`` seems to be ignoring specified ``BLASLIB`` and ``LAPACKLIB``.

PETSc
=====

| Version: 3.7.5
| Source: http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-lite-3.7.5.tar.gz

ML and Hypre are enabled.

Build commands::

    ./configure --prefix="${PREFIX}" --with-openmp=1 --with-mpi=1 --with-x=0 --with-debugging=0 --with-blas-lapack-lib="${PREFIX}/lib/libopenblas.a" --with-scalapack-lib="${PREFIX}/lib/libscalapack.a" --download-ml=yes --download-hypre=yes
    make PETSC_DIR="${HOME}/SRC/petsc-3.7.5" PETSC_ARCH="arch-linux2-c-opt" all         # This is indicated at the end of configure
    make PETSC_DIR="${HOME}/SRC/petsc-3.7.5" PETSC_ARCH="arch-linux2-c-opt" install     # This is indicated at the end of make all
    make PETSC_DIR="${HOME}/aster" PETSC_ARCH="" test                                   # This is indicated at the end of make install
    make PETSC_DIR="${HOME}/aster" PETSC_ARCH= streams                                  # This is indicated at the end of make test

Unused configure options::

    --with-mpi-dir="${PREFIX}/lib/openmpi"
    --with-shared-libraries=0
    --configModules=PETSc.Configure
    --optionsModule=config.compilerOptions

TODO
----

* Check CUDA support (``--with-cuda``)

Code_Aster
==========

| Version: 12.7 (stable)
| Source: http://www.code-aster.org/FICHIERS/aster-full-src-12.7.0-1.noarch.tar.gz

The following environmental variables should be set when building from source:
