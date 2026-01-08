def Afficher_menu():

    print("----------------Menu principal Orange Money----------------")
    print("1- Consulter le solde")
    print("2- Acheter du credit")
    print("3- Effectuer un transfert")
    print("------------------------------------------------------------")


code_ussd = "#144#"
saisie_user = input("Saisir un code: ")


while saisie_user != code_ussd:
    print("veuiller saisir un code valide")
    saisie_user = input("Saisir un code: ")

print(Afficher_menu())

Afficher_menu()






