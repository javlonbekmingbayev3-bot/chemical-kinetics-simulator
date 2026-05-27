import numpy as np


def calculate_conversion(C0, final_R):
    return ((C0 - final_R) / C0) * 100


def calculate_error(R_exact, R_numeric):
    errors = np.abs(R_exact - R_numeric)
    max_error = np.max(errors)
    return errors, max_error
