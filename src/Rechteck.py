class Rechteck:
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def Flaeche(self):
        return (self.laenge * self.breite)

    def Umfang(self):
        return 2*(self.laenge + self.breite)


