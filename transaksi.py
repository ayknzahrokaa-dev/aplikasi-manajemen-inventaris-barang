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
        self.__barang = barang
        self.__jumlah = jumlah

    def get_barang(self):
        return self.__barang

    def get_jumlah(self):
        return self.__jumlah
    
    def set_jumlah(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus positif")
        self.__jumlah = jumlah

    def proses(self):
        try:
            self.__barang.tambah_stok(self.__jumlah)
            print("Barang masuk berhasil")
        except Exception as e:
            print("Error:", e)

class BarangKeluar(AbstractTransaksi):

    def __init__(self, id_transaksi, barang, jumlah):
        super().__init__(id_transaksi)
        self.__barang = barang
        self.__jumlah = jumlah

    def get_barang(self):
        return self.__barang

    def get_jumlah(self):
        return self.__jumlah
    
    def set_jumlah(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus positif")
        self.__jumlah = jumlah

    def proses(self):
        try:
            self.__barang.tambah_stok(self.__jumlah)
            print("Barang keluar berhasil")
        except Exception as e:
            print("Error:", e)

class DetailTransaksi:
    def __init__(self, barang, jumlah):
        self.__barang = barang
        self.set_jumlah(jumlah)

    def get_barang(self):
        return self.__barang

    def get_jumlah(self):
        return self.__jumlah

    def set_jumlah(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus positif")
        self.__jumlah = jumlah

    def subtotal(self):
        return self.__barang.get_harga() * self.__jumlah