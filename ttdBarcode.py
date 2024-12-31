import pyautogui as agui
import barcode
from barcode.writer import ImageWriter
from PIL import Image

nm = ""
gambar = "https://kudav5.github.io/"

ean = barcode.get('code128', gambar, writer=ImageWriter()) # param2 = ganti teks(nm) / gambar
nama = agui.prompt('Masukkan nama barcode: ')
ean.save(nama)
ean = Image.open(nama + ".png")
ean.show()

agui.alert('Gambar sudah disimpan sebagai ' + nama + '.png')