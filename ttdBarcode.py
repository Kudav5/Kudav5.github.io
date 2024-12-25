import pyautogui as agui
import barcode
from barcode.writer import ImageWriter
from PIL import Image

nm = ""
gambar = "https://drive.google.com/file/d/18yOMYU9N3JWOPEEuahK5KOl5eYg2mR9K/view?usp=drive_link"
# b = agui.confirm('pilih text atau gambar', buttons=["text", "gambar"])

ean = barcode.get('code128', gambar, writer=ImageWriter()) # param2 = ganti teks(nm) / gambar
nama = agui.prompt('Masukkan nama barcode: ')
ean.save(nama)
ean = Image.open(nama + ".png")
ean.show()

agui.alert('Gambar sudah disimpan sebagai ' + nama + '.png')