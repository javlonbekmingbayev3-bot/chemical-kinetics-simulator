"""
Mini Reactor Simulator - Main Entry Point
-----------------------------------------
Runs reactor simulations and visualizes results.
"""

import numpy as np
from simulation import simulate_batch, simulate_cstr
from plotting import plot_results


def simulate_reactor():
    print("\n--- Chemical Reactor Kinetics Simulator ---")

    reactor_mode = input("Enter reactor type (BATCH, CSTR, PFR): ").strip().upper()
    if reactor_mode not in ["BATCH", "CSTR", "PFR"]:
        print("Invalid type. Defaulting to BATCH.")
        reactor_mode = "BATCH"

    try:
        C0 = float(input("Initial concentration (mol/L): "))
        k = float(input("Rate constant k (1/s): "))
        t_final = float(input("Total time (s): "))
        num_intervals = int(input("Number of intervals: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # --- model dispatch (clean architecture) ---
    MODELS = {
        "BATCH": simulate_batch,
        "CSTR": simulate_cstr,
        "PFR": simulate_batch  # placeholder (same as batch for now)
    }

    results = MODELS[reactor_mode](C0, k, t_final, num_intervals)

    (
        time,
        R_analytical,
        R_numerical,
        P_analytical,
        P_numerical,
        error,
        max_error,
        conversion
    ) = results

    # --- output ---
    print("\n" + "=" * 45)
    print(f"{reactor_mode} REACTOR RESULTS")
    print("=" * 45)
    print(f"Final reactant concentration: {R_analytical[-1]:.5f} mol/L")
    print(f"Final product concentration:  {P_analytical[-1]:.5f} mol/L")
    print(f"Conversion:                  {conversion:.2f}%")
    print(f"Max numerical error:         {max_error:.6f}")

    # --- visualization ---
    plot_results(time, R_analytical, P_analytical, R_numerical, reactor_mode)


if __name__ == "__main__":
    simulate_reactor()
