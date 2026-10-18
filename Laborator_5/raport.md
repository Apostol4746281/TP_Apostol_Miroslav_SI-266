Raport - Laboratorul 5
Apostol Miroslav, SI-266

Lucrarea A:
- Mesajul codat in straturi: FLAG{straturi_decodate_cu_succes}
- Cheia XOR gasita: 42 (mesaj: FLAG{xor_spart_prin_forta_bruta})
- Parola din wordlist pentru hash MD5: securitate

Lucrarea B:
- Tipul real verificat prin magic bytes: jpeg si png
- Strings pe ascuns.png: gasit INDICIU:secret.txt la final
- EXIF si GPS: afisat Latitudine 47.061389, Longitudine 28.866944
- File carving: extras zip de la octetul 362 (continut: secret.txt cu FLAG{arhiva_extrasa_prin_carving})
- Steganografie LSB: mesaj extras cu succes -> FLAG{ascuns_in_pixeli}
