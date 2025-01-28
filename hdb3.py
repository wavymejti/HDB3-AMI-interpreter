# Program do przekształcania ciągu binarnego na AMI i HDB3

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
