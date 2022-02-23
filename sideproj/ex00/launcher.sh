#conda info

prefix='       base environment :'
suffix='  (writable)'

CONDA_PREFIX=$(conda info | grep -i 'base environment' | sed -e "s/$prefix//" -e "s/$suffix$//")

source $CONDA_PREFIX/etc/profile.d/conda.sh

conda activate tf-gta

python test.py