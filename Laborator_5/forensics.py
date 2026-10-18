import re
import zipfile
from PIL import Image
from PIL.ExifTags import TAGS

# B1
def tip_real(cale):
    cap = open(cale, "rb").read(8)
    if cap.startswith(b"%PDF"):
        return "pdf"
    if cap.startswith(b"\x89PNG"):
        return "png"
    if cap.startswith(b"\xff\xd8"):
        return "jpeg"
    if cap.startswith(b"PK\x03\x04"):
        return "zip/docx"
    return cap.hex()

print(tip_real("probe/foto.jpg"))
print(tip_real("probe/ascuns.png"))

# B2
date = open("probe/ascuns.png", "rb").read()
for m in re.findall(rb"[ -~]{4,}", date):
    print(m.decode())

# B3
exif = Image.open("probe/foto.jpg")._getexif() or {}
for id, val in exif.items():
    print(TAGS.get(id, id), "=", val)

gps = exif.get(34853)
if gps:
    lat_dms = gps[2]
    lon_dms = gps[4]
    lat = float(lat_dms[0]) + float(lat_dms[1])/60 + float(lat_dms[2])/3600
    lon = float(lon_dms[0]) + float(lon_dms[1])/60 + float(lon_dms[2])/3600
    print("Latitudine:", round(lat, 6))
    print("Longitudine:", round(lon, 6))

# B4
i = date.find(b"PK\x03\x04")
if i != -1:
    open("gasit.zip", "wb").write(date[i:])
    print("arhiva extrasa de la octetul", i)
    z = zipfile.ZipFile("gasit.zip")
    for f in z.namelist():
        print(f, z.read(f).decode())
