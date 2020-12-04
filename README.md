# Evaluating Probes by Synthetic Representations

This repository extends the code from "Pareto Probing"(Pimentel et al., EMNLP 2020). We evaluate multiple probes metrics by various synthetic representations.

## Install Dependencies

Install transformers, fastText, and other dependencies on Google Colab:
```
!pip install transformers==3.5.1
!pip install git+https://github.com/facebookresearch/fastText
!pip install seaborn ipdb conllu

```

## Download and parse universal dependencies (UD) data

```
!make get_ud
!make process LANGUAGE=english REPRESENTATION=onehot
!make process LANGUAGE=english REPRESENTATION=bert
```

## Generate synthetic representations

### Inversed Bert representations

`generate_inverse.py` 

### Bert representations with removed dimensions

`generate_missing_data.py`

## Train your models

We use the following instructions to train the models, fixing 'pos_tag' task and 'linear' model:
```!python -u src/h02_learn/random_search.py --language english --data-path ./data/processed --representation onehot --checkpoint-path ./checkpoints --task pos_tag --model linear```
```!python -u src/h02_learn/random_search.py --language english --data-path ./data/processed --representation inv_bert --checkpoint-path ./checkpoints_new --task pos_tag --model linear```


