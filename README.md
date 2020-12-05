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

## Download universal dependencies (UD) data and preprocess (produce BERT representations)

```
make get_ud
make preprocess
```

## Generate the data (synthetic representations)

Generate data with specific parameters using `generate_missing_data.py` which removes part of embeddings of bert representetions or reduces the training set size with the command
```
$ make generate_data.sh PERCNET_TO_REMOVE=<percent_to_remove> TRAINING_SIZE=<training_size>
```
There is a range of "precent_to_remove" we tried: [10,20,30,40,50,60,70,80,90].
And the range of "training_size": [10,20,30,40,50,60,70,80,90,100].

The output data are saved in `B_bert_d80_d20_reduced_training_size` and `reduced_training_data`.


Generate a number of data using `generate_data_run.py`, which loads the configuration from `default_generate.py`, iteratively writes and calls `schedule_*.sh`, and repetitively runs `random_search.py`, with the command
```
$ make generate_data_run.sh --config=default --trainer=inference --dataset=dataset_new --model==model_inference --experiment==1
```
The output data is saved in `B_bert`.


## Train the models

Train a model using  `random_search.py` with the command
```
$ make train LANGUAGE=<language> REPRESENTATION_TYPE=<representation_type> MISSING_DATA=<missing_data> TRAINING_DATA=<training_data> REPRESENTATION=<representation> TASK=<task> MODEL=<model> 
```

Train a number of models using `run.py`, which loads the configuration from `default.py`, repetetively calls `schedule_*.sh`, and runs `random_search.py`, with the command
```
$ make run
```

