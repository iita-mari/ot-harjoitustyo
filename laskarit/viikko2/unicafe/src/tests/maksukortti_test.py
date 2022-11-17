import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_saldo_vahenee_jos_rahaa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        kortti =  Maksukortti(2000)
        kortti.ota_rahaa(5000)

        self.assertEqual(str(kortti), "Kortilla on rahaa 20.00 euroa")

    def test_palauttaa_True_jos_rahat_riittavat(self):
        self.assertIs(self.maksukortti.ota_rahaa(1000), True)

    def test_palauttaa_False_jos_rahat_eivat_riita(self):
        self.assertIs(self.maksukortti.ota_rahaa(5000), False)