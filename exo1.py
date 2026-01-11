
deduc_montant = 0
code_secret = "1200"
solde_om = 100000
#========================================MENU PRINCIPAL========================================
def menu():
    print("----------------Menu principal Orange Money----------------")
    print("1- Consulter le solde")
    print("2: Acheter du credit et pass internet")
    print("3: Achat forfait")
    print("4: Effectuer un transfert")
    print("5: Annuler")
    print("9: Retour au menu")
    print("0: Quitter")
    print("------------------------------------------------------------")


#========================================ACHAT CREDIT===============================================
def achat_credit():
    global solde_om
    code_secret = "1200"

    print("Vous allez recharger votre numero.")
    saisie_montant = float(input("Veuillez saisir le montant telephonique que vous souhaitez acheter : "))
    if saisie_montant > solde_om:
        print("Solde insuffisant")
        return  # on arrête la fonction ici

    code = input("Entrez votre code secret pour valider : ")
    if code != code_secret:
        print("Code invalide.")
    else:
        solde_om -= saisie_montant
        print("Code valide.")
        print("Recharge effectuée.")
        print("Nouveau solde :", solde_om)




#==========================================TRANSFERT ET ANNULER TRANSFERT========================================
def Effectuer_transfert():
        global solde_om
        transfert_montant = 0
        choix = ""
        print("Vous allez saisir votre numero.")
        numero = input("Entrez votre numero: ").strip()
        if len(numero)!= 9 or not numero.isdigit():
            print("numero invalide")
            menu()
            return 
            
        transfert_montant = (input("Entrez un montant:"))
        if not transfert_montant.isdigit():
            print("Transaction non autoriser")
            print("9: Acceuill")
            print("0: Quitter")
            choix = input("entrez votre choix :")
        
            if choix == "9":
                  menu()
            elif choix == "0":
                  exit()
            return
            
        transfert_montant = int(transfert_montant)

        if transfert_montant <= 0:
           print("Montant invalide")
           return 


        if transfert_montant > solde_om:
            print("solde inssufissant")
            return
        
        code = input("Entrez votre code secret pour valider : ")
        if code != code_secret:
            print("Code invalide.")
        else:
            solde_om -= transfert_montant
            print(f"le numero destinataire {numero}")
            print(f"MOntant tranferer {transfert_montant}")
            print(f"Solde {solde_om}")
            print("")
            print("0:Annuler")
            annul = input()
            if annul == 0:
                 print("Voulez vous annuler ce transfert ?")
        num= input("Entrez le numero: ")
        print(f"vous voulez annuler le transfert de {num} ")
        confimer = input("Pour annuler une transaction, veuillez saisir votre code secret pour confirmer: ")
        if confimer == "1":
            solde = solde_om + transfert_montant
            solde_om = solde
            print(f"confirmation {confimer}")
            print(f"le numero destinataire {numero}")
            print(f"MOntant tranferer {transfert_montant}")
            print("Votre transfert vers 785070208 a ete annuler")
            print(f"Solde {solde_om}")
            return



#================================ACHAT FORFAIT==========================================================
def pass_1():
    
    print("vous aller acheter le pass jour 100M0 a 500F avec votre compte orange money")
    while True:
        code = input("veuillez saisir votre code secret pour confirmer: ")
        if code != code_secret:
             print(f"Code invalide.")
        elif code == code_secret:
             print("Vous avez activer le pass jour 100MO a 500F")
             break
        else:
             print("erreur veuiller ressayer")

             

def pass_2():
    
    print("vous aller acheter le pass jour 500M0 a 1000F avec votre compte orange money")
    while True:
        code = input("veuillez saisir votre code secret pour confirmer: ")
        if code != code_secret:
             print(f"Code invalide.")
        elif code == code_secret:
             print("Vous avez activer le pass jour 500MO a 1000F")
             break
        else:
             print("erreur veuiller ressayer")


def pass_3():
    
    print("vous aller acheter le pass jour 1G0 a 2000F avec votre compte orange money")
    while True:
        code = input("veuillez saisir votre code secret pour confirmer: ")
        if code != code_secret:
             print(f"Code invalide.")
        elif code == code_secret:
             print("Vous avez activer le pass jour 500MO a 1000F")
             break
        else:
             print("erreur veuiller ressayer")


#=====================================CODE USSD====================================================
def ussd_code():
    code_ussd = "#144#"
    saisie_user = ""
    while True:
         saisie_user = input("Saisir le code USSD: ").strip()
         if saisie_user == code_ussd:
             menu()
             return
         else:
              print("veuiller saisir un code valide")
              


#========================================CHOIX FORFAIT=================================================
def choix_pass():
  

    while True:
        print("1- pass 100 Mo a 500 F")
        print("2: pass 500 Mo a 1000 F")
        print("3: passe 1 Go a 2000 F")
        print("9: Retour au menu")
        print("5: Quitter")
    
        choix = ""
        choix = input("entrez votre choix: ")
        if choix == "1":
            pass_1()
        elif choix == "2":
                pass_2()
        elif choix == "3":
                pass_3()
        elif choix == "9":
                menu()
        elif choix == "5":
                exit()
        else:
            print("erreur veuiller entrez les chiffres en 1 rt 5")

#=======================================CHOIX MENU PRINCIPAL========================================================
def menu_solde():
     
     ussd_code()

    
     while True:
            choix = ""
            choix = input("Entrez votre choix: ")
            if choix == "1":
                print(f"votre solde est : {solde_om}")
            elif choix == "2":
                achat_credit()
            elif choix == "3":
                 choix_pass()
            elif choix == "4":
                 Effectuer_transfert()
            elif choix == "9":
                    menu()
            elif choix == "0":
                    exit()
            else:
                print("Votre choix est invalide veuillez saisir les chiffres et 1 et 3")
menu_solde()
 







