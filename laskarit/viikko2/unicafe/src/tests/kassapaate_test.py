import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_rahamaara_ja_myydyt_luonaat_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullisilla_raha_riittaa(self):
        palautettava = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(palautettava, 60)

    def test_kateisosto_edullisilla_raha_ei_riita(self):
        palautettava = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(palautettava, 200)

    def test_kateisosto_maukkaille_raha_riittaa(self):
        palautettava = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(palautettava, 100)

    def test_kateisosto_maukkaille_raha_ei_riita(self):
        palautettava = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(palautettava, 300)

    def test_korttiosto_edullisille_kortilla_tarpeeksi_rahaa(self):
        palautettava = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(palautettava, True)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_korttiosto_edullisille_kortilla_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(800)
        palautettava = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(palautettava, False)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_korttiosto_maukkaille_kortilla_tarpeeksi_rahaa(self):
        palautettava = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(palautettava, True)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_korttiosto_maukkaille_kortilla_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(800)
        palautettava = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(palautettava, False)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_rahan_lataus_kortille_positiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.maksukortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_epakelvon_summan_lataus_kortille(self):
        palautettava = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(palautettava, None)



        

