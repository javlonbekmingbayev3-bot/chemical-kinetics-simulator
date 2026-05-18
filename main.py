"""A computational tool that simulates
 chemical reactions in a reactor and visualizes
   how concentrations change over time."""
import math
import numpy as np
import matplotlib.pyplot as plt

def simulate_reactor():
    print("--- Chemical Reactor Kinetics Simulator ---")
    
    reactor_mode = input("Enter reactor type (BATCH, CSTR, PFR): ").strip().upper()
    if reactor_mode not in ["BATCH", "CSTR", "PFR"]:
        print("Invalid type. Defaulting to BATCH.")
        reactor_mode = "BATCH"

    try:
        C0 = float(input("Enter the initial concentration of the reactant (moles/L): "))
        k = float(input("Enter the rate constant, k (1/s): "))
        t_final = float(input("Enter the total simulation time or space-time (s): "))
        num_intervals = int(input("Enter the number of time intervals: "))
    except ValueError:
        print("Invalid input. Please enter numerical values only.")
        return

    # --- Simulation Setup ---
    dt = t_final / num_intervals
    time_arrays = np.linspace(0, t_final, num_intervals + 1)
    
    # Arrays to store exact analytical vs numerical results
    R_exact = np.zeros(num_intervals + 1)
    R_euler = np.zeros(num_intervals + 1)
    
    R_exact[0] = C0
    R_euler[0] = C0

    # --- Core Computation ---
    for i in range(num_intervals):
        # Upgrade 2: Fixing numerical methods (comparing Euler to Exact Analytical)
        if reactor_mode in ["BATCH", "PFR"]:
            # Exact analytical solution for 1st order: C = C0 * e^(-kt). It is not present for all reactions.
            R_exact[i+1] = C0 * math.exp(-k * time_arrays[i+1])
            
            # Forward Euler Numerical Method: C_new = C_old + (dC/dt) * dt. Computer's guess.
            dRdt = -k * R_euler[i]
            R_euler[i+1] = R_euler[i] + (dRdt * dt)
            
        elif reactor_mode == "CSTR":
            # For continuous stirred-tank reactors, 'time' acts as space-time (tau)
            # Exact steady-state design equation for 1st order: C = C0 / (1 + k*tau)
            R_exact[i+1] = C0 / (1 + k * time_arrays[i+1])
            
            # CSTR equations are algebraic at steady state, so numerical ODE 
            # integration (Euler) doesn't apply the same way as Batch/PFR.
            R_euler[i+1] = R_exact[i+1] 

    # Calculate Product Concentrations
    P_exact = C0 - R_exact
    P_euler = C0 - R_euler

    # Upgrade 4: Show error
    errors = np.abs(R_exact - R_euler)
    max_error = np.max(errors)
    
    final_R = R_exact[-1]
    conversion = ((C0 - final_R) / C0) * 100

    # --- Console Output ---
    print("\n" + "="*40)
    print(f"RESULTS FOR {reactor_mode} REACTOR")
    print("="*40)
    print(f"Final exact concentration of reactant: {final_R:.4f} mol/L")
    print(f"Final exact concentration of product:  {P_exact[-1]:.4f} mol/L")
    print(f"Final Conversion:                      {conversion:.2f}%")
    
    if reactor_mode in ["BATCH", "PFR"]:
        print(f"Maximum Numerical Error (Euler):       {max_error:.4e} mol/L")
        if max_error > (0.05 * C0):
            print("WARNING: High numerical error. Increase the number of time intervals to improve Euler accuracy.")

    # --- Upgrade 1: Plot results ---
    plt.figure(figsize=(10, 6))
    
    # Plot exact analytical solutions (smooth lines)
    plt.plot(time_arrays, R_exact, 'b-', label='Reactant (Exact)', linewidth=2)
    plt.plot(time_arrays, P_exact, 'g-', label='Product (Exact)', linewidth=2)
    
    # Plot numerical approximations (dashed lines)
    if reactor_mode in ["BATCH", "PFR"]:
        plt.plot(time_arrays, R_euler, 'r--', label='Reactant (Numerical Euler)', alpha=0.8)
        plt.plot(time_arrays, P_euler, 'y--', label='Product (Numerical Euler)', alpha=0.8)

    plt.title(f"{reactor_mode} Reactor Simulation: First-Order Kinetics ($A \\rightarrow B$)")
    xlabel = "Space-Time, $\\tau$ (s)" if reactor_mode != "BATCH" else "Time, t (s)"
    plt.xlabel(xlabel)
    plt.ylabel("Concentration (mol/L)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_reactor()
