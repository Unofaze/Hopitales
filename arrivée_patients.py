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

def chambre_libre(dico):
    chambres_libres = []
    for chambre in dico:
        if dico[chambre] == 0:
            chambres_libres.append(chambre)
    return chambres_libres

def nom_patient():
    prenoms = ["Alice", "Bob", "Charlie", "David", "Amélie", "Frank", "Patrick", "Anna", "Erwan", "Julia"]
    noms = ["Dupont", "Martin", "Bernard", "Dubois", "Robert", "Richard", "Thomas", "Petit", "Rossi", "Smith"]
    return random.choice(prenoms) + " " + random.choice(noms)

def stuck_problem():
    thing = ["un 36 tonnes", "un Boeing 747", "un TGV Inoui", "une pastèque", "un câble USB-C vers HDMI", "un bout de peau de pomme", "1 milliard de petit pois", "une poire", "un vélo"]
    body_part = ["dans la gorge", "dans l'oreille", "dans l'anus", "dans l'urètre", "dans l'estomac", "entre les dents"]
    return random.choice(thing) + " coincé " + random.choice(body_part)

class Patient:
    def __init__(self, probleme, gravite_probleme = randint(1, 10), nom = nom_patient(), sprite = pygame.Rect(config.screen_width//2, config.screen_height + config.screen_height * 3/4, 50, 50)):
        self.nom = nom
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
            print("Le patient a", self.probleme)
        elif self.probleme == "un membre à emputer":
            print("Le patient doit se faire emputer un membre ")
        else:
            print("Le patient a ", self.probleme)
        print("La gravité du problème est :", self.gravite_probleme, "sur une échelle de 1 à 10.")

    def message(self):
        return "Bonjour, je m'appelle", self.nom, "Je viens parce que j'ai", self.probleme
        
        
def nouveau_patient():
    patients = config.File()
    clock = pygame.time.Clock()
    debut_temps = pygame.time.get_ticks()
    if chambre_libre(dico_chambre) != []:
        if pygame.time.get_ticks() - debut_temps >= 10000:   # 10000 millisecondes = 10 secondes
            current_patient = Patient()
            patients.enfile(current_patient)
            debut_temps = pygame.time.get_ticks()

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
