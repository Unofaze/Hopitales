import pygame
import time
import random
from random import randint




class Patient:
    def __init__(self, probleme, gravite_probleme = randint(1, 10)):
        self.gravite_probleme = gravite_probleme
        if self.gravite_probleme <= 2:
            self.probleme = "contrôle"
        elif self.gravite_probleme == 3:
            self.probleme = "quelque chose coincé quelque part"
        elif self.gravite_probleme <= 6:
            self.probleme = randint("blessure superficielle", "entorse", "déchirure musculaire")
        elif self.gravite_probleme <= 9:
            self.probleme = randint("fracture", "fracture ouverte","hémorragie interne")
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
    pass
    
        
        