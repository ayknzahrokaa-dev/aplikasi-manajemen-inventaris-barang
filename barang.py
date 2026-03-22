from abc import ABC, abstractmethod
from mixins import LogMixin, ValidasiMixin, DiskonMixin

class AbstractBarang(ABC, LogMixin, ValidasiMixin):
    
    def __init__(self, id_barang, nama, stok, harga):
        self.__id = id_barang
        self.__nama = nama
        self.set_stok(stok)
        self.set_harga(harga)

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_stok(self):
        return self.__stok

    def get_harga(self):
        return self.__harga

    def set_stok(self, stok):
        self.validasi_stok(stok)
        self.__stok = stok

    def set_harga(self, harga):
        self.validasi_harga(harga)
        self.__harga = harga

    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus positif")
        self.__stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah > self.__stok:
            raise ValueError("Stok tidak cukup")
        self.__stok -= jumlah

    @abstractmethod
    def get_info(self):
        pass
    

class BarangElektronik(AbstractBarang, DiskonMixin):

    def __init__(self, id_barang, nama, stok, harga, garansi):
        super().__init__(id_barang, nama, stok, harga)
        self.__garansi = garansi

    def get_info(self):
        return f"Elektronik: {self.get_nama()} | Stok: {self.get_stok()} | Garansi: {self.__garansi}"

class BarangMakanan(AbstractBarang):

    def __init__(self, id_barang, nama, stok, harga, expired):
        super().__init__(id_barang, nama, stok, harga)
        self.__expired = expired

    def get_info(self):
        return f"Makanan: {self.get_nama()} | Expired: {self.__expired}"

class BarangPakaian(AbstractBarang, DiskonMixin):

    def __init__(self, id_barang, nama, stok, harga, ukuran):
        super().__init__(id_barang, nama, stok, harga)
        self.__ukuran = ukuran

    def get_info(self):
        return f"Pakaian: {self.get_nama()} | Ukuran: {self.__ukuran}"