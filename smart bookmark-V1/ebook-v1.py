import json

file_data = "data_buku.json"

def load_data():
    try:
        with open(file_data, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(file_data, "w") as f:
        json.dump(data, f)

def tambah_buku(data):
    judul = input("Masukkan judul buku: ")
    
    buku = {
        "judul": judul,
        "halaman": 0,
        "status": "sedang dibaca"
    }

    data.append(buku)
    save_data(data)
    print("Buku berhasil ditambahkan!")

def lihat_buku(data):
    if len(data) == 0:
        print("Belum ada buku.")
    else:
        for i, buku in enumerate(data):
            print(i+1, "-", buku["judul"], "| halaman:", buku["halaman"], "|", buku["status"])
            
def update_halaman(data):

    lihat_buku(data)

    nomor = int(input("Pilih nomor buku: "))
    halaman_baru = int(input("Masukkan halaman terakhir dibaca: "))

    data[nomor-1]["halaman"] = halaman_baru

    save_data(data)

    print("Progress berhasil diperbarui!")

data = load_data()

def tandai_selesai(data):

    lihat_buku(data)

    nomor = int(input("Pilih nomor buku yang selesai: "))

    data[nomor-1]["status"] = "selesai"

    save_data(data)

    print("Buku ditandai selesai!")
    
def remove(data):

    lihat_buku(data)

    nomor = int(input("Pilih nomor buku yang diremove: "))

    data= data.pop(nomor-1)
    
    save_data(data)

    print("Buku berhasil di hapus")
    
def reset_pages(data):

    lihat_buku(data)

    nomor = int(input("Pilih nomor buku yang direset: "))

    data [nomor-1]["halaman"]=0
    
    save_data(data)

    print("Buku berhasil di reset")
    
while True:

    print("\n=== EBOOK TRACKER ===")
    print("1. Tambah buku")
    print("2. Lihat daftar buku")
    print("3. Update halaman")
    print("4. Tandai selesai")
    print("5. Reset halaman")
    print("6. Hapus daftar buku")
    print("7. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_buku(data)

    elif pilihan == "2":
        lihat_buku(data)

    elif pilihan == "3":
        update_halaman(data)

    elif pilihan == "4":
        tandai_selesai(data)

    elif pilihan == "5":
        reset_pages(data)

    elif pilihan == "6":
        remove(data)

    elif pilihan == "7":
        break

    else:
        print("Pilihan tidak valid")