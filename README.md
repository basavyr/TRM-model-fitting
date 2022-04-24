# TRM Model Fitting

* A fitting implementation for the Triaxial-Rotor-Model which can be used on arbitrary energy spectra.
* Within TRM, the free parameters are the three moments of inertia (corresponding to the principal axes of the deformed ellipsoid). 
* The implementation uses Python's `scipy` module and it is based on the `curve_fit` function.
* As input data, the spins and energies for the collective states within the spectra are required.
* Eventually, the __wobbling phonon number__ is also necessary if there are multiple excited bands built on top of the yrast sequence.
