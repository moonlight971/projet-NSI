# === IMPORTATION DES BIBLIOTHÈQUES ===
import pygame  # Pygame sert à créer des jeux ou des interfaces graphiques interactives
import sys     # Permet de gérer les erreurs système ou de quitter proprement le programme
import os      # Permet de travailler avec les fichiers et les chemins

# === INITIALISATION DE PYGAME ===
pygame.init()  # Démarre tous les modules nécessaires de Pygame (comme l'affichage, l'audio, etc.)

# === CONFIGURATION DE LA FENÊTRE ===
largeur, hauteur = 800, 600  # Dimensions de la fenêtre du jeu (largeur = 800px, hauteur = 600px)
ecran = pygame.display.set_mode((largeur, hauteur))  # Crée la fenêtre avec les dimensions spécifiées
pygame.display.set_caption("Menu Culturel")  # Définit le titre de la fenêtre du jeu
font = pygame.font.SysFont(None, 50)  # Déclare la police utilisée pour le texte (taille 50px)
clock = pygame.time.Clock()  # Crée un objet "clock" pour réguler le nombre d'images par seconde (FPS)

# === DÉFINITION DES COULEURS ===
BLANC = (255, 255, 255)  # Couleur blanche en RGB
NOIR = (0, 0, 0)  # Couleur noire en RGB
BLEU = (100, 149, 237)  # Couleur bleue en RGB (pour les boutons)
GRIS = (220, 220, 220)  # Couleur grise en RGB (pour les boutons)

# === CHARGEMENT MANUEL DES IMAGES POUR LES CATEGORIES PEINTURE ET FILM ===
# Peinture
img_guweiz = pygame.image.load("guweiz.jpg")  # Charge l'image "guweiz.jpg"
img_guweiz = pygame.transform.scale(img_guweiz, (largeur, hauteur))  # Redimensionne l'image à la taille de la fenêtre

img_nuit = pygame.image.load("nuit.jpg")  # Charge l'image "nuit.jpg"
img_nuit = pygame.transform.scale(img_nuit, (largeur, hauteur))  # Redimensionne l'image à la taille de la fenêtre

img_liberte = pygame.image.load("liberté.jpg")  # Charge l'image "liberté.jpg"
img_liberte = pygame.transform.scale(img_liberte, (largeur, hauteur))  # Redimensionne l'image à la taille de la fenêtre

# Film
img_avatar = pygame.image.load("avatar.jpg")  # Charge l'image "avatar.jpg"
img_avatar = pygame.transform.scale(img_avatar, (largeur, hauteur))  # Redimensionne l'image à la taille de la fenêtre

img_siperman = pygame.image.load("siperman.png")  # Charge l'image "siperman.jpg"
img_siperman = pygame.transform.scale(img_siperman, (largeur, hauteur))  # Redimensionne l'image à la taille de la fenêtre

img_titanic = pygame.image.load("titanic.jpg")  # Charge l'image "titanic.jpg"
img_titanic = pygame.transform.scale(img_titanic, (largeur, hauteur))  # Redimensionne l'image à la taille de la fenêtre

# === CRÉATION DES LISTES D'IMAGES POUR CHAQUE CATEGORIE ===
# Liste des images pour la catégorie Peinture
images_peinture = [
    {"surface": img_guweiz, "nom": "guweiz.jpg"},  # Dictionnaire contenant l'image "guweiz" et son nom
    {"surface": img_nuit, "nom": "nuit.jpg"},      # Dictionnaire contenant l'image "nuit" et son nom
    {"surface": img_liberte, "nom": "liberté.jpg"} # Dictionnaire contenant l'image "liberté" et son nom
]

# Liste des images pour la catégorie Film
images_film = [
    {"surface": img_avatar, "nom": "avatar.jpg"},   # Dictionnaire contenant l'image "avatar" et son nom
    {"surface": img_siperman, "nom": "siperman.png"}, # Dictionnaire contenant l'image "siperman" et son nom
    {"surface": img_titanic, "nom": "titanic.jpg"}  # Dictionnaire contenant l'image "titanic" et son nom
]

# === FONCTION POUR AFFICHER LES IMAGES D'UNE CATEGORIE ===
def afficher_images(images):
    """
    Affiche les images de la catégorie donnée dans une boucle.
    Permet de passer d'une image à l'autre en cliquant.
    """
    index = 0  # Position actuelle dans la liste des images (commence à l'image 0)
    affichage = True  # Variable de contrôle de la boucle d'affichage
    while affichage:  # Boucle principale pour afficher les images
        for event in pygame.event.get():  # Gère tous les événements (clavier, souris, etc.)
            if event.type == pygame.QUIT:  # Si l'utilisateur ferme la fenêtre
                pygame.quit()  # Ferme Pygame
                sys.exit()  # Quitte le programme

            if event.type == pygame.KEYDOWN:  # Si une touche est enfoncée
                if event.key == pygame.K_SPACE:  # Si la touche "Espace" est pressée
                    affichage = False  # Quitte la boucle et revient au menu

            if event.type == pygame.MOUSEBUTTONDOWN:  # Si un clic de souris est détecté
                index = (index + 1) % len(images)  # Passe à l'image suivante dans la liste (boucle)

        ecran.blit(images[index]["surface"], (0, 0))  # Affiche l'image courante dans la fenêtre (position (0, 0))

        # Affiche le nom de l'image en haut de l'écran
        texte_nom = font.render(images[index]["nom"], True, NOIR)  # Crée une surface de texte
        fond = pygame.Surface((largeur, 60))  # Crée une surface blanche pour le fond du texte
        fond.set_alpha(160)  # Rend le fond légèrement transparent
        fond.fill((255, 255, 255))  # Remplit le fond de la couleur blanche
        ecran.blit(fond, (0, 0))  # Affiche le fond à l'écran
        ecran.blit(texte_nom, (largeur // 2 - texte_nom.get_width() // 2, 15))  # Affiche le texte centré en haut

        pygame.display.update()  # Met à jour l'écran pour afficher les changements
        clock.tick(60)  # Limite la fréquence d'images à 60 images par seconde

# === FONCTION POUR CRÉER UN BOUTON DANS LE MENU ===
def bouton(texte, x, y, l, h, action=None):
    """
    Crée un bouton cliquable avec du texte.
    Si le bouton est cliqué, une action est exécutée.
    """
    souris = pygame.mouse.get_pos()  # Récupère la position actuelle de la souris
    clic = pygame.mouse.get_pressed()  # Récupère les boutons de la souris actuellement enfoncés

    # Vérifie si la souris est au-dessus du bouton
    if x < souris[0] < x + l and y < souris[1] < y + h:
        pygame.draw.rect(ecran, BLEU, (x, y, l, h))  # Affiche le bouton en surbrillance (bleu)
        if clic[0] == 1 and action:  # Si le bouton gauche de la souris est cliqué
            pygame.time.wait(150)  # Attends 150ms pour éviter plusieurs clics rapides
            action()  # Exécute l'action liée au bouton (comme afficher les images)
    else:
        pygame.draw.rect(ecran, GRIS, (x, y, l, h))  # Affiche le bouton dans son état normal (gris)

    # Affiche le texte du bouton au centre
    texte_rendu = font.render(texte, True, NOIR)  # Crée une surface avec le texte
    ecran.blit(texte_rendu, (x + 20, y + 10))  # Affiche le texte dans le bouton

# === FONCTIONS D'ACTION POUR LES BOUTONS ===
def peinture():
    afficher_images(images_peinture)  # Affiche les images de la catégorie "Peinture"

def film():
    afficher_images(images_film)  # Affiche les images de la catégorie "Film"

def quitter():
    pygame.quit()  # Ferme Pygame
    sys.exit()  # Quitte le programme

# === FONCTION PRINCIPALE DU MENU ===
def menu():
    """
    Affiche le menu principal avec deux boutons (Peinture et Film).
    Attend que l'utilisateur clique sur un bouton pour afficher les images.
    """
    while True:
        ecran.fill(BLANC)  # Efface l'écran en blanc à chaque itération

        # Crée les boutons dans le menu
        bouton("Peinture", 300, 150, 200, 60, peinture)  # Bouton "Peinture"
        bouton("Film", 300, 250, 200, 60, film)  # Bouton "Film"

        for event in pygame.event.get():  # Vérifie les événements
            if event.type == pygame.QUIT:  # Si l'utilisateur ferme la fenêtre
                quitter()  # Quitte le programme

        pygame.display.update()  # Met à jour l'écran avec les boutons affichés
        clock.tick(60)  # Limite la fréquence d'images à 60 FPS

# === LANCEMENT DU MENU PRINCIPAL ===
menu()  # Appelle la fonction pour afficher le menu
