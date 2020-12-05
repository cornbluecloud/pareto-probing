# Evaluating Probes by Synthetic Representations

This repository extends the code from "Pareto Probing"(Pimentel et al., EMNLP 2020). We evaluate multiple probes metrics by various synthetic representations.

## Install Dependencies
Create a Conda environment:
```
$ conda env create -f environment.yml
```

Install transformers, fastText, and other dependencies:
```
$ conda install -y pytorch torchvision cudatoolkit=10.1 -c pytorch
$ pip install transformers==3.5.1
$ pip install git+https://github.com/facebookresearch/fastText
$ pip install seaborn ipdb conllu

```

## Download and parse universal dependencies (UD) data

```
make get_ud
make process LANGUAGE=english REPRESENTATION=onehot
make process LANGUAGE=english REPRESENTATION=bert
```

## Generate the data (synthetic representations)

Generate data with specific parameters using `generate_missing_data.py` which removes part of embeddings of bert representetions as well as reducing the training set size with the command
```
$ make generate_data.sh
```

Generate a number of data using `generate_data_run.py`, which repetetively calls `schedule_*.sh` and runs `random_search.py`, with the command
```
$ make generate_data_run.sh
```


## Train the models

Train a model using random search with the command
```
$ make train LANGUAGE = <language> REPRESENTATION_TYPE = <representation_type> MISSING_DATA = <missing_data> TRAINING_DATA = <training_data> REPRESENTATION = <representation> TASK = <task> MODEL =  <model> 
```

Train a number of models using `run.py`, which repetetively calls `schedule_*.sh` and runs `random_search.py`, with the command
```
$ make run
```


