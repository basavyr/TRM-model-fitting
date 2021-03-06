import numpy as np
import math


import experimental_data as exp


# escape value to be used in case of math failure
MAXVAL = 6969696969


def Wobbling_Frequency(I, I1, I2, I3):
    """
    The wobbling frequency for the rotor Hamiltonian
    """
    # implement fragmented stopping conditions
    if(I1 < 0.0):
        return MAXVAL
    if(I2 < 0.0):
        return MAXVAL
    if(I3 < 0.0):
        return MAXVAL
    if(I1 == 0):
        return MAXVAL
    if(I2 == 0):
        return MAXVAL
    if(I3 == 0):
        return MAXVAL
    if(I1 == I2):
        return MAXVAL
    if(I1 == I3):
        return MAXVAL
    if(I2 == I3):
        return MAXVAL
    if(I3 >= I2 and I3 <= I1):
        return MAXVAL
    if(I3 <= I2 and I3 >= I1):
        return MAXVAL

    # compute the pure product within the square root of the wobbling frequency
    t_pure = (1.0/(2.0*I1)-1.0/(2.0*I3))*(1.0/(2.0*I2)-1.0/(2.0*I3))
    try:
        t_sqrt = math.sqrt(t_pure)
    except ValueError as err:
        print('There was an issue while evaluated the wobbling frequency...\n')
        print(f'Issue => {err}')
        print(f'Failed for: [{I1}, {I2}, {I3}]')
        return MAXVAL
    else:
        # return the wobbling frequency if the term under the square root is positive
        omega = 2.0*I*t_sqrt
        return omega


def Absolute_Energy(n, I, I1, I2, I3):
    """
    Absolute energy formula\n
    n -> wobbling phonon number\n
    I -> Spin\n
    I1,I2,I3 -> the three moments of inertia, fitting parameters\n
    """

    rotor_term = 1.0/(2.0*I3)*I*(I+1.0)
    wobbling_term = Wobbling_Frequency(I, I1, I2, I3)*(n+0.5)
    energy = rotor_term+wobbling_term

    return energy


def Excitation_Energy(n, I, I1, I2, I3):
    """
    Define the excitation energy for the triaxial rotator.\n
    The excitation energy is defined as the difference between an energy level and the band head\n

    n -> wobbling phonon number\n
    I -> Spin\n
    I1,I2,I3 -> the three moments of inertia, fitting parameters\n
    """

    # absolute value for the band head
    e0 = Absolute_Energy(exp.PHONON_BANDHEAD, exp.SPIN_BANDHEAD, I1, I2, I3)

    # absolute value for the current spin value
    e = Absolute_Energy(n, I, I1, I2, I3)

    excitation_energy = e-e0

    return excitation_energy


# create a function which evaluates the excitation energy for a triaxial rotor
def TRM_Model_Energy(input_data, I1, I2, I3):
    """
    The `model_energy` evaluates the TRM energy for an entire set of spins and phonon numbers\n
    The `input_data` will be unpacked into proper lists for the phonons and spins, respectively\n
    Each of the unpacked objects is a numpy array constructed via the `np.asarray()` method\n
    This function will return a list of excitation energies, evaluated for a particular set of moments of inertia (i.e., the fitting parameters\n
    """

    # unpacking procedure such that curve_fit can take a function with multiple arguments
    # curve fit requires that the input data is of the form (DATA), where DATA is made up of multiple `np.asarrays()`
    phonons, spins = input_data
    excitation_energies = Excitation_Energy(phonons, spins, I1, I2, I3)

    return excitation_energies
