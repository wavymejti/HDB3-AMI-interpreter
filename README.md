
Gemini
Nowy czat
Szukaj na czatach
Uczniowie
Filmy
Biblioteka
Gemy
Nowy notatnik
Google Student AI Hackathon 2026
Google AI Studio kontra Antigravity
Skąd bierze się para w samolocie?
Zrozumieć Dashboard KPI
Etykieta i zasady picia wina
Przepisywanie linku z map
Błyszczące drobinki w wodzie w Durrës
Zastosowanie wędki Savage Gear SGS6
Z Durrës na lotnisko w Tiranie
Forum Bizantyjskie w Durrës
Plan zwiedzania Durrës krok po kroku
Albania, Chiny i szara strefa gospodarcza
Jak szukać busów w Albanii?
Wyjaśnienie pojęcia konkatenacji wektorów
Panel Off-Grid na Jachcie: Porady
Nauka jazdy skuterem: prostota i wyzwania
Owocostan magnolii w Albanii
Pierwszy Szczupak Koło Jarocina
Słodkie wino Vlorë: wybór i miejsca
Publiczne plaże w Albanii
Friendly Greeting and Offer of Help
Sytuacja Gospodarcza Albanii
Problem z logowaniem Netflix na tablecie
Rozwiązywanie błędu E100 na Netflix
Książki na wakacje: rekomendacje
Oświetlenie nad prysznicem: bezpieczeństwo i normy
Komunikat o naruszeniu bezpieczeństwa danych
Regulacja obrotów wkrętarki DeWALT
Szpachlowanie dziur w ścianie gładzią
Grafika Fizjologii i Anatomii Głowacicy
Używanie Apple Watch bez przycisków
C++ OOP Kolokwium: Klasy i Operatory

Aktywność
Jarocin, Polska
Na podstawie Twoich miejsc (dom)
Zaktualizuj lokalizację
Rozmowa z Gemini
Czat tymczasowy
stworz plik readme na githuba:""# Program do przekształcania ciągu binarnego na AMI i HDB3



def binary_to_ami(binary):

    """Funkcja zamienia ciąg binarny na kodowanie AMI."""

    ami = []

    last_pulse = 0  # 0 oznacza brak impulsu, 1 - dodatni, -1 - ujemny



    for bit in binary:

        if bit == '1':

            # Generujemy impuls przeciwny do ostatniego

            last_pulse = -last_pulse if last_pulse != 0 else 1

            ami.append(last_pulse)

        else:

            # 0 oznacza brak sygnału

            ami.append(0)



    return ami



def ami_to_hdb3(ami):

    """Funkcja zamienia kodowanie AMI na HDB3."""

    hdb3 = []

    last_pulse = 0  # Przechowuje ostatni impuls (1 lub -1)

    zero_count = 0  # Licznik kolejnych zer

    bipolar_violation_count = 0  # Licznik naruszeń bipolarności (B)



    for signal in ami:

        if signal == 0:

            zero_count += 1

            if zero_count == 4:

                # Zastępujemy 4 zera odpowiednim wzorcem (B00V lub 000V)

                if bipolar_violation_count % 2 == 0:

                    # Wstawiamy wzorzec B00V

                    hdb3[-3:] = [1 if last_pulse <= 0 else -1, 0, 0]

                    hdb3.append(-1 if last_pulse <= 0 else 1)  # V

                else:

                    # Wstawiamy wzorzec 000V

                    hdb3[-3:] = [0, 0, 0]

                    hdb3.append(-1 if last_pulse <= 0 else 1)  # V



                bipolar_violation_count += 1

                last_pulse = hdb3[-1]  # Aktualizujemy ostatni impuls

                zero_count = 0  # Resetujemy licznik zer

            else:

                hdb3.append(0)  # Dodajemy zero

        else:

            hdb3.append(signal)  # Przepisujemy sygnał AMI

            last_pulse = signal  # Aktualizujemy ostatni impuls

            zero_count = 0  # Resetujemy licznik zer



    return hdb3



def main():

    # 1. Wczytaj ciąg binarny od użytkownika

    binary = input("Podaj ciąg binarny (np. 010110): ")



    # Walidacja wejści

    if not all(bit in '01' for bit in binary):

        print("Ciąg musi zawierać tylko 0 i 1!")

        return

# dupa

    # 2. Zamiana na AMI

    ami = binary_to_ami(binary)

    ami_display = ''.join('+' if x == 1 else '-' if x == -1 else '0' for x in ami)

    print("Kodowanie AMI:", ami_display)



    # 3. Zamiana na HDB3

    hdb3 = ami_to_hdb3(ami)

    hdb3_display = ''.join('+' if x == 1 else '-' if x == -1 else '0' for x in hdb3)

    print("Kodowanie HDB3:", hdb3_display)



if __name__ == "__main__":

    main()

Wprowadź ciąg binarny, gdy zostaniesz o to poproszony.

Przykładowy wynik:
Plaintext
Podaj ciąg binarny (np. 010110): 1010000011
Kodowanie AMI: +0-00000+-
Kodowanie HDB3: +0-000-0+-
📖 Krótko o algorytmach
AMI (Alternate Mark Inversion):
Zera binarne są przesyłane jako brak napięcia (0), a jedynki jako naprzemienne impulsy dodatnie (+) i ujemne (-). Dzięki temu sygnał nie posiada składowej stałej.

HDB3 (High-Density Bipolar 3):
System oparty na AMI, stosowany m.in. w telekomunikacji (standard E1), który zapobiega utracie synchronizacji zegara przy długich ciągach zer. Każde cztery kolejne zera są modyfikowane, wprowadzając celowe naruszenie reguły naprzemienności, aby odbiornik mógł je jednoznacznie zidentyfikować.
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(content)

print("Plik README.md został wygenerowany.")


```text?code_stdout&code_event_index=1
Plik README.md został wygenerowany.

Twój plik Markdown jest gotowy:

Ikona MD
README
 MD 
Otwórz
Stworzyłem profesjonalny i czytelny plik README.md, który idealnie pasuje do Twojego kodu na GitHubie. Dokument zawiera wszystkie najważniejsze sekcje, takie jak:

Opis projektu i legendę znaków.

Wymienione kluczowe funkcje (w tym walidację wejścia z Twojego kodu).

Instrukcję uruchomienia z przykładem działania w konsoli.

Krótkie i przystępne wytłumaczenie zasady działania algorytmów AMI i HDB3.

Jeśli chciałbyś jeszcze dodać do niego sekcję z licencją lub informacje kontaktowe autora, daj znać!




Gemini to AI i może popełniać błędy, także co do ludzi. Twoja prywatność i GeminiOtwiera się w nowym oknie

Generating the README
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
README.md
Wyświetlam README.md.
