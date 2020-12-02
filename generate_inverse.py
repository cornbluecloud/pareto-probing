import numpy as np
import pickle
import torch
import os
rootdir = 'R00_d0_100_bert'
def generate_A(d, r):
    cond = False
    while not cond:
        A = r * np.random.rand(d,d)
        P = np.dot(np.linalg.inv(A), A)
        round = np.where(np.abs(P) < 1e-10, 0, P)
        round = np.where(np.abs(round - 1) <  1e-10  , 1, round)
        cond = (round==np.eye(d)).all()
    return torch.from_numpy(np.linalg.inv(A)).float()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        path = os.path.join(subdir, file)

        if 'tch' in path:
            model = torch.load(path, map_location=torch.device('cpu'))['model_state_dict']
            w = model['linear.weight']
            b = model['linear.bias'].view(-1, 1)

            wb = torch.cat((w,b), dim =1 )


            if torch.norm(w, p = 'nuc') > 230 and torch.norm(w, p = 'nuc') < 250:
                print(torch.norm(wb, p = 'nuc'))
                print(torch.matrix_rank(wb))
                print(wb.shape)
                iwb = 1/wb
                print(torch.norm(iwb, p = 'nuc'))
                print(torch.matrix_rank(iwb))

                # Awb = torch.mm(wb, A2)
                # print(torch.norm(wb, p = 'nuc'))
                # print(torch.norm(Awb, p = 'nuc'))
