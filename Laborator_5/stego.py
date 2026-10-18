from PIL import Image

# B5
img = Image.open("probe/foto.jpg").convert("RGB")
px = list(img.getdata())
mesaj = b"FLAG{ascuns_in_pixeli}\x00"
biti = "".join(f"{x:08b}" for x in mesaj)

px_nou = []
i = 0
for (r, g, b) in px:
    if i < len(biti):
        r = (r & ~1) | int(biti[i])
        i += 1
    if i < len(biti):
        g = (g & ~1) | int(biti[i])
        i += 1
    if i < len(biti):
        b = (b & ~1) | int(biti[i])
        i += 1
    px_nou.append((r, g, b))

img.putdata(px_nou)
img.save("stego.png")

# B6
px = list(Image.open("stego.png").convert("RGB").getdata())
biti = ""
for (r, g, b) in px:
    biti += str(r & 1) + str(g & 1) + str(b & 1)

rez = ""
for j in range(0, len(biti), 8):
    octet = int(biti[j:j+8], 2)
    if octet == 0:
        break
    rez += chr(octet)

print("Mesaj:", rez)
