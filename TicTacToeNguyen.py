feld = [" "," "," "," "," "," "," "," "," "]
spieler = 1

def feld_ausgeben():
    print ("|" + feld[0] + "|" + feld[1] + "|" + feld[2]+ "|")
    print ("|" + feld[3] + "|" + feld[4] + "|" + feld[5]+ "|")
    print ("|" + feld[6] + "|" + feld[7] + "|" + feld[8]+ "|")

def feld_zuruecksetzen():
    i = 0
    while i <= 8:
        feld[i] = " "
        i += 1

def spieler_gewonnen():
    print("Gewonnen!")
    print("Druecken Sie Enter um eine neues Spiel zu starten")
    input()
    feld_zuruecksetzen()
    feld_ausgeben()  

def spieler_unentschieden():  
    print("Unentschieden!")
    print("Druecken Sie Enter um eine neues Spiel zu starten")
    input()
    feld_zuruecksetzen()
    feld_ausgeben()  

def spiel_auswerten():    
    if ((feld[0] == feld[1] == feld[2]) and feld[0] !=  " "):
       spieler_gewonnen()
    elif ((feld[3] == feld[4] == feld[5]) and feld[3] !=  " "):
       spieler_gewonnen()
    elif ((feld[6] == feld[7] == feld[8]) and feld[6] !=  " "): 
       spieler_gewonnen()
    elif ((feld[0] == feld[4] == feld[8]) and feld[0] !=  " "):
       spieler_gewonnen()
    elif ((feld[6] == feld[4] == feld[2]) and feld[6] !=  " "):  
       spieler_gewonnen()
    elif ((feld[0] == feld[3] == feld[6]) and feld[0] !=  " "):
       spieler_gewonnen()
    elif ((feld[1] == feld[4] == feld[7]) and feld[1] !=  " "):  
       spieler_gewonnen()
    elif ((feld[2] == feld[5] == feld[8]) and feld[2] !=  " "):
       spieler_gewonnen()  
    elif (feld[0] != " " and feld[0] != " " and feld[1] != " " and feld[2] != " " and feld[3] != " " and feld[4] != " " and feld[5] != " " and feld[6] != " " and feld[7] != " "  and feld[8] != " "):
       spieler_unentschieden()    

print ("|1|2|3|")
print ("|4|5|6|")
print ("|7|8|9|")   

while True:
    print("Spieler " + str(spieler) + " an der Reihe. Waehlen Sie ein Feld von 1 bis 9 aus:" )
    feldnummer = input()
    try: 
        feldnummer = int(feldnummer)
    except ValueError:
        feldnummer = 0
        
    if (int(feldnummer) >= 1 and int(feldnummer) <= 9):
        if (spieler == 1):
            feld[int(feldnummer) - 1] = "X"
            feld_ausgeben()
            spieler = 2            

        elif (spieler == 2):
            feld[int(feldnummer) - 1] = "O"
            feld_ausgeben()
            spieler = 1
    else:
        print("Ungueltige Zahl geben sie eine Zahl von 1 bis 9 ein")
   