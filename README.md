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

Run `generate_inverse.py`, store representations in `inverse_power`. 

### Bert representations with removed dimensions

Run `generate_missing_data.py`, store representations in  `reduced_training_data`.

## Generate reduced training dataset

Store in reduced_training_dataset.

## Train the models

We use the following instructions to train the models, fixing 'pos_tag' task and 'linear' model:

Evaluate the one-hot representations with:
```!python -u src/h02_learn/random_search.py --language english --data-path ./data/processed --representation onehot --checkpoint-path ./checkpoints --task pos_tag --model linear```

Inversed Bert representations:
```!python -u src/h02_learn/random_search.py --language english --data-path ./data/processed --representation inv_bert --checkpoint-path ./checkpoints_new --task pos_tag --model linear```

Negative Bert representations:
```!python -u src/h02_learn/random_search.py --language english --data-path ./data/processed --representation negative_bert --checkpoint-path ./checkpoints_new --task pos_tag --model linear```

Dropped representations:
```!python -u src/h02_learn/random_search.py --language english --data-path ./data/processed --representation d1_bert --checkpoint-path ./checkpoints_new --task pos_tag --model linear```



