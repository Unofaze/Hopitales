import pygame
import time
import random
from random import randint
import config

def dico_chambre():
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

class Patient:
    def __init__(self, probleme, gravite_probleme = randint(1, 10), sprite = pygame.Rect(config.screen_width//2, config.screen_height + config.screen_height * 3/4, 50, 50)):
        self.nom = nom_patient()
        self.gravite_probleme = gravite_probleme
        self.sprite = sprite
        self.probleme = probleme

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

    # Méthode pour afficher les détails du patients
    def afficher_details(self):
        if self.probleme == "un contrôle à faire":
            config.afficher_texte("Le patient a" + self.probleme, config.screen_width*3/4, config.screen_height//2, config.screen_width*3/4+100, (0, 0, 0))
        elif self.probleme == "un membre à emputer":
            config.afficher_texte("Le patient doit se faire emputer un membre ", config.screen_width*3/4, config.screen_height//2, config.screen_width*3/4+100, (0, 0, 0))
        else:
            config.afficher_texte("Le patient a " + self.probleme, config.screen_width*3/4, config.screen_height//2, config.screen_width*3/4+100, (0, 0, 0))
        config.afficher_texte("La gravité du problème est :" + str(self.gravite_probleme) + " sur une échelle de 1 à 10.", config.screen_width*3/4, config.screen_height//2 + 50, config.screen_width*3/4+100, (0, 0, 0))

    def message(self):
        return "Bonjour, je m'appelle", self.nom, "Je viens parce que j'ai", self.probleme
        
class GestionnaireHospitalier:
    def __init__(self, delai_arrivee_ms=10000):  # 10000 millisecondes = 10 secondes
        self.file_d_attente = config.File()
        self.patient_en_cours = None
        self.chambres = dico_chambre()
        self.patients_en_soin = []

        self.delai_arrivee_ms = delai_arrivee_ms
        self.dernier_ajout_ms = pygame.time.get_ticks()

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


def draw(patients):
    '''
    Fonction qui affiche le patient et pourquoi il vient à l"hôpital.

    Paramètres:
    patients : une liste d'instances de la classe Patient
    '''
    assert type(patients) == list, "Le paramètre patients doit être une liste."
    for patient in patients:
        assert isinstance(patient, Patient), "Chaque élément de la liste patients doit être une instance de la classe Patient."

    for patient in patients:
        if patient.etat() == "en attente":
            pygame.draw.rect(config.screen, (randint(0, 255), randint(0, 255), randint(0, 255)), patient.sprite)
            config.afficher_texte(patient.message(), config.screen_width*3/4, config.screen_height//2, config.screen_width*3/4+100, (0, 0, 0))
