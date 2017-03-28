# coding=utf-8

'''Configuration for waf using aster-full prerequisites'''

import os.path as osp
import sys

def configure(self):
    opts = self.options
    if ''.strip():
        self.env.append_value('OPT_ENV', ''.splitlines())

    self.env['FC'] = 'mpif90'
    self.env['CC'] = 'mpicc'
    # to check med libs
    self.env['CXX'] = 'mpiCC'

    # sometimes required
    self.env.append_unique('LINKFLAGS', ['-Wl,--allow-multiple-definition'])

    self.env.append_value('LIBPATH', [
        '/lib',
        '/lib',
        '/home/justin/aster/lib',
        '/home/justin/aster/public/hdf5-1.8.14/lib',
        '/home/justin/aster/public/med-3.2.0/lib',
        '/home/justin/aster/public/metis-4.0.3/lib',
        '/home/justin/aster/public/mfront-2.0.3/lib',
        '/home/justin/aster/public/scotch-5.1.11/lib',
        '/home/justin/aster/public/mumps-mpi-4.10.0/lib',
        '/home/justin/aster/public/petsc-3.5.4/lib',
        '/lib',
        '/lib',
        # autotools uses lib64 on some platforms
        '/lib64',
        '/lib64',
    ])

    self.env.append_value('INCLUDES', [
        '/include',
        '/include',
        '/home/justin/aster/include',
        '/home/justin/aster/public/hdf5-1.8.14/include',
        '/home/justin/aster/public/med-3.2.0/include',
        '/home/justin/aster/public/metis-4.0.3/include',
        '/home/justin/aster/public/mfront-2.0.3/include',
        '/home/justin/aster/public/scotch-5.1.11/include',
        '/home/justin/aster/public/mumps-mpi-4.10.0/lib',
        '/home/justin/aster/public/petsc-3.5.4/include',
        '/include',
        '/include',
    ])

    self.env['OPTLIB_FLAGS'] = '-L/usr/lib/x86_64-linux-gnu -lpthread -L/usr/lib/x86_64-linux-gnu -lz'.split()
    opts.maths_libs = 'openblas scalapack'
    opts.embed_math = True

    opts.enable_hdf5 = True
    # opts.embed_hdf5 = True

    opts.enable_med = True
    # opts.embed_med = True

    opts.enable_scotch = True
    opts.embed_scotch = True

    opts.embed_aster = True
    opts.embed_fermetur = True

    opts.parallel = True

    opts.enable_mumps  = True
    # opts.mumps_version = '4.10.0'
    opts.mumps_libs = 'dmumps zmumps smumps cmumps mumps_common pord metis openblas scalapack esmumps scotch scotcherr'

    opts.enable_petsc = True
    opts.petsc_libs = 'petsc HYPRE ml'
    opts.embed_petsc = True
