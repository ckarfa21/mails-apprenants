from data_base import data_base
from read_file import read_file
from apprenants import apprenants
from email.utils import parseaddr

def main():
    file1 = read_file("apprenantmail.txt")
    mails = file1.lignes
    bdd1 = data_base()
    promo = bdd1.read_db()
    for apprenant in promo:
        nom = str(apprenant.prenom.lower() + "." + apprenant.nom.lower().replace(" ","-").replace("'",""))
        for mail in mails:
            if nom in parseaddr(mail)[1]:
                apprenant.mail = mail
    #bdd1.create()

    for apprenants in promo :
        bdd1.envoie(apprenants.mail,apprenants.id)

    bdd1.fermer()




main()



#comparé deux chaine de caratère, en minuscule
#contaténé nom prenom sans caractère sepciaux et de comparé ensuite

#générer a partir de la table apprenants un objet de classe apprenants, en stockant id, nom, prénom, et mail(vide)
#une fois le test fait on pourra metre l'adresse mail en base

#ALTER TABLE apprenants ADD COLUMN mail VARCHAR(100)