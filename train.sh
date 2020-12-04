#!/bin/sh
#SBATCH --job-name=<exp_id>_B_bert80_pareto_tes
#SBATCH -o /mnt/nfs/scratch1/bgullapalli/pareto-probing/log/%j.txt
#SBATCH --time=1-3:00:00
#SBATCH --partition=titanx-long
#SBATCH --mem-per-cpu=10GB
#SBATCH --gres=gpu:2
#SBATCH --cpus-per-task=1
#SBATCH -d singleton

export MKL_NUM_THREADS=7
export OPENBLAS_NUM_THREADS=7
export OMP_NUM_THREADS=7

 
python -W ignore  -u /mnt/nfs/scratch1/bgullapalli/pareto-probing/src/h02_learn/random_search.py --language <language> --data-path ./data/processed/ --representation B_<representation_type>_d<missing_data>_<training_data>_<representation> --checkpoint-path ./checkpoints --task <task> --model <model> 


