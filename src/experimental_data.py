import numpy as np


def MeV(energy):
    """
    Transform the energy from KeV to MeV
    """
    return np.round(energy/1000.0, 3)


# ABSOLUTE VALUES
ENERGIES_BAND1 = [3790.3, 4256.3, 4884.2, 5678.3,
                  6563.3, 7524.3, 8574.3, 9690.3, 10821.3, 11984.3]
ENERGIES_BAND2 = [4456.2, 4986.2, 5647.2,
                  6442.2, 7319.3, 8265.3, 9283.3, 10436.3]
SPINS_BAND1 = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
SPINS_BAND2 = [11, 13, 15, 17, 19, 21, 23, 25]
PHONONS_BAND1 = [0 for _ in range(len(ENERGIES_BAND1))]
PHONONS_BAND2 = [1 for _ in range(len(ENERGIES_BAND2))]
ENERGY_BANDHEAD = ENERGIES_BAND1[0]
SPIN_BANDHEAD = SPINS_BAND1[0]
PHONON_BANDHEAD = PHONONS_BAND1[0]

# EXCITATION ENERGIES
# Defined as the energy for a given I state minus a reference value
# Reference value: the band head energy for the first state within the zero-phonon band
# Final arrays will not contain the ground spin state from yrast band
EXCITATION_ENERGIES_KEV = [e-ENERGY_BANDHEAD for e in ENERGIES_BAND1[1:]] + \
    [e-ENERGY_BANDHEAD for e in ENERGIES_BAND2]
SPINS = np.asarray(SPINS_BAND1[1:]+SPINS_BAND2)
PHONONS = np.asarray(PHONONS_BAND1[1:]+PHONONS_BAND2)
EXCITATION_ENERGIES = list(map(MeV, EXCITATION_ENERGIES_KEV))
# define the tuple of arrays which will be used within the model function that enters in the curve_fit function
INPUT_DATA = (PHONONS, SPINS)


def main():
    print(f'Spins-> {SPINS}')
    print(f'Phonons-> {PHONONS}')
    print(f'Excitation energies-> {EXCITATION_ENERGIES}')


if __name__ == '__main__':
    main()
