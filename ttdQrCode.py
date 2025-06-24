import qrcode

# Data yang ingin dimasukkan ke QR Code
data = "https://kudav5.github.io/"

# Membuat instance QR Code
qr = qrcode.QRCode(
    version=1,  # Versi dari QR Code, semakin tinggi, semakin besar ukuran QR
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Tingkat koreksi kesalahan
    box_size=10,  # Ukuran kotak (piksel)
    border=4,  # Ukuran border (kotak kosong di sekitar QR)
)

# Menambahkan data ke QR Code
qr.add_data(data)
qr.make(fit=True)

# Membuat gambar QR Code
img = qr.make_image(fill="black", back_color="white")

# Menyimpan gambar QR Code
img.save("qrcode_example.png")
