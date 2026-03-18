from barang import BarangElektronik, BarangMakanan, BarangPakaian
from inventaris import Inventaris
from transaksi import BarangMasuk, BarangKeluar
from user import Admin, Staff

def main():
    print("=== SISTEM MANAJEMEN INVENTARIS ===")

    admin = Admin("U01", "Admin Utama")
    staff = Staff("U02", "Staff Gudang")

    print("\n[USER]")
    print(f"Admin: {admin.akses()}")
    print(f"Staff: {staff.akses()}")

    inv = Inventaris()

    try:
     
        b1 = BarangElektronik("E01", "Laptop", 10, 10000000, "2 Tahun")
        b2 = BarangMakanan("M01", "Roti", 20, 10000, "2026-01-01")
        b3 = BarangPakaian("P01", "Kaos", 15, 50000, "L")

        # Tambah ke inventaris
        inv.tambah_barang(b1)
        inv.tambah_barang(b2)
        inv.tambah_barang(b3)

        print("\n=== DAFTAR BARANG ===")
        inv.tampilkan_barang()

        print("\n=== DISKON ===")
        harga_diskon = b1.hitung_diskon(b1.get_harga(), 10)
        print(f"Harga Laptop setelah diskon 10%: {harga_diskon}")

        print("\n=== TRANSAKSI ===")

        t1 = BarangKeluar("T01", b1, 3)
        t1.proses()

        t2 = BarangMasuk("T02", b2, 5)
        t2.proses()

        print("\n=== SETELAH TRANSAKSI ===")
        inv.tampilkan_barang()

        print("\n=== UPDATE STOK ===")
        b3.set_stok(25)
        print(b3.get_info())


        print("\n=== CARI BARANG ===")
        barang = inv.cari_barang("P01")
        print("Ditemukan:", barang.get_info())


        print("\n=== HAPUS BARANG ===")
        inv.hapus_barang("M01")
        inv.tampilkan_barang()


        print("\n=== TEST ERROR ===")

        # stok negatif
        try:
            b1.set_stok(-5)
        except Exception as e:
            print("Error stok:", e)

        # barang tidak ditemukan
        try:
            inv.cari_barang("X99")
        except Exception as e:
            print("Error cari:", e)

        # stok tidak cukup
        try:
            t3 = BarangKeluar("T03", b1, 999)
            t3.proses()
        except Exception as e:
            print("Error transaksi:", e)

    except Exception as e:
        print("Terjadi error utama:", e)


if __name__ == "__main__":
    main()