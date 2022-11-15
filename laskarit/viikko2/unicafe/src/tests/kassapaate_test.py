import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_rahamaara_alussa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edulliset_alussa_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaat_alussa_oikein(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateisosto_edulliset_toimii(self):
        self.kassa.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kateisosto_maukkaat_toimii(self):
        self.kassa.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kateisosto_edulliset_maksu_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kateisosto_maukkaat_maksu_ei_riita(self):
        self.kassa.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttimaksu_edulliset_palauttaa_True_jos_kortilla_rahaa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertIs(self.kortti.ota_rahaa(240), True)

    def test_korttimaksu_maukkaasti_palauttaa_True_jos_kortilla_rahaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertIs(self.kortti.ota_rahaa(400), True)

    def test_korttimaksu_edulliset_palauttaa_False_jos_kortilla_ei_riittavasti_varaa(self):
        self.kortti = Maksukortti(100)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertIs(self.kortti.ota_rahaa(240), False)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_korttimaksu_maukkaasti_palauttaa_False_jos_kortilla_ei_riittavasti_varaa(self):
        self.kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertIs(self.kortti.ota_rahaa(400), False)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla__edullisen_ostettaessa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla__maukkaan_ostettaessa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)

    def test_kortille_ladataan_negatiivinen_summa_ei_muuta_saldoa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)