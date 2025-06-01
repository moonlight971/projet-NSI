import random  # Importe le module random pour choisir un mot au hasard


def dessinPendu(nb):  # Fonction qui retourne le dessin du pendu selon le nombre d'erreurs
    tab = [
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[nb]  # Retourne le dessin correspondant au nombre d'erreurs


import random

def choix_mot_depuis_liste():
    # Lit les mots depuis un fichier texte
    with open("2_pendu_dico.txt", "r", encoding="utf-8") as fichier:
        mots = fichier.read().splitlines()  # Chaque ligne est un mot
    return random.choice(mots).upper()  # Retourne un mot aléatoire en MAJUSCULES



def verifier_saisie(caractere):  # Vérifie que la saisie est une seule lettre valide
    caractere = caractere.upper()  # Convertit en majuscule
    return caractere.isalpha() and len(caractere) == 1  # Retourne True si c'est une lettre unique


def cacher_mot(mot):  # Remplace chaque lettre du mot par un underscore
    return "_" * len(mot)  # Retourne une chaîne de underscores de la même longueur


def verifier_lettre(mot, caractere):  # Vérifie si la lettre proposée est dans le mot
    return caractere in mot  # Retourne True si la lettre est dans le mot


def nb_erreur(nb):  # Incrémente le compteur d'erreurs
    return nb + 1  # Retourne le nombre d'erreurs +1


def potence(nb_erreurs):  # Affiche le dessin du pendu
    print(dessinPendu(nb_erreurs))  # Affiche le pendu selon le nombre d'erreurs


def lettre(mot_inconnu, mot_cache, caractere):  # Révèle les lettres trouvées dans le mot caché
    nouveau_mot = ""  # Initialise la nouvelle version du mot caché
    for i in range(len(mot_inconnu)):  # Parcourt chaque lettre du mot
        if mot_inconnu[i] == caractere:  # Si la lettre est correcte
            nouveau_mot += caractere  # On ajoute la lettre
        else:
            nouveau_mot += mot_cache[i]  # Sinon on garde l'underscore
    return nouveau_mot  # Retourne le mot mis à jour


def score(nom, points, fichier="scores.txt"):  # Enregistre le score du joueur dans un fichier
    try:
        with open(fichier, "a") as f:  # Ouvre le fichier en mode ajout
            f.write(f"{nom} : {points} points\n")  # Écrit le nom et le score
    except OSError:
        print("️ Impossible d'enregistrer le score (accès fichier refusé).")  # Message d'erreur si problème fichier


def deviner_mot(mot):  # Fonction principale du jeu qui gère les tours
    mot_cache = cacher_mot(mot)  # Mot à deviner masqué
    nb_erreurs = 0  # Compteur d'erreurs
    lettres_utilisées = []  # Liste des lettres déjà proposées

    while "_" in mot_cache and nb_erreurs < 7:  # Tant que le mot n'est pas trouvé et que le joueur n'est pas pendu
        print("\nMot :", " ".join(mot_cache))  # Affiche le mot avec espaces
        potence(nb_erreurs)  # Affiche le pendu
        print("Lettres utilisées :", ", ".join(lettres_utilisées))  # Affiche les lettres déjà utilisées

        lettre_input = input("Propose une lettre : ").upper()  # Demande une lettre

        if not verifier_saisie(lettre_input):  # Vérifie la validité de la saisie
            print("❌ Saisie invalide. Tape une seule lettre A-Z.")
            continue
        if lettre_input in lettres_utilisées:  # Si la lettre a déjà été utilisée
            print("⚠️ Lettre déjà utilisée.")
            continue

        lettres_utilisées.append(lettre_input)  # Ajoute la lettre à la liste des lettres proposées

        if verifier_lettre(mot, lettre_input):  # Si la lettre est correcte
            mot_cache = lettre(mot, mot_cache, lettre_input)  # Met à jour le mot masqué
        else:
            nb_erreurs = nb_erreur(nb_erreurs)  # Incrémente les erreurs
            print(f"❌ Mauvaise lettre ! Il reste {7 - nb_erreurs} tentatives.")

    if "_" not in mot_cache:  # Si le mot est trouvé
        print("\n🎉 Bravo ! Tu as trouvé le mot :", mot)
        return True  # Retourne True = victoire
    else:
        potence(nb_erreurs)  # Affiche le pendu final
        print("💀 Tu es pendu ! Le mot était :", mot)
        return False  # Retourne False = défaite


# ----------- Programme principal ----------
if __name__ == "__main__":  # Exécution du programme principal
    print("🎮 Bienvenue dans le jeu du Pendu 🎮")  # Message d'accueil
    nom_joueur = input("Entre ton nom : ")  # Demande le nom du joueur
    mot = choix_mot_depuis_liste()  # Choisit un mot à deviner

    gagné = deviner_mot(mot)  # Lance le jeu avec le mot choisi

    if gagné:
        score(nom_joueur, 1)  # Enregistre un point si gagné
    else:
        score(nom_joueur, 0)  # Enregistre zéro point si perdu
