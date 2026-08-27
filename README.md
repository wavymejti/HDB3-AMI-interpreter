# Kodowanie Sygnałów: Binarny na AMI i HDB3

Ten projekt zawiera prosty skrypt w języku Python, który przekształca podany ciąg binarny na kody liniowe **AMI** (Alternate Mark Inversion) oraz **HDB3** (High-Density Bipolar 3).

## 📌 Opis

Program pobiera od użytkownika ciąg składający się z zer i jedynek, a następnie symuluje jego kodowanie do postaci sygnału bipolarnego. Wynik prezentowany jest w czytelnej formie znakowej:
- `0` - brak sygnału (napięcie 0V)
- `+` - impuls dodatni
- `-` - impuls ujemny

## 🚀 Funkcje
- **Walidacja wejścia:** Program sprawdza, czy wprowadzony ciąg składa się wyłącznie z cyfr `0` i `1`.
- **Kodowanie AMI:** Zamiana jedynek na naprzemienne impulsy dodatnie i ujemne.
- **Kodowanie HDB3:** Rozszerzenie kodu AMI, które eliminuje problem długich ciągów zer poprzez zastępowanie sekwencji czterech zer odpowiednimi wzorcami (`B00V` lub `000V`), zachowując przy tym odpowiednią regułę naruszeń bipolarności (V).

## 💻 Wymagania
- Python 3.x (nie wymaga żadnych zewnętrznych bibliotek, korzysta tylko z wbudowanych funkcji)

## 🛠️ Jak używać

1. Pobierz plik ze skryptem (np. `encoder.py`).
2. Uruchom skrypt w terminalu / wierszu poleceń:
   ```bash
   python encoder.py
   ```
3. Wprowadź ciąg binarny, gdy zostaniesz o to poproszony.

### Przykładowy wynik:
```text
Podaj ciąg binarny (np. 010110): 1010000011
Kodowanie AMI: +0-00000+-
Kodowanie HDB3: +0-000-0+-
```

## 📖 Krótko o algorytmach

* **AMI (Alternate Mark Inversion):**
  Zera binarne są przesyłane jako brak napięcia (`0`), a jedynki jako naprzemienne impulsy dodatnie (`+`) i ujemne (`-`). Dzięki temu sygnał nie posiada składowej stałej.
* **HDB3 (High-Density Bipolar 3):**
  System oparty na AMI, stosowany m.in. w telekomunikacji (standard E1), który zapobiega utracie synchronizacji zegara przy długich ciągach zer. Każde cztery kolejne zera są modyfikowane, wprowadzając celowe naruszenie reguły naprzemienności, aby odbiornik mógł je jednoznacznie zidentyfikować.
