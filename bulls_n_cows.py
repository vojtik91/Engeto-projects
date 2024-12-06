from random import sample
from time import time

def bulls(list_1, list_2):
    """Porovnává dva seznamy a vrací počet Bulls (stejný prvek na stejném indexu)."""
    return sum(1 for x, y in zip(list_1, list_2) if x == y)

def cows(list_1, list_2):
    """Porovnává dva seznamy a vrací počet Cows (shodné prvky na různých indexech)."""
    bulls_and_cows = len(set(list_1) & set(list_2))
    return bulls_and_cows - bulls(list_1, list_2)

def generovani_cisla():
    """Generuje čtyřciferné číslo (každá číslice je unikátní)."""
    while True:
        number_as_list = sample(range(10), 4)
        if number_as_list[0] != 0:
            return number_as_list

def zpracuj_vstup(prompt="Zadej 4ciferné číslo: "):
    """
    Zpracuje vstup uživatele a vrací seznam číslic, platnost a případnou zprávu.
    """
    user_input = input(prompt).strip().upper()
    if user_input == "Q":
        return None, False, "QUIT"
    if not user_input.isdigit() or len(user_input) != 4:
        print("Chyba: Vstup musí být 4ciferné číslo.")
        return None, False, "INVALID"
    if user_input[0] == "0":
        print("Chyba: Číslo nesmí začínat nulou")
        return None, False, "INVALID"
    if len(set(user_input)) != len(user_input):
        print("Chyba: Číslo musí obsahovat unikátní číslice.")
        return None, False, "INVALID"
    return list(map(int, user_input)), True, None

# Uvítání
lane = "-" * 30
uvod = "Hey man, let's play Bulls 'n Cows!\nGuess my 4-digit number! \nor press 'q' for quit "
print(lane, uvod, lane, sep="\n")

# Vygenerování čísla
number_as_list = generovani_cisla()
print(number_as_list)
# Měření času hry
start_time = time()

# Inicializace počítadla pokusů
attempts = 0

# Herní smyčka
while True:
    result, is_valid, message = zpracuj_vstup()
    if message == "QUIT":
        print("Hra byla ukončena uživatelem.")
        break
    if not is_valid:
        continue

    # Zvýšení čítače při každém validním pokusu
    attempts += 1

    if result == number_as_list:
        print("Gratuluji, uhodl jsi správné číslo!")
        break

    bulls_count = bulls(number_as_list, result)
    cows_count = cows(number_as_list, result)
    if bulls_count == 1 and cows_count != 1:
        print(f"Bull: {bulls_count}, Cows: {cows_count}")
        print("Zkus to znovu!")
    elif bulls_count != 1 and cows_count == 1: 
        print(f"Bulls: {bulls_count}, Cow: {cows_count}")
        print("Zkus to znovu!")
    elif bulls_count == 1 and cows_count == 1:
        print(f"Bull: {bulls_count}, Cow: {cows_count}")
        print("Zkus to znovu!") 
    else:
        print(f"Bulls: {bulls_count}, Cows: {cows_count}")
        print("Zkus to znovu!")


end_time = time()
elapsed_time = end_time - start_time
print(f"Délka hry: {elapsed_time:.1f} sekund")
print(f"Počet pokusů: {attempts}")
