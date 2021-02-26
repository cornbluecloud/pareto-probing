import pathlib
import os
import pickle
import math,sys
import numpy as np,time
import argparse
import torch,random

def write_data(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def read_data(filename):
    with open(filename, "rb") as f:
        data = pickle.load(f)
    return data

def mkdir(folder):
    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)




def generate_remove(number_to_remove,percent_to_remove,training_size,output_file_base): 
    np.random.seed(768)
    idx = np.random.choice(768, number_to_remove, replace=False)
#    print(output_file_base % ('train', 'd%d_bert'%percent_to_remove))
#    return
    for mode in ['train', 'dev', 'test']:
        input_file = output_file_base % (mode, 'bert')
        bert_embeddings = read_data(input_file)

        del_bert = []
        for embeddings in bert_embeddings:
            temp = embeddings.copy()
            #temp=temp**3
            #temp=1/temp
            temp= temp.astype(np.float32)
            temp[:,idx] = 0
            del_bert.append(temp)
        if(mode=='train'):
            del_bert=del_bert[:int(training_size*0.01*len(del_bert))]
        
        write_data(output_file_base % (mode, 'B_bert_d%d_%d_bert'%(percent_to_remove,training_size)), del_bert)
            
    return



def main():
    
    language = 'english'
    output_path = './data/processed'
    output_path = os.path.join(output_path, language)
    mkdir(output_path)
    output_file_base = os.path.join(output_path, '%s--%s.pickle.bz2') 
    parser = argparse.ArgumentParser()
    parser.add_argument("--percent_to_remove", type=int, default=0 )
    parser.add_argument("--training_size", type=int, default=50 )
    
    args = parser.parse_args()
    
    percent_to_remove=args.percent_to_remove
        
    torch.manual_seed(42)
    torch.cuda.manual_seed(42)
    random.seed(42)
    np.random.seed(12)
    
#    multiplying_factor=[0.01,0.1,1,10,100]
#    for idx,representation in enumerate(np.arange(1,len(multiplying_factor)+1)):
#        det=False
#        while(det==False):
#            A = multiplying_factor[idx]*np.random.rand(768,768)
#            P = np.dot(np.linalg.inv(A), A)
#            round = np.where(np.abs(P) < 1e-10, 0, P)
#            round = np.where(np.abs(round - 1) <  1e-10  , 1, round)
#            det=(round==np.eye(768)).all()
#        A=multiplying_factor[idx]
#        for percent_to_remove in [0,80]:
#            for training_size in [100]:
#                print("removing features %d training size is %d"%(percent_to_remove,training_size))
#                number_to_remove=int((768*percent_to_remove)/100)
#    
#                generate_remove(number_to_remove,percent_to_remove,training_size,output_file_base,A,multiplying_factor[idx])
#                print("Done this experiment \n")
                

#    det=False
#    while(det==False):
#        A = np.random.rand(768,768)
#        P = np.dot(np.linalg.inv(A), A)
#        round = np.where(np.abs(P) < 1e-10, 0, P)
#        round = np.where(np.abs(round - 1) <  1e-10  , 1, round)
#        det=(round==np.eye(768)).all()
    #A=multiplying_factor[idx]
    for percent_to_remove in [80]:
        for training_size in np.arange(1,11)*10:
            print("removing features %d training size is %d"%(percent_to_remove,training_size))
            number_to_remove=int((768*percent_to_remove)/100)

            generate_remove(number_to_remove,percent_to_remove,training_size,output_file_base)
            print("Done this experiment \n")
    #R1<experiment_id>_d<dimension_remov>_<training>
    #I<experiment_id>_d<dimension_remov>_<training>
    
if __name__ == '__main__':
    main()
    
    

    
    