#Functie om het pensioenbedrag te berekenen
def bereken_pensioen(leeftijd,werkstatuut):
    if werkstatuut == "medewerker":
        pensioen_bedrag = 350
        if leeftijd >= 70:
            pensioen_bedrag += 20
    elif werkstatuut == "zelfstandige":
        pensioen_bedrag = 300
        if leeftijd >= 70:
            pensioen_bedrag += 15
    elif werkstatuut == "ambtenaar":
        pensioen_bedrag = 370
        if leeftijd >= 70:
            pensioen_bedrag += 25

    return pensioen_bedrag

#Functie om het aantal jaren tot aan het pensioen te berekenen
def bereken_resterende_jaren(leeftijd):
    if leeftijd < 65:
        resterende_jaren = 65 - leeftijd
        return f"Van werken word je gelukkig, je mag nog {resterende_jaren} jaar genieten van je baan."
    else:
        return ""

#Hoofdprogramma
leeftijd = int(input("Wat is je leeftijd? Voer het aantal jaren in: "))
werkstatuut = input("Wat is je werkstatuut? Voer in: medewerker, zelfstandige of ambtenaar: ")

resterende_jaren = bereken_resterende_jaren(leeftijd)

if leeftijd >= 65:
    pensioen = bereken_pensioen(leeftijd, werkstatuut)
    print(f"Je krijgt {pensioen} euro pensioen per week.")
    
print(resterende_jaren)