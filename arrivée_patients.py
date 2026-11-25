import pygame
import time
import random
from random import randint
import config

def dico_chambre():
    chambres = {}
    for i in range(1, 21):
        chambres[chambre[i]] = 0
    return chambres

def chambre_libre(dico):
    chambres_libres = []
    for chambre in dico:
        if dico[chambre] == 0:
            chambres_libres.append(chambre)
    return chambres_libre

def nom_patient():
prenoms = ["Alice", "Bob", "Charlie", "David", "Amélie", "Frank", "Patrick", "Anna", "Erwan", "Julia"]
noms = ["Dupont", "Martin", "Bernard", "Dubois", "Robert", "Richard", "Thomas", "Petit", "Rossi", "Smith"]
return random.choice(prenoms) + random.choice(noms)


class Patient:
    def __init__(self, probleme, gravite_probleme = randint(1, 10), nom = nom_patient(), sprite = pygame.rect(config.screen_width//2, config.screen_height//2, 50, 50)):
        self.nom = nom
        self.gravite_probleme = gravite_probleme
        self.sprite = sprite
        if self.gravite_probleme <= 2:
            self.probleme = "contrôle"
        elif self.gravite_probleme == 3:
            self.probleme = "quelque chose coincé quelque part"
        elif self.gravite_probleme <= 6:
            self.probleme = random.choice(["blessure superficielle", "entorse", "déchirure musculaire"])
        elif self.gravite_probleme <= 9:
            self.probleme = random.choice(["fracture", "fracture ouverte","hémorragie interne"])
        else:
            self.probleme = "membre à emputer"
        
        
    def get_probleme(self):
        return self.probleme

    def get_gravite_probleme(self):
        return self.gravite_probleme

    def set_probleme(self, new_probleme):
        self.probleme = self.new_probleme
        

    def set_gravite_probleme(self, new_gravite_probleme):
        self.gravite_probleme = new_gravite_probleme

    # Méthode pour afficher les détails du compte
    def afficher_details(self):
        if self.probleme == "contrôle":
            print("Le patient doit réaliser un ", self.probleme)
        elif self.probleme == "entorse" or self.probleme == "hémorragie interne":
            print("Le patient souffre d'une ", self.probleme)
        elif self.probleme == "membre à emputer":
            print("Le patient doit se faire emputer un membre ")
        else:
            print("Le patient souffre de ", self.probleme)
        print("La gravité du problème est :", self.gravite_probleme, "sur une échelle de 1 à 10.")
        
        
def nouveau_patient():
    clock = pygame.time.Clock()
    debut_temps = pygame.time.get_ticks()
    patient0 = Patient()
    if chambre_libre(dico_chambre) != []:
        if pygame.time.get_ticks() - debut_temps >= 10000:   # 10000 millisecondes = 10 secondes
            patient = Patient()
    











        
        