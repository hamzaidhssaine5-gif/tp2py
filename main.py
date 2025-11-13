from ex1 import CompteBancaire
from ex2 import Client

def test_exercice1():
    print("\n===== EXERCICE 1 =====")
    compte = CompteBancaire("Ali", 1000)
    compte.deposer(200)
    compte.retirer(150)
    print(compte)
    print("Solde (lecture) :", compte.solde)
    try:
        compte.solde = 500
    except Exception as e:
        print("Erreur attendue :", e)

def test_exercice2():
    print("\n===== EXERCICE 2 =====")
    cli = Client("Yassir")
    cli.compte.deposer(300)
    cli.compte.retirer(50)
    cli.afficher()

if __name__ == "__main__":
    test_exercice1()
    test_exercice2()
