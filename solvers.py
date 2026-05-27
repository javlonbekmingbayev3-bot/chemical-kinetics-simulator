"""
Numerical solvers for ODEs.
"""

def euler_step(C, rate, dt):
    return C + rate * dt
