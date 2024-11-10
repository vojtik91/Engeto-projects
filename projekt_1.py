#uvodni stranka
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Vojtech Potuzak
email: potuzak.vojtech@gmail.com
"""
# nase texty
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Analyzator textu
def analyze_texts(text):
      

    #rozdeleni na jednotliva slova
    words = text.split()
    words_number = len(words)

    #pocet slov s zacinajicich velkym pismenem
    capitalized_words = []
    for word in words:
        if word[0].isupper():
            capitalized_words.append(word)
    capitalized_words_number = len(capitalized_words)

    #pocet slov psanych velkymi pismeny
    uppercase_words = []
    for word in words:
        if word.isupper() and word.isalpha():
            uppercase_words.append(word)
    uppercase_words_words_number = len(uppercase_words)

    #pocet slov psanych malymi pismeny
    lowercase_words = []
    for word in words:
        if word.islower():
            lowercase_words.append(word)
    lowercase_words_number = len(lowercase_words)

    #pocet cisel v textu a jejich soucet
    numbers = []
    for word in words:
        if word.isdigit():
            numbers.append(int(word))
    numbers_number = len(numbers)
    sum_numbers = sum(numbers)

    # Vypsani vysledku
    print(f"pocet slov v textu je {words_number}")
    print(f"pocet slov zacinajicich velkym pismenem je {capitalized_words_number}")
    print(f"pocet slov psanych velkymi pismeny je {uppercase_words_words_number}")
    print(f"pocet slov psanych malymi pismeny je {lowercase_words_number}")
    print(f"pocet cisel v textu je {numbers_number}")
    print(f"suma cisel  textu je {sum_numbers}")

    #pocet vyskytu ruznych delek slov - potreba pro graf
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))

    lenght_counts = {}
    for lenght in word_lengths:
        if lenght in lenght_counts:
            lenght_counts[lenght] += 1
        else:
            lenght_counts[lenght] = 1

    #samotny hvezdickovy graf
    max_stars = max(lenght_counts.values())
    print("-" * 30)
    print(f"LEN| OCCURENCES  | NR.")
    for lenght in sorted(lenght_counts):
        count = lenght_counts[lenght]
        print(f"{str(lenght).rjust(2)} | {("*" * count).ljust(max_stars)} | {count}")   



# nase cara
cara = "-" * 30

#prihlasovaci udaje
login_credentials = {}
login_credentials["bob"] = "123"
login_credentials["mike"] = "pasword123"
login_credentials["ann"] = "pass123"
login_credentials["liz"] = "pass123"

#prihlaseni a overeni vstupnich prihlasovacich udaju
username = input("Zadej prihlasovaci jmeno:")
password = input("Zadej heslo:")

if username not in login_credentials:
    print("neni registrovany")
else:
    if login_credentials[username] != password:
        print("spatne heslo")
    else:
        print(cara)
        print(f"Vitej v nasi appce {username}")
        print(cara)
        print("Mame zde 3 texty, ktere muzes analyzovat.")
        print(cara)
        
        
        # vyber textu a overeni zda je zadano cislo a zda je cislo v intervalu <1,3>
        # nasleduje samotna anlyza textu
        try:
            text_number = int(input("zadej cislo textu, ktery chces analyzovat (od 1 do 3):"))
            print(cara)
        
            if text_number < 0 or text_number > 4:
                print("zamysli se jeste jednou a zadej opravdu cislo od 1 do 3")
            else:
                analyze_texts(TEXTS[text_number - 1])

                
                
            
        except ValueError:
            print("nepis kraviny a zadej cislo prosim")
        
             





