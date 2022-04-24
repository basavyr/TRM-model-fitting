from scipy.optimize import curve_fit
import numpy as np


def Fit_Model(model_function, input_data, experimental_data, initial_params, param_bounds):
    """
    Main procedure which generates a set of output parameters that `best` reproduce the experimental data

    TRM FITTING PARAMETERS: 1-, 2-, 3-axis moments of inertia

    - `model_function`: the method which defines the energy for a triaxial rotor model. For each band (yrast n=0,n=1,...), the energy depends on the spin sequence I,I+2,..., the corresponding wobbling phonon number, and the three Moments of Inertia (the MOI are the **fitting parameters**)

    - `input_data`: a tuple of the form (data0_1,data0_2), where each item represents an array created via the numpy's `np.asarray()` method. Within the TRM, the two items are the wobbling phonons and the spins,, respectively.

    - `experimental_data`: an array (defined as classic Python arrays) containing the experimental values for the energies within each band (no sorting is required, each energy will correspond to a spin and a phonon number given in the `input_data`)
    """

    try:
        fit_parameters, _ = curve_fit(
            model_function, input_data, experimental_data, p0=initial_params, bounds=param_bounds)
    except Exception as issue:
        print('There was an issue within the fitting procedure')
        return -1
    else:
        return fit_parameters
