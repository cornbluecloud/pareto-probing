#!/bin/sh
#SBATCH --job-name=<exp_id>_pareto_generate_data
#SBATCH -o /mnt/nfs/scratch1/bgullapalli/pareto-probing/log/%j.txt
#SBATCH --time=3:50:00
#SBATCH --partition=2080ti-short
#SBATCH --mem-per-cpu=10GB
#SBATCH --gres=gpu:2
#SBATCH --cpus-per-task=1
#SBATCH -d singleton

export MKL_NUM_THREADS=7
export OPENBLAS_NUM_THREADS=7
export OMP_NUM_THREADS=7

 
python -W ignore  generate_missing_data.py --percent_to_remove 20 --training_size 20 --multiplication_factor 1
