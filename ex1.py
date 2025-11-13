class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant

    @property
    def solde(self):
        return self.__solde

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"
