import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(3000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 40.00)

    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.00)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_palauttaa_True_jos_rahat_riittavat(self):
        self.assertIs(self.maksukortti.ota_rahaa(1000), True)

    def test_palauttaa_False_jos_rahat_eivat_riita(self):
        self.assertIs(self.maksukortti.ota_rahaa(5000), False)

    def test_saldon_tulostus_tulee_oikeassa_muodossa(self):
        self.maksukortti.ota_rahaa(12)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.88 euroa")