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
                print(torch.norm(w, p = 'nuc'))

                d = w.shape[1]
                print(d)
                for r in [0.1, 1, 10]:
                    for i in range(10):

                        A = generate_A(d, r)

                        Aw = torch.mm(w, A)
                        print(r, torch.norm(Aw, p = 'nuc'))
                # A2 = generate_A(wb.shape[1])
                # Awb = torch.mm(wb, A2)
                # print(torch.norm(wb, p = 'nuc'))
                # print(torch.norm(Awb, p = 'nuc'))
