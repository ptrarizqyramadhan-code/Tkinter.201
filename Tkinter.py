import tkinter as tk
from tkinter import ttk

MAPEL = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika",
]

def hasil_prediksi():
    """Apapun input yang diberikan, hasilnya selalu Teknologi Informasi."""
    label_hasil.config(text="Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.resizable(False, False)

lebar, tinggi = 520, 520
x = (root.winfo_screenwidth() - lebar) // 2
y = (root.winfo_screenheight() - tinggi) // 2
root.geometry(f"{lebar}x{tinggi}+{x}+{y}")

label_judul = tk.Label(
    root, text="Aplikasi Prediksi Prodi Pilihan",
    font=("Times New Roman", 18, "bold"), fg="#1f795a",
)
label_judul.pack(pady=(20, 10))

frame_input = ttk.LabelFrame(root, text="Masukkan Nilai Mata Pelajaran")
frame_input.pack(padx=20, pady=10, fill="x")

entries = []
for i, mapel in enumerate(MAPEL):
    baris = i % 5
    kolom = (i // 5) * 2
    tk.Label(frame_input, text=mapel, anchor="w", width=16).grid(
        row=baris, column=kolom, padx=(15, 5), pady=6, sticky="w")
    entry = tk.Entry(frame_input, width=8, justify="center")
    entry.grid(row=baris, column=kolom + 1, padx=(0, 15), pady=6)
    entries.append(entry)

frame_input.columnconfigure((0, 1, 2, 3), weight=1)

btn_prediksi = tk.Button(
    root, text="Hasil Prediksi", command=hasil_prediksi,
    font=("Arial", 12, "bold"), bg="#2e75b6", fg="white",
    activebackground="#1f4e79", activeforeground="white",
    width=20, pady=4,
)
btn_prediksi.pack(pady=15)

label_hasil = tk.Label(
    root, text="", font=("Arial", 16, "bold"), fg="#0600c0",
    relief="groove", width=30, height=2,
)
label_hasil.pack(pady=(0, 20))

root.mainloop()