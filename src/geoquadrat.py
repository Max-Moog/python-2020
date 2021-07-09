from georechteck import Rechteck

class Quadrat(Rechteck):

    def __init__(self, laenge, breite):
        GeoForm.__init__(self)
        self.laenge = laenge
        self.breite = breite
        self.laenge = self.breite

    def umfang(self):
        return self.laenge * 4

    def flaeche(self):
        return self.laenge * 2
