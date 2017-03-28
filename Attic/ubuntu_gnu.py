# encoding: utf-8

"""
Fichier de configuration WAF pour version séquentielle sur Ubuntu 12.04 :
- Compilateur : GNU
- BLAS        : OpenBLAS
"""

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
        '/home/justin/aster/public/hdf5-1.8.14/lib',
        '/home/justin/aster/public/med-3.2.0/lib',
        '/home/justin/aster/public/metis-4.0.3/lib',
        '/home/justin/aster/public/scotch-5.1.11/lib',
        '/home/justin/aster/public/mfront-2.0.3/lib',
        '/lib',
        '/lib64',
        ])

    self.env.append_value('INCLUDES', [
        '/home/justin/aster/public/hdf5-1.8.14/include',
        '/home/justin/aster/public/med-3.2.0/include',
        '/home/justin/aster/public/metis-4.0.3/include',
        '/home/justin/aster/public/scotch-5.1.11/include',
        '/home/justin/aster/public/mfront-2.0.3/include',
        '/include',
        ])

    self.env['OPTLIB_FLAGS'] = '-L/home/justin/aster/lib -lopenblas -lscalapack'.split() + '-L/usr/lib/x86_64-linux-gnu -lpthread -L/usr/lib/x86_64-linux-gnu -lz'.split() + [ '-Wl,--no-as-needed' ]

    opts.maths_libs = 'openblas scalapack'
    opts.embed_math = True

    opts.enable_hdf5 = True
    opts.hdf5_libs  = 'hdf5 dl z'
    opts.embed_hdf5 = True

    opts.enable_med = True
    opts.med_libs  = 'med stdc++'
    opts.embed_med  = True

    opts.enable_petsc = True

    opts.enable_scotch = True
    opts.embed_scotch  = True

    opts.embed_aster    = True
    opts.embed_fermetur = True
