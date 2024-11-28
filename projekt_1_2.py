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

# pocet textů v listu TEXTS
pocet_textu = len(TEXTS)

# Analyzator textu
def analyze_text(text):
    # nase cara
    graph_line = "-" * 30
       
    #vycisteni textu -> nebude do delky slov zapocitavat znaky jako .,!?;
    #clean_text = text.replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace(";", "")
    
                                                                       
    
    #rozdeleni na jednotliva slova
    words = text.split()

    #vycisteni slov pomoci metody strip
    cleaned_words = []
    for word in words:
        cleaned_words.append(word.strip(",.?!"))



    capitalized_words = []              #list slov s zacinajicich velkym pismenem
    uppercase_words = []                #list slov psanych velkymi pismeny
    lowercase_words = []                #list slov psanych malymi pismeny
    numbers = []                        #list cisel v textu
    word_lengths = []                   #list slov ruznych delek - potreba pro graf

    for word in cleaned_words:
        if word[0].isupper():
            capitalized_words.append(word)
        if word.isupper() and word.isalpha():
            uppercase_words.append(word)
        if word.islower():
            lowercase_words.append(word)
        if word.isdigit():
            numbers.append(int(word))
        word_lengths.append(len(word))

    words_number = len(words)                                   #pocet slov v textu
    capitalized_words_number = len(capitalized_words)           #pocet slov v textu zacinajicich velkym pismenem
    uppercase_words_words_number = len(uppercase_words)         #pocet slov v textu psanych velkymi pismeny
    lowercase_words_number = len(lowercase_words)               #pocet slov v textu psanych malymi pismeny
    numbers_number = len(numbers)                               #pocet cisel v textu
    sum_numbers = sum(numbers)                                  #soucet vsech cisel v textu

    # Vypsani vysledku
    print(f"pocet slov v textu je {words_number}")
    print(f"pocet slov zacinajicich velkym pismenem je {capitalized_words_number}")
    print(f"pocet slov psanych velkymi pismeny je {uppercase_words_words_number}")
    print(f"pocet slov psanych malymi pismeny je {lowercase_words_number}")
    print(f"pocet cisel v textu je {numbers_number}")
    print(f"suma cisel  textu je {sum_numbers}")

    #vytvoreni Dictionary, kde KEY je pocet znaku ve slove a VALUE je pocet vyskytu techto slov v textu 
    lenght_counts = {}
    for lenght in word_lengths:
        if lenght in lenght_counts:
            lenght_counts[lenght] += 1
        else:
            lenght_counts[lenght] = 1

    #hvezdickovy graf, kde pocet hvezdicek ukazuje vyskyt slov urcite delky v textu
    max_stars = max(lenght_counts.values())
    print(graph_line)
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
        print(f"Mame zde {pocet_textu} texty, ktere muzes analyzovat.")
        print(cara)
                
        # vyber textu a overeni zda je zadano cislo a zda je cislo v intervalu <1,pocet textu>
        # nasleduje samotna anlyza textu
        try:
            text_number = int(input(f"zadej cislo textu, ktery chces analyzovat (od 1 do {pocet_textu}):"))
            print(cara)
        
            if text_number < 1 or text_number > pocet_textu:  
                print(f"zamysli se jeste jednou a zadej opravdu cislo od 1 do {pocet_textu}")
            else:
                analyze_text(TEXTS[text_number - 1])

                
                
            
        except ValueError:
            print("nepis kraviny a zadej cislo prosim")

