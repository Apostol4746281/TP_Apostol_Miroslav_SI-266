import os, base64, hashlib, zipfile
from urllib.parse import quote
from PIL import Image

os.makedirs("probe", exist_ok=True)

clar = b"FLAG{straturi_decodate_cu_succes}"
s1 = quote(clar.decode())
s2 = s1.encode().hex()
s3 = base64.b64encode(s2.encode()).decode()
open("probe/mesaj.txt", "w").write(s3)

msg_xor = b"FLAG{xor_spart_prin_forta_bruta}"
open("probe/xor.bin", "wb").write(bytes(b ^ 42 for b in msg_xor))

cuvinte = ["123456", "admin", "student", "parola123", "securitate", "utm"]
open("probe/wordlist.txt", "w", encoding="latin1").write("\n".join(cuvinte) + "\n")
open("probe/hashuri.txt", "w").write(hashlib.md5(b"securitate").hexdigest() + "\n")

img = Image.new("RGB", (200, 200), color=(70, 130, 180))
ex = img.getexif()
ex[271] = "Canon"
ex[272] = "Canon EOS 2000D"
img.save("probe/foto.jpg", "JPEG", exif=ex.tobytes())

img_png = Image.new("RGB", (120, 120), color=(34, 139, 34))
img_png.save("probe/ascuns.png", "PNG")
with zipfile.ZipFile("probe/temp.zip", "w") as z:
    z.writestr("secret.txt", "FLAG{arhiva_extrasa_prin_carving}\n")
png_b = open("probe/ascuns.png", "rb").read()
zip_b = open("probe/temp.zip", "rb").read()
open("probe/ascuns.png", "wb").write(png_b + b"INDICIU:secret.txt" + zip_b)
os.remove("probe/temp.zip")
