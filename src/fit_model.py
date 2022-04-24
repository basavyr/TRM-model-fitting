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


def Show_Params(params):
    """
    print the parameters to console
    """
    print(params[0], params[1], params[2])


def Save_Params(params, path):
    """
    write parameters to file
    """
    with open(path, 'w+') as writer:
        writer.write(str(params[0]))
        writer.write("\n")
        writer.write(str(params[1]))
        writer.write("\n")
        writer.write(str(params[2]))
        writer.write("\n")


def Fitting_Workflow():
    """
    Evaluate the TRM model via the fitting procedure defined in `Fit_Model`, but with different initial guesses for [I1,I2,I3]\n
    GENERAL WORKFLOW ->\n
    1. For every initial guess `p0_i` a set of fitting parameters will be obtained `P_fit_i(p0_i)`
    2. For that particular `P_fit_i`, the chi_2 function (i.e., RMS) of the theoretical energies will be calculated
    3. Choose the `P_fit_i` which gives the smallest chi_2 value
    4. Return the best `P_fit_i`
    """

    test_array1 = [12]
    test_array2 = [13]
    test_array3 = [14]

    for I1_guess in test_array1:
        for I2_guess in test_array2:
            for I3_guess in test_array3:
                p0_i = [I1_guess, I2_guess, I3_guess]
                print(p0_i)


def main():
    Fitting_Workflow()


if __name__ == "__main__":
    main()
