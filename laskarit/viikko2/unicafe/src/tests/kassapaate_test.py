import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_rahamaara_ja_myytyjen_lounaiden_maara_on_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullisen_lounaan_osalta_oikein_kun_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_toimii_maukkaan_lounaan_osalta_oikein_kun_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_maksu_ei_riittava_rahat_palautetaan_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_maksu_ei_riittava_rahat_palautetaan_maukkaat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_edullisissa_kun_rahaa_riittavasti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        
        self.assertEqual(self.kortti.ota_rahaa(240), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)        
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_toimii_maukkaissa_kun_rahaa_riittavasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        
        self.assertEqual(self.kortti.ota_rahaa(400), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_mene_lapi_kun_rahaa_ei_ole_riittavasti_edulliset(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.ota_rahaa(240), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_ei_mene_lapi_kun_rahaa_ei_ole_riittavasti_maukkaat(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.ota_rahaa(400), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kortille_rahan_lataaminen_lisaa_saldoa_ja_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(self.kortti.saldo, 2000)

    def test_kortille_ei_voi_ladata_negatiivista_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kortti.saldo, 1000)

    def test_kassassa_rahaa_antaa_oikean_luvun_euroina(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa_euroina()), "1000.0")