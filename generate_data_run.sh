#!/bin/sh
#SBATCH --job-name=generate_data
#SBATCH -o /mnt/nfs/scratch1/bgullapalli/pareto-probing/log/%j.txt
#SBATCH --time=6-14:00:00
#SBATCH --partition=titanx-long
#SBATCH --mem-per-cpu=10GB
#SBATCH --gres=gpu:2
#SBATCH --cpus-per-task=1
#SBATCH -d singleton

export MKL_NUM_THREADS=7
export OPENBLAS_NUM_THREADS=7
export OMP_NUM_THREADS=7

python -W ignore generate_data_run.py  




