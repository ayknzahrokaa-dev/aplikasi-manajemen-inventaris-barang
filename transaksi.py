from abc import ABC, abstractmethod
from datetime import datetime

class AbstractTransaksi(ABC):

    def __init__(self, id_transaksi):
        self._id = id_transaksi
        self._tanggal = datetime.now()

    @abstractmethod
    def proses(self):
        pass

class BarangMasuk(AbstractTransaksi):

    def __init__(self, id_transaksi, barang, jumlah):
        super().__init__(id_transaksi)
        self.barang = barang
        self.jumlah = jumlah

    def proses(self):
        try:
            self.barang.tambah_stok(self.jumlah)
            print("Barang masuk berhasil")
        except Exception as e:
            print("Error:", e)

class BarangKeluar(AbstractTransaksi):

    def __init__(self, id_transaksi, barang, jumlah):
        super().__init__(id_transaksi)
        self.barang = barang
        self.jumlah = jumlah

    def proses(self):
        try:
            self.barang.kurangi_stok(self.jumlah)
            print("Barang keluar berhasil")
        except Exception as e:
            print("Error:", e)