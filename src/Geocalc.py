from Rechteck import Rechteck
import unittest

def calc_run():
    antwort = input("Rechteck oder Kreis? :")

    if antwort == "Rechteck":
        r = Rechteck(2,4)
        u = r.Umfang()
        laenge = input("Gebe die Laenge ein:")
        breite = input("Gebe die Breite ein:")
        print(r, u)

    if antwort == "Kreis":
        f = Flaeche()
        u = Umfang()
        radius = input("Gebe den Radius ein:")
        print(f,u)


class Kreis_test(unittest.TestCase):

    def test_umfang(self):
        k = Kreis(2)
        self.assertEqual(k.umfang(), 12.5663704)

    def test_flaeche(self):
        k = Kreis(2)
        self.assertEqual(k.flaeche(), 12.5663704)

if __name__ == '__main__':
    unittest.main()
