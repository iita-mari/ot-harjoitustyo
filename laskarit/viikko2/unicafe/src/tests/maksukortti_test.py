import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_saldo_vahenee_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_metodi_palauttaa_True_jos_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)

    def test_ota_rahaa_metodi_palauttaa_False_jos_rahat_eivat_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5000), False)

    def test_saldo_euroina_laskee_saldon_euroina_oikein(self):
        self.maksukortti.lataa_rahaa(87)
        self.assertEqual(str(self.maksukortti.saldo_euroina()), "10.87")