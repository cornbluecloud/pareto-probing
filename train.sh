#!/bin/sh
#SBATCH --job-name=pareto_test
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

 
python -W ignore  -u src/h02_learn/random_search.py --language english --data-path ./data/processed/ --representation bert --checkpoint-path ./checkpoints --task dep_label --model linear 


