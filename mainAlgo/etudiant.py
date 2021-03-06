# -*- coding: utf-8 -*-
class Etudiant(object):
    """Représentation d'un étudiant et de ses capacités    """

    def __init__(self, nId, prenom, nom, niveauxCompetences={}, resultats={}):
        self.nId = nId
        self.prenom = prenom
        self.nom = nom
        self.niveauxCompetences = niveauxCompetences ## {1:theta_1, 2:theta_2, ...}
        if niveauxCompetences=={}:
            for i in range (1,174):
                if not i==172:
                    self.niveauxCompetences[i]=0
        self.resultats = resultats ## {ex.idNb: -1 non repondue, 0 faux ou 1 juste}
        
    def getNiveau(self, competenceId):
        return self.niveauxCompetences[competenceId]
        
    def setNiveaux(self, niveaux):
        self.niveauxCompetences = {}
        self.niveauxCompetences=niveaux
 
    def getCompetences(self):
        return self.niveauxCompetences
        
    def majResultat(self, dict):
        self.resultats.update(dict)
    
