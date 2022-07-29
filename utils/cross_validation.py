import os, numpy as np

input_path = '../complete_drug_response_data/Folds'
output_path = '../expirement_data/cross_validation'

for iteration in range(5):
    if not os.path.exists(f'{output_path}/{iteration}'):
        os.mkdir(f'{output_path}/{iteration}')
        
    outer_folds = np.loadtxt(f'{input_path}/outer_folds.txt').astype(int)
    np.random.shuffle(outer_folds)
    np.savetxt(f'{output_path}/{iteration}/outer_folds.txt', outer_folds, fmt='%i')
    
    for i_out in range(10):
        inner_folds = np.loadtxt(f'{input_path}/inner_folds_outer{i_out}.txt').astype(int)
        np.random.shuffle(inner_folds)
        np.savetxt(f'{output_path}/{iteration}/inner_folds_outer{i_out}.txt', inner_folds, fmt='%i')