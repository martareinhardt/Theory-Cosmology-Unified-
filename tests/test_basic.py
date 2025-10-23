import pytest
import numpy as np

def test_hubble_constant_positive():
    """Check if the Hubble constant is positive."""
    H0 = 67.74
    assert H0 > 0, "Hubble constant should be positive."

def test_cosmic_density_sum():
    """Check that the sum of density parameters is approximately 1."""
    omega_m = 0.315
    omega_r = 0.0001
    omega_lambda = 0.685
    total = omega_m + omega_r + omega_lambda
    assert np.isclose(total, 1.0, atol=0.01), f"Density sum = {total}, expected ~1"
