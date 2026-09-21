class Mahasiswa:
    def __init__(self, nama: str, nim: str, sks: int) -> None:
        self.nama: str = nama
        self.nim: str = nim
        # Atribut privat untuk melindungi data SKS yang diambil
        self.__sks: int = 0
        # Validasi SKS melalui setter
        self.set_sks(sks)

    # Getter untuk membaca atribut privat __sks
    def get_sks(self) -> int:
        return self.__sks

    # Setter dengan validasi SKS (minimal 1 SKS, maksimal 24 SKS)
    def set_sks(self, beban_sks: int) -> None:
        if 1 <= beban_sks <= 24:
            self.__sks = beban_sks
        else:
            print(f"Peringatan: Beban SKS {self.nama} ({beban_sks} SKS) tidak valid! Diset default ke 2 SKS.")
            self.__sks = 2


class JadwalKelas:
    def __init__(self, kode_mk: str, nama_mk: str, hari_jam: str, ruangan: str) -> None:
        self.kode_mk: str = kode_mk
        self.nama_mk: str = nama_mk
        self.hari_jam: str = hari_jam
        self.ruangan: str = ruangan
        # Enkapsulasi array data mahasiswa dalam kelas (private attribute)
        self.__daftar_mahasiswa: list[Mahasiswa] = []

    def tambah_mahasiswa(self, mahasiswa: Mahasiswa) -> None:
        # Validasi objek menggunakan isinstance() sesuai petunjuk teknis
        if isinstance(mahasiswa, Mahasiswa):
            self.__daftar_mahasiswa.append(mahasiswa)
            print(f"Berhasil menambahkan {mahasiswa.nama} ke kelas {self.nama_mk}")
        else:
            print("Gagal: Objek yang dimasukkan harus merupakan instansi dari class Mahasiswa!")

    # Private method yang hanya bisa dipanggil dari dalam class
    def __calculate_payroll(self) -> int:
        # Menghitung total beban SKS akumulasi seluruh mahasiswa di kelas ini
        total_sks_kelas = sum(m.get_sks() for m in self.__daftar_mahasiswa)
        return total_sks_kelas

    # Public method untuk memproses & mengevaluasi total beban SKS kelas
    def process_payroll(self) -> None:
        print(f"\n--- Rekapitulas Beban SKS Kelas {self.nama_mk} ---")
        total_sks = self.__calculate_payroll()
        print(f"Jumlah Mahasiswa Terdaftar : {len(self.__daftar_mahasiswa)} orang")
        print(f"Total Beban SKS Terakumulasi: {total_sks} SKS")

    def tampilkan_jadwal(self) -> None:
        print(f"\n==================================================")
        print(f" Kode & Mata Kuliah : {self.kode_mk} - {self.nama_mk}")
        print(f" Jadwal Kuliah     : {self.hari_jam}")
        print(f" Ruangan           : {self.ruangan}")
        print(f"==================================================")
        if not self.__daftar_mahasiswa:
            print("Belum ada mahasiswa yang mengambil jadwal ini.")
            return
        print("Daftar Mahasiswa Terdaftar:")
        for idx, m in enumerate(self.__daftar_mahasiswa, start=1):
            print(f" {idx}. {m.nama} (NIM: {m.nim}) - Beban: {m.get_sks()} SKS")


# ==========================================
# Pengujian Program Utama (Main Program)
# ==========================================
if __name__ == "__main__":
    # 1. Buat objek JadwalKelas
    jadwal_pbo = JadwalKelas(
        kode_mk="CSP2171",
        nama_mk="Pemrograman Berorientasi Objek",
        hari_jam="Senin, 13.00 - 15.30 WITA",
        ruangan="Ruang Lab Komputer 2"
    )

    # 2. Instansiasi objek Mahasiswa (Uji validasi SKS)
    mhs1 = Mahasiswa("Sicilia Dien", "250211060048", 3)  # Valid (3 SKS)
    mhs2 = Mahasiswa("Debora Ludong", "250211060108", 30)   # Tidak valid (>24, diatur default ke 2 SKS)

    print("\n--- Pendaftaran Jadwal Kelas ---")
    # 3. Tambahkan Mahasiswa ke Jadwal Kelas
    jadwal_pbo.tambah_mahasiswa(mhs1)
    jadwal_pbo.tambah_mahasiswa(mhs2)

    # 4. Uji validasi `isinstance()` dengan menginput data non-Mahasiswa
    jadwal_pbo.tambah_mahasiswa("Dosen Pengajar")

    # 5. Tampilkan Jadwal Kelas dan Daftar Mahasiswa
    jadwal_pbo.tampilkan_jadwal()

    # 6. Memproses rekap SKS (memanggil private method `__calculate_payroll`)
    jadwal_pbo.process_payroll()