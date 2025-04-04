### Imports ################################################## 
import os   #per neteja la pantalla
import json

#Variables ###################################################

#Nom del fitxer on desar/carregar dades
nom_fitxer = "alumnes.json" 

# Llista d'alumnes en memòria
alumnes = []

### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla. 
#   
#   Retorna (str): l'opció escollida per l'usuari
##############################################################
def menu():
    #Netejem la pantalla
    os.system('cls')            
    
    #Mostrem les diferents opcions
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")
    
    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    #i retornem l'opció escollida per l'usuari
    return input()

### Funció per carregar dades inicials
def carregar_alumnes():
    if os.path.exists(nom_fitxer):
        with open(nom_fitxer, 'r') as f:
            return json.load(f)
    return []

### Funció per desar dades
def desar_alumnes():
    with open(nom_fitxer, 'w') as f:
        json.dump(alumnes, f, indent=4)

### Funció per obtenir nou ID
def obtenir_id():
    if not alumnes:
        return 1
    return alumnes[-1]['id'] + 1

### Programa ################################################

# Carregar alumnes inicials
alumnes = carregar_alumnes()

#Fins a l'infinit (i més enllà)
while True:
    
    #Executem una opció funció del que hagi escollit l'usuari
    match menu():

        # Mostrar alumnes ##################################
        case "1":
            os.system('cls')
            print("Mostrar alumnes")
            print("-------------------------------")
            
            #Mostrem només ID, nom i cognom de cada alumne
            for alumne in alumnes:
                print(f"ID: {alumne['id']} - {alumne['nom']} {alumne['cognom']}")
            
            input("\nEnter per continuar")
    
        # Afegir alumne ##################################
        case "2":
            os.system('cls')
            print("Afegir alumne")
            print("-------------------------------")
            
            #Demanem dades de l'alumne
            nou_alumne = {
                "id": obtenir_id(),
                "nom": input("Nom: "),
                "cognom": input("Cognom: "),
                "data": {
                    "dia": int(input("Dia naixement: ")),
                    "mes": int(input("Mes naixement: ")),
                    "any": int(input("Any naixement: "))
                },
                "email": input("Email: "),
                "feina": input("Treballa? (s/n): ").lower() == 's',
                "curs": input("Curs: ")
            }
            
            #Afegim a la llista
            alumnes.append(nou_alumne)
            print("\nAlumne afegit correctament")
            input("\nEnter per continuar")
    
        # Veure alumne ##################################
        case "3":
            os.system('cls')
            print("Veure alumne")
            print("-------------------------------")
            
            #Demanem ID de l'alumne
            id_alumne = int(input("Introdueix ID de l'alumne: "))
            
            #Busquem l'alumne
            alumne_trobat = None
            for alumne in alumnes:
                if alumne["id"] == id_alumne:
                    alumne_trobat = alumne
                    break
            
            #Mostrem resultat
            if alumne_trobat:
                print("\nDades completes:")
                print(f"Nom: {alumne_trobat['nom']} {alumne_trobat['cognom']}")
                print(f"Data naixement: {alumne_trobat['data']['dia']}/{alumne_trobat['data']['mes']}/{alumne_trobat['data']['any']}")
                print(f"Email: {alumne_trobat['email']}")
                print(f"Treballa: {'Sí' if alumne_trobat['feina'] else 'No'}")
                print(f"Curs: {alumne_trobat['curs']}")
            else:
                print(f"\nNo existeix alumne amb ID {id_alumne}")
            
            input("\nEnter per continuar")

        # Esborrar alumne ##################################
        case "4":
            os.system('cls')
            print("Esborrar alumne")
            print("-------------------------------")
          
            #Demanem ID de l'alumne a esborrar
            id_alumne = int(input("Introdueix ID de l'alumne: "))
            
            #Busquem i eliminem
            eliminat = False
            for i, alumne in enumerate(alumnes):
                if alumne["id"] == id_alumne:
                    alumnes.pop(i)
                    eliminat = True
                    break
            
            #Mostrem resultat
            if eliminat:
                print("\nAlumne eliminat correctament")
                desar_alumnes()  #Actualitzem fitxer
            else:
                print(f"\nNo existeix alumne amb ID {id_alumne}")
            
            input("\nEnter per continuar")

        # Desar a fitxer ##################################
        case "5":
            os.system('cls')
            print("Desar a fitxer")
            print("-------------------------------")

            #Desem les dades al fitxer
            desar_alumnes()
            print("\nDades desades correctament")
            input("\nEnter per continuar")

        # Llegir fitxer ##################################
        case "6":    
            os.system('cls')
            print("Llegir fitxer")
            print("-------------------------------")

            #Carreguem dades del fitxer
            alumnes = carregar_alumnes()
            print("\nDades carregades correctament")
            input("\nEnter per continuar")

        # Sortir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")

            #Trenquem el bucle infinit
            break

        #Qualsevol altra cosa #####################   
        case _:
            print("\nOpció incorrecta")            
            input()