
import argparse
import importlib
import numpy as np
import os.path
import glob
from os import path
import sys


def argument_parser():
    parser = argparse.ArgumentParser(description="sample")
    parser.add_argument('--config', default='default', type=str, help='configuration')
    parser.add_argument('--trainer', default='inference', type=str, help='trainer scripts')
    parser.add_argument('--dataset', default='dataset_new', type=str, help='dataset')
    parser.add_argument('--model', default='model_inference', type=str, help='model')
    parser.add_argument('--experiment', default=1, type=int, help='comet.ml')
    args = parser.parse_args()
    return args

import os
import subprocess


def train_all(index, config_keys, configs):
    global exp_id
    global job_queues


    
    if index >= len(config_keys):

        
        with open("generate_data.sh", "r") as f:
            schedule_template = f.read()
            
            

        curr_template = schedule_template.replace("<exp_id>", str(exp_id))
        curr_template = curr_template.replace("<percent_to_remove>", str(cf['percent_to_remove'])).replace("<training_size>",str(cf['training_size']))
     

        with open("/mnt/nfs/scratch1/bgullapalli/pareto-probing/schedule_%d.sh" % (exp_id), "w") as f:
            f.write(curr_template + "\n")
            
        command = "sbatch /mnt/nfs/scratch1/bgullapalli/pareto-probing/schedule_%d.sh" % (exp_id)
        job_queues.append(command)
        exp_id+=1

            
    else:
        if type(configs[config_keys[index]]) == list:
            for val in configs[config_keys[index]]:
                cf[config_keys[index]] = val
                train_all(index+1, config_keys, configs)
        else:
            cf[config_keys[index]] = configs[config_keys[index]]
            train_all(index+1, config_keys, configs)
            
###            




def main():
    global cf
    global model_def
    global dataset
    global job_queues
    global train
    global experiment
    

    args = argument_parser()
    configs = importlib.import_module("default_generate").config
    config_keys = list(configs.keys())

    cf = {}
    train_all(0, config_keys, configs)

    while(len(job_queues)>0):
        out = subprocess.Popen(['squeue', '-u', 'bgullapalli'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        if(len(stdout.split())<8*30):
            command=job_queues.pop()
            print(subprocess.check_output(command, shell=True))


exp_id=0
job_queues=[]
main()


