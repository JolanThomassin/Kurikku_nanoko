from tkinter import *
import time
import random

class Jeux() :
	def __init__(self):
		### Paramètres ###
		self.LargeurEcran = 1080
		self.HauteurEcran = 720 
		self.EcranDeJeux = Tk()
		self.EcranDeJeux.title("Kurikku nanoko")
		self.EcranDeJeux.geometry("1080x720+200+40")
		self.EcranDeJeux.iconbitmap("miku.ico")
		self.EcranDeJeux.resizable(width=0, height=0)
		self.CanvaUn = Canvas(self.EcranDeJeux, width=self.LargeurEcran, height=self.HauteurEcran, bg="black")
		self.CanvaUn.pack()

		### Variables ###
		self.InGame = False
		self.argent = 0
		self.argentTotal = 0
		self.niveauQuete = 0
		
		### Prix ###
		self.weeb = 0
		self.prixWeeb = 5

		### Waifu ###
		self.nombreWaifu = 0
		self.imageRessource = PhotoImage(file="boutonBoutique/boutonRessource.png")
		self.imageWaifu = PhotoImage(file="boutonBoutique/boutonWaifu.png")
		self.imageCaisse = PhotoImage(file="boutonBoutique/boutonCaisse.png")
		self.imageCollection = PhotoImage(file="boutonBoutique/boutonCollection.png")
		self.imageStats = PhotoImage(file="boutonBoutique/boutonStats.png")
		self.imageQuête = PhotoImage(file="boutonBoutique/boutonQuête.png")
		self.imageCode = PhotoImage(file="boutonBoutique/boutonCode.png")
		self.imageCode = PhotoImage(file="boutonBoutique/boutonCode.png")
		self.imageMilitaire = PhotoImage(file="boutonBoutique/boutonMilitaire.png")
				
		### Waifu un ###
		self.imageWaifuUnNoir = PhotoImage(file="waifu/waifuUnPetitNoir.png")
		self.imageWaifuUnColor = PhotoImage(file="waifu/waifuUnPetitColor.png")
		self.waifuUn = False
		self.puissanceClique = 1
		self.waifuUnNiveau = 1
		self.waifuUnPrixNiveau = 5000

		### Waifu deux ###
		self.imageWaifuDeuxNoir = PhotoImage(file="waifu/waifuDeuxPetitNoir.png")
		self.imageWaifuDeuxColor = PhotoImage(file="waifu/waifuDeuxPetitColor.png")
		self.waifuDeux = False
		self.bonusWaifuDeux = 1
		self.waifuDeuxNiveau = 1
		self.waifuDeuxPrixNiveau = 10000

		### Waifu code ###
		self.imageWaifuCodeNoir = PhotoImage(file="waifu/waifuCodePetitNoir.png")
		self.imageWaifuCodeColor = PhotoImage(file="waifu/waifuCodePetitColor.png")
		self.waifuCode = False
		self.waifuCodeNiveau = 1
		self.waifuCodePrixNiveau = 2500

		### Millitaire ###
		self.waifuUnPuissance = 100
		self.waifuUnEquipé = False
		self.waifuDeuxPuissance = 200
		self.waifuDeuxEquipé = False
		self.waifuCodePuissance = 150
		self.waifuCodeEquipé = False
		self.manche = 0
		self.puissanceEnnemi = 500
		self.puissanceAllié = 500
		self.facteurAllié = 5
		self.facteurEnnemi = 15

		### Cosmétique ###
		self.LunetteCommunPossession = False
		self.LunetteCommunÉquipé = False
		self.CasquetteCommunPossession = False
		self.CasquetteCommunÉquipé = False
		self.MasqueCommunPossession = False
		self.MasqueCommunÉquipé = False
		self.BoucleOreilleCommunPossession = False
		self.BoucleOreilleCommunÉquipé = False
		self.YeuxRougeRarePossession = False
		self.YeuxRougeRareÉquipé = False 
		self.ShibaRarePossession = False
		self.ShibaRareÉquipé = False
		self.TailsÉpiquePossession = False
		self.TailsÉpiqueÉquipé = False
		self.LégendairePossession = False
		self.LégendaireÉquipé = False

		### Codes ###
		self.codeUn = False
		self.codeDeux = False

		### Caisse de Skin ###
		self.prixCaisse = 5000
		self.compteur = 0
		self.résultatPrécédent = random.randint(0, 99) 
		self.résultatActuel = random.randint(0, 99) 
		self.résulatSuivant = random.randint(0, 99)  
		self.résultatActuelString = ""
		self.couleurRésultatActuel = ""
		self.contenuCaisse = [
		"Lunette", "Lunette", "Lunette", "Lunette", "Lunette", "Lunette", "Lunette", "Lunette", "Lunette", "Lunette", 
		"Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", 
		"Masque", "Lunette", "Masque", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", 
		"Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", 
		"Boucle d'oreilles", "Boucle d'oreilles", "Lunette", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", 
		"Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", 
		"Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", 
		"Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Shiba", "Shiba", "Shiba", "Shiba", 
		"Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", 
		"Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Légendaire"]

		self.contenuCaisseAmélioré = [
		"Légendaire", "Légendaire", "Légendaire", "Légendaire", "Légendaire", "Légendaire", "Lunette", "Lunette", "Lunette", "Lunette", 
		"Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", "Masque", 
		"Masque", "Masque", "Masque", "Lunette", "Lunette", "Casquette", "Lunette", "Lunette", "Casquette", "Casquette", 
		"Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", "Casquette", 
		"Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", 
		"Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Boucle d'oreilles", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", 
		"Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", 
		"Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Yeux rouge", "Shiba", "Shiba", "Shiba", "Shiba", 
		"Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", "Shiba", 
		"Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Tail", "Légendaire"]

		### Démarrage ###
		self.MenuAccueil()

		### Lancement ###
		self.FonctionTimer()
		self.EcranDeJeux.mainloop() 

	def MenuAccueil(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Images ###
		self.BackgroundDécor = PhotoImage(file="salle/salleAccueil.png")
		self.CanvaUn.create_image(540, 360, image=self.BackgroundDécor)

		### Textes ###
		self.texteDébut = self.CanvaUn.create_text(545, 155, text= "Kurikku nanoko", font=("OCR A Extended", 50), fill="#AE0D1E")
		self.texteDébut2 = self.CanvaUn.create_text(540, 150, text= "Kurikku nanoko", font=("OCR A Extended", 50), fill="#CF3747")

		### Boutons ###
		self.boutonChargerPartie = Button(self.EcranDeJeux, text="  Charger partie  ", font=("OCR A Extended", 30), bg='white', fg='#A44040', command=self.ChargerLaPartie)
		self.boutonChargerPartie = self.CanvaUn.create_window(self.LargeurEcran/2, (self.HauteurEcran/2)-50, window=self.boutonChargerPartie)
		self.boutonNouvellePartie = Button(self.EcranDeJeux, text="  Nouvelle partie  ", font=("OCR A Extended", 30), bg='white', fg='#A44040', command=self.PremièrePageTuto)
		self.boutonNouvellePartie = self.CanvaUn.create_window(self.LargeurEcran/2, (self.HauteurEcran/2)+50, window=self.boutonNouvellePartie)
		self.boutonMenuCrédit = Button(self.EcranDeJeux, text="  Crédit  ", font=("OCR A Extended", 25), bg='white', fg='#A44040', command=self.LancerCredit)
		self.boutonMenuCrédit = self.CanvaUn.create_window(self.LargeurEcran/2, (self.HauteurEcran/2)+150, window=self.boutonMenuCrédit)
		self.boutonMenuQuitter = Button(self.EcranDeJeux, text="  Quitter  ", font=("OCR A Extended", 25), bg='white', fg='#A44040', command=self.QuitterJeu)
		self.boutonMenuQuitter = self.CanvaUn.create_window(self.LargeurEcran/2, (self.HauteurEcran/2)+250, window=self.boutonMenuQuitter)

	def ChargerLaPartie(self):
		self.FenetrePrincipale()
		self.ChargerSauvegarde()

	def QuitterJeu(self):
		self.EcranDeJeux.destroy()

	def LancerCredit(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Textes ###
		self.texteFaitPar = self.CanvaUn.create_text(self.LargeurEcran/2, 103, text= "Réalisé par", font=("OCR A Extended", 30), fill="#AE0D1E")
		self.texteFaitParDouble = self.CanvaUn.create_text(self.LargeurEcran/2, 100, text= "Réalisé par", font=("OCR A Extended", 30), fill="#AE0D1E")
		self.texteJolanThomassin = self.CanvaUn.create_text(self.LargeurEcran/2, 173, text= "Jolan Thomassin", font=("OCR A Extended", 60), fill="#FF14E6")
		self.texteJolanThomassinDouble = self.CanvaUn.create_text(self.LargeurEcran/2, 170, text= "Jolan Thomassin", font=("OCR A Extended", 60), fill="#FBFF0F")

		self.betaTesteur = self.CanvaUn.create_text(self.LargeurEcran/2, 303, text= "Béta testeur", font=("OCR A Extended", 30), fill="#AE0D1E")
		self.betaTesteurDouble = self.CanvaUn.create_text(self.LargeurEcran/2, 300, text= "Béta testeur", font=("OCR A Extended", 30), fill="#AE0D1E")
		self.texteBéta2 = self.CanvaUn.create_text(self.LargeurEcran/2, 423, text= "Mehdi Seddik", font=("OCR A Extended", 45), fill="#FF14E6")
		self.texteBéta2Double = self.CanvaUn.create_text(self.LargeurEcran/2, 420, text= "Mehdi Seddik", font=("OCR A Extended", 45), fill="#FBFF0F")

		### Boutons ###
		self.boutonMenuQuitter = Button(self.EcranDeJeux, text="  Retour  ", font=("OCR A Extended", 20), bg='white', fg='#A44040', command=self.MenuAccueil)
		self.boutonMenuQuitter = self.CanvaUn.create_window(self.LargeurEcran/2, self.LargeurEcran/1.70, window=self.boutonMenuQuitter)

	def GagnerArgent(self):
		self.argent = self.argent + self.puissanceClique
		self.argentTotal = self.argentTotal + self.puissanceClique
		self.ActualisationArgent()

	def FenetrePrincipale(self):
		### Reset ###
		self.CanvaUn.delete(ALL)
		self.InGame = True

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/bureau.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Cosmétique ###
		if self.TailsÉpiqueÉquipé == True :
			self.cosmTailsEquipement = PhotoImage(file="cosmétique/cosmétiqueTailsÉpique.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-300, (self.HauteurEcran/2), image=self.cosmTailsEquipement)
		if self.YeuxRougeRareÉquipé == True :
			self.cosmYeuxRougeEquipement = PhotoImage(file="cosmétique/cosmétiqueYeuxRougeRare.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2+50), image=self.cosmYeuxRougeEquipement)
		else :
			self.personnagePrincipale = PhotoImage(file="Mio Akiyama/waifuPersonnage.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.personnagePrincipale)
		if self.BoucleOreilleCommunÉquipé == True :
			self.cosmBoucleOreilleEquipement = PhotoImage(file="cosmétique/cosmétiqueBoucleOreilleCommun.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.cosmBoucleOreilleEquipement) 
		if self.LunetteCommunÉquipé == True :
			self.cosmLunetteEquipement = PhotoImage(file="cosmétique/cosmétiqueLunetteCommun.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.cosmLunetteEquipement)
		if self.LégendaireÉquipé == True :
			self.cosmLégendaire = PhotoImage(file="cosmétique/cosmétiqueLégendaire.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.cosmLégendaire)
		if self.ShibaRareÉquipé == True :
			self.cosmShibaEquipement = PhotoImage(file="cosmétique/cosmétiqueShibaRare.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-50, (self.HauteurEcran/2)+200, image=self.cosmShibaEquipement)
		if self.CasquetteCommunÉquipé == True :
			self.cosmCasquetteEquipement = PhotoImage(file="cosmétique/cosmétiqueCasquetteCommun.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.cosmCasquetteEquipement)
		if self.MasqueCommunÉquipé == True :
			self.cosmMasqueCommunEquipement = PhotoImage(file="cosmétique/cosmétiqueMasqueCommun.png")
			self.CanvaUn.create_image((self.LargeurEcran/2)-200, (self.HauteurEcran/2)+50, image=self.cosmMasqueCommunEquipement)

		### Texte ###
		self.ArgentTextuel()
 
		### Boutons ###
		self.boutonArgent = Button(self.EcranDeJeux, text=" Vendre des photos ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.GagnerArgent)
		self.boutonArgent = self.CanvaUn.create_window(self.LargeurEcran/2, 660, window=self.boutonArgent)
		self.boutonMenuSauvegarde = Button(self.EcranDeJeux, text=" Menu Sauvegarde ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuSauvegarde)
		self.boutonMenuSauvegarde = self.CanvaUn.create_window(200, 660, window=self.boutonMenuSauvegarde)
		self.boutonBoutique = Button(self.EcranDeJeux, text=" Téléphone ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonBoutique = self.CanvaUn.create_window(820, 660, window=self.boutonBoutique) 
		self.boutonQuitter = Button(self.EcranDeJeux, text=" ❌ ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.QuitterJeu)
		self.boutonQuitter = self.CanvaUn.create_window(990, 660, window=self.boutonQuitter)

	def Sauvegarde(self):
		with open("sauvegarde.txt", "r") as fichier :
			lignes = fichier.readlines()
			lignes[0] = str(self.argent) + "\n"
			lignes[1] = str(self.argentTotal) + "\n"
			lignes[2] = str(self.weeb) + "\n"
			lignes[3] = str(self.nombreWaifu) + "\n"
			lignes[4] = str(self.waifuUn) + "\n"
			lignes[5] = str(self.puissanceClique) + "\n"
			lignes[6] = str(self.LunetteCommunPossession) + "\n"
			lignes[7] = str(self.LunetteCommunÉquipé) + "\n"
			lignes[8] = str(self.CasquetteCommunPossession) + "\n"
			lignes[9] = str(self.CasquetteCommunÉquipé) + "\n"
			lignes[10] = str(self.MasqueCommunPossession) + "\n"
			lignes[11] = str(self.MasqueCommunÉquipé) + "\n"
			lignes[12] = str(self.BoucleOreilleCommunPossession) + "\n"
			lignes[13] = str(self.BoucleOreilleCommunÉquipé) + "\n"
			lignes[14] = str(self.YeuxRougeRarePossession) + "\n"
			lignes[15] = str(self.YeuxRougeRareÉquipé) + "\n"
			lignes[16] = str(self.ShibaRarePossession) + "\n"
			lignes[17] = str(self.ShibaRareÉquipé) + "\n"
			lignes[18] = str(self.TailsÉpiquePossession) + "\n"
			lignes[19] = str(self.TailsÉpiqueÉquipé) + "\n"
			lignes[20] = str(self.LégendairePossession) + "\n"
			lignes[21] = str(self.LégendaireÉquipé) + "\n"
			lignes[22] = str(self.prixCaisse) + "\n"
			lignes[23] = str(self.waifuCode) + "\n"
			lignes[24] = str(self.codeUn) + "\n"
			lignes[25] = str(self.prixWeeb) + "\n"
			lignes[26] = str(self.codeDeux) + "\n"
			lignes[27] = str(self.waifuDeux) + "\n"
			lignes[28] = str(self.bonusWaifuDeux) + "\n"
			lignes[29] = str(self.waifuUnNiveau) + "\n"
			lignes[30] = str(self.waifuUnPrixNiveau) + "\n"
			lignes[31] = str(self.waifuDeuxNiveau) + "\n"
			lignes[32] = str(self.waifuDeuxPrixNiveau) + "\n"
			lignes[33] = str(self.waifuCodeNiveau) + "\n"
			lignes[34] = str(self.waifuCodePrixNiveau) + "\n"
			lignes[35] = str(self.waifuUnPuissance) + "\n"
			lignes[36] = str(self.waifuUnEquipé) + "\n"
			lignes[37] = str(self.waifuDeuxPuissance) + "\n"
			lignes[38] = str(self.waifuDeuxEquipé) + "\n"
			lignes[39] = str(self.waifuCodePuissance) + "\n"
			lignes[40] = str(self.waifuCodeEquipé) + "\n"
			lignes[41] = str(self.manche) + "\n"

		with open("sauvegarde.txt", "w") as fichier :
			fichier.writelines(lignes)

	def ChargerSauvegarde(self):
		with open("sauvegarde.txt", "r") as fichier :
			lignes = fichier.readlines()
			self.argent = int(lignes[0])
			self.argentTotal = int(lignes[1])
			self.weeb = int(lignes[2])
			self.nombreWaifu = int(lignes[3])
			self.waifuUn = str(lignes[4])
			if self.waifuUn == "False\n" :
				self.waifuUn = False
			else :
				self.waifuUn = True
			self.puissanceClique = int(lignes[5])
			self.LunetteCommunPossession = str(lignes[6])
			if self.LunetteCommunPossession == "False\n" :
				self.LunetteCommunPossession = False
			else :
				self.LunetteCommunPossession = True
			self.LunetteCommunÉquipé = str(lignes[7])
			if self.LunetteCommunÉquipé == "False\n" :
				self.LunetteCommunÉquipé = False
			else :
				self.LunetteCommunÉquipé = True

			self.CasquetteCommunPossession = str(lignes[8])
			if self.CasquetteCommunPossession == "False\n" :
				self.CasquetteCommunPossession = False
			else :
				self.CasquetteCommunPossession = True

			self.CasquetteCommunÉquipé = str(lignes[9])
			if self.CasquetteCommunÉquipé == "False\n" :
				self.CasquetteCommunÉquipé = False
			else :
				self.CasquetteCommunÉquipé = True

			self.MasqueCommunPossession = str(lignes[10])
			if self.MasqueCommunPossession == "False\n" :
				self.MasqueCommunPossession = False
			else :
				self.MasqueCommunPossession = True

			self.MasqueCommunÉquipé = str(lignes[11])
			if self.MasqueCommunÉquipé == "False\n" :
				self.MasqueCommunÉquipé = False
			else :
				self.MasqueCommunÉquipé = True

			self.BoucleOreilleCommunPossession = str(lignes[12])
			if self.BoucleOreilleCommunPossession == "False\n" :
				self.BoucleOreilleCommunPossession = False
			else :
				self.BoucleOreilleCommunPossession = True

			self.BoucleOreilleCommunÉquipé = str(lignes[13])
			if self.BoucleOreilleCommunÉquipé == "False\n" :
				self.BoucleOreilleCommunÉquipé = False
			else :
				self.BoucleOreilleCommunÉquipé = True

			self.YeuxRougeRarePossession = str(lignes[14])
			if self.YeuxRougeRarePossession == "False\n" :
				self.YeuxRougeRarePossession = False
			else :
				self.YeuxRougeRarePossession = True

			self.YeuxRougeRareÉquipé = str(lignes[15])
			if self.YeuxRougeRareÉquipé == "False\n" :
				self.YeuxRougeRareÉquipé = False
			else :
				self.YeuxRougeRareÉquipé = True

			self.ShibaRarePossession = str(lignes[16])
			if self.ShibaRarePossession == "False\n" :
				self.ShibaRarePossession = False
			else :
				self.ShibaRarePossession = True

			self.ShibaRareÉquipé = str(lignes[17])
			if self.ShibaRareÉquipé == "False\n" :
				self.ShibaRareÉquipé = False
			else :
				self.ShibaRareÉquipé = True

			self.TailsÉpiquePossession = str(lignes[18])
			if self.TailsÉpiquePossession == "False\n" :
				self.TailsÉpiquePossession = False
			else :
				self.TailsÉpiquePossession = True

			self.TailsÉpiqueÉquipé = str(lignes[19])
			if self.TailsÉpiqueÉquipé == "False\n" :
				self.TailsÉpiqueÉquipé = False
			else :
				self.TailsÉpiqueÉquipé = True

			self.LégendairePossession = str(lignes[20])
			if self.LégendairePossession == "False\n" :
				self.LégendairePossession = False
			else :
				self.LégendairePossession = True

			self.LégendaireÉquipé = str(lignes[21])
			if self.LégendaireÉquipé == "False\n" :
				self.LégendaireÉquipé = False
			else :
				self.LégendaireÉquipé = True

			self.prixCaisse = int(lignes[22])
			self.waifuCode = str(lignes[23])
			if self.waifuCode == "False\n" :
				self.waifuCode = False
			else :
				self.waifuCode = True
			self.codeUn = str(lignes[24])
			if self.codeUn == "False\n" :
				self.codeUn = False
			else :
				self.codeUn = True
			self.prixWeeb = int(lignes[25])
			self.codeDeux = str(lignes[26])
			if self.codeDeux == "False\n" :
				self.codeDeux = False
			else :
				self.codeDeux = True
			self.waifuDeux = str(lignes[27])
			if self.waifuDeux == "False\n" :
				self.waifuDeux = False
			else :
				self.waifuDeux = True
			self.bonusWaifuDeux = int(lignes[28])
			self.waifuUnNiveau = int(lignes[29])
			self.waifuUnPrixNiveau = int(lignes[30])
			self.waifuDeuxNiveau = int(lignes[31])
			self.waifuDeuxPrixNiveau = int(lignes[32])
			self.waifuCodeNiveau = int(lignes[33])
			self.waifuCodePrixNiveau = int(lignes[34])
			self.waifuUnPuissance = int(lignes[35])
			self.waifuUnEquipé = str(lignes[36])
			if self.waifuUnEquipé == "False\n" :
				self.waifuUnEquipé = False
			else :
				self.waifuUnEquipé = True
			self.waifuDeuxPuissance = int(lignes[37])
			self.waifuDeuxEquipé = str(lignes[38])
			if self.waifuDeuxEquipé == "False\n" :
				self.waifuDeuxEquipé = False
			else :
				self.waifuDeuxEquipé = True
			self.waifuCodePuissance = int(lignes[39])
			self.waifuCodeEquipé = str(lignes[40])
			if self.waifuCodeEquipé == "False\n" :
				self.waifuCodeEquipé = False
			else :
				self.waifuCodeEquipé = True
			self.manche = int(lignes[41])

		### Textes ###
		self.ActualisationArgent()

		### Reset ###
		self.FenetrePrincipale()

	def MenuStats(self):
		### Compteur ###
		nombreCosmetique = 0
		if self.LunetteCommunPossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.CasquetteCommunPossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.MasqueCommunPossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.BoucleOreilleCommunPossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.YeuxRougeRarePossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.ShibaRarePossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.TailsÉpiquePossession == True :
			nombreCosmetique = nombreCosmetique + 1
		if self.LégendairePossession == True :
			nombreCosmetique = nombreCosmetique + 1

		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.boutonCode2Image = PhotoImage(file="waifu/boutonCode2.png")
		self.bureauPrincipal = PhotoImage(file="salle/stats.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Texte ###
		self.statsArgent = self.CanvaUn.create_text((self.LargeurEcran/2), 100, text= "Argent total :", font=("OCR A Extended", 30), fill="white")
		self.statsArgentDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 103, text= "Argent total :", font=("OCR A Extended", 30), fill="Grey")
		self.affichageArgentTotal = self.CanvaUn.create_text((self.LargeurEcran/2)+6, 146, text= self.argentTotal, font=("OCR A Extended", 30), fill="#1CF8FF")
		self.affichageArgentTotalDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 143, text= self.argentTotal, font=("OCR A Extended", 30), fill="#FF14E6")
		self.affichageArgentTotalTriple = self.CanvaUn.create_text(self.LargeurEcran/2, 140, text= self.argentTotal, font=("OCR A Extended", 30), fill="#FBFF0F")

		self.statsWeeb = self.CanvaUn.create_text((self.LargeurEcran/2), 200, text= "Weebs possédés :", font=("OCR A Extended", 30), fill="white")
		self.statsWeebDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 203, text= "Weebs possédés :", font=("OCR A Extended", 30), fill="Grey")
		self.afficheWeeb = self.CanvaUn.create_text((self.LargeurEcran/2)+6, 246, text= self.weeb, font=("OCR A Extended", 30), fill="#1CF8FF")
		self.afficheWeebDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 243, text= self.weeb, font=("OCR A Extended", 30), fill="#FF14E6")
		self.afficheWeebTriple = self.CanvaUn.create_text(self.LargeurEcran/2, 240, text= self.weeb, font=("OCR A Extended", 30), fill="#FBFF0F")

		self.statsNombreWaifu = self.CanvaUn.create_text((self.LargeurEcran/2), 300, text= "Waifu possédés :", font=("OCR A Extended", 30), fill="white")
		self.statsNombreWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 303, text= "Waifu possédés :", font=("OCR A Extended", 30), fill="Grey")
		self.afficheWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+6, 346, text= str(self.nombreWaifu) + "/3", font=("OCR A Extended", 30), fill="#1CF8FF")
		self.afficheWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 343, text= str(self.nombreWaifu) + "/3", font=("OCR A Extended", 30), fill="#FF14E6")
		self.afficheWaifuTriple = self.CanvaUn.create_text(self.LargeurEcran/2, 340, text= str(self.nombreWaifu) + "/3", font=("OCR A Extended", 30), fill="#FBFF0F")

		self.statsNombreCosmétique = self.CanvaUn.create_text((self.LargeurEcran/2), 400, text= "Cosmétique possédés :", font=("OCR A Extended", 30), fill="white")
		self.statsNombreCosmétiqueDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 403, text= "Cosmétique possédés :", font=("OCR A Extended", 30), fill="Grey")
		self.afficheCosmétique = self.CanvaUn.create_text((self.LargeurEcran/2)+6, 446, text= str(nombreCosmetique) + "/8", font=("OCR A Extended", 30), fill="#1CF8FF")
		self.afficheCosmétiqueDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 443, text= str(nombreCosmetique) + "/8", font=("OCR A Extended", 30), fill="#FF14E6")
		self.afficheCosmétiqueTriple = self.CanvaUn.create_text(self.LargeurEcran/2, 440, text= str(nombreCosmetique) + "/8", font=("OCR A Extended", 30), fill="#FBFF0F")

		### Boutons ###
		self.boutonCode2 = Button(self.EcranDeJeux, image=self.boutonCode2Image, font=("OCR A Extended", 20), bg='white', fg='black', borderwidth=0, command=self.pageBoutonSecret2)
		self.boutonCode2 = self.CanvaUn.create_window(self.LargeurEcran/2+447, 495, window=self.boutonCode2)
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueTroisième)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 650, window=self.boutonRetour)

	def pageBoutonSecret2(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Textes ###
		self.texteFaitPar = self.CanvaUn.create_text(self.LargeurEcran/2-3, self.HauteurEcran/2-103, text= "2 - B", font=("OCR A Extended", 60), fill="#464E88")
		self.texteFaitParDouble = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-100, text= "2 - B", font=("OCR A Extended", 60), fill="#88466E")

		### Boutons ###
		self.boutonMenuQuitter = Button(self.EcranDeJeux, text="  Retour  ", font=("OCR A Extended", 20), bg='white', fg='#A44040', command=self.MenuStats)
		self.boutonMenuQuitter = self.CanvaUn.create_window(self.LargeurEcran/2, self.LargeurEcran/1.70, window=self.boutonMenuQuitter)

	def MenuSauvegarde(self):
		### Reset ###
		self.CanvaUn.delete(self.boutonMenuSauvegarde)

		### Boutons ###
		self.boutonChargerSauvegarde = Button(self.EcranDeJeux, text=" Charger sauvegarde ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.ChargerSauvegarde)
		self.boutonChargerSauvegarde = self.CanvaUn.create_window(200, 460, window=self.boutonChargerSauvegarde)
		self.boutonSauvegarde = Button(self.EcranDeJeux, text=" Sauvegarder ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.Sauvegarde)
		self.boutonSauvegarde = self.CanvaUn.create_window(200, 560, window=self.boutonSauvegarde)
		self.boutonFermerSauvegarde = Button(self.EcranDeJeux, text=" Fermer Menu ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonFermerSauvegarde = self.CanvaUn.create_window(200, 660, window=self.boutonFermerSauvegarde)

	def MenuBoutique(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/shop.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Boutons ###
		self.boutonDeGauche = Button(self.EcranDeJeux, image=self.imageRessource, command=self.Ressources, borderwidth=0)
		self.boutonDeGauche = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonDeGauche)
		self.boutonDeDroite = Button(self.EcranDeJeux, image=self.imageWaifu, command=self.pageWaifuUn, borderwidth=0)
		self.boutonDeDroite = self.CanvaUn.create_window(self.LargeurEcran/2+250, self.HauteurEcran/2, window=self.boutonDeDroite)

		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueDeuxième)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueQuatrième)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)

		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		self.texteGauche = self.CanvaUn.create_text(self.LargeurEcran/2-250, self.HauteurEcran/2+250, text= "Ressource", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteGaucheDouble = self.CanvaUn.create_text(self.LargeurEcran/2-247, self.HauteurEcran/2+247, text= "Ressource", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.texteDroite = self.CanvaUn.create_text(self.LargeurEcran/2+250, self.HauteurEcran/2+250, text= "Waifu", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteDroiteDouble = self.CanvaUn.create_text(self.LargeurEcran/2+247, self.HauteurEcran/2+247, text= "Waifu", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.ArgentTextuel()

	def MenuBoutiqueDeuxième(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/shop.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Boutons ###
		self.boutonDeGauche = Button(self.EcranDeJeux, image=self.imageCaisse, command=self.pageCaisse, borderwidth=0)
		self.boutonDeGauche = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonDeGauche)
		self.boutonDeDroite = Button(self.EcranDeJeux, image=self.imageCollection, command=self.pageCollection, borderwidth=0)
		self.boutonDeDroite = self.CanvaUn.create_window(self.LargeurEcran/2+250, self.HauteurEcran/2, window=self.boutonDeDroite)

		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueTroisième)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)

		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		self.texteGauche = self.CanvaUn.create_text(self.LargeurEcran/2-250, self.HauteurEcran/2+250, text= "Caisse", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteGaucheDouble = self.CanvaUn.create_text(self.LargeurEcran/2-247, self.HauteurEcran/2+247, text= "Caisse", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.texteDroite = self.CanvaUn.create_text(self.LargeurEcran/2+250, self.HauteurEcran/2+250, text= "Collection", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteDroiteDouble = self.CanvaUn.create_text(self.LargeurEcran/2+247, self.HauteurEcran/2+247, text= "Collection", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.ArgentTextuel()

	def MenuBoutiqueTroisième(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/shop.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Boutons ###
		self.boutonDeGauche = Button(self.EcranDeJeux, image=self.imageCode, command=self.pageCode, borderwidth=0)
		self.boutonDeGauche = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonDeGauche)
		self.boutonDeDroite = Button(self.EcranDeJeux, image=self.imageStats, command=self.MenuStats, borderwidth=0)
		self.boutonDeDroite = self.CanvaUn.create_window(self.LargeurEcran/2+250, self.HauteurEcran/2, window=self.boutonDeDroite)

		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueQuatrième)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueDeuxième)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)

		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		self.texteGauche = self.CanvaUn.create_text(self.LargeurEcran/2-250, self.HauteurEcran/2+250, text= "Code", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteGaucheDouble = self.CanvaUn.create_text(self.LargeurEcran/2-247, self.HauteurEcran/2+247, text= "Code", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.texteDroite = self.CanvaUn.create_text(self.LargeurEcran/2+250, self.HauteurEcran/2+250, text= "Stats", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteDroiteDouble = self.CanvaUn.create_text(self.LargeurEcran/2+247, self.HauteurEcran/2+247, text= "Stats", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.ArgentTextuel()

	def MenuBoutiqueQuatrième(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/shop.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Boutons ###
		self.boutonDeGauche = Button(self.EcranDeJeux, image=self.imageQuête, command=self.pageQuête, borderwidth=0)
		self.boutonDeGauche = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonDeGauche)
		self.boutonDeDroite = Button(self.EcranDeJeux, image=self.imageMilitaire, command=self.pageMillitaire, borderwidth=0)
		self.boutonDeDroite = self.CanvaUn.create_window(self.LargeurEcran/2+250, self.HauteurEcran/2, window=self.boutonDeDroite)

		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueTroisième)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)

		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		self.texteGauche = self.CanvaUn.create_text(self.LargeurEcran/2-250, self.HauteurEcran/2+250, text= "Quête", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteGaucheDouble = self.CanvaUn.create_text(self.LargeurEcran/2-247, self.HauteurEcran/2+247, text= "Quête", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.texteDroite = self.CanvaUn.create_text(self.LargeurEcran/2+250, self.HauteurEcran/2+250, text= "Millitaire", font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteDroiteDouble = self.CanvaUn.create_text(self.LargeurEcran/2+247, self.HauteurEcran/2+247, text= "Millitaire", font=("OCR A Extended", 30), fill="#FBFF0F")
		self.ArgentTextuel()

	def pageQuête(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		def vérificationQuete() :
			limitation = False

			if (self.niveauQuete == 0) and (limitation == False) :
				if self.argentTotal >= 1000 :
					limitation = True
					self.niveauQuete = 1

			if (self.niveauQuete == 1) and (limitation == False) :
				if self.manche >= 1 :
					limitation = True
					self.niveauQuete = 2

			if (self.niveauQuete == 2) and (limitation == False) :
				if self.nombreWaifu >= 2 :
					limitation = True
					self.niveauQuete = 3

			self.pageQuête()

		def affichageQuete() :
			if self.niveauQuete == 0 :
				self.texteQueteActuelle = self.CanvaUn.create_text((self.LargeurEcran/2)+3, self.HauteurEcran/2-50+3, text= "Gagner 1.000$", font=("OCR A Extended", 45), fill="#FF14E6")
				self.texteQueteActuelle = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-50, text= "Gagner 1.000$", font=("OCR A Extended", 45), fill="#FBFF0F")
				self.texteQueteActuelleValeur = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2+50+3, text= str(self.argentTotal) + " / 1.000", font=("OCR A Extended", 50), fill="#FF14E6")
				self.texteQueteActuelleValeur = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2+50, text= str(self.argentTotal) + " / 1.000", font=("OCR A Extended", 50), fill="#FBFF0F")
			if self.niveauQuete == 1 :
				self.texteQueteActuelle = self.CanvaUn.create_text((self.LargeurEcran/2)+3, self.HauteurEcran/2-50+3, text= "Finir une manche millitaire", font=("OCR A Extended", 45), fill="#FF14E6")
				self.texteQueteActuelle = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-50, text= "Finir une manche millitaire", font=("OCR A Extended", 45), fill="#FBFF0F")
				self.texteQueteActuelleValeur = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2+50+3, text= str(self.manche) + " / 1", font=("OCR A Extended", 45), fill="#FF14E6")
				self.texteQueteActuelleValeur = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2+50, text= str(self.manche) + " / 1", font=("OCR A Extended", 45), fill="#FBFF0F")
			if self.niveauQuete == 2 :
				self.texteQueteActuelle = self.CanvaUn.create_text((self.LargeurEcran/2)+3, self.HauteurEcran/2-50+3, text= "Avoir au moins 2 waifu", font=("OCR A Extended", 45), fill="#FF14E6")
				self.texteQueteActuelle = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-50, text= "Avoir au moins 2 waifu", font=("OCR A Extended", 45), fill="#FBFF0F")
				self.texteQueteActuelleValeur = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2+50+3, text= str(self.nombreWaifu) + " / 2", font=("OCR A Extended", 45), fill="#FF14E6")
				self.texteQueteActuelleValeur = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2+50, text= str(self.nombreWaifu) + " / 2", font=("OCR A Extended", 45), fill="#FBFF0F")
			if self.niveauQuete == 3 :
				self.texteQueteActuelle = self.CanvaUn.create_text((self.LargeurEcran/2)+3, self.HauteurEcran/2-50+3, text= "Vous avez fini toutes les quêtes disponibles", font=("OCR A Extended", 25), fill="#FF14E6")
				self.texteQueteActuelle = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-50, text= "Vous avez fini toutes les quêtes disponibles", font=("OCR A Extended", 25), fill="#FBFF0F")
				self.texteQueteActuelleValeur = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2+50+3, text= "Suite bientôt disponible", font=("OCR A Extended", 30), fill="#FF14E6")
				self.texteQueteActuelleValeur = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2+50, text= "Suite bientôt disponible", font=("OCR A Extended", 30), fill="#FBFF0F")

		### Textes ###
		affichageQuete()
		self.texteNiveauQuete = self.CanvaUn.create_text((self.LargeurEcran/2)+3, self.HauteurEcran/2-300+3, text= "Niveau quête : " + str(self.niveauQuete), font=("OCR A Extended", 30), fill="#FF14E6")
		self.texteNiveauQueteDeux = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-300, text= "Niveau quête : " + str(self.niveauQuete), font=("OCR A Extended", 30), fill="#FBFF0F")

		### Boutons ###
		if self.niveauQuete != 3 :
			self.boutonValider = Button(self.EcranDeJeux, text=" Valider quête ", font=("OCR A Extended", 20), bg='white', fg='black', command=vérificationQuete, width=20)
			self.boutonValider = self.CanvaUn.create_window(self.LargeurEcran/2, 500, window=self.boutonValider)
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueQuatrième)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

	def pageCode(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Fonction ###
		def récupérationValeur():
			code = un_entry.get()
			if (code == "un code") and (self.codeUn == False) :
				self.CanvaUn.itemconfigure(self.résultaCode, text="Vous êtes un petit rigolo (+1.000€)")
				self.argent = self.argent + 1000
				self.argentTotal = self.argentTotal + 1000
				self.codeUn = True
			if (code == "XBD") and (self.waifuCode == False) :
				self.CanvaUn.itemconfigure(self.résultaCode, text="Vous avez débloqué : Kimoko")
				self.waifuCode = True
				self.nombreWaifu += 1
			if (code == "Jolan") :
				self.CanvaUn.itemconfigure(self.résultaCode, text="Il est magnifique")
			if (code == "Mehdi") :
				self.CanvaUn.itemconfigure(self.résultaCode, text="Il est pas drole")
			if (code == "Manono") :
				self.CanvaUn.itemconfigure(self.résultaCode, text="Il fait la vaiselle")
			if (code == "Caisse") and (self.codeDeux == False) :
				self.CanvaUn.itemconfigure(self.résultaCode, text="Tirage ! (+5.000€)")
				self.argent = self.argent + 5000
				self.argentTotal = self.argentTotal + 5000
				self.codeDeux = True

		def entry_clear(e):
			un_entry.delete(0, END)

		### Saisie  ###
		un_entry = Entry(self.EcranDeJeux, font=("Helvectica", 24), width=20, fg="#336d92", bd=0)
		un_window = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2-150, anchor="n", window=un_entry)
		un_entry.insert(0, "Entrer un code")
		un_entry.bind("<Button-1>", entry_clear)

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), width=20, bg='white', fg='black', command=self.MenuBoutiqueTroisième)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)
		self.boutonValidationCode = Button(self.EcranDeJeux, text=" Validation ", font=("OCR A Extended", 20), width=20, bg='white', fg='black', command=récupérationValeur)
		self.boutonValidationCode = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2, window=self.boutonValidationCode)

		### Textes ###
		self.résultaCode = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+150, text="", font=("OCR A Extended", 30), fill="#1CF8FF")

	def pageCollection(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.imageDeCollection = PhotoImage(file="salle/pageCollection.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.imageDeCollection)
		self.imageIconeCaché = PhotoImage(file="cosmétique/iconeCaché.png")
		self.imageIconeLunette = PhotoImage(file="cosmétique/iconeLunette.png")
		self.imageIconeCasquette = PhotoImage(file="cosmétique/iconeCasquette.png")
		self.imageIconeBoucleOreille = PhotoImage(file="cosmétique/iconeBoucleOreille.png")
		self.imageIconeMasque = PhotoImage(file="cosmétique/iconeMasque.png")
		self.imageIconeYeuxRouge = PhotoImage(file="cosmétique/iconeYeuxRouge.png")
		self.imageIconeShiba = PhotoImage(file="cosmétique/iconeCasquette.png")
		self.imageIconeTails = PhotoImage(file="cosmétique/iconeTails.png")
		self.imageIconeShiba = PhotoImage(file="cosmétique/iconeShiba.png")
		self.imageIconeLégendaire = PhotoImage(file="cosmétique/iconeLégendaire.png")

		### Boutons ###
		if self.LunetteCommunPossession == True :
			self.boutonDeFullGaucheHaut = Button(self.EcranDeJeux, image=self.imageIconeLunette, command=self.EquipementLunette, borderwidth=2, highlightcolor="grey",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullGaucheHaut = self.CanvaUn.create_window(self.LargeurEcran/2-400, self.HauteurEcran/2-170, window=self.boutonDeFullGaucheHaut)
		else :		
			self.boutonDeFullGaucheHaut = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullGaucheHaut = self.CanvaUn.create_window(self.LargeurEcran/2-400, self.HauteurEcran/2-170, window=self.boutonDeFullGaucheHaut)
		if self.CasquetteCommunPossession == True :
			self.boutonGaucheHaut = Button(self.EcranDeJeux, image=self.imageIconeCasquette, command=self.EquipementCasquette, borderwidth=2, highlightcolor="grey",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonGaucheHaut = self.CanvaUn.create_window(self.LargeurEcran/2-135, self.HauteurEcran/2-170, window=self.boutonGaucheHaut)
		else :
			self.boutonGaucheHaut = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonGaucheHaut = self.CanvaUn.create_window(self.LargeurEcran/2-135, self.HauteurEcran/2-170, window=self.boutonGaucheHaut)
		if self.BoucleOreilleCommunPossession == True :
			self.boutonDeFullDroiteHaut = Button(self.EcranDeJeux, image=self.imageIconeBoucleOreille, command=self.EquipementBoucleOreille, borderwidth=2, highlightcolor="grey",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullDroiteHaut = self.CanvaUn.create_window(self.LargeurEcran/2+400, self.HauteurEcran/2-170, window=self.boutonDeFullDroiteHaut)
		else :
			self.boutonDeFullDroiteHaut = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullDroiteHaut = self.CanvaUn.create_window(self.LargeurEcran/2+400, self.HauteurEcran/2-170, window=self.boutonDeFullDroiteHaut)
		if self.MasqueCommunPossession == True :
			self.boutonDroiteHaut = Button(self.EcranDeJeux, image=self.imageIconeMasque, command=self.EquipementMasque, borderwidth=2, highlightcolor="grey",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDroiteHaut = self.CanvaUn.create_window(self.LargeurEcran/2+135, self.HauteurEcran/2-170, window=self.boutonDroiteHaut)
		else :
			self.boutonDroiteHaut = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDroiteHaut = self.CanvaUn.create_window(self.LargeurEcran/2+135, self.HauteurEcran/2-170, window=self.boutonDroiteHaut)
		
		if self.YeuxRougeRarePossession == True :
			self.boutonDeFullGaucheBas = Button(self.EcranDeJeux, image=self.imageIconeYeuxRouge, command=self.EquipementYeuxRouge, borderwidth=2, highlightcolor="aqua",highlightbackground="aqua",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullGaucheBas = self.CanvaUn.create_window(self.LargeurEcran/2-400, self.HauteurEcran/2+170, window=self.boutonDeFullGaucheBas)
		else :
			self.boutonDeFullGaucheBas = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullGaucheBas = self.CanvaUn.create_window(self.LargeurEcran/2-400, self.HauteurEcran/2+170, window=self.boutonDeFullGaucheBas)
		if self.ShibaRarePossession == True :
			self.boutonGaucheBas = Button(self.EcranDeJeux, image=self.imageIconeShiba, command=self.EquipementShiba, borderwidth=2, highlightcolor="aqua",highlightbackground="aqua",highlightthickness=5,relief=SOLID, default='active')
			self.boutonGaucheBas = self.CanvaUn.create_window(self.LargeurEcran/2-135, self.HauteurEcran/2+170, window=self.boutonGaucheBas)
		else :
			self.boutonGaucheBas = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonGaucheBas = self.CanvaUn.create_window(self.LargeurEcran/2-135, self.HauteurEcran/2+170, window=self.boutonGaucheBas)
		if self.TailsÉpiquePossession == True :
			self.boutonDroiteBas = Button(self.EcranDeJeux, image=self.imageIconeTails, command=self.EquipementTails, borderwidth=2, highlightcolor="purple",highlightbackground="purple",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDroiteBas = self.CanvaUn.create_window(self.LargeurEcran/2+135, self.HauteurEcran/2+170, window=self.boutonDroiteBas)
		else :
			self.boutonDroiteBas = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDroiteBas = self.CanvaUn.create_window(self.LargeurEcran/2+135, self.HauteurEcran/2+170, window=self.boutonDroiteBas)
		if self.LégendairePossession == True :
			self.boutonDeFullDroiteBas = Button(self.EcranDeJeux, image=self.imageIconeLégendaire, command=self.EquipementDrip, borderwidth=2, highlightcolor="yellow",highlightbackground="yellow",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullDroiteBas = self.CanvaUn.create_window(self.LargeurEcran/2+400, self.HauteurEcran/2+170, window=self.boutonDeFullDroiteBas)
		else :
			self.boutonDeFullDroiteBas = Button(self.EcranDeJeux, image=self.imageIconeCaché, command=self.EquipementNul, borderwidth=2, highlightcolor="red",highlightbackground="red",highlightthickness=5,relief=SOLID, default='active')
			self.boutonDeFullDroiteBas = self.CanvaUn.create_window(self.LargeurEcran/2+400, self.HauteurEcran/2+170, window=self.boutonDeFullDroiteBas)

		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueDeuxième)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		self.confirmationEquipement = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2, text= "", font=("OCR A Extended", 30), fill="black")
		self.texteCodeSecret2 = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2, text= "", font=("OCR A Extended", 30), fill="black")
		self.texteCodeSecret2Double = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2, text= "", font=("OCR A Extended", 30), fill="black")

	def EquipementLunette(self):
		if self.LunetteCommunÉquipé == True :
			self.LunetteCommunÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Lunette déséquipé")
		else : 
			self.LunetteCommunÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Lunette équipé")

	def EquipementCasquette(self):
		if self.CasquetteCommunÉquipé == True :
			self.CasquetteCommunÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Casquette déséquipé")
		else : 
			self.CasquetteCommunÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Casquette équipé")

	def EquipementBoucleOreille(self):
		if self.BoucleOreilleCommunÉquipé == True :
			self.BoucleOreilleCommunÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Boucle d'oreilles déséquipé")
		else : 
			self.BoucleOreilleCommunÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Boucle d'oreilles équipé")

	def EquipementMasque(self):
		if self.MasqueCommunÉquipé == True :
			self.MasqueCommunÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Masque déséquipé")
		else : 
			self.MasqueCommunÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Masque équipé")

	def EquipementTails(self):
		if self.TailsÉpiqueÉquipé == True :
			self.TailsÉpiqueÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Tails déséquipé")
		else : 
			self.TailsÉpiqueÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Tails équipé")

	def EquipementShiba(self):
		if self.ShibaRareÉquipé == True :
			self.ShibaRareÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Shiba déséquipé")
		else : 
			self.ShibaRareÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Shiba équipé")

	def EquipementYeuxRouge(self):
		if self.YeuxRougeRareÉquipé == True :
			self.YeuxRougeRareÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Yeux rouge déséquipé")
		else : 
			self.YeuxRougeRareÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Yeux rouge équipé")

	def EquipementDrip(self):
		if self.LégendaireÉquipé == True :
			self.LégendaireÉquipé = False
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Drip déséquipé")
		else : 
			self.LégendaireÉquipé = True
			self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Drip équipé")

	def EquipementNul(self):
		self.CanvaUn.itemconfigure(self.confirmationEquipement, text="Non débloqué")

	def pageCaisse(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.salleTirage = PhotoImage(file="salle/salleTirage.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.salleTirage)

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutiqueDeuxième)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)
		self.boutonCollection = Button(self.EcranDeJeux, text=" Collection ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageCollection)
		self.boutonCollection = self.CanvaUn.create_window(self.LargeurEcran/2+415, 680, window=self.boutonCollection)
		self.boutonDrop = Button(self.EcranDeJeux, text=" Drop ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageDrop)
		self.boutonDrop = self.CanvaUn.create_window(self.LargeurEcran/2-463, 680, window=self.boutonDrop)
		self.boutonTirage = Button(self.EcranDeJeux, text="Tirer une caisse : " + str(self.prixCaisse) +"€", font=("OCR A Extended", 20), bg='white', fg='black', command=self.debitArgentCaisse)
		self.boutonTirage = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2, window=self.boutonTirage)

		### Textes ###
		self.texteCodeSecret1 = self.CanvaUn.create_text(self.LargeurEcran/2+388, 120, text= "1 - X", font=("OCR A Extended", 18), fill="#8DFCE3")
		self.texteCodeSecret1Double = self.CanvaUn.create_text(self.LargeurEcran/2+390, 122, text= "1 - X", font=("OCR A Extended", 18), fill="#8DDEFC")
		if self.waifuCode == True :
			self.texteChanceLégendaire = self.CanvaUn.create_text(self.LargeurEcran/2, 120, text= "Légendaire - 7%", font=("OCR A Extended", 30), fill="yellow")
			self.texteChanceÉpique = self.CanvaUn.create_text(self.LargeurEcran/2, 170, text= "Épique - 9%", font=("OCR A Extended", 30), fill="purple")
			self.texteChanceRare = self.CanvaUn.create_text(self.LargeurEcran/2, 220, text= "Rare - 35%", font=("OCR A Extended", 30), fill="aqua")
			self.texteChanceCommun = self.CanvaUn.create_text(self.LargeurEcran/2, 270, text= "Commun - 49%", font=("OCR A Extended", 30), fill="grey")
		else : 
			self.texteChanceLégendaire = self.CanvaUn.create_text(self.LargeurEcran/2, 120, text= "Légendaire - 1%", font=("OCR A Extended", 30), fill="yellow")
			self.texteChanceÉpique = self.CanvaUn.create_text(self.LargeurEcran/2, 170, text= "Épique - 9%", font=("OCR A Extended", 30), fill="purple")
			self.texteChanceRare = self.CanvaUn.create_text(self.LargeurEcran/2, 220, text= "Rare - 35%", font=("OCR A Extended", 30), fill="aqua")
			self.texteChanceCommun = self.CanvaUn.create_text(self.LargeurEcran/2, 270, text= "Commun - 55%", font=("OCR A Extended", 30), fill="grey")
		self.résultatDuTiragePrécédent = self.CanvaUn.create_text(self.LargeurEcran/2-300, self.HauteurEcran/2+100, text= "", font=("OCR A Extended", 15), fill="#FF14E6")
		self.résultatDuTirageActuel = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2+100, text= "", font=("OCR A Extended", 25), fill="#FF14E6")
		self.résultatDuTirageSuivant = self.CanvaUn.create_text(self.LargeurEcran/2+300, self.HauteurEcran/2+100, text= "", font=("OCR A Extended", 15), fill="#FF14E6")
		self.résultatDuTirageFinale = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2+175, text= "", font=("OCR A Extended", 15), fill="#FF14E6")
		self.ArgentTextuel()

	def pageDrop(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.salleDrop = PhotoImage(file="salle/salleDrop.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.salleDrop)

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageCaisse)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		### Textes ###
		if self.waifuCode == True :
			self.dropLunette = self.CanvaUn.create_text((self.LargeurEcran/2+3), 153, text= "Lunette : 10%", font=("OCR A Extended", 30), fill="white")
			self.dropLunetteD = self.CanvaUn.create_text((self.LargeurEcran/2), 150, text= "Lunette : 10%", font=("OCR A Extended", 30), fill="grey")
			self.dropCasquette = self.CanvaUn.create_text((self.LargeurEcran/2+3), 203, text= "Casquette : 13%", font=("OCR A Extended", 30), fill="white")
			self.dropCasquetteD = self.CanvaUn.create_text((self.LargeurEcran/2), 200, text= "Casquette : 13%", font=("OCR A Extended", 30), fill="grey")
			self.dropBoucleOreille = self.CanvaUn.create_text((self.LargeurEcran/2+3), 253, text= "Boucle d'oreilles : 14%", font=("OCR A Extended", 30), fill="white")
			self.dropBoucleOreille = self.CanvaUn.create_text((self.LargeurEcran/2), 250, text= "Boucle d'oreilles : 14%", font=("OCR A Extended", 30), fill="grey")
			self.dropMasque = self.CanvaUn.create_text((self.LargeurEcran/2+3), 303, text= "Masque : 12%", font=("OCR A Extended", 30), fill="white")
			self.dropMasqueD = self.CanvaUn.create_text((self.LargeurEcran/2), 300, text= "Masque : 12%", font=("OCR A Extended", 30), fill="grey")
			self.dropYeuxRouge = self.CanvaUn.create_text((self.LargeurEcran/2+3), 353, text= "Yeux rouge : 21%", font=("OCR A Extended", 30), fill="white")
			self.dropYeuxRougeD = self.CanvaUn.create_text((self.LargeurEcran/2), 350, text= "Yeux rouge : 21%", font=("OCR A Extended", 30), fill="aqua")
			self.dropShiba = self.CanvaUn.create_text((self.LargeurEcran/2+3), 403, text= "Shiba : 14%", font=("OCR A Extended", 30), fill="white")
			self.dropShibaD = self.CanvaUn.create_text((self.LargeurEcran/2), 400, text= "Shiba : 14%", font=("OCR A Extended", 30), fill="aqua")
			self.dropTail = self.CanvaUn.create_text((self.LargeurEcran/2+3), 453, text= "Tail : 9%", font=("OCR A Extended", 30), fill="white")
			self.dropTail = self.CanvaUn.create_text((self.LargeurEcran/2), 450, text= "Tail : 9%", font=("OCR A Extended", 30), fill="purple")
			self.dropLégendaire = self.CanvaUn.create_text((self.LargeurEcran/2+3), 503, text= "Légendaire : 7%", font=("OCR A Extended", 30), fill="white")
			self.dropLégendaire = self.CanvaUn.create_text((self.LargeurEcran/2), 500, text= "Légendaire : 7%", font=("OCR A Extended", 30), fill="yellow")
		else :
			self.dropLunette = self.CanvaUn.create_text((self.LargeurEcran/2+3), 153, text= "Lunette : 10%", font=("OCR A Extended", 30), fill="white")
			self.dropLunetteD = self.CanvaUn.create_text((self.LargeurEcran/2), 150, text= "Lunette : 10%", font=("OCR A Extended", 30), fill="grey")
			self.dropCasquette = self.CanvaUn.create_text((self.LargeurEcran/2+3), 203, text= "Casquette : 17%", font=("OCR A Extended", 30), fill="white")
			self.dropCasquetteD = self.CanvaUn.create_text((self.LargeurEcran/2), 200, text= "Casquette : 17%", font=("OCR A Extended", 30), fill="grey")
			self.dropBoucleOreille = self.CanvaUn.create_text((self.LargeurEcran/2+3), 253, text= "Boucle d'oreilles : 15%", font=("OCR A Extended", 30), fill="white")
			self.dropBoucleOreille = self.CanvaUn.create_text((self.LargeurEcran/2), 250, text= "Boucle d'oreilles : 15%", font=("OCR A Extended", 30), fill="grey")
			self.dropMasque = self.CanvaUn.create_text((self.LargeurEcran/2+3), 303, text= "Masque : 13%", font=("OCR A Extended", 30), fill="white")
			self.dropMasqueD = self.CanvaUn.create_text((self.LargeurEcran/2), 300, text= "Masque : 13%", font=("OCR A Extended", 30), fill="grey")
			self.dropYeuxRouge = self.CanvaUn.create_text((self.LargeurEcran/2+3), 353, text= "Yeux rouge : 21%", font=("OCR A Extended", 30), fill="white")
			self.dropYeuxRougeD = self.CanvaUn.create_text((self.LargeurEcran/2), 350, text= "Yeux rouge : 21%", font=("OCR A Extended", 30), fill="aqua")
			self.dropShiba = self.CanvaUn.create_text((self.LargeurEcran/2+3), 403, text= "Shiba : 14%", font=("OCR A Extended", 30), fill="white")
			self.dropShibaD = self.CanvaUn.create_text((self.LargeurEcran/2), 400, text= "Shiba : 14%", font=("OCR A Extended", 30), fill="aqua")
			self.dropTail = self.CanvaUn.create_text((self.LargeurEcran/2+3), 453, text= "Tail : 9%", font=("OCR A Extended", 30), fill="white")
			self.dropTail = self.CanvaUn.create_text((self.LargeurEcran/2), 450, text= "Tail : 9%", font=("OCR A Extended", 30), fill="purple")
			self.dropLégendaire = self.CanvaUn.create_text((self.LargeurEcran/2+3), 503, text= "Légendaire : 1%", font=("OCR A Extended", 30), fill="white")
			self.dropLégendaire = self.CanvaUn.create_text((self.LargeurEcran/2), 500, text= "Légendaire : 1%", font=("OCR A Extended", 30), fill="yellow")

	def tirageCaisse(self):
		self.CanvaUn.delete(self.boutonTirage)
		self.CanvaUn.delete(self.boutonRetour)
		self.CanvaUn.delete(self.boutonCollection)
		self.CanvaUn.delete(self.boutonDrop)
		self.CanvaUn.itemconfigure(self.résultatDuTirageFinale, text="")
		while self.compteur < 30 :
			self.calculCaisse()
			time.sleep(0.1)
			self.CanvaUn.update()
		self.compteur = 0
		while self.compteur < 7 :
			self.calculCaisse()
			time.sleep(0.7)
			self.CanvaUn.update()
		self.compteur = 0
		while self.compteur < 3 :
			self.calculCaisse()
			time.sleep(1.5)
			self.CanvaUn.update()
		self.CanvaUn.itemconfigure(self.résultatDuTirageFinale, text=("Vous avez remporté un cosmétique : " + self.résultatActuelString), fill=self.couleurRésultatActuel)
		self.boutonTirage = Button(self.EcranDeJeux, text="Tirer une caisse : " + str(self.prixCaisse) +"€", font=("OCR A Extended", 20), bg='white', fg='black', command=self.debitArgentCaisse)
		self.boutonTirage = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2, window=self.boutonTirage)
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)
		self.boutonCollection = Button(self.EcranDeJeux, text=" Collection ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageCollection)
		self.boutonCollection = self.CanvaUn.create_window(self.LargeurEcran/2+415, 680, window=self.boutonCollection)
		if self.résultatActuelString == "Lunette" :
			self.LunetteCommunPossession = True
		elif self.résultatActuelString == "Casquette" :
			self.CasquetteCommunPossession = True
		elif self.résultatActuelString == "Boucle d'oreilles" :
			self.BoucleOreilleCommunPossession = True
		elif self.résultatActuelString == "Masque" :
			self.MasqueCommunPossession = True
		elif self.résultatActuelString == "Yeux rouge" :
			self.YeuxRougeRarePossession = True
		elif self.résultatActuelString == "Shiba" :
			self.ShibaRarePossession = True
		elif self.résultatActuelString == "Tail" :
			self.TailsÉpiquePossession = True
		elif self.résultatActuelString == "Légendaire" :
			self.LégendairePossession = True
		else :
			None

	def debitArgentCaisse(self):
		if self.argent >= self.prixCaisse :
			self.argent = self.argent - self.prixCaisse
			self.prixCaisse = self.prixCaisse + int(self.prixCaisse/5)
			self.ActualisationArgent()
			self.tirageCaisse()
		else :
			None

	def calculCaisse(self):
		couleurRésultatPrécédent = "grey"
		couleurRésultatSuivant = "grey"
		if self.waifuCode == True :
			résultatPrécédentString = self.contenuCaisseAmélioré[self.résultatPrécédent]
			self.résultatActuelString = self.contenuCaisseAmélioré[self.résultatActuel]
			résulatSuivantString = self.contenuCaisseAmélioré[self.résulatSuivant]
		else :
			résultatPrécédentString = self.contenuCaisse[self.résultatPrécédent]
			self.résultatActuelString = self.contenuCaisse[self.résultatActuel]
			résulatSuivantString = self.contenuCaisse[self.résulatSuivant]

		### Résultat Précédent ###
		if résultatPrécédentString == "Lunette" or résultatPrécédentString == "Casquette" or résultatPrécédentString == "Boucle d'oreilles" or résultatPrécédentString == "Masque" :
			couleurRésultatPrécédent = "grey"
		elif résultatPrécédentString == "Yeux rouge" or résultatPrécédentString =="Shiba" :
			couleurRésultatPrécédent = "aqua"
		elif résultatPrécédentString == "Tail" :
			couleurRésultatPrécédent = "purple"
		else :
			couleurRésultatPrécédent = "yellow"
		### Résultat Actuel ###
		if self.résultatActuelString == "Lunette" or self.résultatActuelString == "Casquette" or  self.résultatActuelString == "Boucle d'oreilles" or self.résultatActuelString == "Masque" :
			self.couleurRésultatActuel = "grey"
		elif self.résultatActuelString == "Yeux rouge" or self.résultatActuelString == "Shiba" :
			self.couleurRésultatActuel = "aqua"
		elif self.résultatActuelString == "Tail" :
			self.couleurRésultatActuel = "purple"
		else :
			self.couleurRésultatActuel = "yellow"
		### Résultat Suivant ###
		if résulatSuivantString == "Lunette" or résulatSuivantString == "Casquette" or résulatSuivantString == "Boucle d'oreilles" or résulatSuivantString == "Masque" :
			couleurRésultatSuivant = "grey"
		elif résulatSuivantString == "Yeux rouge" or résulatSuivantString =="Shiba" :
			couleurRésultatSuivant = "aqua"
		elif résulatSuivantString == "Tail" :
			couleurRésultatSuivant = "purple"
		else :
			couleurRésultatSuivant = "yellow"
		self.CanvaUn.itemconfigure(self.résultatDuTiragePrécédent, text=résultatPrécédentString, fill=couleurRésultatPrécédent)
		self.CanvaUn.itemconfigure(self.résultatDuTirageActuel, text=self.résultatActuelString, fill=self.couleurRésultatActuel)
		self.CanvaUn.itemconfigure(self.résultatDuTirageSuivant, text=résulatSuivantString, fill=couleurRésultatSuivant)
		self.résultatPrécédent = self.résultatActuel
		self.résultatActuel = self.résulatSuivant
		self.résulatSuivant = random.randint(0, 99)
		self.compteur = self.compteur + 1

	def pageWaifuUn(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Fonctions ###
		def levelUp() :
			if self.argent >= self.waifuUnPrixNiveau :
				self.argent -= self.waifuUnPrixNiveau
				self.waifuUnNiveau += 1
				self.waifuUnPuissance = self.waifuUnPuissance * 2
				self.waifuUnPrixNiveau = self.waifuUnPrixNiveau + int(self.waifuUnPrixNiveau/2)
				self.puissanceClique = self.puissanceClique * 2
				self.pageWaifuUn()

		### Images ###
		self.bureauPrincipal = PhotoImage(file="salle/pageWaifu.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		if self.waifuUn == False :
			self.boutonWaifuUn = Button(self.EcranDeJeux, image=self.imageWaifuUnNoir, command=self.AchatLyne, borderwidth=0)
			self.boutonWaifuUn = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonWaifuUn)
		else :
			self.boutonWaifuUn = Button(self.EcranDeJeux, image=self.imageWaifuUnColor, command=None, borderwidth=0)
			self.boutonWaifuUn = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonWaifuUn)
			self.boutonLevelUp = Button(self.EcranDeJeux, text="Prochain niveau : " + str(self.waifuUnPrixNiveau) + "€", font=("OCR A Extended", 20), bg='white', fg='black', command=levelUp)
			self.boutonLevelUp = self.CanvaUn.create_window((self.LargeurEcran/2)+220, (self.HauteurEcran/2)+50, window=self.boutonLevelUp)
			self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+220, (self.HauteurEcran/2), text= "Niveau : " + str(self.waifuUnNiveau), font=("OCR A Extended", 30), fill="white")
			self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+220+3, (self.HauteurEcran/2)+3, text= "Niveau : " + str(self.waifuUnNiveau), font=("OCR A Extended", 30), fill="black")
		self.texteNomWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+230, (self.HauteurEcran/2)-203, text= "Lyne", font=("OCR A Extended", 30), fill="black")
		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageWaifuCode)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageWaifuDeux)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)

		### Textes ###
		self.texteNomWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+233, (self.HauteurEcran/2)-200, text= "Lyne", font=("OCR A Extended", 30), fill="white")
		self.texteNomWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+230, (self.HauteurEcran/2)-203, text= "Lyne", font=("OCR A Extended", 30), fill="black")
		self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+223, (self.HauteurEcran/2)-103, text= "Augmente la puissance\n     des cliques", font=("OCR A Extended", 30), fill="white")
		self.descriptionWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+220, (self.HauteurEcran/2)-100, text= "Augmente la puissance\n     des cliques", font=("OCR A Extended", 30), fill="black")
		if self.waifuUn == False :
			self.prixWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+233, (self.HauteurEcran/2)+203, text= "Prix : 5.000 €", font=("OCR A Extended", 30), fill="white")
			self.prixWaifuDouuble = self.CanvaUn.create_text((self.LargeurEcran/2)+230, (self.HauteurEcran/2)+200, text= "Prix : 5.000 €", font=("OCR A Extended", 30), fill="black")
		self.ArgentTextuel()

	def pageWaifuDeux(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Fonctions ###
		def levelUp() :
			if self.argent >= self.waifuDeuxPrixNiveau :
				self.argent -= self.waifuDeuxPrixNiveau
				self.waifuDeuxNiveau += 1
				self.waifuDeuxPuissance = self.waifuDeuxPuissance * 2
				self.waifuDeuxPrixNiveau = self.waifuDeuxPrixNiveau + int(self.waifuDeuxPrixNiveau/2)
				self.bonusWaifuDeux = self.bonusWaifuDeux * 2
				self.pageWaifuDeux()

		### Images ###
		self.bureauPrincipal = PhotoImage(file="salle/pageWaifu.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)

		if self.waifuDeux == False :
			self.boutonWaifuDeux = Button(self.EcranDeJeux, image=self.imageWaifuDeuxNoir, command=self.AchatW2, borderwidth=0)
			self.boutonWaifuDeux = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonWaifuDeux)
		else :
			self.boutonWaifuUn = Button(self.EcranDeJeux, image=self.imageWaifuDeuxColor, command=None, borderwidth=0)
			self.boutonWaifuUn = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonWaifuUn)
			self.boutonLevelUp = Button(self.EcranDeJeux, text="Prochain niveau : " + str(self.waifuDeuxPrixNiveau) + "€", font=("OCR A Extended", 20), bg='white', fg='black', command=levelUp)
			self.boutonLevelUp = self.CanvaUn.create_window((self.LargeurEcran/2)+220, (self.HauteurEcran/2)+50, window=self.boutonLevelUp)
			self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+220, (self.HauteurEcran/2), text= "Niveau : " + str(self.waifuDeuxNiveau), font=("OCR A Extended", 30), fill="white")
			self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+220+3, (self.HauteurEcran/2)+3, text= "Niveau : " + str(self.waifuDeuxNiveau), font=("OCR A Extended", 30), fill="black")
		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageWaifuUn)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageWaifuCode)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)

		### Textes ###
		self.texteNomWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+233, (self.HauteurEcran/2)-200, text= "Elo", font=("OCR A Extended", 30), fill="white")
		self.texteNomWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+230, (self.HauteurEcran/2)-203, text= "Elo", font=("OCR A Extended", 30), fill="black")
		self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+223, (self.HauteurEcran/2)-103, text= "Augmentera le rendement\n     de vos weebs", font=("OCR A Extended", 30), fill="white")
		self.descriptionWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+220, (self.HauteurEcran/2)-100, text= "Augmentera le rendement\n     de vos weebs", font=("OCR A Extended", 30), fill="black")
		if self.waifuDeux == False :
			self.prixWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+233, (self.HauteurEcran/2)+203, text= "Prix : 5.000 €", font=("OCR A Extended", 30), fill="white")
			self.prixWaifuDouuble = self.CanvaUn.create_text((self.LargeurEcran/2)+230, (self.HauteurEcran/2)+200, text= "Prix : 5.000 €", font=("OCR A Extended", 30), fill="black")
		self.ArgentTextuel()

	def pageWaifuCode(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Fonctions ###
		def levelUp() :
			if self.argent >= self.waifuCodePrixNiveau :
				self.argent -= self.waifuCodePrixNiveau
				self.waifuCodeNiveau += 1
				self.waifuCodePuissance = self.waifuCodePuissance * 2
				self.waifuCodePrixNiveau = self.waifuCodePrixNiveau + int(self.waifuCodePrixNiveau/2)
				self.pageWaifuCode()

		### Images ###
		self.bureauPrincipal = PhotoImage(file="salle/pageWaifu.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)
		self.imageBoutonSecret = PhotoImage(file="waifu/boutonCode.png")

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)
		
		if self.waifuCode == False :
			self.boutonWaifuCode = Button(self.EcranDeJeux, image=self.imageWaifuCodeNoir, command=None, borderwidth=0)
			self.boutonWaifuCode = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonWaifuCode)
		else :
			self.boutonWaifuCode = Button(self.EcranDeJeux, image=self.imageWaifuCodeColor, command=None, borderwidth=0)
			self.boutonWaifuCode = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2, window=self.boutonWaifuCode)
			self.boutonLevelUp = Button(self.EcranDeJeux, text="Prochain niveau : " + str(self.waifuCodePrixNiveau) + "€", font=("OCR A Extended", 20), bg='white', fg='black', command=levelUp)
			self.boutonLevelUp = self.CanvaUn.create_window((self.LargeurEcran/2)+220, (self.HauteurEcran/2)+50, window=self.boutonLevelUp)
			self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+220, (self.HauteurEcran/2), text= "Niveau : " + str(self.waifuCodeNiveau), font=("OCR A Extended", 30), fill="white")
			self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+220+3, (self.HauteurEcran/2)+3, text= "Niveau : " + str(self.waifuCodeNiveau), font=("OCR A Extended", 30), fill="black")
		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageWaifuDeux)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageWaifuUn)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)
		self.boutonSecret = Button(self.EcranDeJeux, image=self.imageBoutonSecret, font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageBoutonSecret, border=0)
		self.boutonSecret = self.CanvaUn.create_window(20, 700, window=self.boutonSecret)

		### Textes ###
		self.texteNomWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+233, (self.HauteurEcran/2)-200, text= "Kimoko", font=("OCR A Extended", 30), fill="white")
		self.texteNomWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+230, (self.HauteurEcran/2)-203, text= "Kimoko", font=("OCR A Extended", 30), fill="black")
		
		if self.waifuCode == True :
			self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+223, (self.HauteurEcran/2)-103, text= "Augmente le taux\n    de drop de\n  cosmétique légendaire", font=("OCR A Extended", 30), fill="white")
			self.descriptionWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+220, (self.HauteurEcran/2)-100, text= "Augmente le taux\n    de drop de\n  cosmétique légendaire", font=("OCR A Extended", 30), fill="black")	
		else :
			self.descriptionWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+223, (self.HauteurEcran/2)-103, text= "Pouvoir inconnu", font=("OCR A Extended", 30), fill="white")
			self.descriptionWaifuDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+220, (self.HauteurEcran/2)-100, text= "Pouvoir inconnu", font=("OCR A Extended", 30), fill="black")
			self.prixWaifu = self.CanvaUn.create_text((self.LargeurEcran/2)+233, (self.HauteurEcran/2)+203, text= "Débloquable par code", font=("OCR A Extended", 30), fill="white")
			self.prixWaifuDouuble = self.CanvaUn.create_text((self.LargeurEcran/2)+230, (self.HauteurEcran/2)+200, text= "Débloquable par code", font=("OCR A Extended", 30), fill="black")
		self.ArgentTextuel()

	def pageBoutonSecret(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Textes ###
		self.texteFaitPar = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-100, text= "3 - D", font=("OCR A Extended", 60), fill="#464E88")
		self.texteFaitParDouble = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-100, text= "3 - D", font=("OCR A Extended", 60), fill="#88466E")

		### Boutons ###
		self.boutonMenuQuitter = Button(self.EcranDeJeux, text="  Retour  ", font=("OCR A Extended", 20), bg='white', fg='#A44040', command=self.pageWaifuCode)
		self.boutonMenuQuitter = self.CanvaUn.create_window(self.LargeurEcran/2, self.LargeurEcran/1.70, window=self.boutonMenuQuitter)

	def AchatLyne(self):
		if self.argent >= 5000 :
			self.CanvaUn.delete(self.affichageArgent)
			self.CanvaUn.delete(self.affichageArgentDouble)
			self.CanvaUn.delete(self.affichageArgentTriple)
			self.argent = self.argent - 5000
			self.waifuUn = True
			self.nombreWaifu = self.nombreWaifu + 1
			self.puissanceClique = 2
			self.ActualisationArgent()
			self.pageWaifuUn()

	def AchatW2(self):
		if self.argent >= 5000 :
			self.CanvaUn.delete(self.affichageArgent)
			self.CanvaUn.delete(self.affichageArgentDouble)
			self.CanvaUn.delete(self.affichageArgentTriple)
			self.argent = self.argent - 5000
			self.waifuDeux = True
			self.nombreWaifu = self.nombreWaifu + 1
			self.bonusWaifuDeux = self.bonusWaifuDeux + 1
			self.ActualisationArgent()
			self.pageWaifuDeux()

	def Ressources(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bureauPrincipal = PhotoImage(file="salle/shop.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bureauPrincipal)

		### Variables ###
		self.ArgentTextuel()

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text=" Retour ", font=("OCR A Extended", 20), bg='white', fg='black', command=self.MenuBoutique)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, 680, window=self.boutonRetour)
		self.boutonAchatWeebs = Button(self.EcranDeJeux, text=" Achat de 1 Weeb pour : "  + str(self.prixWeeb) + "€", font=("OCR A Extended", 20), bg='white', fg='black', command=self.AchatWeeb)
		self.boutonAchatWeebs = self.CanvaUn.create_window(self.LargeurEcran/2, 300, window=self.boutonAchatWeebs)

	def AchatWeeb(self) :
		if self.argent >= self.prixWeeb :
			self.argent = self.argent - self.prixWeeb
			self.weeb = self.weeb + 1
			self.prixWeeb = self.prixWeeb + int(self.prixWeeb/5)
			self.ActualisationArgent()
			self.Ressources()

	def ActualisationArgent(self):
		if self.argent >= 1000000 and self.argent < 1000000000000:
			self.CanvaUn.itemconfigure(self.affichageArgent, text=str(int(self.argent/1000000)) + " Million(s)" )
			self.CanvaUn.itemconfigure(self.affichageArgentDouble, text=str(int(self.argent/1000000)) + " Million(s)" )
			self.CanvaUn.itemconfigure(self.affichageArgentTriple, text=str(int(self.argent/1000000)) + " Million(s)" )
		elif self.argent >= 1000000000000 :
			self.CanvaUn.itemconfigure(self.affichageArgent, text=str(int(self.argent/1000000000000)) + " Billion(s)" )
			self.CanvaUn.itemconfigure(self.affichageArgentDouble, text=str(int(self.argent/1000000000000)) + " Billion(s)" )
			self.CanvaUn.itemconfigure(self.affichageArgentTriple, text=str(int(self.argent/1000000000000)) + " Billion(s)" )
		else : 
			self.CanvaUn.itemconfigure(self.affichageArgent, text=self.argent)
			self.CanvaUn.itemconfigure(self.affichageArgentDouble, text=self.argent)
			self.CanvaUn.itemconfigure(self.affichageArgentTriple, text=self.argent)

	def ArgentTextuel(self):
		self.affichageArgent = self.CanvaUn.create_text((self.LargeurEcran/2)+6, 76, text= self.argent, font=("OCR A Extended", 30), fill="#1CF8FF")
		self.affichageArgentDouble = self.CanvaUn.create_text((self.LargeurEcran/2)+3, 73, text= self.argent, font=("OCR A Extended", 30), fill="#FF14E6")
		self.affichageArgentTriple = self.CanvaUn.create_text(self.LargeurEcran/2, 70, text= self.argent, font=("OCR A Extended", 30), fill="#FBFF0F")
		self.ActualisationArgent()

	def FonctionTimer(self):
		self.argent = self.argent + ( (int(self.weeb)) * self.bonusWaifuDeux )
		self.argentTotal = self.argentTotal + ( (int(self.weeb)) * self.bonusWaifuDeux )
		### Textes ###
		if self.InGame == True :
			self.ActualisationArgent()
		self.CanvaUn.after(5000, self.FonctionTimer)

	def PremièrePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoUn.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.DeuxièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)

	def DeuxièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoDeux.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.TroisèmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)

	def TroisèmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoTrois.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.QuatrièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)

	def QuatrièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoQuatre.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.CinquièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)

	def CinquièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoCinq.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.SixièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)
		
	def SixièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoSix.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.SeptièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)
		
	def SeptièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoSept.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.HuitièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)
		
	def HuitièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoHuit.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.NeuvièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)

	def NeuvièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoNeuf.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.DixièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)

	def DixièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoDix.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.OnzièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)
	
	def OnzièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoOnze.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.DouzièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)

	def DouzièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoDouze.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.TreizièmePageTuto)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)

	def TreizièmePageTuto(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Image ###
		self.bandeau = PhotoImage(file="tuto/pageTutoTreize.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.bandeau)

		### Boutons ###
		self.boutonSuivant = Button(self.EcranDeJeux, text="Suivant", font=("OCR A Extended", 20), bg='white', fg='black', command=self.FenetrePrincipale)
		self.boutonSuivant = self.CanvaUn.create_window((self.LargeurEcran/2)+320, (self.HauteurEcran/2)+120, window=self.boutonSuivant)

	def pageMillitaire(self) :
		self.CanvaUn.delete(ALL)

		### Image ###
		self.backgroundMillitaire = PhotoImage(file="salle/pageMillitaire.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.backgroundMillitaire)
		self.imageWaifuMillitaire = PhotoImage(file="./waifu/waifuMilli.png")
		self.CanvaUn.create_image(self.LargeurEcran/2/2+50, self.HauteurEcran/2+100, image=self.imageWaifuMillitaire)

		### Fonctions ###
		def calculPuissance() :
			valeur = 0
			if self.waifuUnEquipé == True :
				valeur += self.waifuUnPuissance
			if self.waifuDeuxEquipé == True :
				valeur += self.waifuDeuxPuissance
			if self.waifuCodeEquipé == True :
				valeur += self.waifuCodePuissance
			self.puissanceAllié = valeur

		### Textes ###
		calculPuissance()
		self.puissanceTotale = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-300, text= "Puissance : " + str(self.puissanceAllié), font=("OCR A Extended", 47), fill="white")
		self.puissanceTotaleDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2-300+3, text= "Puissance : " + str(self.puissanceAllié), font=("OCR A Extended", 47), fill="grey")

		### Boutons ###
		self.premierBouton = Button(self.EcranDeJeux, text="Attaquer", font=("OCR A Extended", 25), bg='white', fg='black', command=self.pageAttaque, width=20)
		self.premierBouton = self.CanvaUn.create_window(self.LargeurEcran/2+(self.LargeurEcran/2/2), self.HauteurEcran/2-150, window=self.premierBouton)
		self.deuxièmeBouton = Button(self.EcranDeJeux, text="Gérer équipe", font=("OCR A Extended", 25), bg='white', fg='black', command=self.pageGestionEquipeUne, width=20)
		self.deuxièmeBouton = self.CanvaUn.create_window(self.LargeurEcran/2+(self.LargeurEcran/2/2), self.HauteurEcran/2-50, window=self.deuxièmeBouton)
		self.quatrièmeBouton = Button(self.EcranDeJeux, text="Retour", font=("OCR A Extended", 25), bg='white', fg='black', command=self.FenetrePrincipale, width=20)
		self.quatrièmeBouton = self.CanvaUn.create_window(self.LargeurEcran/2+(self.LargeurEcran/2/2), self.HauteurEcran/2+150, window=self.quatrièmeBouton)

	def pageGestionEquipeUne(self) :
		self.CanvaUn.delete(ALL)

		### Image ###
		self.backgroundMillitaire = PhotoImage(file="salle/pageMillitaire.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.backgroundMillitaire)

		### Fonctions ###
		def EquipementWaifu() :
			if self.waifuUnEquipé == False :
				self.waifuUnEquipé = True
			else :
				self.waifuUnEquipé = False
			self.pageGestionEquipeUne()

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text="Retour", font=("OCR A Extended", 25), bg='white', fg='black', command=self.pageMillitaire, width=20)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2+300, window=self.boutonRetour)

		if (self.waifuUn == True) and (self.waifuUnEquipé == True) :
			self.boutonWaifu = Button(self.EcranDeJeux, image=self.imageWaifuUnColor, command=EquipementWaifu, borderwidth=2, highlightcolor="green",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonWaifu = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2-25, window=self.boutonWaifu)
		elif (self.waifuUn == True) and (self.waifuUnEquipé == False):		
			self.boutonWaifu = Button(self.EcranDeJeux, image=self.imageWaifuUnColor, command=EquipementWaifu, borderwidth=2, highlightcolor="red",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonWaifu = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2-25, window=self.boutonWaifu)
		else :
			self.boutonWaifu = Button(self.EcranDeJeux, image=self.imageWaifuUnNoir, command=None, borderwidth=2, highlightcolor="red",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonWaifu = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2-25, window=self.boutonWaifu)

		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageGestionEquipeTrois)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageGestionEquipeDeux)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)
		
		### Textes ###
		self.nomWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-250, text= "Lyne", font=("OCR A Extended", 60), fill="white")
		self.nomWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-250+3, text= "Lyne", font=("OCR A Extended", 60), fill="grey")
		self.equipeWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-150, text= "Équipé : " + str(self.waifuUnEquipé), font=("OCR A Extended", 30), fill="white")
		self.equipeWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-150+3, text= "Équipé : " + str(self.waifuUnEquipé), font=("OCR A Extended", 30), fill="grey")
		self.niveauWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-100, text= "Niveau : " + str(self.waifuUnNiveau), font=("OCR A Extended", 30), fill="white")
		self.niveauWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-100+3, text= "Niveau : " + str(self.waifuUnNiveau), font=("OCR A Extended", 30), fill="grey")
		self.puissanceWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-50, text= "Puissance : " + str(self.waifuUnPuissance), font=("OCR A Extended", 30), fill="white")
		self.puissanceWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-50+3, text= "Puissance : " + str(self.waifuUnPuissance), font=("OCR A Extended", 30), fill="grey")

	def pageGestionEquipeDeux(self) :
		self.CanvaUn.delete(ALL)

		### Image ###
		self.backgroundMillitaire = PhotoImage(file="salle/pageMillitaire.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.backgroundMillitaire)

		### Fonctions ###
		def EquipementWaifu() :
			if self.waifuDeuxEquipé == False :
				self.waifuDeuxEquipé = True
			else :
				self.waifuDeuxEquipé = False
			self.pageGestionEquipeDeux()

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text="Retour", font=("OCR A Extended", 25), bg='white', fg='black', command=self.pageMillitaire, width=20)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2+300, window=self.boutonRetour)

		if (self.waifuDeux == True) and (self.waifuDeuxEquipé == True) :
			self.boutonWaifu = Button(self.EcranDeJeux, image=self.imageWaifuDeuxColor, command=EquipementWaifu, borderwidth=2, highlightcolor="green",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonWaifu = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2-25, window=self.boutonWaifu)
		elif (self.waifuDeux == True) and (self.waifuDeuxEquipé == False):		
			self.boutonWaifu = Button(self.EcranDeJeux, image=self.imageWaifuDeuxColor, command=EquipementWaifu, borderwidth=2, highlightcolor="red",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonWaifu = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2-25, window=self.boutonWaifu)
		else :
			self.boutonWaifu = Button(self.EcranDeJeux, image=self.imageWaifuDeuxNoir, command=None, borderwidth=2, highlightcolor="red",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonWaifu = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2-25, window=self.boutonWaifu)

		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageGestionEquipeUne)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageGestionEquipeTrois)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)
		
		### Textes ###
		self.nomWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-250, text= "Elo", font=("OCR A Extended", 60), fill="white")
		self.nomWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-250+3, text= "Elo", font=("OCR A Extended", 60), fill="grey")
		self.equipeWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-150, text= "Équipé : " + str(self.waifuDeuxEquipé), font=("OCR A Extended", 30), fill="white")
		self.equipeWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-150+3, text= "Équipé : " + str(self.waifuDeuxEquipé), font=("OCR A Extended", 30), fill="grey")
		self.niveauWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-100, text= "Niveau : " + str(self.waifuDeuxNiveau), font=("OCR A Extended", 30), fill="white")
		self.niveauWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-100+3, text= "Niveau : " + str(self.waifuDeuxNiveau), font=("OCR A Extended", 30), fill="grey")
		self.puissanceWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-50, text= "Puissance : " + str(self.waifuDeuxPuissance), font=("OCR A Extended", 30), fill="white")
		self.puissanceWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-50+3, text= "Puissance : " + str(self.waifuDeuxPuissance), font=("OCR A Extended", 30), fill="grey")

	def pageGestionEquipeTrois(self) :
		self.CanvaUn.delete(ALL)

		### Image ###
		self.backgroundMillitaire = PhotoImage(file="salle/pageMillitaire.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.backgroundMillitaire)

		### Fonctions ###
		def EquipementWaifu() :
			if self.waifuCodeEquipé == False :
				self.waifuCodeEquipé = True
			else :
				self.waifuCodeEquipé = False
			self.pageGestionEquipeTrois()

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text="Retour", font=("OCR A Extended", 25), bg='white', fg='black', command=self.pageMillitaire, width=20)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2+300, window=self.boutonRetour)

		if (self.waifuCode == True) and (self.waifuCodeEquipé == True) :
			self.boutonWaifu = Button(self.EcranDeJeux, image=self.imageWaifuCodeColor, command=EquipementWaifu, borderwidth=2, highlightcolor="green",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonWaifu = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2-25, window=self.boutonWaifu)
		elif (self.waifuCode == True) and (self.waifuCodeEquipé == False):		
			self.boutonWaifu = Button(self.EcranDeJeux, image=self.imageWaifuCodeColor, command=EquipementWaifu, borderwidth=2, highlightcolor="red",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonWaifu = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2-25, window=self.boutonWaifu)
		else :
			self.boutonWaifu = Button(self.EcranDeJeux, image=self.imageWaifuCodeNoir, command=None, borderwidth=2, highlightcolor="red",highlightbackground="grey",highlightthickness=5,relief=SOLID, default='active')
			self.boutonWaifu = self.CanvaUn.create_window(self.LargeurEcran/2-250, self.HauteurEcran/2-25, window=self.boutonWaifu)

		self.boutonGauche = Button(self.EcranDeJeux, text="←", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageGestionEquipeDeux)
		self.boutonGauche = self.CanvaUn.create_window(self.LargeurEcran/2-500, self.HauteurEcran/2, window=self.boutonGauche)
		self.boutonDroite = Button(self.EcranDeJeux, text="→", font=("OCR A Extended", 20), bg='white', fg='black', command=self.pageGestionEquipeUne)
		self.boutonDroite = self.CanvaUn.create_window(self.LargeurEcran/2+500, self.HauteurEcran/2, window=self.boutonDroite)
		
		### Textes ###
		self.nomWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-250, text= "Kimoko", font=("OCR A Extended", 60), fill="white")
		self.nomWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-250+3, text= "Kimoko", font=("OCR A Extended", 60), fill="grey")
		self.equipeWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-150, text= "Équipé : " + str(self.waifuCodeEquipé), font=("OCR A Extended", 30), fill="white")
		self.equipeWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-150+3, text= "Équipé : " + str(self.waifuCodeEquipé), font=("OCR A Extended", 30), fill="grey")
		self.niveauWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-100, text= "Niveau : " + str(self.waifuCodeNiveau), font=("OCR A Extended", 30), fill="white")
		self.niveauWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-100+3, text= "Niveau : " + str(self.waifuCodeNiveau), font=("OCR A Extended", 30), fill="grey")
		self.puissanceWaifu = self.CanvaUn.create_text(self.LargeurEcran/2+200, self.HauteurEcran/2-50, text= "Puissance : " + str(self.waifuCodePuissance), font=("OCR A Extended", 30), fill="white")
		self.puissanceWaifuDeux = self.CanvaUn.create_text(self.LargeurEcran/2+200+3, self.HauteurEcran/2-50+3, text= "Puissance : " + str(self.waifuCodePuissance), font=("OCR A Extended", 30), fill="grey")

	def pageAttaque(self) :
		self.CanvaUn.delete(ALL)

		### Image ###
		self.backgroundMillitaire = PhotoImage(file="salle/pageMillitaire.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.backgroundMillitaire)

		self.facteurAllié = 5
		self.facteurEnnemi = 15

		### Fonctions ###
		finCampagneMillitaire = False
		if self.manche == 0 :
			self.puissanceEnnemi = 100
		elif self.manche == 1 :
			self.puissanceEnnemi = 500
		elif self.manche == 2 :
			self.puissanceEnnemi = 1000
		elif self.manche == 3 :
			self.puissanceEnnemi = 5000
		elif self.manche == 4 :
			self.puissanceEnnemi = 10000
		elif self.manche == 5 :
			self.puissanceEnnemi = 30000
		elif self.manche == 6 :
			finCampagneMillitaire = True

		if finCampagneMillitaire == False :
			### Textes ###
			self.puissanceTotale = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-300, text= "Puissance : " + str(self.puissanceAllié), font=("OCR A Extended", 47), fill="white")
			self.puissanceTotaleDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2-300+3, text= "Puissance : " + str(self.puissanceAllié), font=("OCR A Extended", 47), fill="grey")
			self.mancheActuelle = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-100, text= "Manche : " + str(self.manche), font=("OCR A Extended", 47), fill="white")
			self.mancheActuelleDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2-100+3, text= "Manche : " + str(self.manche), font=("OCR A Extended", 47), fill="red")
			self.puissanceEnnemiTexte = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2, text= "Puissance ennemi : " + str(self.puissanceEnnemi), font=("OCR A Extended", 47), fill="white")
			self.puissanceEnnemiDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2+3, text= "Puissance ennemi : " + str(self.puissanceEnnemi), font=("OCR A Extended", 47), fill="red")

			### Boutons ###
			self.boutonAttaque = Button(self.EcranDeJeux, text="Attaque", font=("OCR A Extended", 25), bg='white', fg='black', command=self.créationAttaque, width=20)
			self.boutonAttaque = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2+200, window=self.boutonAttaque)
		else :
			### Textes ###
			self.puissanceEnnemiTexte = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2, text= "Vous avez finis la campagne", font=("OCR A Extended", 47), fill="white")
			self.puissanceEnnemiDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2+3, text= "Vous avez finis la campagne", font=("OCR A Extended", 47), fill="red")

		### Boutons ###
		self.boutonRetour = Button(self.EcranDeJeux, text="Retour", font=("OCR A Extended", 25), bg='white', fg='black', command=self.pageMillitaire, width=20)
		self.boutonRetour = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2+300, window=self.boutonRetour)

	def créationAttaque(self) :
		self.CanvaUn.delete(ALL)

		### Image ###
		self.backgroundMillitaire = PhotoImage(file="salle/pageAttaque.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.backgroundMillitaire)

		### Fonctions ###
		def couleurTexte() :
			if self.puissanceAllié > self.puissanceEnnemi :
				cA = "lime"
				cM = "red"
			elif self.puissanceAllié == self.puissanceEnnemi :
				cA = "white"
				cM = "white"
			else :
				cA = "red"
				cM = "lime"
			return(cM,cA)

		def vérificationVivant() :
			if self.puissanceAllié <= 0 :
				self.pageDéfaite()
			elif self.puissanceEnnemi <= 0 :
				self.pageVictoire()
			elif (self.puissanceAllié <= 0) and (self.puissanceEnnemi <= 0) :
				self.pageVictoire()

		def boutonAttaqueFct() :
			self.puissanceEnnemi -= self.facteurAllié
			tourEnnemi()
		def boutonHealFct() :
			self.puissanceAllié += self.facteurAllié
			tourEnnemi()
		def boutonUpgradeFct() :
			self.facteurAllié = self.facteurAllié + int(self.facteurAllié/4)
			tourEnnemi()

		def tourEnnemi() :
			valeurAleatoire = random.randint(0, 9)
			if valeurAleatoire <= 5 :
				self.puissanceAllié -= self.facteurEnnemi
			elif valeurAleatoire > 8 :
				self.puissanceEnnemi += self.facteurEnnemi
			else :
				self.facteurEnnemi = self.facteurEnnemi + int(self.facteurEnnemi/4)
			self.créationAttaque()
			vérificationVivant()
			
		### Textes ###
		couleur = couleurTexte()
		self.puissanceEnnemiTexte = self.CanvaUn.create_text(self.LargeurEcran/2-150, self.HauteurEcran/2-275, text= "Puissance ennemi : ", font=("OCR A Extended", 47), fill="black")
		self.puissanceEnnemiTexteDeux = self.CanvaUn.create_text(self.LargeurEcran/2-150+3, self.HauteurEcran/2-275+3, text= "Puissance ennemi : ", font=("OCR A Extended", 47), fill=couleur[0])
		self.puissanceEnnemiValeur = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-175, text=self.puissanceEnnemi, font=("OCR A Extended", 47), fill="black")
		self.puissanceEnnemiValeurDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2-175+3, text=self.puissanceEnnemi, font=("OCR A Extended", 47), fill=couleur[0])
		self.puissanceEnnemiModificateur = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-100, text="Modificateur : " + str(self.facteurEnnemi), font=("OCR A Extended", 47), fill="black")
		self.puissanceEnnemiModificateurDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2-100+3, text="Modificateur : " + str(self.facteurEnnemi), font=("OCR A Extended", 47), fill=couleur[0])
	
		self.puissanceAlliéTexte = self.CanvaUn.create_text(self.LargeurEcran/2-150, self.HauteurEcran/2, text= "Votre puissance : ", font=("OCR A Extended", 47), fill="black")
		self.puissanceAlliéTexteDeux = self.CanvaUn.create_text(self.LargeurEcran/2-150+3, self.HauteurEcran/2+3, text= "Votre puissance : ", font=("OCR A Extended", 47), fill=couleur[1])
		self.puissanceAlliéValeur = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2+75, text=self.puissanceAllié, font=("OCR A Extended", 47), fill="black")
		self.puissanceAlliéValeurDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2+75+3, text=self.puissanceAllié, font=("OCR A Extended", 47), fill=couleur[1])
		self.puissanceAlliéModificateur = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2+150, text="Modificateur : " + str(self.facteurAllié), font=("OCR A Extended", 47), fill="black")
		self.puissanceAlliéModificateurDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2+150+3, text="Modificateur : " + str(self.facteurAllié), font=("OCR A Extended", 47), fill=couleur[1])

		### Boutons ###
		self.boutonAttaque = Button(self.EcranDeJeux, text="⚔️", font=("OCR A Extended", 25), bg='white', fg='black', command=boutonAttaqueFct, width=5, height=3)
		self.boutonAttaque = self.CanvaUn.create_window((self.LargeurEcran/2)/2, self.HauteurEcran-100, window=self.boutonAttaque)
		self.boutonHeal = Button(self.EcranDeJeux, text="❤️", font=("OCR A Extended", 25), bg='white', fg='black', command=boutonHealFct, width=5, height=3)
		self.boutonHeal = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran-100, window=self.boutonHeal)
		self.boutonRecherche = Button(self.EcranDeJeux, text="⚙️", font=("OCR A Extended", 25), bg='white', fg='black', command=boutonUpgradeFct, width=5, height=3)
		self.boutonRecherche = self.CanvaUn.create_window((self.LargeurEcran)-(self.LargeurEcran/2)/2, self.HauteurEcran-100, window=self.boutonRecherche)

	def pageVictoire(self) :
		self.CanvaUn.delete(ALL)

		print(self.manche)

		### Image ###
		self.backgroundMillitaire = PhotoImage(file="salle/pageMillitaire.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.backgroundMillitaire)
		self.imageWaifuMillitaire = PhotoImage(file="./waifu/waifuMilli.png")
		self.CanvaUn.create_image(self.LargeurEcran/2/2+50, self.HauteurEcran/2+100, image=self.imageWaifuMillitaire)

		### Fonctions ###
		self.argent += int(self.argent/10)
		self.argentTotal += int(self.argent/10)
		self.manche += 1

		### Textes
		self.texteVictoire = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-300, text= "Vous avez gagné !", font=("OCR A Extended", 47), fill="white")
		self.texteVictoireDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2-300+3, text= "Vous avez gagné !", font=("OCR A Extended", 47), fill="grey")
		self.texteRécompense = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2, text= "Récompense : " + str(int(self.argent/10)) + "€", font=("OCR A Extended", 47), fill="white")
		self.texteRécompenseDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2+3, text= "Récompense : " + str(int(self.argent/10)) + "€", font=("OCR A Extended", 47), fill="red")

		### Boutons ###
		self.retourPageMillitaire = Button(self.EcranDeJeux, text="Retour", font=("OCR A Extended", 25), bg='white', fg='black', command=self.pageMillitaire, width=20)
		self.retourPageMillitaire = self.CanvaUn.create_window(self.LargeurEcran/2, self.HauteurEcran/2+300, window=self.retourPageMillitaire)

		print(self.manche)

	def pageDéfaite(self) :
		self.CanvaUn.delete(ALL)

		### Image ###
		self.backgroundMillitaire = PhotoImage(file="salle/pageMillitaire.png")
		self.CanvaUn.create_image(self.LargeurEcran/2, self.HauteurEcran/2, image=self.backgroundMillitaire)
		self.imageWaifuMillitaire = PhotoImage(file="./waifu/waifuMilli.png")
		self.CanvaUn.create_image(self.LargeurEcran/2/2+50, self.HauteurEcran/2+100, image=self.imageWaifuMillitaire)

		self.texteVictoire = self.CanvaUn.create_text(self.LargeurEcran/2, self.HauteurEcran/2-300, text= "Vous avez échoué !", font=("OCR A Extended", 47), fill="white")
		self.texteVictoireDeux = self.CanvaUn.create_text(self.LargeurEcran/2+3, self.HauteurEcran/2-300+3, text= "Vous avez échoué !", font=("OCR A Extended", 47), fill="grey")

		### Boutons ###
		self.retourPageMillitaire = Button(self.EcranDeJeux, text="Retour", font=("OCR A Extended", 25), bg='white', fg='black', command=self.pageMillitaire, width=20)
		self.retourPageMillitaire = self.CanvaUn.create_window(self.LargeurEcran/2+(self.LargeurEcran/2/2), self.HauteurEcran/2+150, window=self.retourPageMillitaire)

jeux = Jeux()
jeux 
