import pathlib
import os
import pickle
import math
import numpy as np

def write_data(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def read_data(filename):
    with open(filename, "rb") as f:
        data = pickle.load(f)
    return data

def mkdir(folder):
    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)

language = 'english'
output_path = './data/processed'
output_path = os.path.join(output_path, language)
mkdir(output_path)
output_file_base = os.path.join(output_path, '%s--%s.pickle.bz2') 

def generate_remove(number_to_remove,percent_to_remove): 
    np.random.seed(768)
    idx = np.random.choice(768, number_to_remove, replace=False)
    for mode in ['train', 'dev', 'test']:
        input_file = output_file_base % (mode, 'bert')
        bert_embeddings = read_data(input_file)
        del_bert = []
        for embeddings in bert_embeddings:
            temp = embeddings.copy()
            temp[:,idx] = 0
            del_bert.append(temp)
            write_data(output_file_base % (mode, 'd%d_bert'%percent_to_remove), del_bert)
            
    return

for i in range(10,100,10):

    temp=int((768*i)/100)
    generate_remove(temp,i)
    print(temp) 