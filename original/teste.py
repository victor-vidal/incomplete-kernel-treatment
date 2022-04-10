import numpy as np
import copy
from math import sqrt
from sklearn import preprocessing, metrics
from pairwisemkl.learner.compute_M import *
from pairwisemkl.learner.compute_a_regression import *
from pairwisemkl.learner.optimize_kernel_weights import *
from pairwisemkl.learner.cg_kron_rls import CGKronRLS

print('There is hope in this world.')