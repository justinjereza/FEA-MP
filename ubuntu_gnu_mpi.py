# encoding: utf-8

"""
Fichier de configuration WAF pour version parallèle sur Ubuntu 12.04 :
- Compilateur : GNU
- MPI         : système (OpenMPI, Ubuntu 12.04)
- BLAS        : OpenBLAS
- Scalapack   : système (Ubuntu 12.04)
- PETSc       :
"""



import ubuntu_gnu

def configure(self):
    opts = self.options
    ubuntu_gnu.configure(self)

    self.env.prepend_value('LIBPATH', [
        '/home/justin/aster/public/mumps-mpi-4.10.0/lib',
        '/home/justin/aster/public/petsc-3.7.5/lib',
        ])

    self.env.prepend_value('INCLUDES', [
        '/home/justin/aster/public/petsc-3.7.5/include',
        '/home/justin/aster/public/petsc-3.7.5/include/petsc'
        ])

    # self.env.append_value('LIB', ('X11',))

    opts.parallel = True

    opts.enable_mumps  = True
    opts.mumps_version = '4.10.0'
    opts.mumps_libs = 'dmumps zmumps smumps cmumps mumps_common pord metis scalapack-openmpi blas esmumps scotch scotcherr'

    opts.enable_petsc = True
    opts.petsc_libs='petsc HYPRE ml'
    opts.embed_petsc = True

