import pygame
import time
import random
from random import randint
import config

sprites_patients = [
    pygame.image.load("hopital pour projet nsi/fps/client 1/c1b.png").convert_alpha(),
    pygame.image.load("hopital pour projet nsi/fps/client 1/c1g.png").convert_alpha(),
    pygame.image.load("hopital pour projet nsi/fps/client 1/c1o.png").convert_alpha(),
    pygame.image.load("hopital pour projet nsi/fps/client 1/c1r.png").convert_alpha(),
    pygame.image.load("hopital pour projet nsi/fps/client 2/c2r.png").convert_alpha(),
    pygame.image.load("hopital pour projet nsi/fps/client riche/cr.png").convert_alpha()
]

bulles_patients = [
    pygame.image.load("hopital pour projet nsi/fps/client 1/bulle client 1.png").convert_alpha(),
    pygame.image.load("hopital pour projet nsi/fps/client 2/bulle client 2.png").convert_alpha(),
    pygame.image.load("hopital pour projet nsi/fps/client riche/crb.png").convert_alpha()
]

def dico_chambre():
    '''
    Crée un dictionnaire représentant les chambres de l'hôpital (clés du dictionnaire).
    Chaque chambre a une valeur associée de 0, ce qui signifie qu'elle est libre. (elle vaut 1 si elle est occupée)
    '''
    chambres = {}
    for i in range(1, 21):
        chambres[i] = 0
    return chambres
    
def nom_patient():
    prenoms = ["Alice", "Bob", "Charlie", "David", "Amélie", "Frank", "Patrick", "Anna", "Erwan", "Julia"]
    noms = ["Dupont", "Martin", "Bernard", "Dubois", "Robert", "Richard", "Thomas", "Petit", "Rossi", "Smith"]
    return random.choice(prenoms) + " " + random.choice(noms)

def stuck_problem():
    thing = ["un 36 tonnes", "un Boeing 747", "un TGV Inoui", "une pastèque", "un câble USB-C vers HDMI", "un bout de peau de pomme", "1 milliard de petit pois", "une poire", "un vélo"]
    body_part = ["dans la gorge", "dans l'oreille", "dans l'anus", "dans l'urètre", "dans l'estomac", "entre les dents"]
    return random.choice(thing) + " coincé " + random.choice(body_part)

def sprite_patient(sprites_list):
    return sprites_list[randint(0, len(sprites_list) - 1)]

class Patient:
    def __init__(self, gravite_probleme = randint(1, 10)):
        self.nom = nom_patient()
        self.gravite_probleme = gravite_probleme
        self.sprite = sprite_patient(sprites_patients)

        if self.sprite in sprites_patients[0:4]:
            self.type_client = "client 1"
        elif self.sprite == sprites_patients[4]:
            self.type_client = "client 2"
        else:
            self.type_client = "client riche"

        if self.gravite_probleme <= 2:
            self.probleme = "un contrôle à faire"
        elif self.gravite_probleme == 3:
            self.probleme = stuck_problem()
        elif self.gravite_probleme <= 6:
            self.probleme = random.choice(["une blessure superficielle", "une entorse", "une déchirure musculaire"])
        elif self.gravite_probleme <= 9:
            self.probleme = random.choice(["une fracture", "une fracture ouverte","une hémorragie interne"])
        else:
            self.probleme = "un membre à emputer"
            
    def get_probleme(self):
        return self.probleme

    def get_gravite_probleme(self):
        return self.gravite_probleme

    def set_probleme(self, new_probleme):
        self.probleme = new_probleme     

    def set_gravite_probleme(self, new_gravite_probleme):
        self.gravite_probleme = new_gravite_probleme

# ! Ne surtout pas supprimer, je vais la mettre à un autre endroit!

#    # Méthode pour afficher les détails du patients
#    def afficher_details(self):
#        if self.probleme == "un contrôle à faire":
#            config.afficher_texte("Le patient a" + self.probleme, config.screen_width*3/4, config.screen_height//2, config.screen_width*3/4+100, (0, 0, 0))
#        elif self.probleme == "un membre à emputer":
#            config.afficher_texte("Le patient doit se faire emputer un membre ", config.screen_width*3/4, config.screen_height//2, config.screen_width*3/4+100, (0, 0, 0))
#        else:
#            config.afficher_texte("Le patient a " + self.probleme, config.screen_width*3/4, config.screen_height//2, config.screen_width*3/4+100, (0, 0, 0))
#        config.afficher_texte("La gravité du problème est :" + str(self.gravite_probleme) + " sur une échelle de 1 à 10.", config.screen_width*3/4, config.screen_height//2 + 50, config.screen_width*3/4+100, (0, 0, 0))

    def message(self):
        return f"Bonjour, je m'appelle {self.nom}. Je viens parce que j'ai {self.probleme}"

class GestionnaireHospitalier:
    def __init__(self, delai_arrivee_ms):
        self.file_d_attente = config.File()
        self.patient_en_cours = None
        self.chambres = dico_chambre()
        self.patients_en_soin = []

        self.delai_arrivee_ms = delai_arrivee_ms
        self.dernier_ajout_ms = pygame.time.get_ticks()

        self.fond_salle_d_attente = pygame.image.load("hopital pour projet nsi/fps/salle d'attente.png").convert_alpha()
        self.bureau = pygame.image.load("hopital pour projet nsi/fps/bureau.png").convert_alpha()

    def get_delai_arrivee_ms(self):
        return self.delai_arrivee_ms

    def get_file_d_attente(self):
        return self.file_d_attente

    def get_patient_en_cours(self):
        return self.patient_en_cours

    def get_chambres(self):
        return self.chambres

    def get_patients_en_soin(self):
        return self.patients_en_soin

    def set_delai_arrivee_ms(self, new_delai):
        self.delai_arrivee_ms = new_delai

    def set_chambres(self, new_chambres):
        self.chambres = new_chambres

    def chambres_libres(self):
        chambres_disponibles = []
        for chambre in self.chambres:
            if self.chambres[chambre] == 0:
                chambres_disponibles.append(chambre)
        return chambres_disponibles

    def premiere_chambre_libre(self):
        for chambre in self.chambres:
            if self.chambres[chambre] == 0:
                return chambre
        return None

    def nouveau_patient_dans_la_file_d_attente(self, maintenant_ms):
        if self.chambres_libres() != [] and maintenant_ms - self.dernier_ajout_ms >= self.delai_arrivee_ms:
            self.file_d_attente.enfile(Patient())
            self.dernier_ajout_ms = maintenant_ms
        else:
            return None

    def assigner_patient_a_chambre(self, num_chambre):
        if self.patient_en_cours is not None and self.chambres[num_chambre] == 0:
            self.chambres[num_chambre] = 1
            self.patients_en_soin.append(self.patient_en_cours)
            self.patient_en_cours = None
        else:
            return None

    def mettre_a_jour_accueil(self, maintenant_ms=None):
        if maintenant_ms is None:
            maintenant_ms = pygame.time.get_ticks()

        self.nouveau_patient_dans_la_file_d_attente(maintenant_ms)

        if self.patient_en_cours is None and not self.file_d_attente.est_vide():
            self.patient_en_cours = self.file_d_attente.defile()

    def draw_salle_d_attente(self):
        config.screen.fill(config.COULEUR_FOND)

        fond_scaled = config.scale_fit(self.fond_salle_d_attente, config.screen_width, config.screen_height)
        rect_scene = fond_scaled.get_rect(center=(config.screen_width // 2, config.screen_height // 2))
        config.screen.blit(fond_scaled, rect_scene.topleft)

        if self.patient_en_cours is not None:
            # Taille max 2 fois plus grande que les proportions de référence, sans déformation
            max_w = rect_scene.width
            max_h = rect_scene.height
            sprite_scaled = config.scale_fit(self.patient_en_cours.sprite, max_w, max_h)

            sprite_rect = sprite_scaled.get_rect()
            sprite_rect.x = rect_scene.x + rect_scene.width
            sprite_rect.bottom = rect_scene.bottom
            sprite_rect.right = min(sprite_rect.right, rect_scene.right)
            config.screen.blit(sprite_scaled, sprite_rect.topleft)

            if self.patient_en_cours.type_client == "client 1":
                bulle_img = bulles_patients[0]
            elif self.patient_en_cours.type_client == "client 2":
                bulle_img = bulles_patients[1]
            elif self.patient_en_cours.type_client == "client riche":
                bulle_img = bulles_patients[2]

            bulle_scaled = config.scale_fit(bulle_img, rect_scene.width, rect_scene.height)
            bulle_rect = bulle_scaled.get_rect()
            bulle_rect.topleft = rect_scene.topleft
            config.screen.blit(bulle_scaled, bulle_rect.topleft)

            cadre_de_texte = pygame.Rect(rect_scene.width * 30 / 180, rect_scene.height * 22 / 109, rect_scene.width * 70 / 180, rect_scene.height * 32 / 109)
            texte_x = cadre_de_texte.x
            texte_y = cadre_de_texte.y
            maxi_texte = cadre_de_texte.x + cadre_de_texte.width
            config.afficher_texte(self.patient_en_cours.message(), texte_x, texte_y, maxi_texte, (0, 0, 0))

        bureau_scaled = config.scale_fit(self.bureau, rect_scene.width, rect_scene.height)
        bureau_rect = bureau_scaled.get_rect(midbottom=rect_scene.midbottom)
        config.screen.blit(bureau_scaled, bureau_rect.topleft)