import matplotlib.pyplot as plt


def plot_results(time, R, P, R_num, reactor_mode):
    plt.figure(figsize=(10, 6))

    # analytical
    plt.plot(time, R, label="Reactant (Analytical)", linewidth=2)
    plt.plot(time, P, label="Product (Analytical)", linewidth=2)

    # numerical
    plt.plot(time, R_num, "--", label="Reactant (Euler)", alpha=0.8)

    plt.title(f"{reactor_mode} Reactor Simulation")
    plt.xlabel("Time (s)")
    plt.ylabel("Concentration (mol/L)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
