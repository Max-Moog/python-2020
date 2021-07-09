from geoform import GeoForm

class Dreieck(GeoForm):

    def __init__(self, a, b, c, alpha, beta, gamma):
        GeoForm.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    def umfang(self):
        return self.a + self.b + self.c

    def flaeche(self):
        return 0
