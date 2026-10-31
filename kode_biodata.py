import os

daftar_pegawai = []

def tampilkan_biodata():
    if not os.path.exists("biodata.txt"):
        print("belum ada data pegawai")
        return
    with open("biodata.txt","r") as f:
        print(f.read())

def cari_pegawai(nama):
    for pegawai in daftar_pegawai:
        if pegawai["nama"].lower() == nama.lower():
            return pegawai
    return None 
def validasi_input(pesan):
    while True:
        try:
            angka = int(input(pesan))
            if angka > 0:
                return angka
            print("angka harus lebih dari 0")
        except ValueError:
            print("masukkan angka bukan huruf")

def input_pegawai():
    nama = input("Masukkan nama: ")
    umur = validasi_input("Masukkan umur: ")
    alamat = input("Masukkan alamat: ")
    pekerjaan = input("Masukkan pekerjaan: ")
    return {"nama": nama, "umur": umur, "alamat": alamat, "pekerjaan": pekerjaan}

def simpan_pegawai(pegawai):
    with open("biodata.txt", "a") as f:
        f.write(f"{pegawai['nama']} | {pegawai['umur']} | {pegawai['alamat']} | {pegawai['pekerjaan']}\n")

def muat_biodata():
    if not os.path.exists("biodata.txt"):
        return
    with open("biodata.txt", "r") as f:
        for baris in f:
            bagian = baris.strip().split(" | ")
            if len(bagian) == 4:
                daftar_pegawai.append({
                    "nama": bagian[0],
                    "umur": int(bagian[1]),
                    "alamat": bagian[2],
                    "pekerjaan": bagian[3],
                })

tampilkan_biodata()
muat_biodata()
while True:
    pegawai = input_pegawai()
    daftar_pegawai.append(pegawai)
    simpan_pegawai(pegawai)
    lanjut = input("Tambah pegawai lagi? (y/n): ")
    if lanjut.lower() != "y":
        break
        

cari = input("Cari nama pegawai: ")
hasil = cari_pegawai(cari)

if hasil:
    print(hasil)
else:
    print("Pegawai tidak ditemukan.")

