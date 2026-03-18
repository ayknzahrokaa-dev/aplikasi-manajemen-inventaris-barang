from mixins import LogMixin

class Inventaris(LogMixin):

    def __init__(self):
        self.__daftar_barang = []

    def tambah_barang(self, barang):
        try:
            self.__daftar_barang.append(barang)
            self.log(f"{barang.get_nama()} ditambahkan")
        except Exception as e:
            print("Error:", e)

    def tampilkan_barang(self):
        for b in self.__daftar_barang:
            print(b.get_info())

    def cari_barang(self, id_barang):
        for b in self.__daftar_barang:
            if b.get_id() == id_barang:
                return b
        raise ValueError("Barang tidak ditemukan")

    def hapus_barang(self, id_barang):
        try:
            barang = self.cari_barang(id_barang)
            self.__daftar_barang.remove(barang)
            self.log("Barang dihapus")
        except Exception as e:
            print("Error:", e)