def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)

def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

# variable input
class Permintaan():
    minimum = 2100
    maximum = 3500

    def turun(self, x):
        if x <= self.minimum:
            return 1
        elif x >= self.maximum:
            return 0
        else:
            return down(x, self.minimum, self.maximum)
    
    def naik(self, x):
        if x <= self.minimum:
            return 0
        elif x >= self.maximum:
            return 1
        else:
            return up(x, self.minimum, self.maximum)

class Persediaan():
    minimum = 100
    maximum = 250

    def sedikit(self, x):
        if x <= self.minimum:
            return 1
        elif x >= self.maximum:
            return 0
        else:
            return down(x, self.minimum, self.maximum)

    def banyak(self, x):
        if x <= self.minimum:
            return 0
        elif x >= self.maximum:
            return 1
        else:
            return up(x, self.minimum, self.maximum)

# variable output
class Produksi():
    minimum = 1000
    maximum = 5000
    permintaan = 0
    persediaan = 0

    def berkurang(self, a):
        return self.maximum - a * (self.maximum - self.minimum)

    def bertambah(self, a):
        return self.minimum + a * (self.maximum - self.minimum)

    def _inferensi(self):
        pmt = Permintaan()
        psd = Persediaan()
        data_inferensi = []
        # [R1] JIKA Permintaan TURUN, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERKURANG.
        a1 = min(pmt.turun(self.permintaan), psd.banyak(self.persediaan))
        z1 = self.berkurang(a1)
        # [R2] JIKA Permintaan TURUN, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERKURANG.
        a2 = min(pmt.turun(self.permintaan), psd.sedikit(self.persediaan))
        z2 = self.berkurang(a2)
        # [R3] JIKA Permintaan NAIK, dan Persediaan BANYAK, MAKA
        # Produksi Barang BERTAMBAH.
        a3 = min(pmt.naik(self.permintaan), psd.banyak(self.persediaan))
        z3 = self.bertambah(a3)
        # [R4] JIKA Permintaan NAIK, dan Persediaan SEDIKIT, MAKA
        # Produksi Barang BERTAMBAH.
        a4 = min(pmt.naik(self.permintaan), psd.sedikit(self.persediaan))
        z4 = self.bertambah(a4)