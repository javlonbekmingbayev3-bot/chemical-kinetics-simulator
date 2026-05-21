# chemical-reactor-simulator
Simulation of chemical reactors (Batch, CSTR, PFR) using analytical and numerical methods to model reaction kinetics and concentration changes over time.

# Purpose
This project explores how concentration of reactants and products change over time in various reactor types - such as Batch, CSTR (continuous stirred-tank reactor), PFR (plug flow reactor). Additionally, it calculates reaction progress, concentration behavior, and conversion in first-order reaction systems.

# ⚙️ Features 
- Batch, CSTR, PFR modeling (concentration changes in each)
- First-order kinetics simulation
- Euler numerical method for comparison between Analytical and numerical methods
- Error estimation
- Conversion tracking
- Visualization of concentration profiles using matplotlib.pyplot

# 🧪 Scientific Background
The model includes first-order reaction kinetics and material balance equations expressed as ordinary differential equations.

# 🧮 Methods used
- Analytical solution
- Euler method (numerical integration)
- Time sampling (NumPy)

# How to run
python main.py

# 📊 Output
- concentration vs time plots
- comparison graphs

# Future Potential Improvements
- Runge-Kutta methods
- GUI interface
