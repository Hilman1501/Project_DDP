import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

def tampilkan_rekomendasi():
    preferensi_berkuah = var_berkuah.get()
    preferensi_rasa = var_rasa.get()
    preferensi_harga = var_harga.get()

    rekomendasi = dapatkan_rekomendasi(preferensi_berkuah, preferensi_rasa, preferensi_harga)

    if rekomendasi:
        teks_rekomendasi.delete(1.0, tk.END)
        for makanan, harga in rekomendasi.items():
            teks_rekomendasi.insert(tk.END, f"- {makanan} (Harga: {harga} IDR)\n")
    else:
        messagebox.showinfo("Info", "Maaf, tidak ada rekomendasi sesuai preferensi Anda.")

def dapatkan_rekomendasi(berkuah, rasa, harga):
    makanan = {
        'berkuah': {
            'manis': {'bubur kacang hijau': 15000, 'bubur sumsum': 12000, 'kolak': 18000, 'wedang ronde': 16000},
            'asin': {'sop': 20000, 'soto': 18000, 'bakso': 15000, 'mie ayam': 17000},
            'pedas manis': {'topokki': 25000, 'gulai': 22000, 'tahu gejrot': 18000, 'kwetiaw goreng': 20000}
        },
        'tidak berkuah': {
            'manis': {'sate': 25000, 'ketoprak': 18000, 'roti bakar': 12000},
            'asin': {'kentang goreng': 15000, 'bakso goreng': 18000, 'cimol': 12000, 'cireng': 16000},
            'pedas manis': {'rendang': 28000, 'dendeng': 25000, 'cilok': 15000}
        }
    }

    if berkuah == "Berkuah":
        jenis_makanan = makanan['berkuah']
    else:
        jenis_makanan = makanan['tidak berkuah']

    if rasa == "Manis":
        kategori_rasa = 'manis'
    elif rasa == 'Asin':
        kategori_rasa = 'asin'
    else:
        kategori_rasa = 'pedas manis'

    filtered_recommendations = {}
    for makanan_item, harga_item in jenis_makanan[kategori_rasa].items():
        if "low" in harga:
            if harga_item <= 15000:
                filtered_recommendations[makanan_item] = harga_item
        elif "Medium" in harga:
            if harga_item <= 20000:
                filtered_recommendations[makanan_item] = harga_item
        elif "high" in harga:
            if harga_item <= 25000:
                filtered_recommendations[makanan_item] = harga_item

    return filtered_recommendations

def atur_rentang_harga(pilihan_terpilih):
    var_harga.set(pilihan_terpilih)
    tampilkan_rekomendasi()

root = tk.Tk()
root.title("Aplikasi Rekomendasi Makanan")

style = Style(theme='cosmo') 
root.configure(bg='#90E0EF')

frame_apk = ttk.Frame(root, padding=70, borderwidth=2, relief="solid", style='BW.TFrame')
frame_apk.pack(pady=50)


var_berkuah = tk.StringVar(root)
var_rasa = tk.StringVar(root)
var_harga = tk.StringVar(root)

label_berkuah = ttk.Label(frame_apk, text="Pilih jenis makanan:",  font=('Arial', 10, 'bold'))
label_berkuah.pack()

optionmenu_berkuah = ttk.Combobox(frame_apk, textvariable=var_berkuah, values=["Berkuah", "Tidak Berkuah"],)
optionmenu_berkuah.pack()

label_rasa = ttk.Label(frame_apk, text="Pilih rasa:" , font=('Arial', 10, 'bold'))
label_rasa.pack()

optionmenu_rasa = ttk.Combobox(frame_apk, textvariable=var_rasa, values=["Manis", "Asin", "Pedas Manis"])
optionmenu_rasa.pack()

label_harga = ttk.Label(frame_apk, text="Pilih harga (IDR):" , font=('Arial', 10, 'bold'))
label_harga.pack()

pilihan_rentang_harga = ["low (<= 15000)", "Medium (<= 20000)", "high (<= 25000)"]
optionmenu_harga = ttk.Combobox(frame_apk, textvariable=var_harga, values=pilihan_rentang_harga)
optionmenu_harga.pack(pady=(10, 10))

tombol_rekomendasi = ttk.Button(frame_apk, text="Dapatkan Rekomendasi", command=tampilkan_rekomendasi)
tombol_rekomendasi.pack(pady=(10, 10))

teks_rekomendasi = tk.Text(frame_apk, height=12, width=60)
teks_rekomendasi.pack()

root.mainloop()