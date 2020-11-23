#!/bin/sh
#SBATCH --job-name=pareto_pre_process
#SBATCH -o /mnt/nfs/scratch1/bgullapalli/pareto-probing/log/%j.txt
#SBATCH --time=3:00:00
#SBATCH --partition=1080ti-short
#SBATCH --mem-per-cpu=10GB
#SBATCH --gres=gpu:2
#SBATCH --cpus-per-task=1
#SBATCH -d singleton

export MKL_NUM_THREADS=7
export OPENBLAS_NUM_THREADS=7
export OMP_NUM_THREADS=7

python -W ignore src/h01_data/process.py --language english --ud-path ./data/ud/ud-treebanks-v2.5 --output-path ./data/processed/ --representation onehot
