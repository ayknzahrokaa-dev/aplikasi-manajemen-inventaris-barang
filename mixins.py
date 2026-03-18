from datetime import datetime

class LogMixin:
    def log(self, message):
        print(f"[LOG {datetime.now()}] {message}")


class ValidasiMixin:
    def validasi_stok(self, stok):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")

    def validasi_harga(self, harga):
        if harga < 0:
            raise ValueError("Harga tidak boleh negatif")


class DiskonMixin:
    def hitung_diskon(self, harga, persen):
        return harga - (harga * persen / 100)