# This is a list of environmental variables used in attempt #1
# to build Code_Aster. It is provided as a reference.

[ -d "${HOME}/aster" ] || exit 1

[ -d "${HOME}/aster" ] && export PREFIX="${HOME}/aster"
# [ -x "${PREFIX}/bin/mpicc" ] && export CC="mpicc"
# [ -x "${PREFIX}/bin/mpiCC" ] && export CPP="mpiCC"

[ -x "${PREFIX}/bin/mpicc" ] && export MPICC="mpicc"
[ -x "${PREFIX}/bin/mpiCC" ] && export MPICXX="mpiCC"
[ -x "${PREFIX}/bin/mpif90" ] && export MPIFC="mpif90"
[ -x "${PREFIX}/bin/mpif77" ] && export MPIF77="mpif77"

export LDFLAGS="-L${PREFIX}/lib"

# Used by OpenBLAS
export USE_OPENMP=1
export OMP_NUM_THREADS=4    # Do we really need this?
export TARGET="HASWELL"

# -fopenmp implies -fopenmp-simd
export CFLAGS="-I${PREFIX}/include -O2 -fno-stack-protector -fPIC -fopenmp"

# Used by ScaLAPACK
# Use SLmake.inc for now
# export CFLAGS="-I${PREFIX}/include -fopenmp"
