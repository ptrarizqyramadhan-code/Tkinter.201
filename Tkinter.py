import tkinter as tk
from tkinter import ttk

MAPEL = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika",
]

def hasil_prediksi():
    """Apapun input yang diberikan, hasilnya selalu Teknologi Informasi."""
    label_hasil.config(text="Teknologi Informasi")
