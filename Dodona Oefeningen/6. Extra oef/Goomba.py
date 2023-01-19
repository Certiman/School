#OPNIEUW GEMAAKT DOOR MIJ EN MIJN VADER
#NIET GEBRUIKEN DAN WETEN ZE DIRECT DAT JE KOPIEERDE

# werkt wel
LK = int(input("Lengte van de kamer:"))
A = int(input("Afstand A:"))
B = int(input("Afstand B:"))
TotaleAfstand = (2 * LK - A) #enige berekening, Eenheid is meter
Snelheid = 1 # meter/minuut
Tijd = int(TotaleAfstand / Snelheid) # dus in minuten

print("De laatste Goomba heeft na", Tijd, "minuten de kamer verlaten")
