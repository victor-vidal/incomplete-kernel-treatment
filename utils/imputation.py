import os, numpy as np
from fancyimpute import IterativeSVD, KNN


input_data_path = '../incomplete_kernels'
output_data_path = '../imputed_kernels'


def imputate_matrix(
    kernel_matrix: np.ndarray, 
    kernel_name: str, 
    iteration: int, 
    percentage: int, 
    technique: str
) -> None:
    dim = len(kernel_matrix)
    
    matrix = kernel_matrix.copy()
    
    if not os.path.exists(output_data_path + f'/{iteration}/{technique}/{percentage}'):
        os.makedirs(output_data_path + f'/{iteration}/{technique}/{percentage}')
    
    if technique == 'zero':
        inputed_value = 0
    elif technique == 'mean':
        inputed_value = np.nanmean(matrix)
    elif technique == 'isvd':
        matrix = IterativeSVD().fit_transform(kernel_matrix)
        
        np.savetxt(
            output_data_path + f'/{iteration}/{technique}/{percentage}/{kernel_name}', 
            matrix, 
            delimiter='\t'
        )
        return
    elif technique == 'knn':
        matrix = KNN(k=3).fit_transform(kernel_matrix)
        
        np.savetxt(
            output_data_path + f'/{iteration}/{technique}/{percentage}/{kernel_name}', 
            matrix, 
            delimiter='\t'
        )
        return
    else:
        inputed_value = np.nanmedian(matrix)
    
    for r in range(dim):
        for c in range(dim):
            if np.isnan(matrix[r][c]):
                matrix[r][c] = inputed_value
                matrix[c][r] = inputed_value
        
    np.savetxt(
        output_data_path + f'/{iteration}/{technique}/{percentage}/{kernel_name}', 
        matrix, 
        delimiter='\t'
    )
    

# Drug kernels
# Read file names of drug kernels
with open('../complete_drug_response_data/Drug_kernels/Drug_kernel_file_names.txt', 'r') as f:
    kd_file_names = f.readlines()
kd_file_names = [x.split('\n')[0] for x in kd_file_names]


# Cell line kernels
# Read file names of cell line kernels
with open('../complete_drug_response_data/Cell_line_kernels/Cell_kernel_file_names.txt', 'r') as f:
    kc_file_names = f.readlines()
kc_file_names = [x.split('\n')[0] for x in kc_file_names]


# Merging lists of kernels names
kernel_file_names = kd_file_names + kc_file_names


# Imputating missing data
for iteration in range(5):
    for percentage in [10, 30, 50, 70]:
        for kernel_file_name in kernel_file_names:
            with open(input_data_path + f'/{iteration}/{percentage}/{kernel_file_name}', 'r') as f:
                kernel_matrix = np.loadtxt(f)
            for technique in ['zero', 'mean', 'median', 'isvd', 'knn']:
                imputate_matrix(
                    kernel_matrix, 
                    kernel_file_name, 
                    iteration,
                    percentage, 
                    technique
                )