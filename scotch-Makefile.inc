EXE         =
LIB         = .a
OBJ         = .o

MAKE        = make
AR          = ar
ARFLAGS     = -ruv
CAT         = cat
CCS         = gcc
CCP         = mpicc
CCD         = gcc
CFLAGS      = -I$(PREFIX)/include -O2 -fPIC -fno-stack-protector -fopenmp -Wl,--no-as-needed -DCOMMON_FILE_COMPRESS_GZ -DCOMMON_PTHREAD -DCOMMON_RANDOM_FIXED_SEED -DSCOTCH_RENAME -DSCOTCH_RENAME_PARSER -DSCOTCH_PTHREAD -Drestrict=__restrict
CLIBFLAGS   =
LDFLAGS     = -L$(PREFIX)/lib -lz -lm -lrt -lpthread
CP          = cp
LEX         = flex -Pscotchyy -olex.yy.c
LN          = ln
MKDIR       = mkdir
MV          = mv
RANLIB      = ranlib
YACC        = bison -y -pscotchyy -b y
