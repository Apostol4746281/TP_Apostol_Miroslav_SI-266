import re
import base64
from urllib.parse import unquote
import hashlib
import argparse, json

# A1
s = "Salut"
b = s.encode()
print(b, b[0])
print(b.hex(), bytes.fromhex(b.hex()))

# A2
def ghici_strat(s):
    s = s.strip()
    if re.search(r"%[0-9a-fA-F]{2}", s):
        return "url"
    if len(s) % 2 == 0 and re.fullmatch(r"[0-9a-fA-F]+", s):
        return "hex"
    if re.fullmatch(r"[A-Za-z0-9+/=]+", s):
        return "base64"
    return "necunoscut"

# A3
def desfa(s):
    s = s.strip()
    strat = ghici_strat(s)
    if strat == "base64":
        return strat, base64.b64decode(s)
    if strat == "hex":
        return strat, bytes.fromhex(s)
    if strat == "url":
        return strat, unquote(s).encode()
    return strat, s.encode()

# A4
def citibil(b):
    return all(32 <= c < 127 for c in b)

if __name__ == "__main__":
    print(ghici_strat("%2Fetc"))
    print(ghici_strat("48656c6c6f"))

    # A5
    date = open("probe/xor.bin", "rb").read()
    for k in range(256):
        clar = bytes(b ^ k for b in date)
        if citibil(clar):
            print("cheie:", k, clar.decode())

    # A6
    tinta = open("probe/hashuri.txt").readline().strip()
    print(len(tinta))
    for cuv in open("probe/wordlist.txt", encoding="latin1"):
        cuv = cuv.strip()
        if hashlib.md5(cuv.encode()).hexdigest() == tinta:
            print("gasit:", cuv)
            break

    # A7
    p = argparse.ArgumentParser()
    p.add_argument("intrare")
    p.add_argument("--fisier", action="store_true")
    a = p.parse_args()

    if a.fisier:
        val = open(a.intrare, "rb").read().decode().strip()
    else:
        val = a.intrare

    for _ in range(8):
        strat, b = desfa(val)
        val = b.decode()
        if citibil(b) and ghici_strat(val) == "necunoscut":
            print("final:", strat, val)
            break

    json.dump({"strat": strat, "rezultat": val}, open("arsenal/forensics/fisa.json", "w"))
