# Raport Laborator 5
Apostol Miroslav, SI-266

## Lucrarea A
- Mesajul din probe/mesaj.txt a fost codat in base64 -> hex -> url si continea: FLAG{straturi_decodate_cu_succes}
- La xor.bin am gasit cheia 42 si mesajul: FLAG{xor_spart_prin_forta_bruta}
- Hash-ul din hashuri.txt are 32 caractere (md5) si parola gasita in wordlist este: securitate

## Lucrarea B
- Tipul real verificat cu magic bytes: foto.jpg este jpeg, iar ascuns.png este png.
- Cu strings pe ascuns.png am gasit la final textul INDICIU:secret.txt.
- In metadatele EXIF din foto.jpg am gasit modelul camerei Canon EOS 2000D si coordonatele GPS.
- Am extras arhiva zip de la coada fisierului ascuns.png si inauntru era secret.txt cu textul FLAG{arhiva_extrasa_prin_carving}.
- Cu stego.py am ascuns si extras prin LSB din stego.png mesajul: FLAG{ascuns_in_pixeli}
