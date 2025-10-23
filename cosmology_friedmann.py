# test_cosmology.py
import unittest
from astropy.cosmology import Planck18

# Tenta importar o módulo
try:
    import cosmology_friedmann as cf
    MODULE_OK = True
except ImportError:
    MODULE_OK = False

class TestCosmology(unittest.TestCase):

    def test_planck_h0(self):
        """Verifica se o H0 do Planck está correto"""
        self.assertAlmostEqual(Planck18.H0.value, 67.66, delta=0.1)

    @unittest.skipIf(not MODULE_OK, "cosmology_friedmann.py não encontrado")
    def test_friedmann_at_z0(self):
        """H(z=0) deve ser igual a H0"""
        H_at_0 = cf.friedmann(0, alpha=0.0)
        self.assertAlmostEqual(H_at_0.value, Planck18.H0.value, delta=1)

if __name__ == '__main__':
    unittest.main()
