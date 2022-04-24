import numpy as np
import math

import experimental_data as exp
import TRM


def RMS(params):
    """
    Evaluate the chi_2 function between the experimental energies and the theoretical data set which is obtained with the current set of parameters
    """

    exp_data = exp.EXCITATION_ENERGIES

    # generate the theoretical data with the current parameter set
    th_data = [TRM.Excitation_Energy(exp.PHONONS[idx], exp.SPINS[idx],
                                     params[0], params[1], params[2]) for idx in range(len(exp_data))]

    th_data[0] = TRM.MAXVAL

    maxval_checker = any(e == TRM.MAXVAL for e in th_data)
    if(maxval_checker == True):
        return -TRM.MAXVAL

    N = len(exp_data)+1
    chi2_sum = 0
    for idx in range(len(exp_data)):
        f_chi = float(np.power(exp_data[idx]-th_data[idx], 2)/exp_data[idx])
        chi2_sum += f_chi

    chi2 = math.sqrt(1.0/N*chi2_sum)

    return chi2
