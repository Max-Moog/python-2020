from geoform import GeoForm

class Rechteck(GeoForm):

    def __init__(self, laenge, breite):
        GeoForm.__init__(self)
        self.laenge = laenge
        self.breite = breite

    def umfang(self):
        return 2 * (self.laenge + self.breite)

    def flaeche(self):
        return self.laenge * self.breite
