import random
import sys
import time
test = 2
test = 1

Level = 1
#Klassen

class Pokemon:
    def __init__(self,spezies, KP, Level, attacken, typ_1, typ_2):
        self.spezies = spezies
        self.KP = KP
        self.Level = Level
        self.attacken = attacken
        self.typ_1 = typ_1
        self.typ_2 = typ_2

    def __str__(self):
        attacken_namen = ", ".join(a.name for a in self.attacken)
        return (f"{self.spezies} (Typ: {self.typ_1}/{self.typ_2}) | "
                f"Level: {self.Level} | KP: {self.KP} | Attacken: {attacken_namen}")


    def angreifen_spieler(self):
        print(f"attacke_1: {self.attacken[0]} (1 eingeben)")
        print(f"attacke_1: {self.attacken[1]}(2 eingeben)")
        print(f"attacke_1: {self.attacken[2]} (3 eingeben)")
        print(f"attacke_2: {self.attacken[3]} (4 eingeben)")
        while True:
            Angriff = input(f"{pokemon_spieler[0]}\n")
            if not Angriff.isdigit():
                print(f"{Angriff} nicht gefunden!")
                continue
            Angriff = int(Angriff)-1
            attacke = self.attacken[Angriff]
            attacken_typ = self.attacken[Angriff].Typ
            print(f"\n{self.spezies} greift mit {self.attacken[Angriff]} an")
            schaden_ohne_effektivitaet = attacke.Schaden * (self.Level * 0.1)
            attacke.Ladungen -= 1
            return schaden_ohne_effektivitaet, attacken_typ

    def angreifen_gegner(self):
        Angriff = random.randint(1, 3)
        attacke = self.attacken[Angriff]
        attacken_typ = self.attacken[Angriff].Typ
        print(f"\n{self.spezies} greift mit {self.attacken[Angriff]} an")
        schaden_ohne_effektivitaet = attacke.Schaden * (self.Level * 0.1)
        attacke.Ladungen -= 1
        return schaden_ohne_effektivitaet, attacken_typ

    def Schaden_bekommen(self, schaden_ohne_effektivitaet, angriffs_typ):
        #global schaden_ohne_effektivitaet
        effektivitaetsfaktor = 1.0

        #angriffs_typ = attacke.Typ

        if angriffs_typ in effektivitaet:
            if self.typ_1 in effektivitaet[angriffs_typ]:
                effektivitaetsfaktor *= effektivitaet[angriffs_typ][self.typ_1]
            if self.typ_2 != "Leer" and self.typ_2 in effektivitaet[angriffs_typ]:
                effektivitaetsfaktor *= effektivitaet[angriffs_typ][self.typ_2]

        Schaden = schaden_ohne_effektivitaet * effektivitaetsfaktor
        print(f"\nEs macht {Schaden} Schaden an {self.spezies}")
        self.KP -= Schaden

class Glumanda(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Glumanda", KP, Level, attacken, "Feuer", "Leer")


class Schiggy(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Schiggy", KP, Level, attacken, "Wasser", "Leer")



class Bisasam(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Bisasam", KP, Level, attacken, "Pflanze", "Leer")


class Taubsi(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Taubsi", KP, Level, attacken, "Normal", "Leer")


class Raupy(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Raupy", KP, Level, attacken, "Käfer", "Pflanze")

class Gengar(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Gengar", KP, Level, attacken, "Unlicht", "Fee")

class Aquana(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Aquana", KP, Level, attacken, "Wasser", "Leer")

class UHaFnir(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("UHaFnir", KP, Level, attacken, "Flug", "Drache")

class Zoroark(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Zoroark", KP, Level, attacken, "Normal", "Geist")

class Pantimos(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Pantimos", KP, Level, attacken, "Psycho", "Fee")

class Kindwurm(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Kindwurm", KP, Level, attacken, "Drache", "Leer")

class Kosturso(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Kosturso", KP, Level, attacken, "Normal", "Kampf")

class Clavion(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Clavion", KP, Level, attacken, "Stahl", "Fee")

class Castellith(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Castellith", KP, Level, attacken, "Käfer", "Gestein")

class Dummimisel(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Dummimisel", KP, Level, attacken, "Normal", "Leer")

class Hydrapfel(Pokemon):
    def __init__(self, KP, Level, attacken):
        super().__init__("Hydrapfel", KP, Level, attacken, "Pflanze", "Drache")

class Attacke:
    def __init__(self,name, Schaden, Typ, Ladungen, Genauigkeit, Angriffe):
        self.name = name
        self.Schaden = Schaden
        self.Typ = Typ
        self.Ladungen = Ladungen
        self.Genauigkeit = Genauigkeit
        self.Angriffe = Angriffe

    def __str__(self):
        return f"{self.name}"

#Attackendex

Kratzer = Attacke("Kratzer", 40, "Normal", 35, 100, 1)
Tackle = Attacke("Tackle", 40, "Normal", 35, 100, 1)
Ruckzuckhieb = Attacke("Ruckzuckhieb", 40, "Normal", 30, 100, 1)
Bodycheck = Attacke("Bodycheck", 85, "Normal", 15, 100, 1)
Hyperstrahl = Attacke("Hyperstrahl", 150, "Normal", 5, 90, 1)
Donnerblitz = Attacke("Donnerblitz", 95, "Elektro", 15, 100, 1)
Flammenwurf = Attacke("Flammenwurf", 95, "Feuer", 15, 100, 1)
Surfer = Attacke("Surfer", 95, "Wasser", 15, 100, 1)
Eisstrahl = Attacke("Eisstrahl", 95, "Eis", 10, 100, 1)
Solarstrahl = Attacke("Solarstrahl", 120, "Pflanze", 10, 100, 1)
Glut = Attacke("Glut", 40, "Feuer", 35, 100, 1)
Raserei = Attacke("Raserei", 20, "Normal", 20, 100, 1)
Blubber = Attacke("Blubber", 20, "Wasser", 35, 100, 1)
Aquaknarre = Attacke("Aquaknarre", 40, "Wasser", 25, 100, 1)
Biss = Attacke("Biss", 60, "Normal", 22, 100, 1)
Rankenhieb = Attacke("Rankenhieb", 35, "Pflanze", 10, 100, 1)
Rasierblatt = Attacke("Rasierblatt", 55, "Pflanze", 10, 95, 1)
Windstoss = Attacke("Windstoss", 40, "Normal", 35, 100, 1)
Fluegelschlag = Attacke("Fluegelschlag", 35, "Flug", 35, 100, 1)
Schlecker = Attacke("Schlecker", 20, "Geist", 30, 100, 1)
Traumfresser = Attacke("Traumfresser", 100, "Pyscho", 15, 100, 1)
Windschnitt = Attacke("Windschnitt", 60, "Flug", 25, 100, 1)
Klingensturm = Attacke("Klingensturm", 80, "Normal", 10, 100, 1)
Verfolger = Attacke("Verfolger", 40, "Unlicht", 20, 100, 1)
Nachthieb = Attacke("Nachthieb", 70, "Unlicht", 15, 100, 1)
Konfusion = Attacke("Konfusion", 50, "Psycho", 25, 100, 1)
Duplexhieb = Attacke("Duplexhieb", 15, "Normal", 10, 85, 1)
Kopfnuss = Attacke("Kopfnuss", 70, "Normal", 15, 100, 1)
Klammergriff = Attacke("Klammergriff", 15, "Normal", 20, 85, 1)
Feenbrise = Attacke("Feenbrise", 40, "Fee", 30, 100, 1)
Erstauner = Attacke("Estauner", 30, "Geist", 15, 100, 1)
Felswurf = Attacke("Felswurf", 25, "Gestein", 10, 90, 1)
Launenlaser = Attacke("Launenlaser", 80, "Drache", 5, 100, 1)


attacken = [Kratzer, Tackle, Ruckzuckhieb, Bodycheck, Hyperstrahl, Donnerblitz, Flammenwurf, Surfer, Eisstrahl, Solarstrahl]





#Effektivitätstabelle
effektivitaet = {
    "Normal":    {"Gestein": 0.5, "Geist": 0.0, "Stahl": 0.5},
    "Feuer":     {"Feuer": 0.5, "Wasser": 0.5, "Pflanze": 2.0, "Eis": 2.0, "Käfer": 2.0, "Gestein": 0.5, "Drache": 0.5, "Stahl": 2.0},
    "Wasser":    {"Feuer": 2.0, "Wasser": 0.5, "Pflanze": 0.5, "Boden": 2.0, "Gestein": 2.0, "Drache": 0.5},
    "Pflanze":   {"Feuer": 0.5, "Wasser": 2.0, "Pflanze": 0.5, "Gift": 0.5, "Boden": 2.0, "Flug": 0.5, "Käfer": 0.5, "Gestein": 2.0, "Drache": 0.5, "Stahl": 0.5},
    "Elektro":   {"Wasser": 2.0, "Pflanze": 0.5, "Elektro": 0.5, "Boden": 0.0, "Flug": 2.0, "Drache": 0.5},
    "Eis":       {"Wasser": 0.5, "Pflanze": 2.0, "Boden": 2.0, "Flug": 2.0, "Drache": 2.0, "Feuer": 0.5, "Eis": 0.5, "Stahl": 0.5},
    "Kampf":     {"Normal": 2.0, "Eis": 2.0, "Gestein": 2.0, "Unlicht": 2.0, "Stahl": 2.0, "Gift": 0.5, "Flug": 0.5, "Psycho": 0.5, "Käfer": 0.5, "Fee": 0.5, "Geist": 0.0},
    "Gift":      {"Pflanze": 2.0, "Fee": 2.0, "Gift": 0.5, "Boden": 0.5, "Gestein": 0.5, "Geist": 0.5, "Stahl": 0.0},
    "Boden":     {"Feuer": 2.0, "Elektro": 2.0, "Gift": 2.0, "Gestein": 2.0, "Stahl": 2.0, "Pflanze": 0.5, "Käfer": 0.5, "Flug": 0.0},
    "Flug":      {"Pflanze": 2.0, "Kampf": 2.0, "Käfer": 2.0, "Elektro": 0.5, "Gestein": 0.5, "Stahl": 0.5},
    "Psycho":    {"Kampf": 2.0, "Gift": 2.0, "Stahl": 0.5, "Psycho": 0.5, "Unlicht": 0.0},
    "Käfer":     {"Pflanze": 2.0, "Psycho": 2.0, "Unlicht": 2.0, "Feuer": 0.5, "Kampf": 0.5, "Flug": 0.5, "Geist": 0.5, "Stahl": 0.5, "Fee": 0.5},
    "Gestein":   {"Feuer": 2.0, "Eis": 2.0, "Flug": 2.0, "Käfer": 2.0, "Kampf": 0.5, "Boden": 0.5, "Stahl": 0.5},
    "Geist":     {"Geist": 2.0, "Unlicht": 0.5, "Normal": 0.0},
    "Drache":    {"Drache": 2.0, "Stahl": 0.5, "Fee": 0.0},
    "Unlicht":   {"Psycho": 2.0, "Geist": 2.0, "Kampf": 0.5, "Fee": 0.5},
    "Stahl":     {"Eis": 2.0, "Gestein": 2.0, "Fee": 2.0, "Feuer": 0.5, "Wasser": 0.5, "Elektro": 0.5, "Stahl": 0.5},
    "Fee":       {"Kampf": 2.0, "Drache": 2.0, "Unlicht": 2.0, "Feuer": 0.5, "Gift": 0.5, "Stahl": 0.5},
}

#Pokedex

def neues_Glumanda():
    KP = 100
    Level = 1
    attacke_mon = glumanda_attacken
    while len(attacke_mon) < 4:
        attacke_mon = random.sample(attacken, 4)
    return Glumanda(KP, Level, attacke_mon)
glumanda_attacken = [Kratzer, Glut, Flammenwurf,Raserei]

def neues_Schiggy():
    KP = 100
    Level = 1
    attacke_mon = schiggy_attacken
    while len(attacke_mon) < 4:
        attacke_mon = random.sample(attacken, 4)
    return Schiggy(KP, Level, attacke_mon)
schiggy_attacken = [Tackle, Blubber, Aquaknarre, Biss]

def neues_Bisasam():
    KP = 100
    Level = 1
    attacke_mon= []
    while len(attacke_mon) < 4:
        attacke_mon = random.sample(attacken, 4)
    return Bisasam(KP, Level, attacke_mon)
bisasam_attacken = [Tackle, Rankenhieb, Rasierblatt]

def neues_Taubsi():
    KP = 100
    Level = 1
    attacke_mon = taubsi_attacken
    while len(attacke_mon) < 4:
        attacke_mon = random.sample(attacken, 4)
    return Taubsi(KP, Level, attacke_mon)
taubsi_attacken = [Windstoss, Ruckzuckhieb, Fluegelschlag]

def neues_Raupy():
    KP = 100
    Level = 1
    attacke_mon = raupy_attacken
    while len(attacke_mon) < 1:
        attacke_mon = random.sample(attacken, 1)
    return Raupy(KP, Level, attacke_mon)
raupy_attacken = [Tackle]

def neues_Gengar():
    KP = 100
    Level = 1
    attacke_mon = gengar_attacken
    while len(attacke_mon) < 2:
        attacke_mon = random.sample(attacken, 2)
    return Gengar(KP, Level, attacke_mon)
gengar_attacken = [Schlecker, Traumfresser]

def neues_Aquana():
    KP = 100
    Level = 1
    attacke_mon = aquana_attacken
    while len(attacke_mon) < 4:
        attacke_mon = random.sample(attacken, 4)
    return Aquana(KP, Level, attacke_mon)
aquana_attacken = [Aquaknarre, Ruckzuckhieb, Tackle, Biss]

def neues_UHaFnir():
    KP = 100
    Level = 1
    attacke_mon = []
    while len(attacke_mon) < 4:
        attacke_mon = random.sample(attacken, 4)
    return UHaFnir(KP, Level, attacke_mon)
uhafnir_attacken = [Tackle, Windstoss, Windschnitt, Klingensturm]

def neues_Zoroark():
    KP = 100
    Level = 1
    attacke_mon = zoroark_attacken
    while len(attacke_mon) < 3:
        attacke_mon = random.sample(attacken, 3)
    return Zoroark(KP, Level, attacke_mon)
zoroark_attacken = [Kratzer, Verfolger, Nachthieb]

def neues_Pantimos():
    KP = 100
    Level = 1
    attacke_mon = pantimos_attacken
    while len(attacke_mon) < 2:
        attacke_mon = random.sample(attacken, 2)
    return Pantimos(KP, Level, attacke_mon)
pantimos_attacken = [Konfusion, Duplexhieb]

def neues_Kindwurm():
    KP = 100
    Level = 1
    attacke_mon = kindwurm_attacken
    while len(attacke_mon) < 3:
        attacke_mon = random.sample(attacken, 3)
    return Kindwurm(KP, Level, attacke_mon)
kindwurm_attacken = [Raserei, Biss, Kopfnuss]

def neues_Kosturso():
    KP = 100
    Level = 1
    attacke_mon = kosturso_attacken
    while len(attacke_mon) < 2:
        attacke_mon = random.sample(attacken, 2)
    return Kosturso(KP, Level, attacke_mon)
kosturso_attacken =  [Tackle, Klammergriff]

def neues_Clavion():
    KP = 100
    Level = 1
    attacke_mon = clavion_attacken
    while len(attacke_mon) < 3:
        attacke_mon = random.sample(attacken, 3)
    return Clavion(KP, Level, attacke_mon)
clavion_attacken = [Tackle, Feenbrise, Erstauner]

def neues_Castellith():
    KP = 100
    Level = 1
    attacke_mon = castellith_attacken
    while len(attacke_mon) < 1:
        attacke_mon = random.sample(attacken, 1)
    return Castellith(KP, Level, attacke_mon)
castellith_attacken = [Felswurf]

def neues_Dummimisel():
    KP = 100
    Level = 1
    attacke_mon = dummimisel_attacken
    while len(attacke_mon) < 1:
        attacke_mon = random.sample(attacken, 1)
    return Dummimisel(KP, Level, attacke_mon)
dummimisel_attacken = [Raserei]

def neues_Hydrapfel():
    KP = 100
    Level = 1
    attacke_mon = hydrapfel_attacken
    while len(attacke_mon) < 2:
        attacke_mon = random.sample(attacken, 2)
    return Hydrapfel(KP, Level, attacke_mon)
hydrapfel_attacken = [Launenlaser, Erstauner]


moegliche_pokemon = ["glumanda", "schiggy", "bisasam", "taubsi", "raupy", "gengar", "aquana", "uhafnir", "zoroark", "pantimos", "kindwurm", "kosturso", "clavion", "castellith", "dummimisel", "hydrapfel"]

#Spieler

def spieler_pokemon_auswahl():
    while len(Spieler) < 4:
        print(moegliche_pokemon)
        auswahl_pokemon = input(f"\nwelche Pokemon möchtest du in deinem Team?:").lower()
        if auswahl_pokemon in moegliche_pokemon:
            if auswahl_pokemon == "glumanda":
                Spieler.append(neues_Glumanda())
            elif auswahl_pokemon == "schiggy":
                Spieler.append(neues_Schiggy())
            elif auswahl_pokemon == "bisasam":
                Spieler.append(neues_Bisasam())
            elif auswahl_pokemon == "taubsi":
                Spieler.append(neues_Taubsi())
            elif auswahl_pokemon == "raupy":
                Spieler.append(neues_Raupy())
            elif auswahl_pokemon == "gengar":
                Spieler.append(neues_Gengar())
            elif auswahl_pokemon == "aquana":
                Spieler.append(neues_Aquana())
            elif auswahl_pokemon == "uhafnir":
                Spieler.append(neues_UHaFnir())
            elif auswahl_pokemon == "zoroark":
                Spieler.append(neues_Zoroark())
            elif auswahl_pokemon == "pantimos":
                Spieler.append(neues_Pantimos())
            elif auswahl_pokemon == "kindwurm":
                Spieler.append(neues_Kindwurm())
            elif auswahl_pokemon == "kosturso":
                Spieler.append(neues_Kosturso())
            elif auswahl_pokemon == "clavion":
                Spieler.append(neues_Clavion())
            elif auswahl_pokemon == "castellith":
                Spieler.append(neues_Castellith())
            elif auswahl_pokemon == "dummimisel":
                Spieler.append(neues_Dummimisel())
            elif auswahl_pokemon == "hydrapfel":
                Spieler.append(neues_Hydrapfel())
            Kampfanzeige_spieler()

# Spieler Pokemon wechseln

def spieler_pokemon_wechseln():
    while True:
        Kampfanzeige_spieler()
        aktives_pokemon_spieler = input(f"\naktives Pokemon Wählen:")
        if not aktives_pokemon_spieler.isdigit():
            print(f"\nZahl zwischen 1 und {len(Spieler)} wählen")
            continue
        aktives_pokemon_spieler = int(aktives_pokemon_spieler)-1
        if aktives_pokemon_spieler < len(Spieler):
            if len(pokemon_spieler) == 0 :
                pokemon_spieler.append(Spieler[aktives_pokemon_spieler])
                Spieler.pop(aktives_pokemon_spieler)
                Kampfanzeige_spieler()
            else:
                pokemon_spieler.append(Spieler[aktives_pokemon_spieler])
                Spieler.pop(aktives_pokemon_spieler)
                Spieler.append(pokemon_spieler[0])
                pokemon_spieler.pop(0)
                Kampfanzeige_spieler()
            break
        else:
            print(f"Zahl zwischen 1 und {len(Spieler)} wählen")

def spieler_pokemon_besiegt():
    if len(besiegte_pokemon_Spieler) == 4:
        print(f"\nVerloren!")
        time.sleep(5)
        sys.exit()

    else:
        print(f"\n \n \n{pokemon_spieler} (spieler) wurde besiegt\n \n \n")
        pokemon_spieler[0].KP = 0
        besiegte_pokemon_Spieler.append(pokemon_spieler[0])
        pokemon_spieler.pop(0)
        while True:
            aktives_pokemon_spieler = input(f"\naktives Pokemon Wählen:")
            if not aktives_pokemon_spieler.isdigit():
                print(f"Zahl zwischen 1 und {len(Spieler)} wählen")
                continue
            aktives_pokemon_spieler = int(aktives_pokemon_spieler)-1
            if aktives_pokemon_spieler < len(Spieler):
                pokemon_spieler.append(Spieler[aktives_pokemon_spieler])
                Spieler.pop(aktives_pokemon_spieler)
                Kampfanzeige_spieler()
                break
            else:
                print(f"Zahl zwischen 1 und {len(Spieler)} wählen")
                continue


def aktion_spieler():
    Aktion = input(f"\nAngreifen (1) | Pokemon wechseln (2)")
    if Aktion == "1":
        print(f"\nmit was möchtest du angreifen?")
        schaden_typ = pokemon_spieler[0].angreifen_spieler()
        pokemon_gegner[0].Schaden_bekommen(schaden_typ[0],schaden_typ[1])
        Kampfanzeige_spieler()

    elif Aktion == "2":
        spieler_pokemon_wechseln()

    else:
        print("Zahl 1 oder 2 eingeben")
        aktion_spieler()

def Kampfanzeige_spieler():
    Nr = 1
    print(f"\nDein Team:")
    for pokemon in Spieler:
        print(f" {Nr}: {pokemon}")
        Nr += 1
    print(f"\nAktives Pokemon Spieler")
    for pokemon in pokemon_spieler:
        print(pokemon)

#Gegner

def gegner_pokemon_auswahl():
    while len(Gegner) < 4:
        auswahl_gegner = random.choice(moegliche_pokemon)
        if auswahl_gegner == "glumanda":
            Gegner.append(neues_Glumanda())
        elif auswahl_gegner == "schiggy":
            Gegner.append(neues_Schiggy())
        elif auswahl_gegner == "bisasam":
            Gegner.append(neues_Bisasam())
        elif auswahl_gegner == "taubsi":
            Gegner.append(neues_Taubsi())
        elif auswahl_gegner == "raupy":
            Gegner.append(neues_Raupy())
        elif auswahl_gegner == "gengar":
            Gegner.append(neues_Gengar())
    Kampfanzeige_spieler()
#Gegner Pokemon wechseln
def gegner_pokemon_wechseln():
    if len(Gegner) != 1:
        aktives_pokemon_gegner = random.randint(0, len(Gegner)-1)
        pokemon_gegner.append(Gegner[aktives_pokemon_gegner])
        Gegner.pop(aktives_pokemon_gegner)
        Kampfanzeige_gegner()
    else:
        pokemon_gegner.append(Gegner[0])
        Gegner.pop(0)
        Kampfanzeige_gegner()

def aktion_gegener():
    schaden_typ = pokemon_gegner[0].angreifen_gegner()
    pokemon_spieler[0].Schaden_bekommen(schaden_typ[0], schaden_typ[1])
    Kampfanzeige_gegner()

def gegner_pokemon_besiegt():
    global Level
    pokemon_gegner[0].KP = 0
    print(f"\n \n \n{pokemon_gegner[0]} (gegner) wurde besiegt\n \n \n")
    pokemon_spieler[0].Level += 1
    print(f"\nHura! {pokemon_spieler[0]} ist 1 Level aufgestiegen!")
    besiegte_pokemon_Gegner.append(pokemon_gegner[0])
    pokemon_gegner.pop(0)
    if len(besiegte_pokemon_Gegner) == 4:
        Gegner.clear()
        pokemon_gegner.clear()
        besiegte_pokemon_Gegner.clear()
        gegner_pokemon_auswahl()
        gegner_pokemon_wechseln()
        Level += 1
        print(f"Gegner Besiegt, du bist nun in Level {Level}")
        Kampfanzeige_gegner()

    else:
        gegner_pokemon_wechseln()


def Kampfanzeige_gegner():
    Nr = 1
    print(f"\nTeam Des Gegners:")
    for pokemon in Gegner:
        print(f" {Nr}: {pokemon}")
        Nr += 1
    print(f"\nAktives Pokemon Gegner")
    for pokemon in pokemon_gegner:
        print(pokemon)



#Team spieler
Spieler = []
#besiegte Pokemon spieler
besiegte_pokemon_Spieler = []
#aktives Pokemon spieler
pokemon_spieler = []
#Team gegner
Gegner = []
#besiegte Pokemon gegner
besiegte_pokemon_Gegner = []
#aktives Pokemon spieler
pokemon_gegner = []

#Spiel
if __name__ == "__main__":
    spieler_pokemon_auswahl()
    gegner_pokemon_auswahl()
    spieler_pokemon_wechseln()
    gegner_pokemon_wechseln()

while True:

    aktion_spieler()

    if pokemon_gegner[0].KP < 0:
       gegner_pokemon_besiegt()
    else:
        aktion_gegener()

    if pokemon_spieler[0].KP < 0:
        spieler_pokemon_besiegt()

