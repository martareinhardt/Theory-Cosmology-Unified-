# test_cosmology.py
import unittest
from astropy.cosmology import Planck18
import cosmology_friedmann as cf

class TestCosmology(unittest.TestCase):

    def test_h0_value(self):
        """Verifica se H0 está perto do valor oficial"""
        self.assertAlmostEqual(Planck18.H0.value, 67.66, delta=0.1)

    def test_friedmann_at_z0(self):
        """H(z=0) deve ser igual a H0"""
        H_at_0 = cf.friedmann(0, alpha=0.0)
        self.assertAlmostEqual(H_at_0.value, Planck18.H0.value, delta=1)

if __name__ == '__main__':
    unittest.main()
