import os, random, numpy as np


input_data_path = '../complete_drug_response_data'
output_data_path = '../incomplete_kernels'


def nan_generator(
    kernel_matrix: np.ndarray, 
    kernel_name: str, 
    iteration: int, 
    percentage: int
) -> None:
    dim = len(kernel_matrix)
    num_total_cells = dim ** 2

    num_nans = round(num_total_cells * (percentage / 100))

    aux = 0
    while aux < num_nans:
        r = random.randrange(dim)
        c = random.randrange(dim)

        if (not np.isnan(kernel_matrix[r][c])) and (r != c):
            kernel_matrix[r][c] = np.nan
            kernel_matrix[c][r] = np.nan
            aux += 2

    if not os.path.exists(output_data_path + f'/{iteration}'):
        os.mkdir(output_data_path + f'/{iteration}')
    if not os.path.exists(output_data_path + f'/{iteration}/{percentage}'):
        os.mkdir(output_data_path + f'/{iteration}/{percentage}')

    np.savetxt(output_data_path + f'/{iteration}' +
               f'/{percentage}/' + kernel_name, kernel_matrix, delimiter='\t')


# Drug kernels
# Read file names of drug kernels
with open(input_data_path + '/Drug_kernels/Drug_kernel_file_names.txt', 'r') as f:
    kd_file_names = f.readlines()
kd_file_names = [x.split('\n')[0] for x in kd_file_names]
# Prepare a list of drug kernels
kd_list = []
for kd in kd_file_names:
    with open(input_data_path + '/Drug_kernels/' + kd, 'r') as f:
        dimension = len(f.readlines())
        kd_list.append(np.loadtxt(input_data_path + '/Drug_kernels/' + kd, skiprows=0, usecols=range(0, dimension)))


# Cell line kernels
# Read file names of cell line kernels
with open(input_data_path + '/Cell_line_kernels/Cell_kernel_file_names.txt', 'r') as f:
    kc_file_names = f.readlines()
kc_file_names = [x.split('\n')[0] for x in kc_file_names]
kc_list = []
# Prepare a list of cell line kernels
for kc in kc_file_names:
    with open(input_data_path + '/Cell_line_kernels/' + kc, 'r') as f:
        dimension = len(f.readlines())
        kc_list.append(np.loadtxt(input_data_path + '/Cell_line_kernels/' + kc, skiprows=0, usecols=range(0, dimension)))


# Generate incomplete kernel matrices
for iteration in range(5):
    for percentage in [10, 30, 50, 70]:
        for i in range(len(kd_file_names)):
            nan_generator(
                kd_list[i].copy(), 
                kd_file_names[i], 
                iteration, 
                percentage
            )

        for i in range(len(kc_file_names)):
            nan_generator(
                kc_list[i].copy(), 
                kc_file_names[i], 
                iteration, 
                percentage
            )
