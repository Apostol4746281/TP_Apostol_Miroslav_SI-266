# -*- coding: utf-8 -*-
"""
===============================================================================

   LUCRAREA DE LABORATOR NR. 3  -  INTRODUCERE IN PYTHON

   Universitatea Tehnica a Moldovei
   Facultatea Calculatoare, Informatica si Microelectronica
   Disciplina: Tehnici de programare        Anul I, grupele SI-265 / SI-266

===============================================================================

   CUM PORNESTI PROIECTUL
   ----------------------

   1. Ai nevoie de Python 3 instalat.  Verifica scriind in linia de comanda:

          python --version

      Daca scrie ceva de forma  Python 3.x.x , esti in regula.
      Daca nu, descarca-l gratuit de la  https://www.python.org/downloads/
      La instalare BIFEAZA casuta  "Add Python to PATH" .

   2. Deschide o linie de comanda in folderul unde se afla acest fisier.
      In Windows: intra in folder, scrie  cmd  in bara de adresa a
      ferestrei si apasa Enter.

   3. Porneste programul:

          python L3_TP_Nume_Prenume_SI-26x.py

      (scrie numele fisierului asa cum il vezi in folder)

   4. Iti apare un meniu. Incepe cu optiunea 5, "Cum se lucreaza".

   -----------------------------------------------------------------------

   CE AI DE FACUT

   Partea 1 - Bazele      13 sarcini      13 puncte
   Partea 2 - Jocul        7 misiuni       7 puncte
   Partea 3 - Bonus        6 sarcini       puncte in plus

   Punctaj maxim luat in calcul: 20.  Nota = punctaj / 2.

   Scrii codul in functiile pregatite mai jos, salvezi fisierul si rulezi
   din nou programul. Iti spune imediat ce e corect si ce nu.

   -----------------------------------------------------------------------

   CUM PREDAI

   Din meniu alegi optiunea 6. Programul iti pregateste automat fisierul
   cu denumirea corecta si iti spune ce sa scrii in email.

   Fisier:   L3_TP_Nume_Prenume_Grupa.py
   Exemplu:  L3_TP_Popescu_Ion_SI-266.py
   Adresa:   cristian.gonceari@isa.utm.md
   Subiect:  acelasi text ca numele fisierului, fara .py

===============================================================================
"""

# ============================================================================
#   DATELE TALE  -  completeaza-le inainte de orice altceva
# ============================================================================

NUME = "Apostol"        # numele de familie, de exemplu "Popescu"
PRENUME = "Miroslav"     # prenumele, de exemplu "Ion"
GRUPA = "SI-266"       # grupa exact asa: "SI-265" sau "SI-266"



# ============================================================================
#   PARTEA 1  -  BAZELE
#   13 sarcini, cate 1 punct fiecare
# ============================================================================

# --- Sarcina 1: Primul program: print sau return ----------------------------
# -*- coding: utf-8 -*-
"""
===============================================================================

   LUCRAREA DE LABORATOR NR. 3  -  INTRODUCERE IN PYTHON

   Universitatea Tehnica a Moldovei
   Facultatea Calculatoare, Informatica si Microelectronica
   Disciplina: Tehnici de programare        Anul I, grupele SI-265 / SI-266

===============================================================================

   CUM PORNESTI PROIECTUL
   ----------------------

   1. Ai nevoie de Python 3 instalat.  Verifica scriind in linia de comanda:

          python --version

      Daca scrie ceva de forma  Python 3.x.x , esti in regula.
      Daca nu, descarca-l gratuit de la  https://www.python.org/downloads/
      La instalare BIFEAZA casuta  "Add Python to PATH" .

   2. Deschide o linie de comanda in folderul unde se afla acest fisier.
      In Windows: intra in folder, scrie  cmd  in bara de adresa a
      ferestrei si apasa Enter.

   3. Porneste programul:

          python L3_TP_Nume_Prenume_SI-26x.py

      (scrie numele fisierului asa cum il vezi in folder)

   4. Iti apare un meniu. Incepe cu optiunea 5, "Cum se lucreaza".

   -----------------------------------------------------------------------

   CE AI DE FACUT

   Partea 1 - Bazele      13 sarcini      13 puncte
   Partea 2 - Jocul        7 misiuni       7 puncte
   Partea 3 - Bonus        6 sarcini       puncte in plus

   Punctaj maxim luat in calcul: 20.  Nota = punctaj / 2.

   Scrii codul in functiile pregatite mai jos, salvezi fisierul si rulezi
   din nou programul. Iti spune imediat ce e corect si ce nu.

   -----------------------------------------------------------------------

   CUM PREDAI

   Din meniu alegi optiunea 6. Programul iti pregateste automat fisierul
   cu denumirea corecta si iti spune ce sa scrii in email.

   Fisier:   L3_TP_Nume_Prenume_Grupa.py
   Exemplu:  L3_TP_Popescu_Ion_SI-266.py
   Adresa:   cristian.gonceari@isa.utm.md
   Subiect:  acelasi text ca numele fisierului, fara .py

===============================================================================
"""

# ============================================================================
#   DATELE TALE  -  completeaza-le inainte de orice altceva
# ============================================================================

NUME = "Apostol"        # numele de familie, de exemplu "Popescu"
PRENUME = "Miroslav"     # prenumele, de exemplu "Ion"
GRUPA = "SI-266"       # grupa exact asa: "SI-265" sau "SI-266"



# ============================================================================
#   PARTEA 1  -  BAZELE
#   13 sarcini, cate 1 punct fiecare
# ============================================================================

# --- Sarcina 1: Primul program: print sau return ----------------------------
def saluta():
    return "Hello, World!"

# --- Sarcina 2: Variabile și tipuri de date ---------------------------------
def celsius_in_fahrenheit(c):
    return c * 9/5 + 32

# --- Sarcina 3: Liste -------------------------------------------------------
def cele_mai_mari_trei(numere):
    return sorted(numere, reverse=True)[:3]

# --- Sarcina 4: Operatori de bază și tupluri --------------------------------
def cat_si_rest(a, b):
    return (a // b, a % b)

# --- Sarcina 5: Formatarea textului -----------------------------------------
def fisa_student(nume, grupa, media):
    return f"{nume} ({grupa}) - media {media:.2f}"

# --- Sarcina 6: Operații cu text --------------------------------------------
def initiale(nume_complet):
    cuvinte = nume_complet.strip().split()
    return "".join(f"{c[0].upper()}." for c in cuvinte)

# --- Sarcina 7: Instrucțiuni condiționale -----------------------------------
def calificativ(nota):
    if nota >= 9:
        return "excelent"
    elif nota >= 7:
        return "bine"
    elif nota >= 5:
        return "satisfacator"
    else:
        return "nepromovat"

# --- Sarcina 8: Cicluri -----------------------------------------------------
def fizzbuzz(n):
    rezultat = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            rezultat.append("FizzBuzz")
        elif i % 3 == 0:
            rezultat.append("Fizz")
        elif i % 5 == 0:
            rezultat.append("Buzz")
        else:
            rezultat.append(str(i))
    return rezultat

# --- Sarcina 9: Funcții proprii ---------------------------------------------
def pret_final(pret, reducere=0):
    return round(pret - (pret * reducere / 100), 2)

# --- Sarcina 10: Clase și obiecte --------------------------------------------
class Student:
    def __init__(self, nume, grupa):
        self.nume = nume
        self.grupa = grupa
        self.note = []

    def adauga_nota(self, nota):
        self.note.append(nota)

    def media(self):
        if not self.note:
            return 0
        return round(sum(self.note) / len(self.note), 2)

# --- Sarcina 11: Dicționare --------------------------------------------------
def frecventa_litere(text):
    rezultat = {}
    for c in text:
        if c.isalpha():
            lc = c.lower()
            rezultat[lc] = rezultat.get(lc, 0) + 1
    return rezultat

# --- Sarcina 12: Module și pachete -------------------------------------------
def zile_intre(data1, data2):
    d1 = datetime.datetime.strptime(data1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(data2, "%Y-%m-%d")
    return abs((d2 - d1).days)

# --- Sarcina 13: Lucrul cu fișiere -------------------------------------------
def salveaza_si_incarca(cale, note):
    with open(cale, "w", encoding="utf-8") as f:
        for n in note:
            f.write(str(n) + "\n")
    rezultat = []
    with open(cale, "r", encoding="utf-8") as f:
        for rand in f:
            if rand.strip():
                rezultat.append(float(rand.strip()))
    return rezultat



# ============================================================================
#   PARTEA 2  -  JOCUL
#   7 misiuni, cate 1 punct fiecare. Comenzi: player.move_forward(),
# ============================================================================

#   player.turn_left(), player.turn_right(), player.collect(),
#   player.push(), player.build("bridge"), player.can_move()

# --- Misiunea 1 ------------------------------------------------------------
def misiunea_1(player):
    for _ in range(4):
        player.move_forward()

# --- Misiunea 2 ------------------------------------------------------------
def misiunea_2(player):
    for _ in range(3):
        player.move_forward()
    player.turn_right()
    for _ in range(3):
        player.move_forward()

# --- Misiunea 3 ------------------------------------------------------------
def misiunea_3(player):
    while not player.at_exit():
        player.move_forward()

# --- Misiunea 4 ------------------------------------------------------------
def misiunea_4(player):
    for _ in range(7):
        if player.look() == "bustean":
            player.collect()
        player.move_forward()

# --- Misiunea 5 ------------------------------------------------------------
def misiunea_5(player):
    player.move_forward()
    player.move_forward()
    player.push()
    while not player.at_exit():
        player.move_forward()

# --- Misiunea 6 ------------------------------------------------------------
def misiunea_6(player):
    for _ in range(4):
        player.move_forward()
        player.collect()
    player.move_forward()
    player.build("bridge")
    while not player.at_exit():
        player.move_forward()

# --- Misiunea 7 ------------------------------------------------------------
def misiunea_7(player):
    player.move_forward()
    player.move_forward()
    player.push()
    player.move_forward()
    for _ in range(3):
        player.collect()
        player.move_forward()
    player.turn_right()
    player.move_forward()
    player.turn_right()
    for _ in range(3):
        player.move_forward()
    player.collect()
    player.turn_left()
    player.move_forward()
    player.turn_left()
    for _ in range(3):
        player.move_forward()
    player.build("bridge")
    player.move_forward()
    player.turn_left()
    player.move_forward()



# ============================================================================
#   PARTEA 3  -  BONUS
#   6 sarcini, cate 1 punct. Acopera sarcinile nerezolvate.
# ============================================================================

# --- Sarcina 1: Liste construite dintr-o singură expresie -------------------
def patrate_pare(n):
    return [x * x for x in range(1, n + 1) if x % 2 == 0]

# --- Sarcina 2: Funcții anonime cu lambda -----------------------------------
def sorteaza_dupa_nota(studenti):
    return sorted(studenti, key=lambda p: (-p[1], p[0]))

# --- Sarcina 3: Tratarea erorilor cu try și except --------------------------
def imparte_sigur(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return None

# --- Sarcina 4: Mulțimi (sets) ----------------------------------------------
def elemente_comune(a, b):
    return sorted(list(set(a) & set(b)))

# --- Sarcina 5: Map, filter, reduce -----------------------------------------
def total_peste_prag(preturi, prag):
    return round(float(sum(filter(lambda x: x > prag, preturi))), 2)

# --- Sarcina 6: Expresii regulate -------------------------------------------
def extrage_grupe(text):
    return re.findall(r"[A-Z]{2}-\d{3}", text)



# ############################################################################
#
#   NU MODIFICA NIMIC SUB ACEASTA LINIE
#
#   Aici se afla motorul care iti verifica raspunsurile si deseneaza jocul.
#   Daca stergi ceva din greseala, descarca din nou fisierul original.
#
# ############################################################################

import sys, os, time, io, re, math, shutil, datetime, traceback

if os.name == "nt":
    os.system("")
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RESET = "\033[0m"; ALDIN = "\033[1m"; GRI = "\033[90m"; ROSU = "\033[91m"
VERDE = "\033[92m"; GALBEN = "\033[93m"; ALBASTRU = "\033[94m"; CYAN = "\033[96m"

EMAIL_PROFESOR = "cristian.gonceari@isa.utm.md"
COD_LAB = "L3"
LATIME = 74


def _c(t, culoare):
    return culoare + str(t) + RESET


def _sterge_ecran():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        print("\n" * 40)


def _linie(ch="-"):
    print(_c(ch * LATIME, GRI))


def _titlu(text, culoare=CYAN):
    print()
    print(_c("=" * LATIME, culoare))
    print(_c("  " + text, culoare + ALDIN))
    print(_c("=" * LATIME, culoare))
    print()


def _pauza():
    try:
        input(_c("\n  [Enter] pentru a continua...", GRI))
    except (EOFError, KeyboardInterrupt):
        print()


def _fara_diacritice(s):
    tabel = str.maketrans("ăâîșşțţĂÂÎȘŞȚŢ", "aaissttAAISSTT")
    return s.translate(tabel)


def _egale(a, b):
    if isinstance(a, float) or isinstance(b, float):
        try:
            return abs(float(a) - float(b)) < 1e-9
        except (TypeError, ValueError):
            return False
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        if type(a) != type(b) or len(a) != len(b):
            return False
        return all(_egale(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        return all(_egale(a[k], b[k]) for k in a)
    return a == b


def _scurt(v, maxim=60):
    t = repr(v)
    return t if len(t) <= maxim else t[:maxim - 3] + "..."


# ---------------------------------------------------------------------------
#  Verificarea unei sarcini
# ---------------------------------------------------------------------------
def verifica_sarcina(s, detaliat=False):
    """Returneaza (reusit, mesaj)."""
    if "verificator" in s:
        try:
            return s["verificator"]()
        except NotImplementedError:
            return False, "Sarcina nu este inca rezolvata."
        except Exception as e:
            return False, "Eroare: " + type(e).__name__ + ": " + str(e)

    f = globals().get(s["functie"])
    if f is None:
        return False, "Functia " + s["functie"] + " nu exista in fisier."
    for args, asteptat in s["teste"]:
        try:
            obtinut = f(*args)
        except NotImplementedError:
            return False, "Sarcina nu este inca rezolvata."
        except Exception as e:
            return False, ("Codul tau a dat eroare la " + s["functie"] +
                           "(" + ", ".join(_scurt(a) for a in args) + ")\n" +
                           "         " + type(e).__name__ + ": " + str(e))
        if not _egale(obtinut, asteptat):
            return False, ("Pentru " + s["functie"] + "(" +
                           ", ".join(_scurt(a) for a in args) + ")\n" +
                           "         asteptam: " + _scurt(asteptat) + "\n" +
                           "         am primit: " + _scurt(obtinut))
    return True, "Corect."


def verifica_misiune(niv, animatie=False):
    f = globals().get("misiunea_" + str(niv["nr"]))
    if f is None:
        return False, "Functia misiunea_" + str(niv["nr"]) + " nu exista."
    try:
        gol = f.__code__.co_code == (lambda p: None).__code__.co_code
    except Exception:
        gol = False
    if gol:
        return False, "Misiunea nu este inca rezolvata."
    return ruleaza_misiune(niv, f, animatie)


def stare_completa():
    """Returneaza lista de (categorie, nr, titlu, reusit)."""
    out = []
    for s in SARCINI_BAZE:
        ok, _ = verifica_sarcina(s)
        out.append(("baze", s["nr"], s["titlu"], ok))
    for niv in NIVELURI:
        ok, _ = verifica_misiune(niv, animatie=False)
        out.append(("joc", niv["nr"], niv["titlu"], ok))
    for s in SARCINI_BONUS:
        ok, _ = verifica_sarcina(s)
        out.append(("bonus", s["nr"], s["titlu"], ok))
    return out


def punctaj(stare):
    ob = sum(1 for c, _, _, ok in stare if c in ("baze", "joc") and ok)
    bo = sum(1 for c, _, _, ok in stare if c == "bonus" and ok)
    total = min(ob + bo, 20)
    nota = max(1, min(10, round(total / 2)))
    return ob, bo, total, nota


# ---------------------------------------------------------------------------
#  Afisare
# ---------------------------------------------------------------------------
def bara(cate, din, latime=30):
    plin = int(latime * cate / din) if din else 0
    return ("[" + _c("#" * plin, VERDE) + _c("." * (latime - plin), GRI) +
            "] " + str(cate) + "/" + str(din))


def arata_progres(stare=None):
    stare = stare or stare_completa()
    _titlu("PROGRESUL TAU")
    for eticheta, cat, total in (("PARTEA 1 - Bazele", "baze", 13),
                                 ("PARTEA 2 - Jocul", "joc", 7),
                                 ("PARTEA 3 - Bonus", "bonus", len(SARCINI_BONUS))):
        randuri = [(n, t, ok) for c, n, t, ok in stare if c == cat]
        cate = sum(1 for _, _, ok in randuri if ok)
        print(_c("  " + eticheta, ALDIN) + "   " + bara(cate, total))
        for n, t, ok in randuri:
            semn = _c("[v]", VERDE) if ok else _c("[ ]", GRI)
            nume = t if ok else _c(t, GRI)
            print("     " + semn + " " + str(n).rjust(2) + ". " + nume)
        print()
    ob, bo, total, nota = punctaj(stare)
    _linie()
    print("  Puncte obligatorii: " + _c(str(ob) + " / 20", ALDIN) +
          "      Bonus: " + _c("+" + str(bo), VERDE if bo else GRI))
    print("  Punctaj total: " + _c(str(total) + " / 20", ALDIN) +
          "      Nota: " + _c(str(nota), (VERDE if nota >= 5 else ROSU) + ALDIN))
    _linie()


def arata_teorie(s):
    _sterge_ecran()
    _titlu(str(s["nr"]) + ". " + s["titlu"])
    for rand in s["teorie"].split("\n"):
        print("  " + rand)
    if s.get("exemplu"):
        print()
        print(_c("  EXEMPLU", GALBEN + ALDIN))
        _linie()
        for rand in s["exemplu"].split("\n"):
            print("  " + _c(rand, CYAN))
        _linie()
    print()
    print(_c("  SARCINA TA", VERDE + ALDIN))
    for rand in s["sarcina"].split("\n"):
        print("  " + rand)
    print()
    print(_c("  Scrie codul in functia  " + s["functie"] +
             "  din partea de sus a fisierului.", GRI))


def arata_indicii(s):
    _titlu("INDICII pentru " + s["titlu"], GALBEN)
    for i, ind in enumerate(s.get("indicii", []), 1):
        print(_c("  Indiciul " + str(i) + ":", GALBEN + ALDIN))
        for rand in ind.split("\n"):
            print("    " + rand)
        print()
        if i < len(s.get("indicii", [])):
            try:
                r = input(_c("    Vrei si urmatorul indiciu? (d/n) ", GRI)).strip().lower()
            except (EOFError, KeyboardInterrupt):
                return
            if r not in ("d", "da", "y", ""):
                return
    if s.get("greseala"):
        print(_c("  GRESEALA FRECVENTA", ROSU + ALDIN))
        for rand in s["greseala"].split("\n"):
            print("    " + rand)


def lucreaza_sarcina(s):
    while True:
        arata_teorie(s)
        ok, msg = verifica_sarcina(s)
        print()
        if ok:
            print(_c("  [v] REZOLVAT - " + msg, VERDE + ALDIN))
        else:
            print(_c("  [ ] Inca nu e gata.", ROSU + ALDIN))
            for rand in msg.split("\n"):
                print(_c("      " + rand, ROSU))
        print()
        print(_c("  [Enter] reverifica    [i] indicii    [q] inapoi la meniu", GRI))
        try:
            r = input("  > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if r == "q":
            return
        if r == "i":
            arata_indicii(s)
            _pauza()


def lucreaza_misiune(niv):
    while True:
        _sterge_ecran()
        _titlu("MISIUNEA " + str(niv["nr"]) + " - " + niv["titlu"])
        for rand in niv["obiectiv"].split("\n"):
            print("  " + rand)
        print()
        print(_c("  Harta:", GALBEN + ALDIN))
        for rand in niv["harta"]:
            print("     " + _c(rand, GRI))
        print()
        print(_c("  @ = tu    * = iesirea    o = bustean    R = stanca", GRI))
        print(_c("  ~ = apa   X = loc de pod    # = perete", GRI))
        print()
        print(_c("  Scrie codul in functia  misiunea_" + str(niv["nr"]) +
                 "(player)  din fisier.", GRI))
        print()
        print(_c("  [Enter] ruleaza    [q] inapoi la meniu", GRI))
        try:
            r = input("  > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if r == "q":
            return
        ok, msg = verifica_misiune(niv, animatie=True)
        print()
        if ok:
            print(_c("  [v] MISIUNE INDEPLINITA - " + msg, VERDE + ALDIN))
        else:
            print(_c("  [x] " + msg, ROSU + ALDIN))
        _pauza()


# ---------------------------------------------------------------------------
#  Pregatirea fisierului pentru trimitere
# ---------------------------------------------------------------------------
def nume_fisier_corect():
    n = _fara_diacritice(NUME.strip()).replace(" ", "_")
    p = _fara_diacritice(PRENUME.strip()).replace(" ", "_")
    g = GRUPA.strip().upper().replace(" ", "")
    if not (n and p and g):
        return None
    return COD_LAB + "_TP_" + n.capitalize() + "_" + p.capitalize() + "_" + g + ".py"


def date_completate():
    return bool(NUME.strip() and PRENUME.strip() and GRUPA.strip())


def pregateste_trimiterea():
    _sterge_ecran()
    _titlu("PREGATIREA FISIERULUI PENTRU TRIMITERE")
    if not date_completate():
        print(_c("  Nu ai completat datele tale.", ROSU + ALDIN))
        print()
        print("  Deschide fisierul si completeaza, sus de tot:")
        print(_c('      NUME = "Popescu"', CYAN))
        print(_c('      PRENUME = "Ion"', CYAN))
        print(_c('      GRUPA = "SI-266"', CYAN))
        return
    stare = stare_completa()
    ob, bo, total, nota = punctaj(stare)
    nume = nume_fisier_corect()
    sursa = os.path.abspath(__file__)
    tinta = os.path.join(os.path.dirname(sursa), nume)
    try:
        if os.path.abspath(tinta) != sursa:
            shutil.copyfile(sursa, tinta)
        creat = True
    except Exception as e:
        creat = False
        print(_c("  Nu am putut crea copia: " + str(e), ROSU))
    arata_progres(stare)
    print()
    if creat:
        print(_c("  Am pregatit fisierul:", VERDE + ALDIN))
        print(_c("     " + nume, VERDE + ALDIN))
        print(_c("  Il gasesti in acelasi folder cu acest fisier.", GRI))
    print()
    print(_c("  TRIMITE-L ASA:", GALBEN + ALDIN))
    print("     Adresa:  " + _c(EMAIL_PROFESOR, ALDIN))
    print("     Subiect: " + _c(nume[:-3], ALDIN))
    print("     Atasat:  " + _c(nume, ALDIN))
    print()
    print(_c("  Subiectul este exact numele fisierului, fara .py", GRI))


# ---------------------------------------------------------------------------
#  Meniuri
# ---------------------------------------------------------------------------
def meniu_lista(titlu, elemente, cat, stare):
    while True:
        _sterge_ecran()
        _titlu(titlu)
        for el in elemente:
            nr = el["nr"]
            ok = next((o for c, n, _, o in stare if c == cat and n == nr), False)
            semn = _c("[v]", VERDE) if ok else _c("[ ]", GRI)
            print("   " + semn + "  " + str(nr).rjust(2) + ". " + el["titlu"])
        print()
        print(_c("   Scrie numarul sarcinii, sau [q] pentru meniul principal.", GRI))
        try:
            r = input("   > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if r == "q":
            return
        if not r.isdigit():
            continue
        el = next((e for e in elemente if e["nr"] == int(r)), None)
        if el is None:
            continue
        if cat == "joc":
            lucreaza_misiune(el)
        else:
            lucreaza_sarcina(el)
        stare = stare_completa()


def banner():
    print()
    print(_c("   ____        _   _                   _        _     ____  ", VERDE))
    print(_c("  |  _ \\ _   _| |_| |__   ___  _ __   | |    __ _| |__ |___ \\ ", VERDE))
    print(_c("  | |_) | | | | __| '_ \\ / _ \\| '_ \\  | |   / _` | '_ \\  __) |", VERDE))
    print(_c("  |  __/| |_| | |_| | | | (_) | | | | | |__| (_| | |_) |/ __/ ", VERDE))
    print(_c("  |_|    \\__, |\\__|_| |_|\\___/|_| |_| |_____\\__,_|_.__/|_____|", VERDE))
    print(_c("         |___/                                               ", VERDE))
    print(_c("        Tehnici de programare  -  Lucrarea de laborator 3", GRI))
    print()


def main():
    while True:
        stare = stare_completa()
        ob, bo, total, nota = punctaj(stare)
        _sterge_ecran()
        banner()
        if date_completate():
            print("   Student: " + _c(NUME + " " + PRENUME + "  (" + GRUPA + ")", ALDIN))
        else:
            print(_c("   ! Nu ti-ai completat NUME, PRENUME si GRUPA sus in fisier.", ROSU))
        print("   Progres: " + bara(total, 20) + "     Nota acum: " +
              _c(str(nota), (VERDE if nota >= 5 else ROSU) + ALDIN))
        print()
        _linie()
        print("   1. Partea 1 - Bazele          (13 sarcini, 13 puncte)")
        print("   2. Partea 2 - Jocul           (7 misiuni, 7 puncte)")
        print("   3. Partea 3 - Bonus           (" + str(len(SARCINI_BONUS)) +
              " sarcini, puncte in plus)")
        print("   4. Vezi progresul detaliat")
        print("   5. Cum se lucreaza (instructiuni)")
        print("   6. Pregateste fisierul pentru trimitere")
        print("   0. Iesire")
        _linie()
        try:
            r = input("   Alege > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if r == "1":
            meniu_lista("PARTEA 1 - BAZELE", SARCINI_BAZE, "baze", stare)
        elif r == "2":
            meniu_lista("PARTEA 2 - JOCUL", NIVELURI, "joc", stare)
        elif r == "3":
            meniu_lista("PARTEA 3 - BONUS", SARCINI_BONUS, "bonus", stare)
        elif r == "4":
            arata_progres(stare); _pauza()
        elif r == "5":
            instructiuni(); _pauza()
        elif r == "6":
            pregateste_trimiterea(); _pauza()
        elif r == "0":
            print(_c("\n   Spor la treaba!\n", VERDE))
            return


def instructiuni():
    _sterge_ecran()
    _titlu("CUM SE LUCREAZA")
    for rand in INSTRUCTIUNI.split("\n"):
        print("  " + rand)



def _verif_student():
    S = globals().get("Student")
    if S is None:
        return False, "Clasa Student nu este definita."
    try:
        s = S("Popescu Ion", "SI-266")
    except NotImplementedError:
        return False, "Sarcina nu este inca rezolvata."
    except Exception as e:
        return False, "Student(\"Popescu Ion\", \"SI-266\") a dat eroare: " + str(e)
    if getattr(s, "nume", None) != "Popescu Ion":
        return False, "Obiectul trebuie sa retina numele in atributul self.nume"
    if getattr(s, "grupa", None) != "SI-266":
        return False, "Obiectul trebuie sa retina grupa in atributul self.grupa"
    try:
        m = s.media()
    except Exception as e:
        return False, "media() a dat eroare: " + str(e)
    if not _egale(m, 0):
        return False, ("Un student fara note trebuie sa aiba media 0.\n"
                       "         am primit: " + _scurt(m))
    try:
        s.adauga_nota(8)
        s.adauga_nota(9)
    except Exception as e:
        return False, "adauga_nota() a dat eroare: " + str(e)
    if not _egale(s.media(), 8.5):
        return False, ("Dupa notele 8 si 9, media trebuie sa fie 8.5\n"
                       "         am primit: " + _scurt(s.media()))
    s.adauga_nota(10)
    if not _egale(s.media(), 9.0):
        return False, ("Dupa notele 8, 9 si 10, media trebuie sa fie 9.0\n"
                       "         am primit: " + _scurt(s.media()))
    s2 = S("Ana Pop", "SI-265")
    if not _egale(s2.media(), 0):
        return False, "Fiecare student trebuie sa aiba propria lista de note."
    return True, "Corect."


def _verif_fisier():
    import tempfile
    f = globals().get("salveaza_si_incarca")
    if f is None:
        return False, "Functia salveaza_si_incarca nu exista."
    cale = os.path.join(tempfile.gettempdir(), "lab3_test_note.txt")
    if os.path.exists(cale):
        try:
            os.remove(cale)
        except Exception:
            pass
    try:
        rez = f(cale, [8, 9.5, 10])
    except NotImplementedError:
        return False, "Sarcina nu este inca rezolvata."
    except Exception as e:
        return False, "Codul tau a dat eroare: " + type(e).__name__ + ": " + str(e)
    if not _egale(rez, [8.0, 9.5, 10.0]):
        return False, ("Pentru salveaza_si_incarca(cale, [8, 9.5, 10])\n"
                       "         asteptam: [8.0, 9.5, 10.0]\n"
                       "         am primit: " + _scurt(rez))
    if not os.path.exists(cale):
        return False, "Fisierul nu a fost creat. Trebuie sa scrii efectiv pe disc."
    try:
        with open(cale, "r", encoding="utf-8") as fh:
            randuri = [r.strip() for r in fh if r.strip()]
    except Exception as e:
        return False, "Nu am putut citi fisierul creat: " + str(e)
    if len(randuri) != 3:
        return False, ("Fisierul trebuie sa aiba cate o nota pe fiecare rand.\n"
                       "         am gasit " + str(len(randuri)) + " randuri.")
    rez2 = f(cale, [])
    if not _egale(rez2, []):
        return False, "Pentru o lista goala trebuie sa returnezi []."
    return True, "Corect."

# ---------------------------------------------------------------------------
#  Jocul pe grila
# ---------------------------------------------------------------------------
class EroareJoc(Exception):
    pass


class Jucator:
    """Personajul pe care il comanzi din cod.

    Metode disponibile:
        player.move_forward()   - un pas inainte
        player.turn_left()      - rotire la stanga
        player.turn_right()     - rotire la dreapta
        player.collect()        - ridica busteanul de sub picioare
        player.push()           - impinge stanca din fata
        player.build("bridge")  - construieste un pod (ai nevoie de 4 busteni)
        player.can_move()       - True daca poti face un pas inainte
        player.at_exit()        - True daca esti pe stea
        player.look()           - ce se afla in fata ta, ca text
    """

    DIRECTII = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # N, E, S, V
    SEMNE = ["^", ">", "v", "<"]
    NUME_DIR = ["nord", "est", "sud", "vest"]

    def __init__(self, harta, max_pasi=250, animatie=True):
        self.grila = [list(r) for r in harta]
        self.animatie = animatie
        self.max_pasi = max_pasi
        self.pasi = 0
        self.busteni = 0
        self.jurnal = []
        self.dir = 1
        self.lin = self.col = 0
        for i, rand in enumerate(self.grila):
            for j, c in enumerate(rand):
                if c == "@":
                    self.lin, self.col = i, j
                    self.grila[i][j] = "."
        self._deseneaza("start")

    # -- intern ------------------------------------------------------------
    def _consuma(self, ce):
        self.pasi += 1
        if self.pasi > self.max_pasi:
            raise EroareJoc(
                "Ai depasit " + str(self.max_pasi) + " de actiuni. "
                "Probabil ai un ciclu care nu se opreste niciodata."
            )
        self.jurnal.append(ce)

    def _in_fata(self):
        dl, dc = self.DIRECTII[self.dir]
        return self.lin + dl, self.col + dc

    def _celula(self, l, c):
        if 0 <= l < len(self.grila) and 0 <= c < len(self.grila[l]):
            return self.grila[l][c]
        return "#"

    def _deseneaza(self, actiune=""):
        if not self.animatie:
            return
        _sterge_ecran()
        print(_c("  " + actiune, GRI))
        print()
        for i, rand in enumerate(self.grila):
            out = "   "
            for j, c in enumerate(rand):
                if (i, j) == (self.lin, self.col):
                    out += _c(self.SEMNE[self.dir], VERDE + ALDIN)
                elif c == "#":
                    out += _c("#", GRI)
                elif c == "*":
                    out += _c("*", GALBEN + ALDIN)
                elif c == "o":
                    out += _c("o", GALBEN)
                elif c == "R":
                    out += _c("R", ROSU)
                elif c == "~":
                    out += _c("~", ALBASTRU)
                elif c == "X":
                    out += _c("X", ALBASTRU)
                elif c == "=":
                    out += _c("=", GALBEN)
                else:
                    out += _c(".", GRI)
            print(out)
        print()
        print(_c("   busteni: " + str(self.busteni) +
                 "    actiuni: " + str(self.pasi) +
                 "    privesti spre: " + self.NUME_DIR[self.dir], GRI))
        time.sleep(0.11)

    # -- API pentru student -------------------------------------------------
    def move_forward(self):
        self._consuma("move_forward")
        l, c = self._in_fata()
        tinta = self._celula(l, c)
        if tinta in ("#", "R"):
            self._deseneaza("te-ai lovit de un obstacol")
            raise EroareJoc("Nu poti merge inainte: in fata ta este un obstacol.")
        if tinta == "~":
            self._deseneaza("ai cazut in apa")
            raise EroareJoc("Ai cazut in apa. Ai nevoie de un pod ca sa treci.")
        if tinta == "X":
            self._deseneaza("ai cazut in apa")
            raise EroareJoc("Aici lipseste podul. Construieste-l cu build.")
        self.lin, self.col = l, c
        self._deseneaza("move_forward()")

    def turn_left(self):
        self._consuma("turn_left")
        self.dir = (self.dir - 1) % 4
        self._deseneaza("turn_left()")

    def turn_right(self):
        self._consuma("turn_right")
        self.dir = (self.dir + 1) % 4
        self._deseneaza("turn_right()")

    def collect(self):
        self._consuma("collect")
        if self.grila[self.lin][self.col] != "o":
            self._deseneaza("nu e nimic de colectat aici")
            raise EroareJoc("Nu exista niciun bustean pe casuta pe care stai.")
        self.grila[self.lin][self.col] = "."
        self.busteni += 1
        self._deseneaza("collect()")

    def push(self):
        self._consuma("push")
        l, c = self._in_fata()
        if self._celula(l, c) != "R":
            self._deseneaza("nu e nicio stanca in fata")
            raise EroareJoc("Nu ai ce impinge: in fata ta nu se afla o stanca.")
        dl, dc = self.DIRECTII[self.dir]
        l2, c2 = l + dl, c + dc
        if self._celula(l2, c2) not in (".", "~"):
            self._deseneaza("stanca nu se poate misca")
            raise EroareJoc("Stanca nu are unde sa fie impinsa.")
        self.grila[l][c] = "."
        self.grila[l2][c2] = "." if self._celula(l2, c2) == "~" else "R"
        self._deseneaza("push()")

    def build(self, ce=""):
        self._consuma("build")
        if str(ce).strip().lower() not in ("bridge", "pod"):
            raise EroareJoc('Scrie exact player.build("bridge") ca sa construiesti podul.')
        if self.busteni < 4:
            self._deseneaza("nu ai destui busteni")
            raise EroareJoc("Ai nevoie de 4 busteni ca sa construiesti un pod. "
                            "Ai doar " + str(self.busteni) + ".")
        l, c = self._in_fata()
        if self._celula(l, c) != "X":
            self._deseneaza("nu se poate construi aici")
            raise EroareJoc("Poti construi un pod doar in fata unui semn X.")
        self.grila[l][c] = "="
        self.busteni -= 4
        self._deseneaza("build(\"bridge\")")

    def can_move(self):
        l, c = self._in_fata()
        return self._celula(l, c) in (".", "*", "o", "=")

    def at_exit(self):
        return self.grila[self.lin][self.col] == "*"

    def look(self):
        l, c = self._in_fata()
        return {"#": "perete", ".": "liber", "*": "iesirea", "o": "bustean",
                "R": "stanca", "~": "apa", "X": "loc de pod",
                "=": "pod"}.get(self._celula(l, c), "necunoscut")


def ruleaza_misiune(nivel, functie, animatie=True):
    """Ruleaza codul studentului pe harta nivelului.
    Returneaza (reusit, mesaj)."""
    p = Jucator(nivel["harta"], nivel.get("max_pasi", 250), animatie)
    try:
        functie(p)
    except EroareJoc as e:
        return False, str(e)
    except RecursionError:
        return False, "Prea multe apeluri imbricate."
    except Exception as e:
        return False, "Codul tau a dat eroare: " + type(e).__name__ + ": " + e
    if not p.at_exit():
        return False, "Nu ai ajuns la stea. Te-ai oprit pe alta casuta."
    if p.busteni < nivel.get("busteni_min", 0):
        return False, ("Ai ajuns la iesire, dar ai colectat doar " +
                       str(p.busteni) + " busteni din " +
                       str(nivel["busteni_min"]) + " ceruti.")
    return True, "Misiune indeplinita in " + str(p.pasi) + " actiuni."


NIVELURI = [
    {
        "nr": 1,
        "titlu": "Primii pasi",
        "obiectiv": ("Mergi inainte pana ajungi pe stea.\n"
                     "Ai la dispozitie o singura comanda: player.move_forward()\n"
                     "Numara cate casute sunt pana la stea si apeleaza comanda\n"
                     "de exact atatea ori, una sub alta."),
        "harta": ["#######",
                  "#@....*",
                  "#######"],
        "invata": "apelarea unei functii, o comanda pe fiecare rand",
    },
    {
        "nr": 2,
        "titlu": "Prima cotitura",
        "obiectiv": ("Drumul face un colt. Pe langa move_forward ai acum\n"
                     "player.turn_right() si player.turn_left().\n"
                     "Rotirea nu te muta din loc, doar schimba directia in care privesti."),
        "harta": ["######",
                  "#@...#",
                  "####.#",
                  "####.#",
                  "####*#",
                  "######"],
        "invata": "ordinea instructiunilor conteaza",
    },
    {
        "nr": 3,
        "titlu": "Coridorul lung",
        "obiectiv": ("Pana la stea sunt multi pasi. Poti scrie move_forward de\n"
                     "zeci de ori... sau poti folosi un ciclu:\n"
                     "    for pas in range(10):\n"
                     "        player.move_forward()\n"
                     "Numara exact cate casute sunt si pune numarul in range."),
        "harta": ["##################",
                  "#@..............*#",
                  "##################"],
        "invata": "ciclul for si range",
    },
    {
        "nr": 4,
        "titlu": "Culegatorul",
        "obiectiv": ("Pe drum sunt busteni, marcati cu o. Cand ajungi pe o casuta\n"
                     "cu bustean, apeleaza player.collect() ca sa il ridici.\n"
                     "Trebuie sa aduni toti cei 3 busteni SI sa ajungi pe stea."),
        "harta": ["##########",
                  "#@.o.o.o*#",
                  "##########"],
        "busteni_min": 3,
        "invata": "combinarea mai multor comenzi intr-un ciclu",
    },
    {
        "nr": 5,
        "titlu": "Stanca din drum",
        "obiectiv": ("O stanca, marcata cu R, iti blocheaza drumul.\n"
                     "Apropie-te de ea si foloseste player.push() ca sa o impingi\n"
                     "in directia in care privesti. Apoi treci mai departe."),
        "harta": ["###########",
                  "#@..R....*#",
                  "###########"],
        "invata": "interactiunea cu obiectele",
    },
    {
        "nr": 6,
        "titlu": "Podul peste apa",
        "obiectiv": ("Apa, marcata cu ~, nu se poate traversa. In dreptul semnului X\n"
                     "poti construi un pod, dar ai nevoie de 4 busteni.\n"
                     "Aduna intai cei 4 busteni, apoi opreste-te chiar in fata lui X\n"
                     'si scrie player.build("bridge"). Apoi treci pe pod.'),
        "harta": ["#############",
                  "#@.oooo.X..*#",
                  "#############"],
        "busteni_min": 0,
        "invata": "conditii si resurse",
    },
    {
        "nr": 7,
        "titlu": "Toate la un loc",
        "obiectiv": ("Ultima misiune aduna tot ce ai invatat: coturi, busteni,\n"
                     "o stanca si un pod. Ia-o pas cu pas si deseneaza-ti traseul\n"
                     "pe hartie inainte sa scrii codul.\n"
                     "Trebuie sa ajungi pe stea cu cel putin 1 bustean ramas."),
        "harta": ["############",
                  "#@..R..ooo.#",
                  "##########.#",
                  "#*...X...o.#",
                  "############"],
        "busteni_min": 1,
        "invata": "descompunerea unei probleme mari in pasi mici",
    },
]


SARCINI_BAZE = [
    {
        'nr': 1,
        'functie': 'saluta',
        'titlu': 'Primul program: print sau return',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((), 'Hello, World!')],
    },
    {
        'nr': 2,
        'functie': 'celsius_in_fahrenheit',
        'titlu': 'Variabile și tipuri de date',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((0,), 32.0), ((100,), 212.0), ((-40,), -40.0), ((37,), 98.6)],
    },
    {
        'nr': 3,
        'functie': 'cele_mai_mari_trei',
        'titlu': 'Liste',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(([5, 1, 9, 3, 7],), [9, 7, 5]), (([2, 1],), [2, 1]), (([4, 4, 4, 4],), [4, 4, 4]), (([],), []), (([-5, -1, -9],), [-1, -5, -9])],
    },
    {
        'nr': 4,
        'functie': 'cat_si_rest',
        'titlu': 'Operatori de bază și tupluri',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((17, 5), (3, 2)), ((10, 2), (5, 0)), ((7, 3), (2, 1)), ((0, 4), (0, 0))],
    },
    {
        'nr': 5,
        'functie': 'fisa_student',
        'titlu': 'Formatarea textului',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(('Popescu Ion', 'SI-266', 8.5), 'Popescu Ion (SI-266) - media 8.50'), (('Ana Pop', 'SI-265', 10), 'Ana Pop (SI-265) - media 10.00'), (('Ion Rusu', 'SI-266', 7.333), 'Ion Rusu (SI-266) - media 7.33')],
    },
    {
        'nr': 6,
        'functie': 'initiale',
        'titlu': 'Operații cu text',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(('popescu ion',), 'P.I.'), (('  Ana Maria Pop ',), 'A.M.P.'), (('Ion',), 'I.'), (('vasile alecsandri',), 'V.A.')],
    },
    {
        'nr': 7,
        'functie': 'calificativ',
        'titlu': 'Instrucțiuni condiționale',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((10,), 'excelent'), ((9,), 'excelent'), ((8,), 'bine'), ((7,), 'bine'), ((6,), 'satisfacator'), ((5,), 'satisfacator'), ((4,), 'nepromovat'), ((1,), 'nepromovat')],
    },
    {
        'nr': 8,
        'functie': 'fizzbuzz',
        'titlu': 'Cicluri',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((5,), ['1', '2', 'Fizz', '4', 'Buzz']), ((3,), ['1', '2', 'Fizz']), ((15,), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']), ((1,), ['1'])],
    },
    {
        'nr': 9,
        'functie': 'pret_final',
        'titlu': 'Funcții proprii',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((200, 25), 150.0), ((100,), 100.0), ((99.99, 10), 89.99), ((50, 100), 0.0)],
    },
    {
        'nr': 10,
        'functie': 'Student',
        'titlu': 'Clase și obiecte',
        'teorie': '...',
        'sarcina': '...',
        'verificator': _verif_student,
    },
    {
        'nr': 11,
        'functie': 'frecventa_litere',
        'titlu': 'Dicționare',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(('Ana are',), {'a': 3, 'n': 1, 'r': 1, 'e': 1}), (('',), {}), (('A1 b!',), {'a': 1, 'b': 1}), (('aaa',), {'a': 3})],
    },
    {
        'nr': 12,
        'functie': 'zile_intre',
        'titlu': 'Module și pachete',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(('2026-09-22', '2026-09-25'), 3), (('2026-09-25', '2026-09-22'), 3), (('2026-01-01', '2026-12-31'), 364), (('2026-03-01', '2026-03-01'), 0)],
    },
    {
        'nr': 13,
        'functie': 'salveaza_si_incarca',
        'titlu': 'Lucrul cu fișiere',
        'teorie': '...',
        'sarcina': '...',
        'verificator': _verif_fisier,
    },
]

SARCINI_BONUS = [
    {
        'nr': 1,
        'functie': 'patrate_pare',
        'titlu': 'Liste construite dintr-o singură expresie',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((6,), [4, 16, 36]), ((1,), []), ((10,), [4, 16, 36, 64, 100]), ((2,), [4])],
    },
    {
        'nr': 2,
        'functie': 'sorteaza_dupa_nota',
        'titlu': 'Funcții anonime cu lambda',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(([('Ana', 7), ('Bogdan', 9)],), [('Bogdan', 9), ('Ana', 7)]), (([('Zina', 8), ('Ana', 8)],), [('Ana', 8), ('Zina', 8)]), (([],), []), (([('C', 5), ('A', 10), ('B', 7)],), [('A', 10), ('B', 7), ('C', 5)])],
    },
    {
        'nr': 3,
        'functie': 'imparte_sigur',
        'titlu': 'Tratarea erorilor cu try și except',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((10, 2), 5.0), ((1, 0), None), (('a', 2), None), ((7, 2), 3.5), ((5, None), None)],
    },
    {
        'nr': 4,
        'functie': 'elemente_comune',
        'titlu': 'Mulțimi (sets)',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(([1, 2, 2, 3], [2, 3, 4]), [2, 3]), (([1], [2]), []), (([5, 3, 1], [1, 3, 5]), [1, 3, 5]), (([], [1]), [])],
    },
    {
        'nr': 5,
        'functie': 'total_peste_prag',
        'titlu': 'Map, filter, reduce',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(([10, 50, 100], 20), 150.0), (([1, 2], 5), 0.0), (([10.5, 20.25], 10), 30.75), (([], 3), 0.0)],
    },
    {
        'nr': 6,
        'functie': 'extrage_grupe',
        'titlu': 'Expresii regulate',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(("Grupele SI-265 si FI-101 vin azi",), ['SI-265', 'FI-101']), (("nimic aici",), []), (("SI-266",), ['SI-266']), (("si-266 nu e valid, SI-2666 nici",), [])],
    },
]

INSTRUCTIUNI = '...'

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n   Intrerupt. Codul tau ramane salvat in fisier.\n")
def saluta():
    return "Hello, World!"

# --- Sarcina 2: Variabile și tipuri de date ---------------------------------
def celsius_in_fahrenheit(c):
    return c * 9/5 + 32

# --- Sarcina 3: Liste -------------------------------------------------------
def cele_mai_mari_trei(numere):
    return sorted(numere, reverse=True)[:3]

# --- Sarcina 4: Operatori de bază și tupluri --------------------------------
def cat_si_rest(a, b):
    return (a // b, a % b)

# --- Sarcina 5: Formatarea textului -----------------------------------------
def fisa_student(nume, grupa, media):
    return f"{nume} ({grupa}) - media {media:.2f}"

# --- Sarcina 6: Operații cu text --------------------------------------------
def initiale(nume_complet):
    cuvinte = nume_complet.strip().split()
    return "".join(f"{c[0].upper()}." for c in cuvinte)

# --- Sarcina 7: Instrucțiuni condiționale -----------------------------------
def calificativ(nota):
    if nota >= 9:
        return "excelent"
    elif nota >= 7:
        return "bine"
    elif nota >= 5:
        return "satisfacator"
    else:
        return "nepromovat"

# --- Sarcina 8: Cicluri -----------------------------------------------------
def fizzbuzz(n):
    rezultat = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            rezultat.append("FizzBuzz")
        elif i % 3 == 0:
            rezultat.append("Fizz")
        elif i % 5 == 0:
            rezultat.append("Buzz")
        else:
            rezultat.append(str(i))
    return rezultat

# --- Sarcina 9: Funcții proprii ---------------------------------------------
def pret_final(pret, reducere=0):
    return round(pret - (pret * reducere / 100), 2)

# --- Sarcina 10: Clase și obiecte --------------------------------------------
class Student:
    def __init__(self, nume, grupa):
        self.nume = nume
        self.grupa = grupa
        self.note = []

    def adauga_nota(self, nota):
        self.note.append(nota)

    def media(self):
        if not self.note:
            return 0
        return round(sum(self.note) / len(self.note), 2)

# --- Sarcina 11: Dicționare --------------------------------------------------
def frecventa_litere(text):
    rezultat = {}
    for c in text:
        if c.isalpha():
            lc = c.lower()
            rezultat[lc] = rezultat.get(lc, 0) + 1
    return rezultat

# --- Sarcina 12: Module și pachete -------------------------------------------
def zile_intre(data1, data2):
    d1 = datetime.datetime.strptime(data1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(data2, "%Y-%m-%d")
    return abs((d2 - d1).days)

# --- Sarcina 13: Lucrul cu fișiere -------------------------------------------
def salveaza_si_incarca(cale, note):
    with open(cale, "w", encoding="utf-8") as f:
        for n in note:
            f.write(str(n) + "\n")
    rezultat = []
    with open(cale, "r", encoding="utf-8") as f:
        for rand in f:
            if rand.strip():
                rezultat.append(float(rand.strip()))
    return rezultat



# ============================================================================
#   PARTEA 2  -  JOCUL
#   7 misiuni, cate 1 punct fiecare. Comenzi: player.move_forward(),
# ============================================================================

#   player.turn_left(), player.turn_right(), player.collect(),
#   player.push(), player.build("bridge"), player.can_move()

# --- Misiunea 1 ------------------------------------------------------------
def misiunea_1(player):
    for _ in range(4):
        player.move_forward()

# --- Misiunea 2 ------------------------------------------------------------
def misiunea_2(player):
    for _ in range(3):
        player.move_forward()
    player.turn_right()
    for _ in range(3):
        player.move_forward()

# --- Misiunea 3 ------------------------------------------------------------
def misiunea_3(player):
    while not player.at_exit():
        player.move_forward()

# --- Misiunea 4 ------------------------------------------------------------
def misiunea_4(player):
    for _ in range(7):
        if player.look() == "bustean":
            player.collect()
        player.move_forward()

# --- Misiunea 5 ------------------------------------------------------------
def misiunea_5(player):
    player.move_forward()
    player.move_forward()
    player.push()
    while not player.at_exit():
        player.move_forward()

# --- Misiunea 6 ------------------------------------------------------------
def misiunea_6(player):
    for _ in range(4):
        player.move_forward()
        player.collect()
    player.move_forward()
    player.build("bridge")
    while not player.at_exit():
        player.move_forward()

# --- Misiunea 7 ------------------------------------------------------------
def misiunea_7(player):
    player.move_forward()
    player.move_forward()
    player.push()
    player.move_forward()
    for _ in range(3):
        player.collect()
        player.move_forward()
    player.turn_right()
    player.move_forward()
    player.turn_right()
    for _ in range(3):
        player.move_forward()
    player.collect()
    player.turn_left()
    player.move_forward()
    player.turn_left()
    for _ in range(3):
        player.move_forward()
    player.build("bridge")
    player.move_forward()
    player.turn_left()
    player.move_forward()



# ============================================================================
#   PARTEA 3  -  BONUS
#   6 sarcini, cate 1 punct. Acopera sarcinile nerezolvate.
# ============================================================================

# --- Sarcina 1: Liste construite dintr-o singură expresie -------------------
def patrate_pare(n):
    return [x * x for x in range(1, n + 1) if x % 2 == 0]

# --- Sarcina 2: Funcții anonime cu lambda -----------------------------------
def sorteaza_dupa_nota(studenti):
    return sorted(studenti, key=lambda p: (-p[1], p[0]))

# --- Sarcina 3: Tratarea erorilor cu try și except --------------------------
def imparte_sigur(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return None

# --- Sarcina 4: Mulțimi (sets) ----------------------------------------------
def elemente_comune(a, b):
    return sorted(list(set(a) & set(b)))

# --- Sarcina 5: Map, filter, reduce -----------------------------------------
def total_peste_prag(preturi, prag):
    return round(float(sum(filter(lambda x: x > prag, preturi))), 2)

# --- Sarcina 6: Expresii regulate -------------------------------------------
def extrage_grupe(text):
    return re.findall(r"[A-Z]{2}-\d{3}", text)



# ############################################################################
#
#   NU MODIFICA NIMIC SUB ACEASTA LINIE
#
#   Aici se afla motorul care iti verifica raspunsurile si deseneaza jocul.
#   Daca stergi ceva din greseala, descarca din nou fisierul original.
#
# ############################################################################

import sys, os, time, io, re, math, shutil, datetime, traceback

if os.name == "nt":
    os.system("")
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RESET = "\033[0m"; ALDIN = "\033[1m"; GRI = "\033[90m"; ROSU = "\033[91m"
VERDE = "\033[92m"; GALBEN = "\033[93m"; ALBASTRU = "\033[94m"; CYAN = "\033[96m"

EMAIL_PROFESOR = "cristian.gonceari@isa.utm.md"
COD_LAB = "L3"
LATIME = 74


def _c(t, culoare):
    return culoare + str(t) + RESET


def _sterge_ecran():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        print("\n" * 40)


def _linie(ch="-"):
    print(_c(ch * LATIME, GRI))


def _titlu(text, culoare=CYAN):
    print()
    print(_c("=" * LATIME, culoare))
    print(_c("  " + text, culoare + ALDIN))
    print(_c("=" * LATIME, culoare))
    print()


def _pauza():
    try:
        input(_c("\n  [Enter] pentru a continua...", GRI))
    except (EOFError, KeyboardInterrupt):
        print()


def _fara_diacritice(s):
    tabel = str.maketrans("ăâîșşțţĂÂÎȘŞȚŢ", "aaissttAAISSTT")
    return s.translate(tabel)


def _egale(a, b):
    if isinstance(a, float) or isinstance(b, float):
        try:
            return abs(float(a) - float(b)) < 1e-9
        except (TypeError, ValueError):
            return False
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        if type(a) != type(b) or len(a) != len(b):
            return False
        return all(_egale(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        return all(_egale(a[k], b[k]) for k in a)
    return a == b


def _scurt(v, maxim=60):
    t = repr(v)
    return t if len(t) <= maxim else t[:maxim - 3] + "..."


# ---------------------------------------------------------------------------
#  Verificarea unei sarcini
# ---------------------------------------------------------------------------
def verifica_sarcina(s, detaliat=False):
    """Returneaza (reusit, mesaj)."""
    if "verificator" in s:
        try:
            return s["verificator"]()
        except NotImplementedError:
            return False, "Sarcina nu este inca rezolvata."
        except Exception as e:
            return False, "Eroare: " + type(e).__name__ + ": " + str(e)

    f = globals().get(s["functie"])
    if f is None:
        return False, "Functia " + s["functie"] + " nu exista in fisier."
    for args, asteptat in s["teste"]:
        try:
            obtinut = f(*args)
        except NotImplementedError:
            return False, "Sarcina nu este inca rezolvata."
        except Exception as e:
            return False, ("Codul tau a dat eroare la " + s["functie"] +
                           "(" + ", ".join(_scurt(a) for a in args) + ")\n" +
                           "         " + type(e).__name__ + ": " + str(e))
        if not _egale(obtinut, asteptat):
            return False, ("Pentru " + s["functie"] + "(" +
                           ", ".join(_scurt(a) for a in args) + ")\n" +
                           "         asteptam: " + _scurt(asteptat) + "\n" +
                           "         am primit: " + _scurt(obtinut))
    return True, "Corect."


def verifica_misiune(niv, animatie=False):
    f = globals().get("misiunea_" + str(niv["nr"]))
    if f is None:
        return False, "Functia misiunea_" + str(niv["nr"]) + " nu exista."
    try:
        gol = f.__code__.co_code == (lambda p: None).__code__.co_code
    except Exception:
        gol = False
    if gol:
        return False, "Misiunea nu este inca rezolvata."
    return ruleaza_misiune(niv, f, animatie)


def stare_completa():
    """Returneaza lista de (categorie, nr, titlu, reusit)."""
    out = []
    for s in SARCINI_BAZE:
        ok, _ = verifica_sarcina(s)
        out.append(("baze", s["nr"], s["titlu"], ok))
    for niv in NIVELURI:
        ok, _ = verifica_misiune(niv, animatie=False)
        out.append(("joc", niv["nr"], niv["titlu"], ok))
    for s in SARCINI_BONUS:
        ok, _ = verifica_sarcina(s)
        out.append(("bonus", s["nr"], s["titlu"], ok))
    return out


def punctaj(stare):
    ob = sum(1 for c, _, _, ok in stare if c in ("baze", "joc") and ok)
    bo = sum(1 for c, _, _, ok in stare if c == "bonus" and ok)
    total = min(ob + bo, 20)
    nota = max(1, min(10, round(total / 2)))
    return ob, bo, total, nota


# ---------------------------------------------------------------------------
#  Afisare
# ---------------------------------------------------------------------------
def bara(cate, din, latime=30):
    plin = int(latime * cate / din) if din else 0
    return ("[" + _c("#" * plin, VERDE) + _c("." * (latime - plin), GRI) +
            "] " + str(cate) + "/" + str(din))


def arata_progres(stare=None):
    stare = stare or stare_completa()
    _titlu("PROGRESUL TAU")
    for eticheta, cat, total in (("PARTEA 1 - Bazele", "baze", 13),
                                 ("PARTEA 2 - Jocul", "joc", 7),
                                 ("PARTEA 3 - Bonus", "bonus", len(SARCINI_BONUS))):
        randuri = [(n, t, ok) for c, n, t, ok in stare if c == cat]
        cate = sum(1 for _, _, ok in randuri if ok)
        print(_c("  " + eticheta, ALDIN) + "   " + bara(cate, total))
        for n, t, ok in randuri:
            semn = _c("[v]", VERDE) if ok else _c("[ ]", GRI)
            nume = t if ok else _c(t, GRI)
            print("     " + semn + " " + str(n).rjust(2) + ". " + nume)
        print()
    ob, bo, total, nota = punctaj(stare)
    _linie()
    print("  Puncte obligatorii: " + _c(str(ob) + " / 20", ALDIN) +
          "      Bonus: " + _c("+" + str(bo), VERDE if bo else GRI))
    print("  Punctaj total: " + _c(str(total) + " / 20", ALDIN) +
          "      Nota: " + _c(str(nota), (VERDE if nota >= 5 else ROSU) + ALDIN))
    _linie()


def arata_teorie(s):
    _sterge_ecran()
    _titlu(str(s["nr"]) + ". " + s["titlu"])
    for rand in s["teorie"].split("\n"):
        print("  " + rand)
    if s.get("exemplu"):
        print()
        print(_c("  EXEMPLU", GALBEN + ALDIN))
        _linie()
        for rand in s["exemplu"].split("\n"):
            print("  " + _c(rand, CYAN))
        _linie()
    print()
    print(_c("  SARCINA TA", VERDE + ALDIN))
    for rand in s["sarcina"].split("\n"):
        print("  " + rand)
    print()
    print(_c("  Scrie codul in functia  " + s["functie"] +
             "  din partea de sus a fisierului.", GRI))


def arata_indicii(s):
    _titlu("INDICII pentru " + s["titlu"], GALBEN)
    for i, ind in enumerate(s.get("indicii", []), 1):
        print(_c("  Indiciul " + str(i) + ":", GALBEN + ALDIN))
        for rand in ind.split("\n"):
            print("    " + rand)
        print()
        if i < len(s.get("indicii", [])):
            try:
                r = input(_c("    Vrei si urmatorul indiciu? (d/n) ", GRI)).strip().lower()
            except (EOFError, KeyboardInterrupt):
                return
            if r not in ("d", "da", "y", ""):
                return
    if s.get("greseala"):
        print(_c("  GRESEALA FRECVENTA", ROSU + ALDIN))
        for rand in s["greseala"].split("\n"):
            print("    " + rand)


def lucreaza_sarcina(s):
    while True:
        arata_teorie(s)
        ok, msg = verifica_sarcina(s)
        print()
        if ok:
            print(_c("  [v] REZOLVAT - " + msg, VERDE + ALDIN))
        else:
            print(_c("  [ ] Inca nu e gata.", ROSU + ALDIN))
            for rand in msg.split("\n"):
                print(_c("      " + rand, ROSU))
        print()
        print(_c("  [Enter] reverifica    [i] indicii    [q] inapoi la meniu", GRI))
        try:
            r = input("  > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if r == "q":
            return
        if r == "i":
            arata_indicii(s)
            _pauza()


def lucreaza_misiune(niv):
    while True:
        _sterge_ecran()
        _titlu("MISIUNEA " + str(niv["nr"]) + " - " + niv["titlu"])
        for rand in niv["obiectiv"].split("\n"):
            print("  " + rand)
        print()
        print(_c("  Harta:", GALBEN + ALDIN))
        for rand in niv["harta"]:
            print("     " + _c(rand, GRI))
        print()
        print(_c("  @ = tu    * = iesirea    o = bustean    R = stanca", GRI))
        print(_c("  ~ = apa   X = loc de pod    # = perete", GRI))
        print()
        print(_c("  Scrie codul in functia  misiunea_" + str(niv["nr"]) +
                 "(player)  din fisier.", GRI))
        print()
        print(_c("  [Enter] ruleaza    [q] inapoi la meniu", GRI))
        try:
            r = input("  > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if r == "q":
            return
        ok, msg = verifica_misiune(niv, animatie=True)
        print()
        if ok:
            print(_c("  [v] MISIUNE INDEPLINITA - " + msg, VERDE + ALDIN))
        else:
            print(_c("  [x] " + msg, ROSU + ALDIN))
        _pauza()


# ---------------------------------------------------------------------------
#  Pregatirea fisierului pentru trimitere
# ---------------------------------------------------------------------------
def nume_fisier_corect():
    n = _fara_diacritice(NUME.strip()).replace(" ", "_")
    p = _fara_diacritice(PRENUME.strip()).replace(" ", "_")
    g = GRUPA.strip().upper().replace(" ", "")
    if not (n and p and g):
        return None
    return COD_LAB + "_TP_" + n.capitalize() + "_" + p.capitalize() + "_" + g + ".py"


def date_completate():
    return bool(NUME.strip() and PRENUME.strip() and GRUPA.strip())


def pregateste_trimiterea():
    _sterge_ecran()
    _titlu("PREGATIREA FISIERULUI PENTRU TRIMITERE")
    if not date_completate():
        print(_c("  Nu ai completat datele tale.", ROSU + ALDIN))
        print()
        print("  Deschide fisierul si completeaza, sus de tot:")
        print(_c('      NUME = "Popescu"', CYAN))
        print(_c('      PRENUME = "Ion"', CYAN))
        print(_c('      GRUPA = "SI-266"', CYAN))
        return
    stare = stare_completa()
    ob, bo, total, nota = punctaj(stare)
    nume = nume_fisier_corect()
    sursa = os.path.abspath(__file__)
    tinta = os.path.join(os.path.dirname(sursa), nume)
    try:
        if os.path.abspath(tinta) != sursa:
            shutil.copyfile(sursa, tinta)
        creat = True
    except Exception as e:
        creat = False
        print(_c("  Nu am putut crea copia: " + str(e), ROSU))
    arata_progres(stare)
    print()
    if creat:
        print(_c("  Am pregatit fisierul:", VERDE + ALDIN))
        print(_c("     " + nume, VERDE + ALDIN))
        print(_c("  Il gasesti in acelasi folder cu acest fisier.", GRI))
    print()
    print(_c("  TRIMITE-L ASA:", GALBEN + ALDIN))
    print("     Adresa:  " + _c(EMAIL_PROFESOR, ALDIN))
    print("     Subiect: " + _c(nume[:-3], ALDIN))
    print("     Atasat:  " + _c(nume, ALDIN))
    print()
    print(_c("  Subiectul este exact numele fisierului, fara .py", GRI))


# ---------------------------------------------------------------------------
#  Meniuri
# ---------------------------------------------------------------------------
def meniu_lista(titlu, elemente, cat, stare):
    while True:
        _sterge_ecran()
        _titlu(titlu)
        for el in elemente:
            nr = el["nr"]
            ok = next((o for c, n, _, o in stare if c == cat and n == nr), False)
            semn = _c("[v]", VERDE) if ok else _c("[ ]", GRI)
            print("   " + semn + "  " + str(nr).rjust(2) + ". " + el["titlu"])
        print()
        print(_c("   Scrie numarul sarcinii, sau [q] pentru meniul principal.", GRI))
        try:
            r = input("   > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if r == "q":
            return
        if not r.isdigit():
            continue
        el = next((e for e in elemente if e["nr"] == int(r)), None)
        if el is None:
            continue
        if cat == "joc":
            lucreaza_misiune(el)
        else:
            lucreaza_sarcina(el)
        stare = stare_completa()


def banner():
    print()
    print(_c("   ____        _   _                   _        _     ____  ", VERDE))
    print(_c("  |  _ \\ _   _| |_| |__   ___  _ __   | |    __ _| |__ |___ \\ ", VERDE))
    print(_c("  | |_) | | | | __| '_ \\ / _ \\| '_ \\  | |   / _` | '_ \\  __) |", VERDE))
    print(_c("  |  __/| |_| | |_| | | | (_) | | | | | |__| (_| | |_) |/ __/ ", VERDE))
    print(_c("  |_|    \\__, |\\__|_| |_|\\___/|_| |_| |_____\\__,_|_.__/|_____|", VERDE))
    print(_c("         |___/                                               ", VERDE))
    print(_c("        Tehnici de programare  -  Lucrarea de laborator 3", GRI))
    print()


def main():
    while True:
        stare = stare_completa()
        ob, bo, total, nota = punctaj(stare)
        _sterge_ecran()
        banner()
        if date_completate():
            print("   Student: " + _c(NUME + " " + PRENUME + "  (" + GRUPA + ")", ALDIN))
        else:
            print(_c("   ! Nu ti-ai completat NUME, PRENUME si GRUPA sus in fisier.", ROSU))
        print("   Progres: " + bara(total, 20) + "     Nota acum: " +
              _c(str(nota), (VERDE if nota >= 5 else ROSU) + ALDIN))
        print()
        _linie()
        print("   1. Partea 1 - Bazele          (13 sarcini, 13 puncte)")
        print("   2. Partea 2 - Jocul           (7 misiuni, 7 puncte)")
        print("   3. Partea 3 - Bonus           (" + str(len(SARCINI_BONUS)) +
              " sarcini, puncte in plus)")
        print("   4. Vezi progresul detaliat")
        print("   5. Cum se lucreaza (instructiuni)")
        print("   6. Pregateste fisierul pentru trimitere")
        print("   0. Iesire")
        _linie()
        try:
            r = input("   Alege > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if r == "1":
            meniu_lista("PARTEA 1 - BAZELE", SARCINI_BAZE, "baze", stare)
        elif r == "2":
            meniu_lista("PARTEA 2 - JOCUL", NIVELURI, "joc", stare)
        elif r == "3":
            meniu_lista("PARTEA 3 - BONUS", SARCINI_BONUS, "bonus", stare)
        elif r == "4":
            arata_progres(stare); _pauza()
        elif r == "5":
            instructiuni(); _pauza()
        elif r == "6":
            pregateste_trimiterea(); _pauza()
        elif r == "0":
            print(_c("\n   Spor la treaba!\n", VERDE))
            return


def instructiuni():
    _sterge_ecran()
    _titlu("CUM SE LUCREAZA")
    for rand in INSTRUCTIUNI.split("\n"):
        print("  " + rand)



def _verif_student():
    S = globals().get("Student")
    if S is None:
        return False, "Clasa Student nu este definita."
    try:
        s = S("Popescu Ion", "SI-266")
    except NotImplementedError:
        return False, "Sarcina nu este inca rezolvata."
    except Exception as e:
        return False, "Student(\"Popescu Ion\", \"SI-266\") a dat eroare: " + str(e)
    if getattr(s, "nume", None) != "Popescu Ion":
        return False, "Obiectul trebuie sa retina numele in atributul self.nume"
    if getattr(s, "grupa", None) != "SI-266":
        return False, "Obiectul trebuie sa retina grupa in atributul self.grupa"
    try:
        m = s.media()
    except Exception as e:
        return False, "media() a dat eroare: " + str(e)
    if not _egale(m, 0):
        return False, ("Un student fara note trebuie sa aiba media 0.\n"
                       "         am primit: " + _scurt(m))
    try:
        s.adauga_nota(8)
        s.adauga_nota(9)
    except Exception as e:
        return False, "adauga_nota() a dat eroare: " + str(e)
    if not _egale(s.media(), 8.5):
        return False, ("Dupa notele 8 si 9, media trebuie sa fie 8.5\n"
                       "         am primit: " + _scurt(s.media()))
    s.adauga_nota(10)
    if not _egale(s.media(), 9.0):
        return False, ("Dupa notele 8, 9 si 10, media trebuie sa fie 9.0\n"
                       "         am primit: " + _scurt(s.media()))
    s2 = S("Ana Pop", "SI-265")
    if not _egale(s2.media(), 0):
        return False, "Fiecare student trebuie sa aiba propria lista de note."
    return True, "Corect."


def _verif_fisier():
    import tempfile
    f = globals().get("salveaza_si_incarca")
    if f is None:
        return False, "Functia salveaza_si_incarca nu exista."
    cale = os.path.join(tempfile.gettempdir(), "lab3_test_note.txt")
    if os.path.exists(cale):
        try:
            os.remove(cale)
        except Exception:
            pass
    try:
        rez = f(cale, [8, 9.5, 10])
    except NotImplementedError:
        return False, "Sarcina nu este inca rezolvata."
    except Exception as e:
        return False, "Codul tau a dat eroare: " + type(e).__name__ + ": " + str(e)
    if not _egale(rez, [8.0, 9.5, 10.0]):
        return False, ("Pentru salveaza_si_incarca(cale, [8, 9.5, 10])\n"
                       "         asteptam: [8.0, 9.5, 10.0]\n"
                       "         am primit: " + _scurt(rez))
    if not os.path.exists(cale):
        return False, "Fisierul nu a fost creat. Trebuie sa scrii efectiv pe disc."
    try:
        with open(cale, "r", encoding="utf-8") as fh:
            randuri = [r.strip() for r in fh if r.strip()]
    except Exception as e:
        return False, "Nu am putut citi fisierul creat: " + str(e)
    if len(randuri) != 3:
        return False, ("Fisierul trebuie sa aiba cate o nota pe fiecare rand.\n"
                       "         am gasit " + str(len(randuri)) + " randuri.")
    rez2 = f(cale, [])
    if not _egale(rez2, []):
        return False, "Pentru o lista goala trebuie sa returnezi []."
    return True, "Corect."

# ---------------------------------------------------------------------------
#  Jocul pe grila
# ---------------------------------------------------------------------------
class EroareJoc(Exception):
    pass


class Jucator:
    """Personajul pe care il comanzi din cod.

    Metode disponibile:
        player.move_forward()   - un pas inainte
        player.turn_left()      - rotire la stanga
        player.turn_right()     - rotire la dreapta
        player.collect()        - ridica busteanul de sub picioare
        player.push()           - impinge stanca din fata
        player.build("bridge")  - construieste un pod (ai nevoie de 4 busteni)
        player.can_move()       - True daca poti face un pas inainte
        player.at_exit()        - True daca esti pe stea
        player.look()           - ce se afla in fata ta, ca text
    """

    DIRECTII = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # N, E, S, V
    SEMNE = ["^", ">", "v", "<"]
    NUME_DIR = ["nord", "est", "sud", "vest"]

    def __init__(self, harta, max_pasi=250, animatie=True):
        self.grila = [list(r) for r in harta]
        self.animatie = animatie
        self.max_pasi = max_pasi
        self.pasi = 0
        self.busteni = 0
        self.jurnal = []
        self.dir = 1
        self.lin = self.col = 0
        for i, rand in enumerate(self.grila):
            for j, c in enumerate(rand):
                if c == "@":
                    self.lin, self.col = i, j
                    self.grila[i][j] = "."
        self._deseneaza("start")

    # -- intern ------------------------------------------------------------
    def _consuma(self, ce):
        self.pasi += 1
        if self.pasi > self.max_pasi:
            raise EroareJoc(
                "Ai depasit " + str(self.max_pasi) + " de actiuni. "
                "Probabil ai un ciclu care nu se opreste niciodata."
            )
        self.jurnal.append(ce)

    def _in_fata(self):
        dl, dc = self.DIRECTII[self.dir]
        return self.lin + dl, self.col + dc

    def _celula(self, l, c):
        if 0 <= l < len(self.grila) and 0 <= c < len(self.grila[l]):
            return self.grila[l][c]
        return "#"

    def _deseneaza(self, actiune=""):
        if not self.animatie:
            return
        _sterge_ecran()
        print(_c("  " + actiune, GRI))
        print()
        for i, rand in enumerate(self.grila):
            out = "   "
            for j, c in enumerate(rand):
                if (i, j) == (self.lin, self.col):
                    out += _c(self.SEMNE[self.dir], VERDE + ALDIN)
                elif c == "#":
                    out += _c("#", GRI)
                elif c == "*":
                    out += _c("*", GALBEN + ALDIN)
                elif c == "o":
                    out += _c("o", GALBEN)
                elif c == "R":
                    out += _c("R", ROSU)
                elif c == "~":
                    out += _c("~", ALBASTRU)
                elif c == "X":
                    out += _c("X", ALBASTRU)
                elif c == "=":
                    out += _c("=", GALBEN)
                else:
                    out += _c(".", GRI)
            print(out)
        print()
        print(_c("   busteni: " + str(self.busteni) +
                 "    actiuni: " + str(self.pasi) +
                 "    privesti spre: " + self.NUME_DIR[self.dir], GRI))
        time.sleep(0.11)

    # -- API pentru student -------------------------------------------------
    def move_forward(self):
        self._consuma("move_forward")
        l, c = self._in_fata()
        tinta = self._celula(l, c)
        if tinta in ("#", "R"):
            self._deseneaza("te-ai lovit de un obstacol")
            raise EroareJoc("Nu poti merge inainte: in fata ta este un obstacol.")
        if tinta == "~":
            self._deseneaza("ai cazut in apa")
            raise EroareJoc("Ai cazut in apa. Ai nevoie de un pod ca sa treci.")
        if tinta == "X":
            self._deseneaza("ai cazut in apa")
            raise EroareJoc("Aici lipseste podul. Construieste-l cu build.")
        self.lin, self.col = l, c
        self._deseneaza("move_forward()")

    def turn_left(self):
        self._consuma("turn_left")
        self.dir = (self.dir - 1) % 4
        self._deseneaza("turn_left()")

    def turn_right(self):
        self._consuma("turn_right")
        self.dir = (self.dir + 1) % 4
        self._deseneaza("turn_right()")

    def collect(self):
        self._consuma("collect")
        if self.grila[self.lin][self.col] != "o":
            self._deseneaza("nu e nimic de colectat aici")
            raise EroareJoc("Nu exista niciun bustean pe casuta pe care stai.")
        self.grila[self.lin][self.col] = "."
        self.busteni += 1
        self._deseneaza("collect()")

    def push(self):
        self._consuma("push")
        l, c = self._in_fata()
        if self._celula(l, c) != "R":
            self._deseneaza("nu e nicio stanca in fata")
            raise EroareJoc("Nu ai ce impinge: in fata ta nu se afla o stanca.")
        dl, dc = self.DIRECTII[self.dir]
        l2, c2 = l + dl, c + dc
        if self._celula(l2, c2) not in (".", "~"):
            self._deseneaza("stanca nu se poate misca")
            raise EroareJoc("Stanca nu are unde sa fie impinsa.")
        self.grila[l][c] = "."
        self.grila[l2][c2] = "." if self._celula(l2, c2) == "~" else "R"
        self._deseneaza("push()")

    def build(self, ce=""):
        self._consuma("build")
        if str(ce).strip().lower() not in ("bridge", "pod"):
            raise EroareJoc('Scrie exact player.build("bridge") ca sa construiesti podul.')
        if self.busteni < 4:
            self._deseneaza("nu ai destui busteni")
            raise EroareJoc("Ai nevoie de 4 busteni ca sa construiesti un pod. "
                            "Ai doar " + str(self.busteni) + ".")
        l, c = self._in_fata()
        if self._celula(l, c) != "X":
            self._deseneaza("nu se poate construi aici")
            raise EroareJoc("Poti construi un pod doar in fata unui semn X.")
        self.grila[l][c] = "="
        self.busteni -= 4
        self._deseneaza("build(\"bridge\")")

    def can_move(self):
        l, c = self._in_fata()
        return self._celula(l, c) in (".", "*", "o", "=")

    def at_exit(self):
        return self.grila[self.lin][self.col] == "*"

    def look(self):
        l, c = self._in_fata()
        return {"#": "perete", ".": "liber", "*": "iesirea", "o": "bustean",
                "R": "stanca", "~": "apa", "X": "loc de pod",
                "=": "pod"}.get(self._celula(l, c), "necunoscut")


def ruleaza_misiune(nivel, functie, animatie=True):
    """Ruleaza codul studentului pe harta nivelului.
    Returneaza (reusit, mesaj)."""
    p = Jucator(nivel["harta"], nivel.get("max_pasi", 250), animatie)
    try:
        functie(p)
    except EroareJoc as e:
        return False, str(e)
    except RecursionError:
        return False, "Prea multe apeluri imbricate."
    except Exception as e:
        return False, "Codul tau a dat eroare: " + type(e).__name__ + ": " + e
    if not p.at_exit():
        return False, "Nu ai ajuns la stea. Te-ai oprit pe alta casuta."
    if p.busteni < nivel.get("busteni_min", 0):
        return False, ("Ai ajuns la iesire, dar ai colectat doar " +
                       str(p.busteni) + " busteni din " +
                       str(nivel["busteni_min"]) + " ceruti.")
    return True, "Misiune indeplinita in " + str(p.pasi) + " actiuni."


NIVELURI = [
    {
        "nr": 1,
        "titlu": "Primii pasi",
        "obiectiv": ("Mergi inainte pana ajungi pe stea.\n"
                     "Ai la dispozitie o singura comanda: player.move_forward()\n"
                     "Numara cate casute sunt pana la stea si apeleaza comanda\n"
                     "de exact atatea ori, una sub alta."),
        "harta": ["#######",
                  "#@....*",
                  "#######"],
        "invata": "apelarea unei functii, o comanda pe fiecare rand",
    },
    {
        "nr": 2,
        "titlu": "Prima cotitura",
        "obiectiv": ("Drumul face un colt. Pe langa move_forward ai acum\n"
                     "player.turn_right() si player.turn_left().\n"
                     "Rotirea nu te muta din loc, doar schimba directia in care privesti."),
        "harta": ["######",
                  "#@...#",
                  "####.#",
                  "####.#",
                  "####*#",
                  "######"],
        "invata": "ordinea instructiunilor conteaza",
    },
    {
        "nr": 3,
        "titlu": "Coridorul lung",
        "obiectiv": ("Pana la stea sunt multi pasi. Poti scrie move_forward de\n"
                     "zeci de ori... sau poti folosi un ciclu:\n"
                     "    for pas in range(10):\n"
                     "        player.move_forward()\n"
                     "Numara exact cate casute sunt si pune numarul in range."),
        "harta": ["##################",
                  "#@..............*#",
                  "##################"],
        "invata": "ciclul for si range",
    },
    {
        "nr": 4,
        "titlu": "Culegatorul",
        "obiectiv": ("Pe drum sunt busteni, marcati cu o. Cand ajungi pe o casuta\n"
                     "cu bustean, apeleaza player.collect() ca sa il ridici.\n"
                     "Trebuie sa aduni toti cei 3 busteni SI sa ajungi pe stea."),
        "harta": ["##########",
                  "#@.o.o.o*#",
                  "##########"],
        "busteni_min": 3,
        "invata": "combinarea mai multor comenzi intr-un ciclu",
    },
    {
        "nr": 5,
        "titlu": "Stanca din drum",
        "obiectiv": ("O stanca, marcata cu R, iti blocheaza drumul.\n"
                     "Apropie-te de ea si foloseste player.push() ca sa o impingi\n"
                     "in directia in care privesti. Apoi treci mai departe."),
        "harta": ["###########",
                  "#@..R....*#",
                  "###########"],
        "invata": "interactiunea cu obiectele",
    },
    {
        "nr": 6,
        "titlu": "Podul peste apa",
        "obiectiv": ("Apa, marcata cu ~, nu se poate traversa. In dreptul semnului X\n"
                     "poti construi un pod, dar ai nevoie de 4 busteni.\n"
                     "Aduna intai cei 4 busteni, apoi opreste-te chiar in fata lui X\n"
                     'si scrie player.build("bridge"). Apoi treci pe pod.'),
        "harta": ["#############",
                  "#@.oooo.X..*#",
                  "#############"],
        "busteni_min": 0,
        "invata": "conditii si resurse",
    },
    {
        "nr": 7,
        "titlu": "Toate la un loc",
        "obiectiv": ("Ultima misiune aduna tot ce ai invatat: coturi, busteni,\n"
                     "o stanca si un pod. Ia-o pas cu pas si deseneaza-ti traseul\n"
                     "pe hartie inainte sa scrii codul.\n"
                     "Trebuie sa ajungi pe stea cu cel putin 1 bustean ramas."),
        "harta": ["############",
                  "#@..R..ooo.#",
                  "##########.#",
                  "#*...X...o.#",
                  "############"],
        "busteni_min": 1,
        "invata": "descompunerea unei probleme mari in pasi mici",
    },
]


SARCINI_BAZE = [
    {
        'nr': 1,
        'functie': 'saluta',
        'titlu': 'Primul program: print sau return',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((), 'Hello, World!')],
    },
    {
        'nr': 2,
        'functie': 'celsius_in_fahrenheit',
        'titlu': 'Variabile și tipuri de date',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((0,), 32.0), ((100,), 212.0), ((-40,), -40.0), ((37,), 98.6)],
    },
    {
        'nr': 3,
        'functie': 'cele_mai_mari_trei',
        'titlu': 'Liste',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(([5, 1, 9, 3, 7],), [9, 7, 5]), (([2, 1],), [2, 1]), (([4, 4, 4, 4],), [4, 4, 4]), (([],), []), (([-5, -1, -9],), [-1, -5, -9])],
    },
    {
        'nr': 4,
        'functie': 'cat_si_rest',
        'titlu': 'Operatori de bază și tupluri',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((17, 5), (3, 2)), ((10, 2), (5, 0)), ((7, 3), (2, 1)), ((0, 4), (0, 0))],
    },
    {
        'nr': 5,
        'functie': 'fisa_student',
        'titlu': 'Formatarea textului',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(('Popescu Ion', 'SI-266', 8.5), 'Popescu Ion (SI-266) - media 8.50'), (('Ana Pop', 'SI-265', 10), 'Ana Pop (SI-265) - media 10.00'), (('Ion Rusu', 'SI-266', 7.333), 'Ion Rusu (SI-266) - media 7.33')],
    },
    {
        'nr': 6,
        'functie': 'initiale',
        'titlu': 'Operații cu text',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(('popescu ion',), 'P.I.'), (('  Ana Maria Pop ',), 'A.M.P.'), (('Ion',), 'I.'), (('vasile alecsandri',), 'V.A.')],
    },
    {
        'nr': 7,
        'functie': 'calificativ',
        'titlu': 'Instrucțiuni condiționale',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((10,), 'excelent'), ((9,), 'excelent'), ((8,), 'bine'), ((7,), 'bine'), ((6,), 'satisfacator'), ((5,), 'satisfacator'), ((4,), 'nepromovat'), ((1,), 'nepromovat')],
    },
    {
        'nr': 8,
        'functie': 'fizzbuzz',
        'titlu': 'Cicluri',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((5,), ['1', '2', 'Fizz', '4', 'Buzz']), ((3,), ['1', '2', 'Fizz']), ((15,), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']), ((1,), ['1'])],
    },
    {
        'nr': 9,
        'functie': 'pret_final',
        'titlu': 'Funcții proprii',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((200, 25), 150.0), ((100,), 100.0), ((99.99, 10), 89.99), ((50, 100), 0.0)],
    },
    {
        'nr': 10,
        'functie': 'Student',
        'titlu': 'Clase și obiecte',
        'teorie': '...',
        'sarcina': '...',
        'verificator': _verif_student,
    },
    {
        'nr': 11,
        'functie': 'frecventa_litere',
        'titlu': 'Dicționare',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(('Ana are',), {'a': 3, 'n': 1, 'r': 1, 'e': 1}), (('',), {}), (('A1 b!',), {'a': 1, 'b': 1}), (('aaa',), {'a': 3})],
    },
    {
        'nr': 12,
        'functie': 'zile_intre',
        'titlu': 'Module și pachete',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(('2026-09-22', '2026-09-25'), 3), (('2026-09-25', '2026-09-22'), 3), (('2026-01-01', '2026-12-31'), 364), (('2026-03-01', '2026-03-01'), 0)],
    },
    {
        'nr': 13,
        'functie': 'salveaza_si_incarca',
        'titlu': 'Lucrul cu fișiere',
        'teorie': '...',
        'sarcina': '...',
        'verificator': _verif_fisier,
    },
]

SARCINI_BONUS = [
    {
        'nr': 1,
        'functie': 'patrate_pare',
        'titlu': 'Liste construite dintr-o singură expresie',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((6,), [4, 16, 36]), ((1,), []), ((10,), [4, 16, 36, 64, 100]), ((2,), [4])],
    },
    {
        'nr': 2,
        'functie': 'sorteaza_dupa_nota',
        'titlu': 'Funcții anonime cu lambda',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(([('Ana', 7), ('Bogdan', 9)],), [('Bogdan', 9), ('Ana', 7)]), (([('Zina', 8), ('Ana', 8)],), [('Ana', 8), ('Zina', 8)]), (([],), []), (([('C', 5), ('A', 10), ('B', 7)],), [('A', 10), ('B', 7), ('C', 5)])],
    },
    {
        'nr': 3,
        'functie': 'imparte_sigur',
        'titlu': 'Tratarea erorilor cu try și except',
        'teorie': '...',
        'sarcina': '...',
        'teste': [((10, 2), 5.0), ((1, 0), None), (('a', 2), None), ((7, 2), 3.5), ((5, None), None)],
    },
    {
        'nr': 4,
        'functie': 'elemente_comune',
        'titlu': 'Mulțimi (sets)',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(([1, 2, 2, 3], [2, 3, 4]), [2, 3]), (([1], [2]), []), (([5, 3, 1], [1, 3, 5]), [1, 3, 5]), (([], [1]), [])],
    },
    {
        'nr': 5,
        'functie': 'total_peste_prag',
        'titlu': 'Map, filter, reduce',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(([10, 50, 100], 20), 150.0), (([1, 2], 5), 0.0), (([10.5, 20.25], 10), 30.75), (([], 3), 0.0)],
    },
    {
        'nr': 6,
        'functie': 'extrage_grupe',
        'titlu': 'Expresii regulate',
        'teorie': '...',
        'sarcina': '...',
        'teste': [(("Grupele SI-265 si FI-101 vin azi",), ['SI-265', 'FI-101']), (("nimic aici",), []), (("SI-266",), ['SI-266']), (("si-266 nu e valid, SI-2666 nici",), [])],
    },
]

INSTRUCTIUNI = '...'

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n   Intrerupt. Codul tau ramane salvat in fisier.\n")