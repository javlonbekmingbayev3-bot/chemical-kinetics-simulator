"""
Simulation engine for reactor kinetics.
Handles batch and CSTR models.
"""

import numpy as np
import math
from analysis import calculate_conversion, calculate_error
from solvers import euler_step
from kinetics import rate_law_first_order


# -------------------------------------------------
# Shared utilities
# -------------------------------------------------
def initialize_arrays(C0, n):
    R = np.zeros(n + 1)
    R[0] = C0
    return R


# -------------------------------------------------
# Batch Reactor
# -------------------------------------------------
def simulate_batch(C0, k, t_final, n):
    dt = t_final / n
    time = np.linspace(0, t_final, n + 1)

    R_analytical = initialize_arrays(C0, n)
    R_numerical = initialize_arrays(C0, n)

    for i in range(n):
        t = time[i + 1]

        # analytical solution
        R_analytical[i + 1] = C0 * math.exp(-k * t)

        # numerical Euler method
        rate = rate_law_first_order(R_numerical[i], k)
        R_numerical[i + 1] = euler_step(R_numerical[i], rate, dt)

    P_analytical = C0 - R_analytical
    P_numerical = C0 - R_numerical

    errors, max_error = calculate_error(R_analytical, R_numerical)
    conversion = calculate_conversion(C0, R_analytical[-1])

    return (
        time,
        R_analytical,
        R_numerical,
        P_analytical,
        P_numerical,
        errors,
        max_error,
        conversion
    )


# -------------------------------------------------
# CSTR Model (simplified steady-state form)
# -------------------------------------------------
def simulate_cstr(C0, k, t_final, n):
    time = np.linspace(0, t_final, n + 1)

    R_analytical = initialize_arrays(C0, n)
    R_numerical = initialize_arrays(C0, n)

    for i in range(n):
        t = time[i + 1]

        R_analytical[i + 1] = C0 / (1 + k * t)
        R_numerical[i + 1] = R_analytical[i + 1]

    P_analytical = C0 - R_analytical
    P_numerical = P_analytical.copy()

    errors, max_error = calculate_error(R_analytical, R_numerical)
    conversion = calculate_conversion(C0, R_analytical[-1])

    return (
        time,
        R_analytical,
        R_numerical,
        P_analytical,
        P_numerical,
        errors,
        max_error,
        conversion
    )
