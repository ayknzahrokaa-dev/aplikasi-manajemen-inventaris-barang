class Laporan:

    def laporan_stok(self, daftar_barang):
        print("\n=== LAPORAN STOK ===")
        for barang in daftar_barang:
            print(barang.get_info())

    def laporan_nilai(self, daftar_barang):
        print("\n=== TOTAL NILAI INVENTARIS ===")
        total = 0
        for barang in daftar_barang:
            total += barang.get_stok() * barang.get_harga()
        print(f"Total nilai: {total}")